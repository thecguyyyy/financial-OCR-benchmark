# 金融文档 OCR 基准 2.0

[English](README_EN.md) · [评分协议](SCORING_PROTOCOL.md) · [Prediction 归一化](PREDICTION_NORMALIZATION.md) · [模型信息](MODEL_METADATA.md)

本项目用于评测金融 PDF 到结构化 Markdown 的 OCR 与版面重建质量。2.0 版包含 4 份脱敏券商行研报告和 6 份公开金融公告，覆盖长文档正文、标题层级、复杂表格、跨页表、公式及信息图表。

PDF 是 Gold Markdown 的唯一事实来源。Gold 不从任一模型输出直接继承格式，人工校对时只保留文档真实内容和必要结构，不含解析器坐标、分页标记、文件路径或工具元数据。

## 数据集

| 编号 | 类型 | 文档 | 页数 | Gold 特点 |
|---:|---|---|---:|---|
| 001 | 行研报告 | 食品饮料行业深度报告 | 29 | 62 个信息图表、公式、复杂表格 |
| 002 | 行研报告 | 传媒行业深度报告 | 17 | 17 个信息图表、6 张表格 |
| 003 | 行研报告 | 创新药产业链深度报告 | 28 | 44 个信息图表、9 张表格 |
| 004 | 行研报告 | 创新药国际化深度报告 | 17 | 12 个信息图表、8 张表格 |
| 005 | 金融公告 | 中国平安 2023 年中期报告 | 168 | 21 个信息图表、双表格 Gold、长篇公告结构 |
| 006 | 金融公告 | 阿里巴巴 2026 财年中期报告 | 83 | 双表格 Gold、中英文混排 |
| 007 | 金融公告 | 美团 2024 年年度报告 | 345 | 3 个信息图表、双表格 Gold、大量复杂表格 |
| 008 | 金融公告 | 先锋新材 2025 年年度报告 | 167 | 双表格 Gold、A 股公告格式 |
| 009 | 金融公告 | 紫天科技 2022 年年度报告 | 157 | 1 个信息图表、双表格 Gold、A 股公告格式 |
| 010 | 金融公告 | 万和电气 2020 年年度报告 | 210 | 1 个信息图表、双表格 Gold、跨页表密集 |

001–004 PDF 为脱敏版本；005–010 来自公开披露文件。数据布局如下：

```text
data/pdf/                         # 001–010 原始 PDF
data/gt/primary/                  # 001–010 主 Gold Markdown
data/gt/semi_semantic/            # 005–010 半语义表格 Gold
predictions/<system>/             # 原始 OCR 输出
normalized_predictions/<system>/  # 特异归一化后的评分输入
scores/with_charts/               # 计入图表质量
scores/without_charts/            # 不计图表质量
normalizers/                      # 各系统独立适配器及公共引擎
```

001–004 使用一份人工审核 Gold。005–010 同时提供主 Gold 和半语义表格 Gold：当跨页后续表具有独立题目、表头且拆开后仍可完整理解时，半语义版本保留为独立表；评分时每个 Prediction 表分别在两份 Gold 的一对一匹配结果中取较高分。

## Gold Markdown 标准

Gold 以 parser-neutral 为原则：

- 保留正文原意、标题层级、金融数字、单位、公式和表格结构；
- 普通装饰图片写作 `![]`；
- 有信息价值的图表写作 `?[]`，并保留可从 PDF 读取的标题、图例、坐标、单位和数据转写；
- 同时可合理表示为表格的图表使用显式 chart-table 标记，允许 Prediction 的表格结构与 Gold 图表转写等价匹配，但同一内容只计分一次；
- 不保留页码、重复页眉页脚、解析器标签、页面坐标或本地路径；
- 不为提高某个模型分数而修改事实内容。

## 已评测系统

本仓库只列入已经完成 001–010 全量解析的系统。具体版本和运行参数见 [MODEL_METADATA.md](MODEL_METADATA.md)。

1. MinerU 3.4.0 — Hybrid backend（effort=high；MinerU2.5-Pro-2605-1.2B）
2. MinerU 3.4.4 — VLM backend（MinerU2.5-Pro-2605-1.2B）
3. MinerU 3.4.0 — Pipeline backend（method=auto，lang=ch）
4. PaddleOCR-VL-1.6-0.9B — cross-page merge
5. PaddleOCR-VL-1.6-0.9B — no cross-page merge
6. 自研解析模型（版本未记录）

## 2.0.1 结果

### 不考虑图表质量

该模式对 Gold 和 Prediction 中标记的信息图表转写进行对称移除，适合只比较正文、标题和普通表格的场景。

| 排名 | 系统 | 总分 | 表格 | 标题 | 正文 |
|---:|---|---:|---:|---:|---:|
| 1 | PaddleOCR-VL-1.6-0.9B — cross-page merge | 93.21 | 93.26 | 87.76 | 95.79 |
| 2 | MinerU 3.4.4 — VLM backend | 93.13 | 93.56 | 83.68 | 96.76 |
| 3 | MinerU 3.4.0 — Hybrid backend（effort=high） | 93.10 | 93.58 | 84.79 | 96.38 |
| 4 | MinerU 3.4.0 — Pipeline backend | 91.75 | 86.95 | 87.43 | 95.43 |
| 5 | 自研解析模型 | 90.14 | 79.80 | 90.29 | 95.20 |
| 6 | PaddleOCR-VL-1.6-0.9B — no cross-page merge | 89.68 | 80.24 | 86.80 | 95.79 |

### 考虑图表质量

该模式把 `?[]` 内的图表转写作为正文信息模块的一部分；数字优先、兼顾文字，并按出现顺序一对一匹配。001–010 均适用同一开关；006、008 没有可独立转写的数据图表，因此这两份文档在两种模式下相同。

| 排名 | 系统 | 总分 | 表格 | 标题 | 正文及图表 |
|---:|---|---:|---:|---:|---:|
| 1 | MinerU 3.4.0 — Hybrid backend（effort=high） | 92.33 | 93.58 | 84.79 | 94.98 |
| 2 | MinerU 3.4.4 — VLM backend | 91.99 | 93.56 | 83.68 | 94.83 |
| 3 | PaddleOCR-VL-1.6-0.9B — cross-page merge | 83.82 | 93.26 | 87.76 | 82.00 |
| 4 | MinerU 3.4.0 — Pipeline backend | 82.89 | 86.95 | 87.43 | 82.02 |
| 5 | 自研解析模型 | 81.76 | 79.80 | 90.29 | 82.06 |
| 6 | PaddleOCR-VL-1.6-0.9B — no cross-page merge | 80.62 | 80.24 | 86.80 | 82.00 |

完整逐文档报告和机器可读结果位于 [`scores/`](scores/)。上述排名只反映本数据集及当前评分协议，不代表模型在所有 OCR 场景中的通用排名。

## 评分方法

标题布局固定占 20%。其余 80% 根据每份 Gold 的有效信息量在表格和正文之间动态分配：

```text
表格信息量 = 表格语义 token 数 + 展开后的逻辑网格单元数
表格权重 = 80% × 表格信息量 /（表格信息量 + 有效正文信息量）
正文权重 = 80% - 表格权重
```

计图表模式下，Gold 图表转写 token 进入有效正文信息量。这样表格密集文档不会被固定权重低估，正文密集文档也不会因少量小表被过度支配。

- 表格：结构 60% + 单元格内容 40%；候选由结构和关键词共同约束，再进行全局一对一最高质量匹配。单表聚合按 `sqrt(逻辑网格单元数 × max(规范化单元格字符数, 逻辑网格单元数))` 计算占比，漏表按 Gold footprint 计零分，冗余表扩大分母。
- 标题：标题 F1 80% + 相对层级准确率 10% + 顺序 10%。
- 正文：移除业务表格并保留标题文字，对完整规范化正文计算精确 Levenshtein 相似度；公式只做不改变数学含义的表示归一化。
- 图表：只评 `?[]` 标记的信息图表转写，数字匹配优先；chart-table 在表格模块和图表模块之间只路由一次。

完整定义、参数和限制见 [SCORING_PROTOCOL.md](SCORING_PROTOCOL.md)。

## 特异归一化

不同解析器会输出各自的展示协议，例如 MinerU `details/summary`、PaddleOCR 对齐 `div`、自研解析器坐标注释和不同图片路径。直接比较会把协议差异误当成 OCR 错误，因此每个系统先运行自己的适配器，再进入统一评分器。

适配器只能根据该系统输出本身清理可证明的协议噪声。它不得读取 PDF、Gold、其他模型结果、文档编号或历史分数；不得修复 OCR 字词、改写数字、拆并业务表格或重排正文。每次运行都会生成 manifest，记录规则、输入输出哈希、变换计数、幂等性和结构保持校验。详见 [PREDICTION_NORMALIZATION.md](PREDICTION_NORMALIZATION.md)。

## 复现

推荐 Python 3.10 或以上版本：

```bash
python -m pip install -r requirements.txt
python normalize_all_predictions.py
python score_all_benchmark_systems.py --skip-normalization
```

命令会生成 `scores/with_charts/` 和 `scores/without_charts/` 两套榜单。评分一个新解析器时，先基于 `normalizers/normalize_parser_template.py` 编写只针对其输出协议的适配器，再运行：

```bash
python score_prediction_directory.py \
  --pred-dir normalized_predictions/your-parser \
  --system-name "Your Parser" \
  --score-charts on \
  --allow-unmanifested
```

`--allow-unmanifested` 仅用于本地调试；正式提交必须附带通过约束检查的 `normalization_manifest.json`。

## 版本

2.0.1 将公告中的已转写信息图表纳入与行研报告相同的 `?[]` 图表开关；006、008 因没有可独立转写的数据图表而保持 0。2.0.0 首次加入脱敏行研报告、信息图表评分、内容感知动态模块权重、表格 footprint 聚合及统一的 001–010 特异归一化流程。版本变化见 [CHANGELOG.md](CHANGELOG.md)。
