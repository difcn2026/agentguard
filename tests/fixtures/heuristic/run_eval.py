"""Run heuristic evaluation on test fixtures."""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')
import json
from pathlib import Path
from agentguard.scanner.llm_heuristic import (
    heuristic_scan_multi_agent, format_heuristic_results, get_metrics
)

FIXTURES_DIR = Path(__file__).parent

results = {}
for f in sorted(FIXTURES_DIR.glob("test_*.py")):
    code = f.read_text(encoding="utf-8")
    findings = heuristic_scan_multi_agent(str(f), code, [], use_cache=False)
    results[f.name] = {
        "total": len(findings),
        "types": list(set(ff.risk_type for ff in findings)),
        "findings": [
            {
                "risk_type": ff.risk_type,
                "line_start": ff.line_start,
                "line_end": ff.line_end,
                "confidence": ff.confidence,
                "description": ff.description,
                "suggestion": ff.suggestion,
            }
            for ff in findings
        ],
    }
    print(f"\n{f.name}: {len(findings)} findings")
    if findings:
        print(format_heuristic_results(findings))

# Summary
print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)
for name, data in results.items():
    status = "✅ FOUND" if data["total"] > 0 else "❌ MISSED"
    print(f"  {status}: {name} ({data['total']} findings)")

print(f"\nMetrics: {json.dumps(get_metrics(), indent=2)}")

# Save
out_path = FIXTURES_DIR / "results.json"
out_path.write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"\nSaved: {out_path}")
