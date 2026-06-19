# AgentGuard Pro

**Open-source Python SAST scanner with AI-powered false positive reduction and safe auto-fix.**

34 built-in rules + Bandit's 100+ engine. Local LLM review cuts false positives. One command: scan → review → fix.

[![PyPI](https://img.shields.io/pypi/v/agentguard2027)](https://pypi.org/project/agentguard2027/)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/)

---

## Why AgentGuard Pro

SAST tools flood you with false positives and leave you to fix everything by hand. AgentGuard Pro is different:

| | Bandit | Semgrep | **AgentGuard Pro** |
|---|---|---|---|
| Python rules | 100+ | Multi-lang | **34 + Bandit 100+** |
| FP filtering | ❌ | ❌ | **ML + LLM review** |
| Auto-fix | ❌ | ❌ | **✅ Pipeline** |
| Local LLM | ❌ | ❌ | **✅ DeepSeek** |
| Desktop GUI | ❌ | ❌ | **✅ Dark theme** |
| Pricing | Free | Free/$40 | **Free + Pro $29/mo** |

---

## Quick Start

```bash
# Install
pip install agentguard2027

# Scan a project
agentguard scan ./my-project

# Full pipeline: scan → review → fix
agentguard pipeline ./src --bandit --ds --mode safe --write

# JSON output for CI/CD
agentguard scan ./src --format json -o report.json

# Desktop GUI
agentguard serve
# Open http://127.0.0.1:1099
```

---

## Pipeline

```
34 rules + Bandit 100+
        ↓
    ML filter          ← Hardcoded literal detection, confidence threshold
        ↓
    DS Review           ← Local LLM classifies TP/FP per finding
        ↓
    Auto-fix            ← 10 of 17 rule types, safe mode default
        ↓
   Clean report
```

One command:
```bash
agentguard pipeline ./src --bandit --ds --mode safe
```

---

## What It Detects

- **Code Injection**: `eval()`, `exec()`, `os.system()`, `subprocess` shell=True
- **Deserialization**: `pickle.loads()`, `yaml.load()`, `marshal.loads()`
- **Secrets**: Hardcoded API keys, tokens, passwords, private keys
- **Path Traversal**: Unsanitized file paths, directory traversal
- **SSRF**: User-controlled URLs in HTTP requests
- **Weak Crypto**: MD5, SHA1, ECB mode, insecure ciphers, weak random
- **XML Attacks**: External entity injection, XPath injection, bomb expansion
- **Insecure Protocols**: HTTP for sensitive data, FTP, Telnet

---

## Tiers

| | Free | Pro ($29/mo) |
|---|---|---|
| 34 built-in rules | ✅ | ✅ |
| Bandit 100+ rules | ✅ | ✅ |
| ML false-positive filter | ✅ | ✅ |
| LLM (DS) review | — | ✅ |
| Pipeline auto-fix | — | ✅ |
| Desktop GUI | ✅ | ✅ |
| SARIF / JSON / MD output | ✅ | ✅ |
| Files per scan | 100 | Unlimited |

> 🚀 **PH Launch**: $149/year (first 100, code `PH2025`)

---

## [Labs] Preview

We're testing an LLM confirmation agent that reviews SAST findings and confirms or rejects them with higher precision than ML alone. Currently in preview — swallowed_exception detector passes 3/3 on our test suite (confidence 0.95+). Full multi-agent pipeline coming in a future release.

```bash
# Enable [Labs] experimental features
agentguard pipeline ./src --bandit --ds --labs
```

---

## Architecture

```
agentguard/
├── cli.py                    ← CLI (scan/pipeline/fix/serve)
├── gui.py                    ← Desktop GUI (dark theme, port 1099)
├── desktop.py                ← Web-based GUI server
├── pipeline.py               ← scan → review → fix pipeline
├── scanner/
│   ├── code_scanner.py       ← Pattern + AST engine (34 rules)
│   ├── bandit_adapter.py     ← Bandit 100+ rules integration
│   ├── bandit_rules.py       ← Bandit rule ID mapping
│   ├── ml_filter.py          ← Literal detection FP filter
│   ├── llm_review.py         ← DS LLM TP/FP classification
│   └── llm_heuristic.py      ← Multi-agent LLM (Labs preview)
├── rules/
│   └── python_rules.py       ← 34 security rules (7 categories)
├── reporter/
│   └── reporter.py           ← Terminal/JSON/SARIF/Markdown
├── fixer/
│   └── code_fixer.py         ← Auto-fix engine (10/17 rules)
└── docs/
    ├── marketing/            ← Landing copy, pricing, launch kit
    ├── spec/                 ← Technical specs
    └── eval/                 ← DS evaluation reports
```

---

## Local-First

Everything runs on your machine:

- **DS LLM** at `127.0.0.1:57321` — code never leaves your network
- **License server** can be self-hosted
- **Zero telemetry**. We don't know you exist.

---

## Links

- 📦 [PyPI](https://pypi.org/project/agentguard2027/)
- 📖 [Docs](docs/)
- 🧪 [Test Suite](tests/)

---

MIT License. Built by XHLS Team, 2026.
