# Prediction Output Normalization Protocol

The benchmark separates parser-output adaptation from semantic-equivalence scoring. Each parser first runs its own deterministic adapter to produce plain Markdown; every normalized collection then enters the same scorer. This removes output-protocol differences without special-casing missing text, OCR errors, table errors, or heading errors.

## Mandatory constraints

Every scored parser/version must provide an independent adapter that depends only on its stable output format:

- It must not read GT, PDF, score reports, or another parser's output.
- It must not branch on document ID, company name, or known answer content.
- It must not correct entities, numbers, prose, heading text, or table cells.
- It must not merge, split, delete, reorder, or reconstruct tables from GT evidence.
- It may remove representation-only artifacts such as image paths/coordinates, page-control tags, parser containers, presentational HTML, and running headers detected from repetition within the prediction itself.
- It must retain informative `text_image`, chart, and figure text; purely visual elements become `![]`.

Each run emits `normalization_manifest.json`. Standard batch scoring rejects an unmanifested directory and verifies that GT/PDF use, document-specific rules, table-boundary changes, and content reordering are all explicitly marked `false`.

## Published adapters

| Output collection | Independent entry point | Format-specific adaptation |
|---|---|---|
| MinerU 3.4.0 Hybrid high | `normalizers/normalize_mineru_hybrid.py` | Unwrap `details/summary`; retain text/chart content; map images, flowcharts, and Mermaid to `![]` |
| MinerU 3.4.4 VLM | `normalizers/normalize_mineru_vlm.py` | Normalize this VLM format's details blocks, image references, and decorative-image captions |
| MinerU 3.4.0 Pipeline | `normalizers/normalize_mineru_pipeline.py` | Map image paths to `![]`; unwrap presentational `sup/sub` tags |
| Self-developed parser | `normalizers/normalize_self_developed.py` | Remove `pagebreak`; map `page/x/y/w/h` coordinate image containers to `![]` |
| PaddleOCR-VL pagewise | `normalizers/normalize_paddleocr_pagewise.py` | Unwrap alignment `div`; normalize images; never merge page-wise tables |
| PaddleOCR-VL cross-page | `normalizers/normalize_paddleocr_cross_page.py` | Unwrap alignment `div`; preserve the supplied cross-page table boundaries |

The six entry points share validation and file-handling utilities but remain independently runnable and auditable. A new parser should copy `normalizers/normalize_parser_template.py` and implement only transformations supported by that parser's output contract.

## Validation and audit trail

Before writing each file, the framework verifies that:

1. Table counts and 2D cell matrices are unchanged, ignoring only whitespace around the canonical image marker.
2. All headings other than identified duplicate running headers retain their text, level, and order.
3. A second normalization pass is byte-identical to the first.

Any failure stops normalization and scoring. Each manifest records file-level SHA-256 values, transformation counts, and validation results.

Across the current 36 prediction files, the adapters unwrap 208 MinerU details blocks per VLM-style collection, remove 1,130 self-developed-parser page-control tags, normalize 388 coordinate-image containers, and unwrap 277 PaddleOCR alignment divs per Paddle collection. Neither Paddle adapter changes table boundaries.

## Commands

Normalize all published outputs:

```bash
python normalize_all_predictions.py
```

Run one adapter:

```bash
python normalizers/normalize_self_developed.py \
  --input-dir predictions/self-developed-parser \
  --output-dir normalized_predictions/self-developed-parser
```

Score its normalized output. The legacy prediction-only header/footer cleanup remains disabled:

```bash
python score_prediction_directory.py \
  --pred-dir normalized_predictions/self-developed-parser \
  --system-name "Self-developed parser (version not recorded)" \
  --output-dir scores/self-developed-parser
```
