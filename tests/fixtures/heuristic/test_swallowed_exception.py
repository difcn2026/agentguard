"""Test fixture: swallowed_exception vulnerability.

Expected: LLM heuristic Agent should detect bare except:pass masking errors."""
import json
import os


def load_config_bad(filename: str) -> dict:
    """Loads config file but silently fails on ALL errors — security risk."""
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except:
        pass  # VULNERABILITY: swallows FileNotFoundError, PermissionError, JSONDecodeError
    return {}


def authenticate_user(token: str) -> bool:
    """Authenticate user token — but swallowed exception masks auth failure."""
    try:
        if not token or len(token) < 10:
            raise ValueError("Invalid token")
        return True
    except Exception:
        pass  # VULNERABILITY: auth failure silently ignored
    return False


def process_loop(items: list) -> None:
    """Process items in loop — except:continue masks persistent errors."""
    for item in items:
        try:
            result = int(item["value"]) / item.get("divisor", 1)
            print(f"Processed: {result}")
        except:
            continue  # VULNERABILITY: silently skips failed items forever


def main() -> None:
    config = load_config_bad("/nonexistent/config.json")
    print(f"Config: {config}")
    auth_ok = authenticate_user("short")
    print(f"Auth: {auth_ok}")
    process_loop([{"value": "10"}, {"value": "abc"}, {"value": "20"}])


if __name__ == "__main__":
    main()
