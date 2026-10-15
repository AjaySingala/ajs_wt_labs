"""
unsafe_operations_script.py

TRAINING EXERCISE ONLY
----------------------
This script intentionally contains security, governance, and operational
weaknesses for a GitHub Copilot security-review exercise.

DO NOT use this pattern in production.

The script simulates an operational cleanup action against a local
training directory. It does NOT connect to WinTrust production systems.
"""

from pathlib import Path
import shutil
import argparse


def cleanup_logs(folder, days):
    """
    Find old log files and delete them.

    This function intentionally contains several weaknesses:
    - No authorization check
    - No approval workflow
    - No dry-run mode
    - No confirmation before deletion
    - No validation of the supplied folder
    - Recursive operation
    - Permanent deletion
    - No audit trail
    - Weak error handling
    - Caller controls the retention period
    """

    folder = Path(folder)

    for log_file in folder.rglob("*.log"):
        try:
            # Simplified training logic:
            # delete every log file found.
            print(f"Deleting: {log_file}")
            log_file.unlink()

        except Exception as exc:
            print(f"Error deleting {log_file}: {exc}")


def copy_sensitive_files(source, destination):
    """
    Copy files from one location to another.

    This function intentionally has no authorization,
    destination validation, or sensitive-data controls.
    """

    source = Path(source)
    destination = Path(destination)

    destination.mkdir(parents=True, exist_ok=True)

    for file in source.rglob("*"):
        if file.is_file():
            target = destination / file.name
            print(f"Copying: {file} -> {target}")
            shutil.copy2(file, target)


def main():
    parser = argparse.ArgumentParser(
        description="WinTrust operational cleanup utility"
    )

    parser.add_argument(
        "--folder",
        required=True,
        help="Folder to process"
    )

    parser.add_argument(
        "--retention-days",
        type=int,
        default=30,
        help="Number of days to retain logs"
    )

    parser.add_argument(
        "--backup",
        help="Optional location for backup files"
    )

    args = parser.parse_args()

    print("Starting operational cleanup...")
    print(f"Target folder: {args.folder}")
    print(f"Retention period: {args.retention_days} days")

    cleanup_logs(
        args.folder,
        args.retention_days
    )

    if args.backup:
        print("Copying files to backup location...")
        copy_sensitive_files(
            args.folder,
            args.backup
        )

    print("Operation completed.")


if __name__ == "__main__":
    main()
	