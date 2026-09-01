# Financial Document OCR Benchmark 2.0

[中文](README.md) · [Scoring protocol](SCORING_PROTOCOL.md) · [Prediction normalization](PREDICTION_NORMALIZATION_EN.md) · [Model metadata](MODEL_METADATA.md)

This repository evaluates OCR and layout reconstruction from financial PDFs to structured Markdown. Version 2.0 contains four desensitized equity-research reports and six public financial disclosures, covering long-form text, heading hierarchy, complex and cross-page tables, formulas, and informative charts.

The PDF is the only factual source for Gold Markdown. Gold files are manually checked and parser-neutral: they do not inherit coordinates, page markers, local paths, or tool metadata from any parser.

## Dataset

| ID | Type | Document | Pages | Gold characteristics |
|---:|---|---|---:|---|
| 001 | Research | Food and beverage industry report | 29 | 62 informative charts, formulas, complex tables |
| 002 | Research | Media industry report | 17 | 17 informative charts, 6 tables |
| 003 | Research | Innovative-drug value-chain report | 28 | 44 informative charts, 9 tables |
| 004 | Research | Innovative-drug internationalization report | 17 | 12 informative charts, 8 tables |
| 005 | Disclosure | Ping An 2023 interim report | 168 | dual table Gold, long-report structure |
| 006 | Disclosure | Alibaba FY2026 interim report | 83 | dual table Gold, mixed Chinese and English |
| 007 | Disclosure | Meituan 2024 annual report | 345 | dual table Gold, many complex tables |
| 008 | Disclosure | Xianfeng Advanced Material 2025 annual report | 167 | dual table Gold, A-share format |
| 009 | Disclosure | Zitian Technology 2022 annual report | 157 | dual table Gold, A-share format |
| 010 | Disclosure | Vanward 2020 annual report | 210 | dual table Gold, table-heavy and cross-page layouts |

The 001–004 PDFs are desensitized copies; 005–010 are public disclosures.

```text
data/pdf/                         # source PDFs 001–010
data/gt/primary/                  # primary Gold Markdown 001–010
data/gt/semi_semantic/            # alternative table Gold for 005–010
predictions/<system>/             # raw OCR output
normalized_predictions/<system>/  # parser-specific normalized input
scores/with_charts/               # chart-aware evaluation
scores/without_charts/            # chart-excluded evaluation
normalizers/                      # parser adapters and shared engine
```

Research reports 001–004 use one manually audited Gold file. Disclosures 005–010 provide primary and semi-semantic table Gold variants. A continued cross-page section remains separate when it has its own title and header and can be understood independently; each predicted table keeps the better pair score obtained from the two independently one-to-one-matched variants.

## Gold Markdown

The Gold representation is parser-neutral:

- preserve factual body text, heading hierarchy, financial numbers, units, formulas, and table structure;
- represent non-informative images as `![]`;
- represent informative charts as `?[]`, followed by chart titles, legends, axes, units, and readable data transcriptions;
- explicitly mark charts that may also be represented as tables, allowing equivalent prediction tables to match without double credit;
- exclude page numbers, repeated headers and footers, parser tags, coordinates, and local paths;
- never alter factual content to improve a particular parser's score.

## Evaluated systems

Only systems with complete 001–010 outputs are included. Exact versions and run parameters are recorded in [MODEL_METADATA.md](MODEL_METADATA.md).

1. MinerU 3.4.0 — Hybrid backend (effort=high; MinerU2.5-Pro-2605-1.2B)
2. MinerU 3.4.4 — VLM backend (MinerU2.5-Pro-2605-1.2B)
3. MinerU 3.4.0 — Pipeline backend (method=auto, lang=ch)
4. PaddleOCR-VL-1.6-0.9B — cross-page merge
5. PaddleOCR-VL-1.6-0.9B — no cross-page merge
6. Self-developed parser (version not recorded)

## Version 2.0 results

### Informative charts excluded

Marked chart transcriptions are removed symmetrically from Gold and prediction. This view compares body text, headings, and ordinary tables.

| Rank | System | Overall | Table | Heading | Text |
|---:|---|---:|---:|---:|---:|
| 1 | PaddleOCR-VL-1.6-0.9B — cross-page merge | 93.14 | 92.94 | 87.76 | 95.80 |
| 2 | MinerU 3.4.4 — VLM backend | 93.05 | 93.17 | 83.68 | 96.76 |
| 3 | MinerU 3.4.0 — Hybrid backend (effort=high) | 93.01 | 93.19 | 84.79 | 96.38 |
| 4 | MinerU 3.4.0 — Pipeline backend | 91.64 | 86.51 | 87.43 | 95.44 |
| 5 | Self-developed parser | 90.06 | 79.41 | 90.29 | 95.21 |
| 6 | PaddleOCR-VL-1.6-0.9B — no cross-page merge | 89.60 | 79.89 | 86.80 | 95.80 |

### Informative charts included

`?[]` chart transcriptions enter the text-information module. Matching is ordered and one-to-one, prioritizing numeric fidelity and then lexical content. Documents 005–010 contain no independent `?[]` chart objects, so the switch affects only 001–004.

| Rank | System | Overall | Table | Heading | Text and charts |
|---:|---|---:|---:|---:|---:|
| 1 | MinerU 3.4.0 — Hybrid backend (effort=high) | 92.40 | 93.19 | 84.79 | 95.25 |
| 2 | MinerU 3.4.4 — VLM backend | 92.06 | 93.17 | 83.68 | 95.10 |
| 3 | PaddleOCR-VL-1.6-0.9B — cross-page merge | 83.98 | 92.94 | 87.76 | 82.41 |
| 4 | MinerU 3.4.0 — Pipeline backend | 83.00 | 86.51 | 87.43 | 82.44 |
| 5 | Self-developed parser | 81.90 | 79.41 | 90.29 | 82.49 |
| 6 | PaddleOCR-VL-1.6-0.9B — no cross-page merge | 80.76 | 79.89 | 86.80 | 82.41 |

Machine-readable leaderboards and per-document reports are under [`scores/`](scores/). These rankings describe this dataset and protocol only; they are not universal OCR rankings.

## Scoring

Heading layout reserves 20% of the total. The remaining 80% is allocated from each Gold document's information content:

```text
table information = semantic table tokens + expanded logical grid slots
table weight = 80% × table information / (table information + effective text information)
text weight = 80% - table weight
```

In chart-aware mode, Gold chart-transcription tokens enter effective text information.

- Tables: 60% structure and 40% cell content. Structure and keywords constrain candidates before global one-to-one maximum-quality matching. Table aggregation uses `sqrt(logical grid slots × max(normalized cell characters, logical grid slots))`; missing Gold footprint receives zero, while extra prediction footprint enlarges the denominator.
- Headings: heading F1 80%, relative-level accuracy 10%, and order 10%.
- Text: exact Levenshtein similarity on the complete normalized body after removing business tables and retaining heading words. Formula normalization removes representation-only LaTeX differences without changing mathematical tokens.
- Charts: only informative `?[]` transcriptions are scored. Numeric fidelity has priority, and chart-table content is routed to exactly one module.

See [SCORING_PROTOCOL.md](SCORING_PROTOCOL.md) for the complete definition and limitations.

## Parser-specific normalization

Parser protocols differ: MinerU emits `details/summary` containers, PaddleOCR uses alignment `div` elements, and the self-developed parser emits coordinate comments. Direct comparison would incorrectly count these protocol differences as OCR errors. Each system therefore runs through its own adapter before entering the shared scorer.

An adapter may only remove protocol artifacts proven by that parser's output. It cannot read PDFs, Gold, other predictions, document IDs, or historical scores; it cannot repair OCR wording or numbers, split or merge business tables, or reorder content. Every run emits a manifest with rule names, hashes, transformation counts, idempotence checks, and structural-preservation checks. See [PREDICTION_NORMALIZATION_EN.md](PREDICTION_NORMALIZATION_EN.md).

## Reproduction

Python 3.10 or later is recommended:

```bash
python -m pip install -r requirements.txt
python normalize_all_predictions.py
python score_all_benchmark_systems.py --skip-normalization
```

The command produces both `scores/with_charts/` and `scores/without_charts/`. To evaluate a new parser, implement a protocol-only adapter from `normalizers/normalize_parser_template.py`, then run:

```bash
python score_prediction_directory.py \
  --pred-dir normalized_predictions/your-parser \
  --system-name "Your Parser" \
  --score-charts on \
  --allow-unmanifested
```

`--allow-unmanifested` is for local debugging only. A formal submission must include a normalization manifest that passes all constraints.

## Version

Version 2.0.0 adds desensitized research reports, informative-chart scoring, content-aware module weights, table-footprint aggregation, and one unified 001–010 parser-specific normalization workflow. See [CHANGELOG.md](CHANGELOG.md).
