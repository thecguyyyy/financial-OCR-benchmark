# 金融公告 Markdown 自动评分算法说明

本文档说明 `benchmark_scorer.py` 的评分目标、处理流程、核心算法和局限。脚本用于评估金融公告类 PDF 解析结果，即比较模型输出 `pred.md` 与标准答案 `gt.md` 的差异。

## 1. 总体评分

脚本只评估三部分：表格、标题布局、正文。不评估公式。

总分公式：

```text
Final Score = Table Score * 0.40 + Title Layout Score * 0.20 + Text Score * 0.40
```

三个子分数均归一到 `0-100`。

命令行示例：

对一组新的 6 份解析结果进行标准评分：

```powershell
python score_prediction_directory.py `
  --pred-dir predictions/my_parser `
  --system-name "My Parser 1.0" `
  --output-dir scores/my_parser
```

对单份 Markdown 调试评分：

```bash
python benchmark_scorer.py \
  --gt gt.md \
  --pred pred.md \
  --gt-table-alt gt_non_cross_page.md \
  --table-gt-strategy max \
  --normalize-zh t2s \
  --normalize-images on \
  --normalize-footnotes on \
  --normalize-punctuation on \
  --md-out report.md \
  --json-out report.json
```

## 2. 处理流程

脚本的实际流程如下：

```text
1. 读取 GT Markdown 和 Prediction Markdown
2. 仅对 Prediction Markdown 做无信息页眉页脚清洗，GT 不做该类删除
3. 抽取 HTML table 与 Markdown pipe table
4. 从正文评分输入中移除表格，避免表格内容重复进入正文分
5. 从移除表格后的 Markdown 中抽取标题等级序列
6. 标题布局评分比较标题层级，并用标题文字辅助锚点对齐
7. 正文评分只删除标题前缀 #，保留标题文字
8. 正文不做段落合并，换行按一个字符保留，再计算 normalized edit distance
9. 汇总表格分、标题布局分、正文分和总分
10. 输出 Markdown 报告和 JSON 报告
```

## 3. 表格抽取

在表格抽取前，脚本会先对 Prediction Markdown 做一次轻量清洗。该清洗只删除明显无信息价值的页眉页脚类噪声，例如孤立页码、目录点线页码、重复出现的报告名、重复出现的纯公司名。清洗不会作用于 GT，也不会删除 `<table>` 行或 Markdown pipe table 行。

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
1. 按 GT 表格出现顺序逐个处理
2. 每个 GT 表格只能在 Pred 表格集合中选择一个尚未使用的最佳表格
3. 一个 Pred 表格一旦被某个 GT 使用，不能再被其他 GT 使用
4. 不允许多个 Pred 表格合并后匹配一个 GT 表格
5. 同分或近似同分时优先选择文档位置更接近的 Pred 表格，避免重复形状表格交叉匹配
6. 如果 GT 表格更多，多出的 GT 表格计为 missing，按 0 分进入分母
7. 如果 Pred 表格更多，多出的 Pred 表格计为 extra，按 0 分进入分母
```

该顺序感知的一对一匹配保证 GT 对 GT 时表格分为 100，同时仍能惩罚跨页表格未合并导致的 missing / extra 片段。

表格总分：

```text
final_table_score = sum(matched_table_pair_score) / max(gt_table_count, pred_table_count, 1)
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

`max` 策略的计分分母为：

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
9. GT 正文不做重复页眉页脚删除；无信息页眉页脚只在 Prediction Markdown 进入评分前清洗
10. 弱化行首列表符号差异，例如 `-`、`*`、`•`、`>` 等
11. 普通 Markdown 图片、HTML `<img>`、常见 image 占位统一归一化为 `![]`，只保留图片占位，不比较路径和 alt 文本
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

## 8. 输出报告

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

## 9. 可配置参数

脚本默认启用当前优化后的评分口径，也可以通过 CLI 关闭部分归一化或调整表格 pair 权重：

```text
--remove-pred-header-footer on/off
--normalize-images on/off
--normalize-zh t2s/none
--normalize-footnotes on/off
--normalize-punctuation on/off
--table-structure-weight 0.60
--table-content-weight 0.40
```

其中表格 pair 权重会自动归一化；例如 `0.60 + 0.40` 和 `6 + 4` 等价。

## 10. 依赖说明

脚本核心逻辑使用 Python 标准库：

```text
argparse
dataclasses
html.parser
json
pathlib
re
```

不强依赖第三方库。

如果需要启用繁简归一化，建议安装可选依赖：

```bash
python -m pip install opencc-python-reimplemented
```

脚本会优先尝试 `opencc.OpenCC("t2s")`，安装后可将繁体和简体统一到简体；未安装时会自动跳过该步骤。

## 11. 当前局限

当前实现是轻量评分器，不是完整的文档语义判别器，主要局限包括：

```text
1. HTML 嵌套表格只做近似处理
2. 严重损坏的 HTML table 可能解析不完整
3. rowspan / colspan 通过复制文本展开，不能完全表达树结构
4. 表格匹配是 GT-driven 顺序感知一对一匹配，不把多个 Pred 表格拼接成一个 GT 表格
5. 正文评分为严格字符序列评分，不会容忍段落拆分/合并差异
6. 标题布局使用标题文字做锚点，但不直接评价标题文字语义是否正确
7. 表格语义等价、单位换算、同义改写等高级语义不在当前范围内
```
