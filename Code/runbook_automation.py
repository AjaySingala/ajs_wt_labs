"""Safe training-only runbook automation. Python 3.13+.
Only touches the supplied sample_server folder and defaults to dry-run.
"""
from pathlib import Path
from datetime import datetime
import argparse, shutil

def inspect_folder(folder):
    files=[p for p in folder.rglob("*") if p.is_file()]
    return len(files), sum(p.stat().st_size for p in files)

def find_old_logs(folder, age_days):
    cutoff=datetime.now().timestamp()-age_days*86400
    return [p for p in folder.rglob("*.log") if p.is_file() and p.stat().st_mtime < cutoff]

def archive(candidates, archive_dir, approve=False):
    archive_dir.mkdir(parents=True, exist_ok=True)
    for src in candidates:
        dst=archive_dir/src.name
        print(f"ARCHIVE: {src} -> {dst}")
        if approve: shutil.move(str(src),str(dst))

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--folder",default="sample_server")
    p.add_argument("--age-days",type=int,default=30)
    p.add_argument("--approve",action="store_true")
    a=p.parse_args()
    folder=Path(a.folder)
    if not folder.exists(): raise SystemExit(f"Training folder not found: {folder}")
    n,size=inspect_folder(folder); print(f"Files: {n}; bytes: {size}")
    candidates=find_old_logs(folder,a.age_days); print(f"Eligible logs: {len(candidates)}")
    archive(candidates,folder/"archive",a.approve)
    print("APPROVED RUN" if a.approve else "DRY RUN - no files changed")
if __name__=="__main__": main()
