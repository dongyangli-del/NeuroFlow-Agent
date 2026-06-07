<div align="center">
  <a href="https://github.com/dongyangli-del/NeuroFlow-Agent">
    <img src="docs/NeuroFlow_logo.png" alt="NeuroFlow Agent" width="532">
  </a>

  <p>
    <b>面向 AI x BCI 与 NeuroAI research agents 的自进化工作流系统。</b><br>
    支持多 skills 协作、任务深度路由、持久研究记忆、实验排错 playbook 与 reviewer-facing 论文工作流。
  </p>

  <p>
    <img alt="自进化" src="https://img.shields.io/badge/system-self--evolving-0f766e">
    <img alt="工作流中心" src="https://img.shields.io/badge/design-workflow--centric-2563eb">
    <img alt="多 skill 协作" src="https://img.shields.io/badge/orchestration-multi--skill-7c3aed">
    <img alt="任务深度" src="https://img.shields.io/badge/tasks-shallow%20to%20deep-16a34a">
  </p>

  <p>
    <a href="README.md"><img alt="English README" src="https://img.shields.io/badge/README-English-0f766e"></a>
    <a href="docs/WORKFLOWS.md"><img alt="Workflows" src="https://img.shields.io/badge/docs-workflows-2563eb"></a>
    <a href="docs/PLAYBOOKS.md"><img alt="Playbooks" src="https://img.shields.io/badge/docs-playbooks-7c3aed"></a>
    <a href="docs/VALIDATION.md"><img alt="Validation" src="https://img.shields.io/badge/validation-make%20validate-16a34a"></a>
  </p>
</div>

这是一个面向 AI x BCI 研究的自进化工作流系统，用于让 agent 在多模态神经解码、EEG 视觉重建、扩散/生成模型、脑语言对齐、闭环脑调控、Physical AI 和 NeuroAI 项目中更像严谨的科研合作者。

仓库的核心思想不是“做一个简单的 AI 与脑机交叉 skill”，而是把 agent 在垂直科研场景中真正需要被定制的部分沉淀下来。Agent 通常由三部分组成：模型、工具和 workflow。模型和工具越来越像通用基础设施，唯独 workflow 需要根据具体研究领域、实验脆弱点、任务深度、审稿标准和长期项目记忆来定制。因此，本仓库的目标是打造一个具有多 skills 协作、自进化、记忆重放和记忆巩固能力的 AI x BCI 持久工作流系统。

`SKILL.md` 只负责精简路由，`references/` 保存可重放的研究记忆和细分工作流，`scripts/` 保存确定性辅助脚本，`evals/` 保存行为评测 prompt，`docs/` 解释这些机制如何组织成一个可持续迭代的系统。浅层任务可以只读取最小记忆并快速回答；标准任务可以调用一到两个 specialist skills；深度任务可以跨 literature grounding、experiment design、review simulation 和 memory consolidation 协同执行。

## 为什么核心是 Workflow

通用 coding agent 容易忽略 AI x BCI 项目的脆弱点：

- EEG split、重复试次、归一化、刺激 ID 对齐可能静默泄漏或错位。
- 生成式重建指标可能奖励尺度、采样或语义捷径，而不是神经信号对齐。
- diffusion denoising loss 看起来正常时，模型仍可能没有使用具体图像 condition。
- 论文 claim 必须区分 decoding、reconstruction、alignment 和 closed-loop modulation。

这些问题通常不是靠换一个更强的模型或者多接几个工具就能解决，而是要让 agent 遵循正确的科研操作顺序：先查 split 和 leakage，再看 baseline；先定位 target、normalization 和 metric，再讨论模型容量；先区分 offline decoding 和 online closed-loop，再写论文 claim。

这个仓库把这些 workflow 固化下来，让之后的 Codex 会话能从正确假设开始，并且能把新的实验经验回放、压缩、巩固到下一轮工作中。

## 持久工作流系统

```mermaid
flowchart TD
    accTitle: NeuroFlow 持久工作流
    accDescr: 任务先按类型和深度路由，再由一个或多个 specialist skills 执行，并在证据检查后把可复用经验巩固成长期记忆。

    task[研究任务] --> triage[Neuro-Orchestrator<br/>任务类型与深度]
    triage --> shallow[浅层任务<br/>最小记忆重放]
    triage --> standard[标准任务<br/>一到两个 specialist skills]
    triage --> deep[深度任务<br/>多 skills 协作]

    standard --> skill_pool[Skill pool]
    deep --> skill_pool

    skill_pool --> idea[Neuro-Idea-Finder<br/>可验证假设]
    skill_pool --> rag[Paper-RAG++<br/>文献 grounding]
    skill_pool --> benchmark[EEG-Benchmark-Hunter<br/>数据集和协议]
    skill_pool --> repro[Repro-Pack<br/>可运行复现]
    skill_pool --> continual[Continual-Learning-Designer<br/>持续适应协议]
    skill_pool --> experiment[Experiment-Copilot<br/>消融、控制和统计]
    skill_pool --> review[Reviewer-Simulator<br/>审稿风险检查]
    skill_pool --> oral[Oral-Writer<br/>thesis 和 figure narrative]
    skill_pool --> bci[ai-bci-research<br/>AI x BCI guardrails]

    shallow --> evidence[证据检查<br/>split、baseline、metric、claim]
    idea --> evidence
    rag --> evidence
    benchmark --> evidence
    repro --> evidence
    continual --> evidence
    experiment --> evidence
    review --> evidence
    oral --> evidence
    bci --> evidence

    evidence --> output[输出<br/>回答、代码、实验计划、论文文本或 review]
    output --> memory[Neuro-Memory<br/>finding、playbook、workflow、case、eval 或 index]
    memory --> replay[未来记忆重放]
    replay --> triage
```

这个系统希望每一次真实研究工作都能留下可复用的痕迹：失败模式变成 playbook，稳定结论变成 dated finding，常见审稿风险变成 reviewer objection，重要行为变成 eval。

## 多 Skills 协作

| Skill | 角色 |
|---|---|
| `neuro-orchestrator` | 判断任务类型和深度，并协调 specialist skills。 |
| `neuro-idea-finder` | 生成可验证的 EEG/iEEG/fMRI/MEG/LFP/spike/BCI 创新点。 |
| `paper-rag-plus` | 做文献 grounding、claim-to-citation mapping 和 related work 组织。 |
| `eeg-benchmark-hunter` | 发现并审计开源 benchmark、license、split、baseline、metric 和 leakage 风险。 |
| `repro-pack` | 生成一键复现契约：环境、数据、权重、命令、expected output、sanity check 和 failure recovery。 |
| `continual-learning-designer` | 设计跨 subject/session/device adaptation、streaming calibration 和 forgetting protocol。 |
| `experiment-copilot` | 设计实验矩阵、ablation、control、统计检验和 stop rule。 |
| `reviewer-simulator` | 按严格会议审稿标准检查 claim、证据和 rebuttal 风险。 |
| `oral-writer` | 把证据压缩成 Oral 级 thesis、figure narrative 和 reviewer-facing 论文文本。 |
| `neuro-memory` | 把完成的 session 压缩成可复用的 workflow、playbook、finding、case 或 eval。 |
| `ai-bci-research` | 提供 AI x BCI 的共享领域假设、有效性检查和长期研究记忆。 |

## 任务深度

| 深度 | 适合任务 | Agent 行为 |
|---|---|---|
| 浅层 | 解释一个指标差距或给出下一步检查。 | 只重放最相关记忆，快速定位可能失败模式。 |
| 标准 | 设计 EEG reconstruction ablation 或复现实验检查。 | 调用领域 guardrails 和实验规划，输出可复现矩阵。 |
| 深度 | 准备会议投稿、rebuttal 或完整实验计划。 | 协同文献、实验、claim、审稿风险、写作和限制。 |
| 持久 | 把一次排错或论文审查沉淀为可复用知识。 | 更新 finding、playbook、workflow rule、eval 或 index。 |

## 核心能力

- **实验排错**：尺度检查、输出目录检查、train/val/test 定位、condition ablation、采样方差、评估协议对齐。
- **BCI 实验设计**：模态、split、预处理、baseline、metric、leakage、robustness。
- **论文和 rebuttal**：reviewer-facing claim、限制表述、venue checklist、审稿质疑应对。
- **研究记忆**：按日期沉淀实验结论、仓库笔记、论文定位和复现记录。
- **多 skill 编排**：按任务深度组合文献、实验、审稿、记忆和 AI x BCI guardrails。
- **仓库感知执行**：先读本地代码，保护已有修改，围绕研究目标做最小必要改动。

## 仓库组织原则

- `skills/ai-bci-research/SKILL.md`：只放路由、first reads 和高层操作规则。
- `skills/ai-bci-research/references/`：放会改变未来 agent 行为的长期研究记忆。
- `docs/`：解释 workflow、playbook、demo 和验证方式。
- `skills/ai-bci-research/scripts/`：放确定性维护脚本，不放一次性实验脚本。
- `skills/ai-bci-research/evals/`：用 prompt 检查 agent 行为是否符合本仓库要求。

原始日志、checkpoint、数据集、大文件、隐私或人类被试相关材料不应该进入这个仓库。这里保存的是被压缩后的可复用经验。

## 安装

安装完整 NeuroFlow skill library：

```bash
git clone https://github.com/dongyangli-del/NeuroFlow-Agent.git
cd NeuroFlow-Agent
bash install.sh
```

`install.sh` 会把 `skills/` 下的所有 skill 链接到 Codex skills 目录。安装后重启 Codex。

如果只想用 Codex skill installer 安装单个 skill，可以显式指定路径：

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo dongyangli-del/NeuroFlow-Agent \
  --path skills/neuro-orchestrator
```

## 更新知识

添加论文、仓库笔记、数据集或实验结论后：

```bash
cd NeuroFlow-Agent/skills/ai-bci-research
python3 scripts/update_knowledge_index.py --root .
```

然后运行：

```bash
make validate
```

## 文档入口

- [Workflows](docs/WORKFLOWS.md)：核心研究工作流。
- [Playbook Catalog](docs/PLAYBOOKS.md)：排错和写作 playbook 索引。
- [Skill Library Spec](docs/SKILL_LIBRARY_SPEC.md)：完整 10-skill library 的 gap analysis、contracts、task chains 和阶段验收标准。
- [Examples](docs/EXAMPLES.md)：真实 demo case 模板和待补案例。
- [Validation](docs/VALIDATION.md)：验证命令和质量检查。
- [Public Ready](docs/PUBLIC_READY.md)：公开发布检查清单和 private memory 规则。

## 明星项目方向

这个项目不应该变成泛科研笔记库，而应该成为最强的 AI x BCI research agent 持久工作流系统：窄、深、可验证、能真实避免实验和论文错误，并且能随着研究积累不断自我进化。
