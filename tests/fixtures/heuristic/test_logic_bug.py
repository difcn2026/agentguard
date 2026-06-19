"""Test fixture: logic_bug vulnerability.

Expected: LLM heuristic Agent should detect logic flaws enabling security bypass."""
from typing import Optional


def check_admin_access(user: dict) -> bool:
    """Check if user has admin access — INVERTED LOGIC."""
    if not user.get("is_admin"):
        return True  # BUG: should be return False
    return False


def validate_input_size(data: bytes, max_size: int) -> bool:
    """Validate data doesn't exceed max size — OFF-BY-ONE."""
    if len(data) > max_size:
        return False
    return True  # Allows exactly max_size+1 through


def is_user_authorized(user_id: int, resource_id: int) -> bool:
    """Check resource authorization — OPERATOR PRECEDENCE BUG."""
    is_owner = (user_id == resource_id)
    is_admin = (user_id == 0)
    is_banned = False
    if is_owner or is_admin and not is_banned:  # BUG: missing parentheses
        return True
    return False


def verify_signature(payload: bytes, signature: bytes) -> bool:
    """Verify cryptographic signature — DEFAULT-ALLOW."""
    try:
        if not signature:
            return True  # BUG: empty signature = access granted
        return True
    except Exception:
        return True  # VULNERABILITY: exception = access granted


def check_password_strength(password: str) -> bool:
    """Validate password — WRONG COMPARISON."""
    if len(password) > 8:  # BUG: should be >= 8
        return True
    return False


def main() -> None:
    user = {"name": "alice", "is_admin": False}
    print(f"Alice admin? {check_admin_access(user)}")
    print(f"Size valid? {validate_input_size(b'x' * 1024, 1023)}")
    print(f"Owner authorized? {is_user_authorized(42, 42)}")
    print(f"Empty sig valid? {verify_signature(b'data', b'')}")
    print(f"Password strong? {check_password_strength('12345678')}")


if __name__ == "__main__":
    main()
