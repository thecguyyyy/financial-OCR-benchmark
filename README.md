# 金融公告 Markdown 重建基准

一个面向中文金融公告 PDF 的 Markdown 重建评测集。项目关注的不是摘要质量，而是解析结果能否忠实还原原文中的正文、标题层级与表格结构，尤其覆盖长文档、密集表格和跨页表等实际场景。

本仓库包含 6 份金融公告 PDF、两套人工复核的 Markdown 标注，以及 6 组已完成的解析结果和评分产物。所有主榜成绩均来自这 6 份文档的完整评分；未完成的实验不会纳入榜单。

## 数据集

| ID | 文档 |
|---|---|
| 005 | 中国平安 2023 年中期报告 |
| 006 | 阿里巴巴 2026 财年中期报告 |
| 007 | 美团 2024 年年度报告 |
| 008 | 先锋新材 2025 年年度报告 |
| 009 | 紫天科技 2022 年年度报告 |
| 010 | 万和电气 2020 年年度报告 |

每份文档提供一对 GT（ground truth）Markdown：

- **Primary GT**：保留人工确认的原始 Markdown 重建边界。
- **Semi-semantic GT**：针对跨页表补充“可独立理解”的判断。若续页具备自己的题目和表头、拆开后仍能完整表达，则将其视作独立表，而不强制跨页合并。

这种双 GT 设计避免把所有跨页版式都机械地归为“必须合并”，也不会奖励将无关表格错误拼接的结果。

## 评测协议

评分器分别衡量表格、标题布局与正文保真度，最终得分为：

```text
总分 = 表格 × 40% + 标题布局 × 20% + 正文 × 40%
```

| 模块 | 评测方法 |
|---|---|
| 表格 | 支持 HTML 和 Markdown pipe table，统一解析为二维单元格矩阵。每张预测表与两个 GT 版本的候选表进行结构与关键词联合匹配，取较优候选；匹配严格一对一，漏表和冗余表均计入惩罚。单表分由结构（60%）和单元格内容（40%）组成。 |
| 标题布局 | 标题 F1 占 80%，相对层级准确率和顺序分各占 10%。标题文字仍保留在正文模块中评分。 |
| 正文 | 移除已抽取表格后，对归一化全文计算编辑距离；标题文字和有信息量的图表文本保留。 |

表格匹配以两个 GT 的**单表最高匹配分**为准，而不是将多个预测表拼接为一张 GT 表。这使得未正确处理的跨页切分、重复输出和错误合并都能反映在分数中。

完整算法、归一化规则与已知局限见 [SCORING_PROTOCOL.md](SCORING_PROTOCOL.md)。

## 已完成系统与结果

下表为各系统在全部 6 份文档上的算术平均分，范围均为 0–100。所有结果均使用上文同一评分协议，表格匹配启用双 GT 最高匹配策略。

| 排名 | 系统 | 总分 | 表格 | 标题布局 | 正文 |
|---:|---|---:|---:|---:|---:|
| 1 | MinerU 3.4.0 — Hybrid backend（`effort=high`；MinerU2.5-Pro-2605-1.2B） | **94.25** | **95.41** | **85.69** | **97.39** |
| 2 | MinerU 3.4.4 — VLM backend（MinerU2.5-Pro-2605-1.2B） | 93.70 | 95.36 | 84.25 | 96.77 |
| 3 | PaddleOCR-VL-1.6-0.9B — cross-page merge | 92.33 | 92.35 | 84.53 | 96.21 |
| 4 | MinerU 3.4.0 — Pipeline backend（`method=auto`，`lang=ch`） | 90.77 | 89.36 | 84.30 | 95.40 |
| 5 | 自研模型 | 90.50 | 89.16 | 84.18 | 95.01 |
| 6 | PaddleOCR-VL-1.6-0.9B — no cross-page merge | 87.45 | 80.46 | 83.88 | 96.21 |

各系统的命名与运行配置依据见 [MODEL_METADATA.md](MODEL_METADATA.md)。

PaddleOCR-VL-1.6-0.9B 的跨页合并结果相比逐页结果，表格平均分提高 **11.89** 分，总分提高 **4.89** 分。两组正文平均分同为 96.21，差异主要来自跨页表后处理。

上述排名仅用于比较本仓库中的固定文档、GT 与评分版本；不应直接外推为不同版式、语言或下游任务中的通用模型排名。

## 仓库结构

```text
data/
  pdf/                         # 6 份源 PDF
  gt/primary/                  # Primary GT
  gt/semi_semantic/            # Semi-semantic GT
predictions/<system>/          # 每个系统的 6 份 Markdown 输出
scores/<system>/               # summary 与逐文档评分报告
benchmark_scorer.py             # 单文档核心评分器
score_prediction_directory.py   # 评分一个新的解析系统
score_all_benchmark_systems.py  # 重跑仓库内全部正式系统
benchmark_systems.py            # 正式系统名称表
MODEL_METADATA.md               # 模型名称与运行参数核验记录
README.md
README_EN.md
SCORING_PROTOCOL.md
```

## 环境要求

Python 3.10 或更高版本。评分脚本仅使用 Python 标准库，无需安装第三方依赖。

## 复现评分

评分一个新的解析系统时，将它的 6 份 Markdown 放入同一目录。推荐直接命名为 `005.md` 至 `010.md`；以编号开头的更长文件名也可以自动识别。运行：

```bash
python score_prediction_directory.py --pred-dir predictions/my_parser --system-name "My Parser 1.0" --output-dir scores/my_parser
```

标准脚本固定启用双 GT 单表最高匹配和本报告中的全部评分权重，输出 `summary.csv`、`summary.json`、`summary.md` 及 6 份逐文档报告。要重新评分仓库中全部正式系统，可运行：

```powershell
python score_all_benchmark_systems.py
```

---

English version: [README_EN.md](README_EN.md)
