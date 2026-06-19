"""Test fixture: TOCTOU vulnerability.

Expected: LLM heuristic Agent should detect check-then-use race window."""
import os
import shutil


def save_file_unsafe(filename: str, content: str) -> bool:
    """Check if file exists, then write — TOCTOU race window."""
    if os.path.exists(filename):
        print(f"File {filename} exists, appending...")
    else:
        print(f"Creating new file {filename}...")
    with open(filename, "w") as f:
        f.write(content)
    return True


def read_config_check_then_read(path: str) -> dict:
    """Check file permissions then read — TOCTOU."""
    import json
    if not os.access(path, os.R_OK):
        return {}
    with open(path, "r") as f:
        return json.load(f)


def delete_temp_check_then_delete(tmpdir: str) -> None:
    """Check directory exists then delete — TOCTOU in shared dir."""
    if os.path.isdir(tmpdir):
        shutil.rmtree(tmpdir)


def update_user_record(db, user_id: int, new_data: dict) -> bool:
    """Check user exists then update — no transaction."""
    rows = db.execute("SELECT id FROM users WHERE id = ?", [user_id])
    if not rows:
        return False
    db.execute("UPDATE users SET data = ? WHERE id = ?", [str(new_data), user_id])
    return True


def main() -> None:
    save_file_unsafe("/tmp/test_config.txt", "key=value")
    print("File saved.")


if __name__ == "__main__":
    main()
