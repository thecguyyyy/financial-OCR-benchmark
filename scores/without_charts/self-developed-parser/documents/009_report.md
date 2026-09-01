# Financial Markdown Scoring Report

## Overall
- Final Score: 91.4056
- Table Score: 82.0170
- Title Layout Score: 90.3393
- Text Score: 97.9462

## Prediction Cleanup
- Mode: prediction_only_header_footer_cleanup
- Removed pred header/footer lines: 0
- Removed examples:
  - None

## Weights
- Mode: gt_content_information_share
- Table: 31.51%
- Title Layout: 20.00%
- Text: 48.49%
- GT table semantic tokens / grid slots / information units: 27428 / 9218 / 36646
- GT body / active chart / text information units: 56395 / 0 / 56395

## Configuration
- Remove pred header/footer: False
- Normalize images: True
- Score informative charts: False
- Normalize Chinese variants: t2s
- Normalize footnotes: True
- Normalize punctuation: True
- Table pair weights: structure=0.6, content=0.4
- Table aggregation: footprint
- Module weighting: content
- Title layout reserve: 0.2
- Chart scoring mode: excluded_from_scoring
- Detected primary GT / Pred chart blocks: 1 / 0
- Representation-neutral chart score: 0.0000
- GT chart token share inside text module: 0.0021
- Removed primary GT / alt GT / Pred chart blocks: 1 / 1 / 0

## Table Evaluation
- Table GT strategy result: per_table_max
- Primary table score: 82.0170
- Alt table score: 82.0170
- Per-table rule: each predicted table keeps its higher one-to-one pair score from primary or alt GT.
- Per-table selected primary / alt pairs: 182 / 0
- Per-table reference table count: 182
- Matched / missing / extra tables: 182 / 0 / 15
- Table content score: 79.2181
- Table structure score: 83.8830
- Table matrix score: 82.0170
- Table alignment strategy: per_table_best_of_primary_alt_gt_footprint_weighted
- GT footprint total / extra Pred footprint: 21820.8726 / 1763.3861
- Chart-table eligible / auxiliary / matched: 0 / 0 / 0

### Table Matches
- primary GT table 0 -> Pred table 1: pair=99.9461, structure=100.0000, content=99.8652, keywords=100.0000, match=99.9838, GT shape={'rows': 28, 'cols': 3}, Pred shape={'rows': 28, 'cols': 3}
- primary GT table 1 -> Pred table 2: pair=99.7354, structure=100.0000, content=99.3385, keywords=100.0000, match=99.9206, GT shape={'rows': 13, 'cols': 4}, Pred shape={'rows': 13, 'cols': 4}
- primary GT table 2 -> Pred table 3: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 6, 'cols': 3}, Pred shape={'rows': 6, 'cols': 3}
- primary GT table 3 -> Pred table 4: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 3, 'cols': 2}, Pred shape={'rows': 3, 'cols': 2}
- primary GT table 4 -> Pred table 5: pair=81.2727, structure=83.3333, content=78.1818, keywords=83.1250, match=82.6110, GT shape={'rows': 3, 'cols': 2}, Pred shape={'rows': 4, 'cols': 2}
- primary GT table 5 -> Pred table 6: pair=99.6033, structure=100.0000, content=99.0083, keywords=100.0000, match=99.8810, GT shape={'rows': 11, 'cols': 5}, Pred shape={'rows': 11, 'cols': 5}
- primary GT table 6 -> Pred table 7: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 5, 'cols': 5}, Pred shape={'rows': 5, 'cols': 5}
- primary GT table 7 -> Pred table 8: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 11, 'cols': 5}, Pred shape={'rows': 11, 'cols': 5}
- primary GT table 8 -> Pred table 9: pair=98.7097, structure=100.0000, content=96.7742, keywords=100.0000, match=99.6129, GT shape={'rows': 3, 'cols': 6}, Pred shape={'rows': 3, 'cols': 6}
- primary GT table 9 -> Pred table 10: pair=97.3414, structure=100.0000, content=93.3535, keywords=100.0000, match=99.2024, GT shape={'rows': 7, 'cols': 6}, Pred shape={'rows': 7, 'cols': 6}
- primary GT table 10 -> Pred table 11: pair=96.0920, structure=100.0000, content=90.2299, keywords=100.0000, match=98.8276, GT shape={'rows': 4, 'cols': 7}, Pred shape={'rows': 4, 'cols': 7}
- primary GT table 11 -> Pred table 12: pair=99.6209, structure=100.0000, content=99.0521, keywords=100.0000, match=99.8863, GT shape={'rows': 12, 'cols': 6}, Pred shape={'rows': 12, 'cols': 6}
- primary GT table 12 -> Pred table 13: pair=75.2381, structure=77.7778, content=71.4286, keywords=82.5000, match=79.3770, GT shape={'rows': 6, 'cols': 7}, Pred shape={'rows': 4, 'cols': 7}
- primary GT table 13 -> Pred table 14: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 5, 'cols': 7}, Pred shape={'rows': 5, 'cols': 7}
- primary GT table 14 -> Pred table 15: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 3, 'cols': 2}, Pred shape={'rows': 3, 'cols': 2}
- primary GT table 15 -> Pred table 16: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 7, 'cols': 4}, Pred shape={'rows': 7, 'cols': 4}
- primary GT table 16 -> Pred table 17: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 3, 'cols': 2}, Pred shape={'rows': 3, 'cols': 2}
- primary GT table 17 -> Pred table 18: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 7, 'cols': 4}, Pred shape={'rows': 7, 'cols': 4}
- primary GT table 18 -> Pred table 19: pair=99.5676, structure=100.0000, content=98.9189, keywords=100.0000, match=99.8703, GT shape={'rows': 5, 'cols': 5}, Pred shape={'rows': 5, 'cols': 5}
- primary GT table 19 -> Pred table 20: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 11, 'cols': 4}, Pred shape={'rows': 11, 'cols': 4}
- primary GT table 20 -> Pred table 21: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 5, 'cols': 5}, Pred shape={'rows': 5, 'cols': 5}
- primary GT table 21 -> Pred table 22: pair=99.6499, structure=100.0000, content=99.1247, keywords=100.0000, match=99.8950, GT shape={'rows': 10, 'cols': 7}, Pred shape={'rows': 10, 'cols': 7}
- primary GT table 22 -> Pred table 23: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 2, 'cols': 9}, Pred shape={'rows': 2, 'cols': 9}
- primary GT table 23 -> Pred table 24: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 5, 'cols': 9}, Pred shape={'rows': 5, 'cols': 9}
- primary GT table 24 -> Pred table 25: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 2, 'cols': 3}, Pred shape={'rows': 2, 'cols': 3}
- primary GT table 25 -> Pred table 26: pair=95.3502, structure=93.3333, content=98.3755, keywords=100.0000, match=97.2717, GT shape={'rows': 9, 'cols': 15}, Pred shape={'rows': 10, 'cols': 15}
- primary GT table 26 -> Pred table 27: pair=97.6080, structure=100.0000, content=94.0199, keywords=100.0000, match=99.2824, GT shape={'rows': 4, 'cols': 9}, Pred shape={'rows': 4, 'cols': 9}
- primary GT table 27 -> Pred table 28: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 10, 'cols': 3}, Pred shape={'rows': 10, 'cols': 3}
- primary GT table 28 -> Pred table 29: pair=94.8387, structure=100.0000, content=87.0968, keywords=100.0000, match=98.4516, GT shape={'rows': 5, 'cols': 6}, Pred shape={'rows': 5, 'cols': 6}
- primary GT table 29 -> Pred table 30: pair=95.8739, structure=95.5556, content=96.3514, keywords=100.0000, match=97.8733, GT shape={'rows': 14, 'cols': 13}, Pred shape={'rows': 15, 'cols': 13}

## Title Layout Evaluation
- GT raw heading levels: `[1, 2, 2, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 3, 2, 3, 4, 4, 5, 5, 3, 4, 4, 4, 3, 4, 4, 4, 4, 3, 4, 5, 5, 4, 5, 5, 5, 5, 5, 5, 6, 6, 5, 5, 4, 4, 4, 3, 3, 4, 4, 4, 3, 4, 4, 4, 4, 5, 5, 4, 3, 4, 4, 3, 3, 3, 4, 5, 5, 4, 5, 5, 5, 5, 4, 5, 6, 6, 6, 5, 6, 6, 6, 3, 2, 3, 4, 4, 4, 4, 4, 4, 4, 3, 4, 4, 4, 4, 4, 3, 3, 4, 4, 3, 3, 3, 4, 4, 4, 3, 4, 4, 4, 4, 3] ... (460 total)`
- Pred raw heading levels: `[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2] ... (412 total)`
- GT relative heading levels: `[1, 2, 2, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 3, 2, 3, 4, 4, 5, 5, 3, 4, 4, 4, 3, 4, 4, 4, 4, 3, 4, 5, 5, 4, 5, 5, 5, 5, 5, 5, 6, 6, 5, 5, 4, 4, 4, 3, 3, 4, 4, 4, 3, 4, 4, 4, 4, 5, 5, 4, 3, 4, 4, 3, 3, 3, 4, 5, 5, 4, 5, 5, 5, 5, 4, 5, 6, 6, 6, 5, 6, 6, 6, 3, 2, 3, 4, 4, 4, 4, 4, 4, 4, 3, 4, 4, 4, 4, 4, 3, 3, 4, 4, 3, 3, 3, 4, 4, 4, 3, 4, 4, 4, 4, 3] ... (460 total)`
- Pred relative heading levels: `[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2] ... (412 total)`
- Title layout score: 90.3393
- Heading F1 score: 94.4954
- Level accuracy score: 57.8641
- Order score: 89.5652
- Main penalties:
  - 401 aligned headings have different relative levels.
  - 48 GT headings are missing.

## Text Evaluation
- Text mode: normalized_full_text_preserve_newlines
- Text score: 97.9462
- Body-only text score: 97.9462
- Chart score used by text module: 0.0000
- Average edit distance: 0.0205
- Matched / missing / extra blocks: 1 / 0 / 0
- GT / Pred block counts: 1 / 1

### Worst Match Samples
1. op=match, distance=0.0205, GT blocks 0+1, Pred blocks 0+1
   - GT: 福建紫天传媒科技股份有限公司\n\n2022年年度报告\n\n2023-035\n![]\nZTMT\n\n紫天传媒科技\n\n2023年4月28日\n\n2022年年度报告\n\n第一节重要提示目录和释义\n\n公司董事会监事会及董事监事高级管理人员保证年度报告内容的真实...
   - Pred: 福建紫天传媒科技股份有限公司\n\n2022年年度报告\n\n2023-035\n![]\n2023年4月28日\n\n第一节重要提示目录和释义\n\n公司董事会监事会及董事监事高级管理人员保证年度报告内容的真实准确完整不存在虚假记载误导性陈述或者重大遗漏并承担个别和连带的...

## Notes
- Table score compares extracted HTML and Markdown pipe tables after conversion to cell matrices.
- Table matching is Pred-driven semantic one-to-one: structure and header/row-label keywords select the highest-confidence unused GT candidate.
- Footprint aggregation weights each GT table by sqrt(expanded grid slots x normalized cell characters); unmatched GT footprint receives zero and unmatched Pred footprint enlarges the denominator.
- Content-aware module weighting reserves the configured title-layout share, then splits the remaining score budget between tables and text using Gold semantic tokens plus one structural unit per logical table grid slot.
- With max and two GT files, each predicted table keeps the higher pair score from the two independently one-to-one-matched GT variants.
- A chart-embedded table may match only a Gold table marked as chart-table; once routed, that payload is removed from chart scoring to prevent duplicate credit.
- Table pair score is 60% structure score and 40% content score; table content score uses exact normalized Levenshtein distance on complete flattened table text.
- Title layout score uses heading text only for anchor alignment, then combines heading F1, relative-level accuracy, and order coverage.
- Text score removes tables, keeps heading words, preserves newlines, and scores the full body as one character sequence.
- With score_charts=off, marked chart transcriptions are removed symmetrically before table extraction, heading layout, and body scoring.
- No-value page headers and footers are removed from prediction Markdown only; GT Markdown is kept as the reference answer.
- Current limitations: complex nested tables, heavily malformed HTML, and table semantic equivalence beyond cell text are only approximated.
