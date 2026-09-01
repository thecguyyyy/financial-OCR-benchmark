# 金融文档 OCR 基准 2.0 评分协议

本文档说明 `benchmark_scorer.py` 的评分目标、处理流程、核心算法和局限。脚本评估金融 PDF 到结构化 Markdown 的 OCR 与版面重建质量，包括 001–004 行研报告和 005–010 金融公告。

## 1. 总体评分

脚本评估表格、标题布局和正文三个总分模块；信息图表可通过开关计入正文模块。公式不单列分数，但其数学 token 作为正文内容参与评分。

标题布局固定保留 20%，其余 80% 根据每份 GT 的表格与正文信息量动态分配：

```text
table_information = table_semantic_tokens + expanded_logical_grid_slots
effective_text_information = body_semantic_tokens + active_chart_tokens
table_weight = 0.80 * table_information / (table_information + effective_text_information)
text_weight = 0.80 - table_weight
Final Score = Table Score * table_weight
            + Title Layout Score * 0.20
            + Text Score * text_weight
```

三个子分数均归一到 `0-100`。语义 token 统一按中文字符、英文单词和数值项计数；每个展开后的逻辑网格单元再贡献一个结构信息单位，避免纯数字表格因文本短而被低估。所有权重只读取 GT，不读取 Prediction 或模型得分。

存在双 GT 时，拆分版本可能重复表头。顶层表格权重使用两个 GT 中较小的正表格信息量，防止表格拆分方式虚增权重；这不改变单表匹配仍可从两个 GT 中取较优结果的规则。

命令行示例：

对一组新的 10 份解析结果进行标准评分：

```powershell
python normalizers/normalize_my_parser.py `
  --input-dir predictions/my_parser `
  --output-dir normalized_predictions/my_parser

python score_prediction_directory.py `
  --pred-dir normalized_predictions/my_parser `
  --system-name "My Parser 1.0" `
  --score-charts on `
  --output-dir scores/with_charts/my_parser
```

对单份 Markdown 调试评分：

```bash
python benchmark_scorer.py \
  --gt gt.md \
  --pred pred.md \
  --gt-table-alt gt_non_cross_page.md \
  --table-gt-strategy max \
  --remove-pred-header-footer off \
  --normalize-zh t2s \
  --normalize-images on \
  --score-charts on \
  --normalize-formulas on \
  --normalize-footnotes on \
  --normalize-punctuation on \
  --md-out report.md \
  --json-out report.json
```

## 2. 处理流程

脚本的实际流程如下：

```text
1. 使用该解析系统的独立、GT 无关适配器，把原始 Prediction 转为素 Markdown
2. 校验表格矩阵、非噪声标题序列与适配器幂等性，并写入 manifest
3. 读取 GT Markdown 和已归一化的 Prediction Markdown；标准评分关闭隐藏的 Prediction 专属清洗
4. 抽取 HTML table、Markdown pipe table 和 `?[]` 信息图表块
5. 将显式 chart-table 内容路由到表格或图表模块一次，避免重复得分
6. 从正文评分输入中移除业务表格；按开关保留或对称移除图表转写
7. 从移除表格后的 Markdown 中抽取标题等级序列
8. 标题布局评分比较标题层级，并用标题文字辅助锚点对齐
9. 正文评分只删除标题前缀 #，保留标题文字，并对公式做共享表示归一化
10. 正文不做段落合并，换行按一个字符保留，再计算 normalized edit distance
11. 根据 Gold 信息量计算该文档的动态模块权重并汇总总分
12. 输出 Markdown 报告和 JSON 报告
```

### Prediction 独立适配器

每个模型/版本必须提交自己的适配脚本。适配器只能处理该模型稳定的表示层差异，不能读取 GT、PDF 或评分结果，不能按文档 ID/公司名分支，也不能修正文字、数字、表格数据、标题或阅读顺序。表格不得合并、拆分或重排；纯视觉内容可转为 `![]`，有信息量的图表文字必须保留。标准评分要求适配器生成 `normalization_manifest.json`，详细规则见 [PREDICTION_NORMALIZATION.md](PREDICTION_NORMALIZATION.md)。

## 3. 表格抽取

页眉页脚、分页标签、图片坐标和模型容器必须由公开的模型专属适配器处理。标准批量入口将 `--remove-pred-header-footer` 固定为 `off`，评分器不再参照 GT 对 Prediction 做隐藏删除。正文的共享语义等价归一化仍会对 GT 和 Prediction 一视同仁地执行。

脚本支持两类表格：

```text
1. HTML table: <table>...</table>
2. Markdown pipe table:
   | A | B |
   |---|---|
   | 1 | 2 |
```

HTML 表格使用 Python 标准库 `html.parser.HTMLParser` 解析 `<tr>`、`<td>`、`<th>`，并轻量展开 `rowspan` / `colspan`。展开方式是把跨行跨列单元格文本复制到覆盖位置，便于后续结构与内容比较。

Markdown pipe table 使用行扫描识别：若某行包含 `|` 且下一行是 `|---|---|` 形式的分隔行，则视为表格起点，并继续收集后续 pipe 行。

抽取到的每个表格都会转换为二维 cell matrix。

## 4. 表格评分

表格评分包含两个子项：

```text
table_structure_score
table_content_score
```

单表结构分比较：

```text
row_score        = 1 - abs(gt_rows - pred_rows) / max(gt_rows, pred_rows, 1)
col_score        = 1 - abs(gt_cols - pred_cols) / max(gt_cols, pred_cols, 1)
cell_count_score = 1 - abs(gt_cells - pred_cells) / max(gt_cells, pred_cells, 1)

table_structure_score = average(row_score, col_score, cell_count_score) * 100
```

单表内容分比较：

GT 与 Pred 的每个表格单元格在比较前复用正文的语义归一化，包括 Markdown/HTML 外壳、全半角、繁简体、脚注/上标、低价值标点和图片占位；行、列及单元格边界仍然保留。

```text
1. 按最大行列数对齐 GT / Pred cell matrix
2. 缺失位置视为空字符串
3. 每个对应单元格计算 normalized edit distance
4. cell_similarity = 1 - normalized_edit_distance
5. table_content_score = average(cell_similarity) * 100
```

单表最终分：

```text
table_pair_score = table_structure_score * 0.60 + table_content_score * 0.40
```

多表匹配：

```text
1. 以每张 Pred 表格为检索起点，在全部 GT 表格中寻找候选，不按表格出现顺序强制对齐
2. 候选检索联合使用表头/首列关键词锚点与行列结构，再以单表结构和内容得分确认最佳候选
3. Pred 与 GT 严格一对一；任意一侧表格一旦匹配，不能再次使用
4. 不允许多个 Pred 表格合并后匹配一个 GT 表格
5. 全部候选边按匹配置信度排序后执行全局贪心分配；低于语义阈值的候选保持未匹配
6. 如果 GT 表格更多，多出的 GT 表格计为 missing，按 0 分进入分母
7. 如果 Pred 表格更多，多出的 Pred 表格计为 extra，按 0 分进入分母
```

这种基于结构与关键词的最高分一对一匹配允许跳过缺失表格，避免前部漏表导致后续表格连锁错配，同时仍会惩罚跨页表格未合并造成的 missing / extra 片段。

文档级表格篇幅仅依据 Gold Markdown 矩阵计算：

```text
grid_slots = expanded_rows * expanded_cols
character_units = max(normalized_cell_characters, grid_slots)
table_footprint = sqrt(grid_slots * character_units)
gt_table_weight = table_footprint / sum(all_gt_table_footprints)
```

几何平均同时考虑表格结构规模和文字密度，避免大量空单元格或单个超长文字单元格独自主导权重。缺失的 Gold 表格在其整个篇幅上记0分；未匹配的 Prediction 表格以自身篇幅增大分母。

默认表格总分：

```text
final_table_score =
    sum(matched_table_pair_score * matched_gt_table_footprint)
    / (sum(all_gt_table_footprints) + sum(unmatched_pred_table_footprints))
```

用 `--table-aggregation uniform` 可复现旧的每表等权口径：

```text
sum(matched_table_pair_score) / max(gt_table_count, pred_table_count, 1)
```

如果 GT 和 Pred 都没有表格，则表格分为 100。如果只有一侧有表格，则表格分为 0。

跨页表格诊断：

```text
1. 如果 GT 表格前存在 <!-- table spans PDF pages x-y -->，该表视为跨页合并表
2. 匹配到的 Pred 表格如果也有同类跨页标记，则计为跨页表命中
3. cross_page_table_score = cross_page_matched_count / cross_page_gt_table_count * 100
4. 若 GT 没有跨页表，cross_page_table_score = 100
```

该字段只作为诊断信息输出，不直接进入最终表格分。跨页未合并时，一个 GT 跨页大表只能匹配一个 Pred 表格片段，信息缺失会体现在该对表格的内部结构/内容评分里，剩余 Pred 片段会作为 extra table 扣分。

## 5. 双表格 GT 策略

金融公告跨页表格可能存在两种合理标准答案：

```text
1. 跨页表格合并版
2. 非跨页表格拆分版
```

脚本支持通过 `--gt-table-alt` 传入第二套表格 GT，并用 `--table-gt-strategy` 指定策略：

```text
primary: 使用主 GT 表格分
alt:     使用第二套 GT 表格分
max:     对每一个 Pred 表格分别与 primary / alt GT 进行一对一匹配，保留更高的单表分
```

`max` 策略在默认篇幅加权下，先将 primary / alt 中的表格篇幅分别在各自 GT 内归一化，再对每张 Prediction 保留更高分的匹配。未匹配 Prediction 仍按自身篇幅扩大分母。

使用 `--table-aggregation uniform` 时，`max` 策略的旧计分分母为：

```text
max(pred_table_count, min(primary_gt_table_count, alt_gt_table_count), 1)
```

因此，少输出的 Pred 表格会因参考表数量进入分母而扣分；多出的 Pred 表格若未在两套 GT 中匹配，也会以 0 分进入分母。每套 GT 内部仍保持一对一约束，避免同一 GT 表在同一版本内重复得分。

注意：双 GT 只影响表格评分。标题布局和正文评分始终使用主 `--gt`。

## 6. 标题布局评分

标题布局的最终扣分仍主要来自标题数量、顺序和相对等级；标题文字只用于辅助锚点对齐，避免重复标题或相似层级被错配。

原始标题等级来自 `#` 数量：

```md
# 第一章
## 第一节
### 一、业务情况
```

抽取得到：

```text
[1, 2, 3]
```

评分前会转换为相对标题等级。转换规则：

```text
1. 统计当前 Markdown 实际出现过的标题等级
2. 按 # 数量从小到大排序
3. 最小等级映射为 1，第二小等级映射为 2，依次类推
```

例子：

```text
Raw:      [1, 3]
Observed: {1, 3}
Relative: [1, 2]
```

```text
Raw:      [2, 3]
Observed: {2, 3}
Relative: [1, 2]
```

标题序列使用动态规划对齐。对齐阶段会参考标题文字相似度确定 GT 标题和 Pred 标题的对应关系；对齐完成后再统计标题 F1、相对等级准确率和顺序覆盖。

```text
missing heading cost = 1
extra heading cost   = 1
matched heading cost = abs(gt_relative_level - pred_relative_level) / max_level
```

标题布局分：

```text
title_layout_score = heading_f1 * 0.80 + level_accuracy * 0.10 + order_score * 0.10
```

如果 GT 和 Pred 都没有标题，标题布局分为 100。

## 7. 正文评分

正文评分输入的预处理：

```text
1. 移除所有已抽取表格
2. 对标题行只删除 # 前缀，保留标题文字
3. 统一 Windows / Unix 换行为 \n
4. 去除 HTML 标签、图片链接语法、Markdown 链接外壳
5. 统一全角 / 半角字符，例如全角数字、字母、括号会归一到兼容形式
6. 使用 OpenCC 时将繁体 / 简体统一到简体；如果 OpenCC 不可用，则跳过该步骤但脚本不报错
7. 删除目录点线页码行，例如“第一节 ...... 2”
8. 过滤孤立页码和常见页脚，例如“12”“- 12 -”“Page 12 of 90”“第12页/共90页”
9. 重复页眉页脚只允许由该模型的公开适配器根据 Prediction 自身判断；统一评分器不参照 GT 做 Prediction 专属删除
10. 弱化行首列表符号差异，例如 `-`、`*`、`•`、`>` 等
11. 普通 Markdown 图片、HTML `<img>`、成对的 `<image>...</image>` 坐标容器及常见 image 占位统一归一化为 `![]`，只保留图片占位，不比较路径、alt 文本和版面坐标
12. 自然图片、流程图、mermaid 图结构统一归一化为 `![]`，不把 `graph LR` / `graph TD` 等代码放入正文比较
13. 对 `text_image`、带表格数据的 chart/details 等仍去掉外层 HTML 包装并保留内部信息
14. 删除散落的自然图片英文 caption，例如 “Illustration of ... (no text or symbols)”
15. 删除脚注 / 上标标记，例如 `<sup>9</sup>`、`$^{9}$`、`[9]`，并处理 `SSP1-2.69` 这类脚注粘连
16. 统一低价值标点差异，例如中英文冒号、括号、引号、破折号、CJK 之间的顿号 / 逗号
17. 将连续多个空行压缩为一个空行
18. 删除横向空白差异，但换行作为一个正文字符保留，参与编辑距离
```

示例：

```md
## 第三节 管理层讨论与分析
```

进入正文评分时变成：

```text
第三节 管理层讨论与分析
```

正文评分不再做文本块合并或段落合并。脚本会先做正文专用归一化，再把 GT 正文和 Pred 正文分别视为一个完整字符序列：

```text
gt_body   = full normalized GT body text, with \n preserved
pred_body = full normalized Pred body text, with \n preserved
```

因此，全半角、普通空格、目录页码等低价值版式差异会被弱化；无信息页眉页脚只从 Pred 侧删除；如果 GT 有换行而 Pred 把两行合成一行，换行差异仍会按一个字符进入 Levenshtein 距离。

normalized edit distance：

```text
distance = levenshtein_distance(a, b) / max(len(a), len(b), 1)
similarity = 1 - distance
```

正文分：

```text
text_score = (1 - average_edit_distance) * 100
```

如果 GT 正文为空而 Pred 非空，或 Pred 正文为空而 GT 非空，正文分会按完整文本缺失/冗余处理；如果两边正文都为空，正文分为 100。

### 公式表示归一化

公式仍属于正文事实内容。评分器只统一不改变数学含义的表示差异，例如 `$...$` / `\(...\)` 外壳、`​\frac{a}{b}` 与等价的展示层空白、`​\left` / `\right` 和 Unicode 数学符号；变量、数字、上下标、运算符和正负号均保留。`r-g` 与 `r+g`、`16.5%` 与 `165%` 仍会产生实质扣分。

## 8. 信息图表评分

001–004 Gold 使用 `?[]` 标记有信息价值的图表，标记后的结构化文字直到下一个文档对象边界构成图表 payload。普通 `![]` 图片不进入图表评分。

`--score-charts off` 时，Gold 与 Prediction 的图表块在表格、标题和正文抽取前被对称移除。`--score-charts on` 时：

```text
1. 按文档顺序对 Gold / Prediction 图表做一对一匹配
2. 单图优先比较数值 token，再比较规范化文字 token
3. 漏图和冗余图按 0 分进入图表序列
4. 图表分按 Gold 图表 token 在有效正文中的占比混入正文模块
```

图表中以 HTML/Markdown 表格转写的内容，如果 Gold 显式标记为 chart-table，可作为辅助表格参与普通表格匹配；一旦路由成功，该 payload 从图表匹配中移除，确保同一信息不重复得分。未标记的普通业务表格不能通过图题文字自动改类。

## 9. 输出报告

Markdown 报告包含：

```text
1. Overall
2. Weights
3. Table Evaluation
4. Title Layout Evaluation
5. Text Evaluation
6. Notes
```

JSON 报告包含同样核心字段，适合后续批量评测。

## 10. 可配置参数

脚本默认启用共享语义等价归一化，并默认关闭旧式 Prediction 专属页眉页脚清洗。也可以通过 CLI 调试或调整表格 pair 权重：

```text
--remove-pred-header-footer on/off
--normalize-images on/off
--score-charts on/off
--normalize-zh t2s/none
--normalize-footnotes on/off
--normalize-punctuation on/off
--normalize-formulas on/off
--table-structure-weight 0.60
--table-content-weight 0.40
--table-aggregation footprint
--module-weighting content
--title-layout-weight 0.20
```

其中 `--remove-pred-header-footer on` 仅为旧结果复核/调试保留，不得用于正式主榜。表格 pair 权重会自动归一化；例如 `0.60 + 0.40` 和 `6 + 4` 等价。`--table-aggregation uniform` 仅用于复现旧版每表等权结果；`--module-weighting fixed` 可复现旧版总分固定 `40% / 20% / 40%` 权重。

## 11. 依赖说明

脚本核心逻辑使用 Python 标准库：

```text
argparse
dataclasses
html.parser
json
pathlib
re
```

正式复现应安装锁定的评分依赖：

```bash
python -m pip install -r requirements.txt
```

其中 `python-Levenshtein` 用于高速计算整篇正文和单表归一化内容的精确距离，`opencc-python-reimplemented` 用于繁简归一化。缺少原生 Levenshtein 时，评分器只允许退回结果一致但速度较慢的纯 Python 精确实现，不再使用会因换行、段落或表格切块边界而改变分数的分段近似。

## 12. 当前局限

当前实现是轻量评分器，不是完整的文档语义判别器，主要局限包括：

```text
1. HTML 嵌套表格只做近似处理
2. 严重损坏的 HTML table 可能解析不完整
3. rowspan / colspan 通过复制文本展开，不能完全表达树结构
4. 表格匹配是 Pred-driven 的结构与关键词最高分一对一匹配，不把多个 Pred 表格拼接成一个 GT 表格
5. 正文评分为严格字符序列评分，不会容忍段落拆分/合并差异
6. 标题布局使用标题文字做锚点，但不直接评价标题文字语义是否正确
7. 表格语义等价、单位换算、同义改写等高级语义不在当前范围内
8. 图表评分只比较人工转写后可读出的数字和文字，不评估颜色、线型、几何位置或视觉美观
```
