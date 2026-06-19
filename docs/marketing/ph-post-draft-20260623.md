# ProductHunt 帖子草稿 — 6/23 发布
> 基于 DS 最终决策：v0.3.0 = 核心管线，[Labs] 退居预览

---

## Tagline (≤40 字符)

**AgentGuard Pro — Python SAST with local LLM review and auto-fix**

---

## 副标题 (≤260 字符)

34 rules + Bandit's 100+ engine scans your Python code. A local LLM filters false positives. Pipeline auto-fixes 10 rule types. All on your machine. Open source.

---

## 帖子正文

```
I got tired of SAST tools that flood you with false positives and won't help you fix anything.

So I built AgentGuard Pro:

🧠 34 built-in rules + Bandit's 100+ engine
🔍 Local LLM false-positive review — your code never leaves your machine
🪄 Pipeline auto-fix — 10 of 17 rule types, one command: scan → review → fix
🖥️ Desktop GUI — hacker aesthetic, dark theme

Python-only. Local-only. Open source (MIT).

pip install agentguard2027
github.com/difcn2026/agentguard

🚀 PH Launch: $149/year (first 100, code PH2025)
```

---

## 首条评论

```
Why Python-only?

Python's dynamic typing makes it the hardest language for SAST — which means the highest false-positive rates. AgentGuard shines exactly there: the LLM review step handles ambiguity that pattern matchers can't.

I use Bandit for the rule base, but the pipeline (ML filter → LLM review → auto-fix) is the difference. Bandit finds. AgentGuard fixes.
```

---

## Maker Reply 模板

**Q: How is this different from Bandit?**
> Bandit is our rule engine. We add: ML false-positive filter, local LLM review, pipeline auto-fix, desktop GUI.

**Q: Does the LLM send my code anywhere?**
> Never. DeepSeek runs at 127.0.0.1. Zero telemetry.

**Q: Why not Semgrep?**
> Semgrep is multi-language. AgentGuard is Python-deep — deeper rules, fewer FPs, Python-native auto-fixer.

---

## 社交媒体

### Twitter/X
```
Built a Python SAST that runs a local LLM to slash false positives and auto-fixes your code.

scan → review → fix. One command. All local.

pip install agentguard2027
github.com/difcn2026/agentguard
```

### Reddit r/Python
```
Title: I built a Python SAST with local LLM FP filtering and auto-fix

Body: Standard SAST averages 40-60% FPs. AgentGuard Pro runs a local DeepSeek LLM to classify every finding TP/FP, then auto-fixes 10 rule types. 34 rules + Bandit 100+ base. All local. MIT.

pip install agentguard2027
```

### Hacker News Show HN
```
Show HN: AgentGuard Pro — Python SAST with local LLM FP reduction and auto-fix

[Use Reddit body]
```

---

## 发布日时间线 (6/23 UTC+8)

| 时间 | 动作 |
|------|------|
| 06:00 | PH 帖子发布 |
| 06:05 | 首评 |
| 07:00 | Reddit r/Python |
| 08:00 | Twitter/X |
| 10:00 | HN Show HN |
| 全天 | 回复评论 |

---

## 检查清单

- [x] GitHub README 更新
- [ ] PyPI v0.3.0 发布 (Token)
- [ ] GitHub Pages 落地页
- [ ] License server (47.236.24.76:8989)
- [ ] Demo (47.236.24.76:1088)
- [ ] PH2025 优惠码
