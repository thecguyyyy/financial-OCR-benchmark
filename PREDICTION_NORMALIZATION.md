# Prediction 输出归一化协议

本基准把“解析器输出适配”和“语义等价比较”分成两个阶段。每个解析系统先通过自己的确定性适配器生成素 Markdown；随后所有系统进入完全相同的评分器。这样既能消除模型输出协议的差异，也不会把某个模型的缺字、错字、表格错误或标题错误特殊处理掉。

## 1. 强制约束

正式评分使用的每个模型/版本必须提供一个独立适配脚本。适配器只能依赖该模型稳定的输出格式，并满足以下条件：

- 不读取 GT、PDF、评分报告或其他模型的结果。
- 不按文档 ID、公司名或已知答案设置规则。
- 不修正实体、数字、正文、标题文字或表格单元格。
- 不合并、拆分、删除或重排表格；跨页边界必须沿用待评结果本身。
- 只清理表示层信息，例如图片路径/坐标、分页控制符、模型专属容器、展示性 HTML 和预测内部可识别的重复页眉页脚。
- 有信息量的 `text_image`、chart 或图表文字必须保留；纯视觉元素统一为 `![]`。

每次归一化都会输出 `normalization_manifest.json`。标准批量评分拒绝没有 manifest 的目录，也会检查其中的 GT/PDF 依赖、按文档特判、表格边界修改和内容重排标记均为 `false`。

## 2. 当前六个适配器

| 解析结果 | 独立脚本 | 主要格式适配 |
|---|---|---|
| MinerU 3.4.0 Hybrid high | `normalizers/normalize_mineru_hybrid.py` | 展开 `details/summary`；保留 text/chart 内容；图片、流程图及 Mermaid 转 `![]` |
| MinerU 3.4.4 VLM | `normalizers/normalize_mineru_vlm.py` | 与该 VLM 输出协议对应的 details、图片和自然图说明清理 |
| MinerU 3.4.0 Pipeline | `normalizers/normalize_mineru_pipeline.py` | 图片路径转 `![]`；去除展示性 `sup/sub` 外壳 |
| 自研解析模型 | `normalizers/normalize_self_developed.py` | 删除 `pagebreak`；将 `page/x/y/w/h` 图片坐标容器转 `![]` |
| PaddleOCR-VL pagewise | `normalizers/normalize_paddleocr_pagewise.py` | 展开对齐用 `div`；图片路径转 `![]`；不做跨页合并 |
| PaddleOCR-VL cross-page | `normalizers/normalize_paddleocr_cross_page.py` | 展开对齐用 `div`；保留输入中已有的跨页表边界 |

六个脚本共享测试和文件处理工具，但都是可单独运行、可单独审计的入口。新系统应复制 `normalizers/normalize_parser_template.py`，把该解析器确实存在的协议差异写成明确规则。

## 3. 当前变换统计

本次对 36 份预测 Markdown 的归一化包括：

- MinerU Hybrid/VLM 各展开 208 个 `details` 容器，其中保留 27 个文本/图表内容块，181 个纯视觉块转为图片标记。
- MinerU Pipeline 统一 196 个图片标记，展开 49 个展示性 `sup/sub` 外壳。
- 自研结果删除 1,130 个分页标签，将 388 个坐标型图片容器转为图片标记。
- 两组 PaddleOCR 结果各展开 277 个 `div`，统一 108 个图片标记；pagewise 与 cross-page 适配器均不再改变表格边界。

重复页眉页脚只根据同一 Prediction 内部的重复情况判断，并保留首次出现的报告名/公司名；评分器不会再参照 GT 做 Prediction 专属删除。

## 4. 自动校验

适配器在写入每份文件前执行三项校验：

1. 归一化前后的表格数量及二维单元格矩阵一致（仅忽略图片标记周围空白）。
2. 所有非重复页眉页脚类标题的文字、等级和顺序一致。
3. 第二次运行结果与第一次完全一致，即适配器幂等。

任一校验失败都会终止该系统的归一化和后续评分。文件级 SHA-256、变换计数和校验结果记录在各系统的 manifest 中。

## 5. 运行方式

归一化全部正式结果：

```bash
python normalize_all_predictions.py
```

单独运行一个适配器：

```bash
python normalizers/normalize_self_developed.py \
  --input-dir predictions/self-developed-parser \
  --output-dir normalized_predictions/self-developed-parser
```

标准评分读取 `normalized_predictions/`，并把评分器的旧式 Prediction 专属页眉页脚清洗固定为关闭：

```bash
python score_prediction_directory.py \
  --pred-dir normalized_predictions/self-developed-parser \
  --system-name "自研解析模型（版本未记录）" \
  --output-dir scores/self-developed-parser
```
