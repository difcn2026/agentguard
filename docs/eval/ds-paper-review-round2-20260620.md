# DS 第二轮论文评审 — 6篇新文献
> 评审时间: 2026-06-20
> 模型: deepseek-v4-flash
> 来源: 军师第二轮深挖 → arXiv API

---

## 逐篇分析

| 论文 | 关键洞察 | AgentGuard 该怎么做 |
|------|----------|-------------------|
| **Path Feasibility** | LLM 可验证漏洞路径是否可达，砍 40% FP | ✅ 采纳：DS Review 后加路径可达性检验 |
| **AdaTaint** | 神经符号推理自适应匹配 source/sink | ✅ 采纳：taint 分析加上下文自适应 |
| **AgenticSCR** | Agentic AI 抓 SAST 漏掉的"未成熟漏洞" | ✅ 采纳：加 pre-commit agentic review |
| **Prompt vs Fine-tune** | Fine-tuning 全面超越 prompt engineering | ⚠️ 转向：长期应微调本地模型而非纯 prompt |
| **SecureFixAgent** | 修复后必须自验证（重新扫描+跑测试） | ✅ 采纳：fixer 加 self-validation loop |
| **Small LM CWE** | 本地小模型能做 CWE 检测且保护隐私 | ✅ 验证：我们的本地 DS 方案有学术支撑 |

---

## 🔑 三个最优先改进

### 1. LLM 路径可达性过滤
DS Review 之后加一步：对每个 TP finding，让 LLM 验证代码路径是否真的可达。
→ **预期效果**：再砍 40% FP，比现在 DS Review 的"语义分类"更进一步

### 2. Agentic Pre-Commit Review
加轻量 pre-commit 检查：LLM + 代码检索工具，在提交前抓"未成熟漏洞"。
→ **差异化卖点**：SAST 扫静态模式，我们扫 API 误用初态

### 3. 自验证修复闭环
fixer 修完代码后，重新跑 scan 确认不引入新漏洞 + 跑单元测试确认不破坏功能。
→ **信任基础**：修完不验证 = 没人敢用自动修复

---

## ⚠️ 四条警告

1. **不要跳过路径可达性** — 40% SAST 结果因路径不可达是误报（Paper 1）
2. **不要只靠 prompt engineering** — fine-tuning 在罕见 CWE 上召回更高（Paper 4）
3. **不要修复后不验证** — LLM 修复可能引入新漏洞或破坏代码（Paper 5）
4. **不要全走云端** — 本地小模型能做 CWE 检测，精度够且不泄露代码（Paper 6）

---

## PH 发布一句话（DS 帮写的）

> *AgentGuard Pro isn't just another Python SAST scanner — it's your fully-local, privacy-first security co-pilot. Combining 34 rules + 100+ Bandit checks + ML false-positive filter + LLM heuristics, it catches both known vulnerabilities AND the immature patterns traditional scanners miss.*

---

> 保存: docs/eval/ds-paper-review-round2-20260620.md
