# 军师 Dispatch — 2026-06-20
> 签发: 军师 | 执行: 小黑 | 监督: 军师
> 项目: AgentGuard Pro v0.3.0 | 死线: 6/23 ProductHunt

---

## P0-1: GitHub README 更新 🔴

**目标**: GitHub 落地页展示产品价值
**输入**: `docs/marketing/02-landing-copy.md`
**验收标准**:
- [ ] 一句话产品定位（34 rules scan what you know. [Labs] finds what you don't.）
- [ ] 核心能力 4 点（规则扫描 / DS 二审 / Pipeline / Labs）
- [ ] 安装命令 `pip install agentguard2027`
- [ ] 快速开始示例
- [ ] 文档链接指向 docs/
**截止**: 今天完成

---

## P0-2: ProductHunt 帖子草稿 🔴

**目标**: 6/23 周二 00:01 PST 准时发帖
**输入**: `docs/marketing/05-ph-launch-kit.md`
**验收标准**:
- [ ] 标题（≤40 字符，英文）
- [ ] 副标题（≤260 字符）
- [ ] 首条评论 / Maker Comment
- [ ] 3 个平台推广话术（Twitter/X, Reddit, Hacker News）
- [ ] 标签建议
**截止**: 明天

---

## P1-1: 评测框架 — 最小可用版 🟡

**目标**: 有数据支撑 [Labs] 模块宣传
**做法**: 
1. 造 5 个已知漏洞 Python 文件（故意埋 race_condition / swallowed_exception / toctou / missing_auth / logic_bug 各一）
2. 跑 `agentguard scan --labs` 看 LLM heuristic 检出率
3. 输出 `docs/eval/phase-1-heuristic-baseline.md`
**验收标准**:
- [ ] 5 个测试文件在 `tests/fixtures/heuristic/`
- [ ] 每个文件包含 1 个确定的漏洞
- [ ] 检出率报告（哪个 Agent 检出，confidence 多少，漏了哪个）
**截止**: 6/22

---

## P1-2: 精读 SecureFixAgent + Prompt-vs-FT 🟡

**目标**: 判断是否需要给 pipeline 加 self-validation 环节
**论文位置**: 见 `research/strategist-round2-lit-review.md`
**输出**: 200 字以内改进建议，写入 `docs/eval/paper-insights-20260620.md`
**验收标准**:
- [ ] 两篇论文核心结论提炼
- [ ] 对 AgentGuard 的具体改进建议（如有）
- [ ] 判断是否需要立即改代码还是记入 backlog
**截止**: 6/22

---

## 状态追踪

| 任务 | 状态 | 小黑回报 |
|------|------|----------|
| P0-1 README | ⏳ | — |
| P0-2 PH 帖子 | ⏳ | — |
| P1-1 评测框架 | ⏳ | — |
| P1-2 论文精读 | ⏳ | — |

> 完成即回执。军师每半天检查进度。
