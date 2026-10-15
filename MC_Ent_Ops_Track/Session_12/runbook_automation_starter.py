#!/usr/bin/env python3
"""Controlled local runbook exercise. Synthetic files only; dry-run by default."""
from __future__ import annotations
import argparse, json, logging, shutil
from datetime import datetime, timezone
from pathlib import Path

EXERCISE_ROOT = Path(__file__).resolve().parent / "sample_server"
LOG_DIR = EXERCISE_ROOT / "logs"
ARCHIVE_DIR = EXERCISE_ROOT / "archive"

def within_root(path: Path, root: Path) -> bool:
    try:
        path.resolve().relative_to(root.resolve())
        return True
    except ValueError:
        return False

def discover_candidates(log_dir: Path, root: Path, older_than_days: int, now_ts: float) -> list[Path]:
    if older_than_days < 1:
        raise ValueError("older_than_days must be at least 1")
    if not within_root(log_dir, root):
        raise ValueError("log directory is outside the exercise root")
    if not log_dir.exists() or not log_dir.is_dir():
        raise ValueError("log directory does not exist")
    cutoff = now_ts - older_than_days * 86400
    candidates=[]
    for path in log_dir.iterdir():
        if path.is_file() and path.suffix.lower()==".log" and within_root(path,root) and path.stat().st_mtime < cutoff:
            candidates.append(path)
    return sorted(candidates)

def archive_candidates(candidates: list[Path], archive_dir: Path, root: Path) -> list[dict]:
    if not within_root(archive_dir,root):
        raise ValueError("archive directory is outside the exercise root")
    archive_dir.mkdir(parents=True,exist_ok=True)
    results=[]
    for source in candidates:
        if not within_root(source,root):
            raise ValueError(f"source path outside exercise root: {source}")
        destination=archive_dir/source.name
        if destination.exists():
            results.append({"source":str(source),"destination":str(destination),"status":"SKIPPED_DESTINATION_EXISTS"})
            continue
        shutil.move(str(source),str(destination))
        ok=destination.exists() and not source.exists()
        results.append({"source":str(source),"destination":str(destination),"status":"ARCHIVED_AND_VERIFIED" if ok else "VALIDATION_FAILED"})
        if not ok: break
    return results

def main() -> int:
    parser=argparse.ArgumentParser(description="Local-only disk utilization runbook exercise")
    parser.add_argument("--older-than-days",type=int,default=30)
    parser.add_argument("--approve",action="store_true",help="allow archive moves; without it, dry-run only")
    args=parser.parse_args()
    root=EXERCISE_ROOT.resolve(); log_dir=LOG_DIR.resolve(); archive_dir=ARCHIVE_DIR.resolve()
    logging.basicConfig(filename=root/"runbook_audit.log",level=logging.INFO,format="%(asctime)s %(levelname)s %(message)s")
    try:
        candidates=discover_candidates(log_dir,root,args.older_than_days,datetime.now(timezone.utc).timestamp())
        plan={"timestamp_utc":datetime.now(timezone.utc).isoformat(),"mode":"APPROVED_ARCHIVE" if args.approve else "DRY_RUN",
              "exercise_root":str(root),"candidate_count":len(candidates),
              "candidates":[{"path":str(p),"size_bytes":p.stat().st_size} for p in candidates],
              "note":"Moving a file to the exercise archive does not prove the incident is resolved."}
        print(json.dumps(plan,indent=2)); logging.info("plan=%s",json.dumps(plan))
        if not args.approve:
            print("DRY RUN ONLY: no files moved. Review the plan before an approved exercise run."); return 0
        results=archive_candidates(candidates,archive_dir,root)
        print(json.dumps({"archive_results":results},indent=2)); logging.info("archive_results=%s",json.dumps(results))
        if any(r["status"] not in {"ARCHIVED_AND_VERIFIED","SKIPPED_DESTINATION_EXISTS"} for r in results):
            print("VALIDATION FAILED: stop and escalate."); return 2
        print("Archive exercise complete. Independently verify disk utilization and incident recovery."); return 0
    except Exception as exc:
        logging.exception("runbook exercise failed")
        print(f"STOP AND ESCALATE: {type(exc).__name__}: {exc}"); return 2

if __name__=="__main__":
    raise SystemExit(main())
