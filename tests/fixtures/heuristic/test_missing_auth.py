"""Test fixture: missing_auth vulnerability.

Expected: LLM heuristic Agent should detect missing authorization checks."""
import os
import subprocess
from typing import Optional

_users = {"admin": {"role": "admin"}, "alice": {"role": "user"}}


def get_current_user() -> Optional[str]:
    return os.environ.get("CURRENT_USER")


def delete_user_account(username: str) -> bool:
    """Delete user account — NO authorization check!"""
    if username in _users:
        del _users[username]
        print(f"User {username} deleted.")
        return True
    return False


def run_system_command(cmd: str) -> str:
    """Run arbitrary system command — NO auth check!"""
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.stdout


def get_all_user_data() -> list:
    """Return ALL user data — NO ownership check!"""
    return [{"name": k, **v} for k, v in _users.items()]


def read_sensitive_file(filepath: str) -> str:
    """Read arbitrary file — NO permission check!"""
    with open(filepath, "r") as f:
        return f.read()


class AdminPanel:
    """Admin controls — but anyone can call these methods."""
    def reset_passwords(self) -> None:
        print("All passwords reset.")
    def view_system_logs(self) -> None:
        print("Showing system logs...")


def main() -> None:
    delete_user_account("admin")
    output = run_system_command("whoami")
    print(f"Command output: {output}")
    all_data = get_all_user_data()
    print(f"All users: {all_data}")


if __name__ == "__main__":
    main()
