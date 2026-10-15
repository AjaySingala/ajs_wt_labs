"""
WinTrust training sample: unsafe operational automation for code review only.
DO NOT RUN. All actions are illustrative and deliberately unsafe.
"""
import os
import shutil
import subprocess
import requests

API_TOKEN = "EXAMPLE_TOKEN_DO_NOT_USE"

def handle_disk_alert(host, target_dir, user_supplied_path, db_cursor, incident_id):
    # Risk: no host/path allowlist, authorization check, or scoped validation.
    print(f"Handling incident {incident_id} on {host}")

    # Risk: shell interpolation from caller-controlled input; do not execute.
    command = f"ssh {host} 'df -h {user_supplied_path}'"
    subprocess.run(command, shell=True, check=False)

    # Risk: recursive deletion without path containment, dry-run, or approval.
    if os.path.exists(target_dir):
        shutil.rmtree(target_dir)

    # Risk: credential disclosure in logs.
    print("Using API token:", API_TOKEN)

    # Risk: SQL injection through string concatenation; destructive statement.
    sql = "DELETE FROM incident_files WHERE path = '" + user_supplied_path + "'"
    db_cursor.execute(sql)

    # Risk: no timeout, response validation, or destination allowlist.
    requests.get("https://" + host + "/admin/restart")

    return {"incident_id": incident_id, "status": "completed"}
