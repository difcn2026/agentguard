"""Test fixture: race_condition vulnerability.

Expected: LLM heuristic Agent should detect shared counter without lock."""
import threading
import time

# Shared mutable state — NO LOCK
counter = 0
results = []


def worker(worker_id: int) -> None:
    """Worker that modifies shared state without synchronization."""
    global counter, results
    for _ in range(100):
        current = counter
        time.sleep(0.001)  # Small delay to increase race window
        counter = current + 1
    results.append(f"Worker {worker_id} done")


def run_workers() -> None:
    """Launch multiple threads racing on shared state."""
    threads = []
    for i in range(5):
        t = threading.Thread(target=worker, args=(i,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    # Expected: counter would be 500 with proper locking
    # Actual: race condition causes lost updates
    print(f"Final counter: {counter} (expected 500)")
    print(f"Results: {len(results)}")


if __name__ == "__main__":
    run_workers()
