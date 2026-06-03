# Codex AI x BCI Research Skill

这是一个面向 AI x BCI 研究的 Codex skill 仓库，用于让 agent 在多模态神经解码、EEG 视觉重建、扩散/生成模型、脑语言对齐、闭环脑调控、Physical AI 和 NeuroAI 项目中更像严谨的科研合作者。

仓库的核心思想是“可复用研究记忆”：`SKILL.md` 保存精简操作规则，`references/` 保存细分工作流和项目记忆，`scripts/` 保存确定性辅助脚本，`evals/` 保存行为评测 prompt。

## 为什么需要这个 Skill

通用 coding agent 容易忽略 AI x BCI 项目的脆弱点：

- EEG split、重复试次、归一化、刺激 ID 对齐可能静默泄漏或错位。
- 生成式重建指标可能奖励尺度、采样或语义捷径，而不是神经信号对齐。
- diffusion denoising loss 看起来正常时，模型仍可能没有使用具体图像 condition。
- 论文 claim 必须区分 decoding、reconstruction、alignment 和 closed-loop modulation。

这个 skill 把这些 guardrails 固化下来，让之后的 Codex 会话从正确假设开始。

## 核心能力

- **实验排错**：尺度检查、输出目录检查、train/val/test 定位、condition ablation、采样方差、评估协议对齐。
- **BCI 实验设计**：模态、split、预处理、baseline、metric、leakage、robustness。
- **论文和 rebuttal**：reviewer-facing claim、限制表述、venue checklist、审稿质疑应对。
- **研究记忆**：按日期沉淀实验结论、仓库笔记、论文定位和复现记录。
- **仓库感知执行**：先读本地代码，保护已有修改，围绕研究目标做最小必要改动。

## 安装

使用 Codex skill installer：

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo dongyangli-del/codex-ai-bci-research-skill \
  --path skills/ai-bci-research
```

手动安装：

```bash
git clone https://github.com/dongyangli-del/codex-ai-bci-research-skill.git
cd codex-ai-bci-research-skill
bash install.sh
```

安装后重启 Codex。

## 更新知识

添加论文、仓库笔记、数据集或实验结论后：

```bash
cd codex-ai-bci-research-skill/skills/ai-bci-research
python3 scripts/update_knowledge_index.py --root .
```

然后运行：

```bash
make validate
```

## 文档入口

- [Workflows](docs/WORKFLOWS.md)：核心研究工作流。
- [Playbook Catalog](docs/PLAYBOOKS.md)：排错和写作 playbook 索引。
- [Examples](docs/EXAMPLES.md)：真实 demo case 模板和待补案例。
- [Validation](docs/VALIDATION.md)：验证命令和质量检查。

## 明星项目方向

这个项目不应该变成泛科研笔记库，而应该成为最强的 AI x BCI research agent skill：窄、深、可验证、能真实避免实验和论文错误。
