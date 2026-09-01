# 模型与运行参数核验记录

本文件只记录能够由运行参数、现有产物、配置文件或官方模型卡核对到的名称。没有证据的字段明确写“未留档”，不从预测文件名反推。

## 1. MinerU Hybrid high 结果（`pred`）

- 运行方式：`MinerU 3.4.0`、`backend=hybrid-engine`、`effort=high`、`method=auto`。
- 005–010 在 2026-08-05 重跑时使用 `backend=hybrid-engine`、`effort=high`、`method=auto`；随后 001–004 沿用同一配置补跑。10 份 PDF 均归入同一结果集合。
- 运行时加载的 VLM checkpoint 为 `OpenDataLab/MinerU2.5-Pro-2605-1.2B`，即参数量为 1.2B 的对应 checkpoint。
- 因此 `pred` 的正确公开名称是 `MinerU 3.4.0 — Hybrid backend（effort=high；MinerU2.5-Pro-2605-1.2B）`，不是单独的 MinerU2.5 直跑集合。

官方资料：[MinerU2.5-Pro-2605-1.2B 模型卡](https://huggingface.co/opendatalab/MinerU2.5-Pro-2605-1.2B)。

## 2. MinerU 3.x

MinerU 3.x 的 `pipeline`、`vlm` 是解析 backend，不是两个“参数量模型”。

| 集合 | 本地证据 | 公开名称 | 未确认项 |
|---|---|---|---|
| MinerU VLM 结果 | 原始运行中间 JSON：`_backend=vlm`、`_version_name=3.4.4`；配置文件的 VLM 路径为 MinerU2.5-Pro-2605-1.2B | `MinerU 3.4.4 — VLM backend（MinerU2.5-Pro-2605-1.2B）` | 本次输出未在 middle JSON 内重复写 checkpoint 字段 |
| MinerU Pipeline 结果 | 原始运行中间 JSON：`_backend=pipeline`、`_version_name=3.4.0`；运行参数为 `-m auto -l ch` | `MinerU 3.4.0 — Pipeline backend（method=auto，lang=ch）` | 不适合标注成“0.6B”；pipeline 是 OCR/layout/formula/table 组合管线 |

官方仓库说明了 backend 的定位，并记录了 3.3 的默认 VLM 升级到 `MinerU2.5-Pro-2605-1.2B` 以及 3.4 的 pipeline OCR 升级：[MinerU 官方仓库](https://github.com/opendatalab/MinerU)。本次运行配置也直接指向该 checkpoint，因此这里不是根据文件名推断。

## 3. PaddleOCR-VL

- 官方 checkpoint/模型名：`PaddleOCR-VL-1.6-0.9B`。
- 运行参数记录为 `pipeline_version="v1.6"`、`vl_rec_backend="native"`、`device=gpu:0`、PDF 渲染 DPI=144。
- pagewise 与 cross-page 两组结果使用同一 checkpoint；后者只是额外执行跨页重组/合并后处理，不是第二个模型。
- 原始运行日志记录了 `Creating model: ('PaddleOCR-VL-1.6-0.9B', None, None)` 和 `PP-DocLayoutV3`。

官方资料：[PaddleOCR 官方仓库](https://github.com/PaddlePaddle/PaddleOCR) 和 [PaddleOCR-VL-1.6 模型卡](https://huggingface.co/PaddlePaddle/PaddleOCR-VL-1.6)。

## 4. 自研集合

该结果原来被称为“内网模型”。由于没有可公开核验的模型名、checkpoint、参数量或版本文件，因此公开名称统一为 `自研解析模型（版本未记录）`，不再把“内网”误当成模型名称。
