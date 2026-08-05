# Financial Announcement Markdown Reconstruction Benchmark

A benchmark for reconstructing Chinese financial-announcement PDFs as Markdown. It evaluates reconstruction fidelity—not summarization quality—across body text, heading hierarchy, and table structure, with particular emphasis on long documents, dense tables, and cross-page tables.

The repository contains six financial-announcement PDFs, two manually reviewed Markdown ground-truth variants per document, six completed parser-output collections, and their scoring artifacts. The headline leaderboard includes only systems that were scored on all six documents; incomplete experiments are excluded.

## Dataset

| ID | Document |
|---|---|
| 005 | Ping An 2023 Interim Report |
| 006 | Alibaba Fiscal Year 2026 Interim Report |
| 007 | Meituan 2024 Annual Report |
| 008 | Xianfeng New Material 2025 Annual Report |
| 009 | Zitian Technology 2022 Annual Report |
| 010 | Vanward Electric 2020 Annual Report |

Each document has two ground-truth (GT) Markdown files:

- **Primary GT** preserves the manually verified original Markdown reconstruction boundaries.
- **Semi-semantic GT** applies an independent-interpretability rule to cross-page tables. A continuation page is treated as a separate table when it has its own title and header and remains understandable on its own; it is therefore not forced to merge with the preceding page.

The two-GT design avoids treating every cross-page layout as a mandatory merge, while also avoiding credit for incorrectly joining unrelated tables.

## Evaluation protocol

The scorer evaluates table fidelity, heading layout, and body-text fidelity independently:

```text
Overall = 40% Tables + 20% Heading Layout + 40% Body Text
```

| Component | Method |
|---|---|
| Tables | HTML tables and Markdown pipe tables are parsed into 2D cell matrices. Each predicted table is matched against candidates from both GT variants using structure and keyword signals, retaining the better candidate. Matching is strictly one-to-one; missing and redundant tables are penalized. A table score comprises structure (60%) and cell content (40%). |
| Heading layout | Heading F1 contributes 80%; relative-level accuracy and order each contribute 10%. Heading text remains part of the body-text evaluation. |
| Body text | After extracted tables are removed, normalized full text is compared by edit distance. Heading text and meaningful textual visual content are retained. |

For tables, the score uses the **best single-table match across the two GT variants**. It does not concatenate multiple predicted fragments into one GT table, so incorrect cross-page splits, repeated tables, and erroneous merges remain visible in the score.

See [SCORING_PROTOCOL.md](SCORING_PROTOCOL.md) for the complete algorithm, normalization rules, and known limitations.

## Completed systems and results

The table reports arithmetic means over all six documents. Scores range from 0 to 100 and use the protocol above, including the best-match-across-two-GTs table strategy.

| Rank | System | Overall | Tables | Heading layout | Body text |
|---:|---|---:|---:|---:|---:|
| 1 | MinerU 3.4.0 — Hybrid backend (`effort=high`; MinerU2.5-Pro-2605-1.2B) | **94.25** | **95.41** | **85.69** | **97.39** |
| 2 | MinerU 3.4.4 — VLM backend (MinerU2.5-Pro-2605-1.2B) | 93.70 | 95.36 | 84.25 | 96.77 |
| 3 | PaddleOCR-VL-1.6-0.9B — cross-page merge | 92.33 | 92.35 | 84.53 | 96.21 |
| 4 | MinerU 3.4.0 — Pipeline backend (`method=auto`, `lang=ch`) | 90.77 | 89.36 | 84.30 | 95.40 |
| 5 | Self-developed parser (version not recorded) | 90.50 | 89.16 | 84.18 | 95.01 |
| 6 | PaddleOCR-VL-1.6-0.9B — no cross-page merge | 87.45 | 80.46 | 83.88 | 96.21 |

### Findings

- The Hybrid configuration obtains the highest overall and table scores on this benchmark, followed closely by the VLM configuration; both achieve body-text means above 96.
- Cross-page merging materially improves PaddleOCR-VL-1.6-0.9B table reconstruction. Against the page-wise output from the same checkpoint, it raises the mean table score by **11.89** points and the overall score by **4.89** points. Both runs have the same 96.21 mean body-text score, indicating that the gain comes from cross-page table post-processing.
- For all structured outputs, body-text fidelity is generally stronger than table and heading-layout fidelity. The principal remaining errors are table splitting/merging, redundant table output, and flattened multi-level headings.

These rankings apply only to this repository's fixed documents, GT variants, and scoring version. They should not be interpreted as a general ranking across layouts, languages, or downstream tasks.

## System names and scope

| System | Confirmed configuration |
|---|---|
| MinerU Hybrid | MinerU `3.4.0`, `hybrid` backend, `effort=high`; VLM checkpoint: `MinerU2.5-Pro-2605-1.2B`. |
| MinerU VLM | MinerU `3.4.4`, `vlm` backend; VLM checkpoint: `MinerU2.5-Pro-2605-1.2B`. |
| MinerU Pipeline | MinerU `3.4.0`, `pipeline` backend, `method=auto`, `lang=ch`. |
| PaddleOCR-VL | Checkpoint: `PaddleOCR-VL-1.6-0.9B`; the two collections differ only in cross-page table post-processing. |
| Self-developed parser | The six outputs are complete, but no publishable checkpoint or version identifier was retained; no architectural claim is made here. |

## Repository layout

```text
data/
  pdf/                         # six source PDFs
  gt/primary/                  # Primary GT
  gt/semi_semantic/            # Semi-semantic GT
predictions/<system>/          # six Markdown files per system
scores/<system>/               # summary and per-document reports
benchmark_scorer.py             # core single-document scorer
score_prediction_directory.py   # score one new parser
score_all_benchmark_systems.py  # rescore all published systems
benchmark_systems.py            # canonical system names
README.md
README_EN.md
SCORING_PROTOCOL.md
```

## Reproducing the scoring

To score a new parser, place its six Markdown outputs in one directory. The preferred names are `005.md` through `010.md`; longer names beginning with the corresponding identifier are also accepted. Run:

```powershell
python score_prediction_directory.py `
  --pred-dir predictions/my_parser `
  --system-name "My Parser 1.0" `
  --output-dir scores/my_parser
```

The standard entry point fixes the dual-GT best-single-table strategy and all weights documented above. It writes `summary.csv`, `summary.json`, `summary.md`, and six per-document reports. To rescore all published systems in the repository, run:

```powershell
python score_all_benchmark_systems.py
```

Do not publish model weights, local environments, cloud logs, page-level intermediate files, or files containing access credentials. Redistribution of the PDFs must comply with the terms of the original disclosure sites and copyright holders.

---

中文版本：[README.md](README.md)
