# -*- coding: utf-8 -*-
"""AgentGuard ignore config parser.
Supports three ignore patterns:
  1. filepath glob     — ignores all findings in matching files
  2. rule_id           — ignores all findings of that rule
  3. filepath: rule_id — ignores specific rule in specific file
Lines starting with # are comments. Blank lines are ignored.
"""
import fnmatch
import re
from pathlib import Path
from typing import List, Set, Tuple, Optional


class IgnoreConfig:
    def __init__(self):
        self.file_patterns: List[str] = []     # glob patterns
        self.rule_ids: Set[str] = set()         # rule IDs to ignore globally
        self.file_rules: List[Tuple[str, str]] = []  # (pattern, rule_id) pairs

    @classmethod
    def from_file(cls, path: str = ".agentguard-ignore") -> "IgnoreConfig":
        """Load ignore config from file. Returns empty config if file not found."""
        config = cls()
        p = Path(path)
        if not p.exists():
            return config

        try:
            for line in p.read_text(encoding="utf-8", errors="replace").splitlines():
                line = line.strip()
                if not line or line.startswith("#"):
                    continue

                # Pattern 3: filepath: rule_id
                if ":" in line:
                    parts = line.split(":", 1)
                    file_pat = parts[0].strip()
                    rule_id = parts[1].strip()
                    if rule_id.startswith("#"):
                        rule_id = rule_id[1:].strip()
                    config.file_rules.append((file_pat, rule_id))
                # Pattern 2: rule_id only (starts with PY/JS + digits)
                elif re.match(r"^[A-Z]{2}\d{3}$", line):
                    config.rule_ids.add(line)
                # Pattern 1: filepath glob
                else:
                    config.file_patterns.append(line)
        except Exception:
            pass  # Non-blocking — bad config = no ignores

        return config

    def should_ignore(self, filepath: str, rule_id: str) -> bool:
        """Check if a finding should be ignored."""
        # Normalize filepath to forward slashes
        norm_path = filepath.replace("\\", "/")

        # 1. Global rule ignore
        if rule_id in self.rule_ids:
            return True

        # 2. File glob ignore
        for pattern in self.file_patterns:
            # Try matching against full path and just filename
            if fnmatch.fnmatch(norm_path, pattern) or fnmatch.fnmatch(norm_path, f"*/{pattern}"):
                return True
            # Also try just the filename
            fname = norm_path.split("/")[-1]
            if fnmatch.fnmatch(fname, pattern):
                return True

        # 3. File + rule combo
        for file_pat, rid in self.file_rules:
            if rid != rule_id:
                continue
            if fnmatch.fnmatch(norm_path, file_pat) or fnmatch.fnmatch(norm_path, f"*/{file_pat}"):
                return True
            fname = norm_path.split("/")[-1]
            if fnmatch.fnmatch(fname, file_pat):
                return True

        return False

    def summary(self) -> str:
        return (f"IgnoreConfig: {len(self.file_patterns)} file patterns, "
                f"{len(self.rule_ids)} rules, {len(self.file_rules)} file+rule combos")


if __name__ == "__main__":
    import sys
    path = sys.argv[1] if len(sys.argv) > 1 else ".agentguard-ignore"
    cfg = IgnoreConfig.from_file(path)
    print(cfg.summary())
    for fp in cfg.file_patterns:
        print(f"  file: {fp}")
    for rid in sorted(cfg.rule_ids):
        print(f"  rule: {rid}")
    for fp, rid in cfg.file_rules:
        print(f"  combo: {fp}:{rid}")
