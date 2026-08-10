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

GT 已转换为不依赖具体解析器的素 Markdown：删除分页协议、内部图片路径和图表容器，同时保留可评分的正文、标题、表格与图表信息。处理原则见 [GT_NORMALIZATION.md](GT_NORMALIZATION.md)。

Prediction 也不直接进入评分器。每个模型/版本必须提供一个独立、GT 无关的格式适配器，先生成 `normalized_predictions/` 中的素 Markdown，再使用统一评分器。适配器不得读取 GT/PDF、按文档特判或改变表格边界；完整规则、当前 6 个脚本及校验方法见 [PREDICTION_NORMALIZATION.md](PREDICTION_NORMALIZATION.md)。

## 已完成系统与结果

下表为各系统在全部 6 份文档上的算术平均分，范围均为 0–100。所有结果均使用上文同一评分协议，表格匹配启用双 GT 最高匹配策略。

| 排名 | 系统 | 总分 | 表格 | 标题布局 | 正文 |
|---:|---|---:|---:|---:|---:|
| 1 | MinerU 3.4.0 — Hybrid backend（`effort=high`；MinerU2.5-Pro-2605-1.2B） | **92.73** | **94.25** | 81.98 | **96.58** |
| 2 | MinerU 3.4.4 — VLM backend（MinerU2.5-Pro-2605-1.2B） | 92.19 | 94.19 | 80.64 | 95.97 |
| 3 | PaddleOCR-VL-1.6-0.9B — cross-page merge | 91.80 | 91.94 | **83.88** | 95.61 |
| 4 | 自研解析模型（版本未记录） | 90.67 | 89.36 | 83.46 | 95.60 |
| 5 | MinerU 3.4.0 — Pipeline backend（`method=auto`，`lang=ch`） | 90.31 | 88.76 | 83.70 | 95.17 |
| 6 | PaddleOCR-VL-1.6-0.9B — no cross-page merge | 86.77 | 80.10 | 82.43 | 95.61 |

各系统的命名与运行配置依据见 [MODEL_METADATA.md](MODEL_METADATA.md)。

PaddleOCR-VL-1.6-0.9B 的跨页合并结果相比逐页结果，表格平均分提高 **11.84** 分，总分提高 **5.03** 分。两组正文平均分同为 95.61，差异来自跨页表后处理。

上述排名仅用于比较本仓库中的固定文档、GT 与评分版本；不应直接外推为不同版式、语言或下游任务中的通用模型排名。

## 仓库结构

```text
data/
  pdf/                         # 6 份源 PDF
  gt/primary/                  # Primary GT
  gt/semi_semantic/            # Semi-semantic GT
predictions/<system>/          # 每个系统的 6 份 Markdown 输出
normalized_predictions/<system>/ # 适配后的素 Markdown 与 manifest
scores/<system>/               # summary 与逐文档评分报告
normalizers/                    # 6 个独立模型适配器、公共工具和新模型模板
normalize_all_predictions.py    # 生成并校验全部归一化 Prediction
benchmark_scorer.py             # 单文档核心评分器
score_prediction_directory.py   # 评分一个新的解析系统
score_all_benchmark_systems.py  # 重跑仓库内全部正式系统
benchmark_systems.py            # 正式系统名称表
normalize_gt_markdown.py         # GT 素 Markdown 规范化与检查
MODEL_METADATA.md               # 模型名称与运行参数核验记录
GT_NORMALIZATION.md              # GT 规范化原则与复现说明
PREDICTION_NORMALIZATION.md      # Prediction 独立适配器协议
README.md
README_EN.md
SCORING_PROTOCOL.md
```

## 环境要求

Python 3.10 或更高版本。评分脚本提供纯 Python 回退，无强制第三方依赖；为启用主榜使用的繁简归一化并加快全量评分，建议安装 `opencc-python-reimplemented` 和 `python-Levenshtein`。

## 复现评分

评分一个新系统时，将 6 份原始 Markdown 命名为 `005.md` 至 `010.md` 并放入同一目录。复制 `normalizers/normalize_parser_template.py`，为该系统实现独立适配器，然后先生成带 manifest 的素 Markdown：

```bash
python normalizers/normalize_my_parser.py --input-dir predictions/my_parser --output-dir normalized_predictions/my_parser
```

再评分归一化目录：

```bash
python score_prediction_directory.py --pred-dir normalized_predictions/my_parser --system-name "My Parser 1.0" --output-dir scores/my_parser
```

标准脚本要求 `normalization_manifest.json`，固定启用双 GT 单表最高匹配，并关闭隐藏的 Prediction 专属清洗。要重新生成 6 组归一化结果并评分全部 36 份文档，可运行：

```powershell
python score_all_benchmark_systems.py
```

---

English version: [README_EN.md](README_EN.md)
