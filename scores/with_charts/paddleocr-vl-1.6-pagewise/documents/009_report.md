# Financial Markdown Scoring Report

## Overall
- Final Score: 84.9725
- Table Score: 58.0091
- Title Layout Score: 92.5680
- Text Score: 99.3268

## Prediction Cleanup
- Mode: prediction_only_header_footer_cleanup
- Removed pred header/footer lines: 0
- Removed examples:
  - None

## Weights
- Mode: gt_content_information_share
- Table: 31.47%
- Title Layout: 20.00%
- Text: 48.53%
- GT table semantic tokens / grid slots / information units: 27428 / 9218 / 36646
- GT body / active chart / text information units: 56395 / 118 / 56513

## Configuration
- Remove pred header/footer: False
- Normalize images: True
- Score informative charts: True
- Normalize Chinese variants: t2s
- Normalize footnotes: True
- Normalize punctuation: True
- Table pair weights: structure=0.6, content=0.4
- Table aggregation: footprint
- Module weighting: content
- Title layout reserve: 0.2
- Chart scoring mode: included_as_order_aware_numeric_first_token_score
- Detected primary GT / Pred chart blocks: 1 / 0
- Representation-neutral chart score: 0.0000
- GT chart token share inside text module: 0.0021
- Removed primary GT / alt GT / Pred chart blocks: 0 / 0 / 0

## Table Evaluation
- Table GT strategy result: per_table_max
- Primary table score: 58.0091
- Alt table score: 58.0091
- Per-table rule: each predicted table keeps its higher one-to-one pair score from primary or alt GT.
- Per-table selected primary / alt pairs: 182 / 0
- Per-table reference table count: 182
- Matched / missing / extra tables: 182 / 0 / 56
- Table content score: 52.1152
- Table structure score: 61.9384
- Table matrix score: 58.0091
- Table alignment strategy: per_table_best_of_primary_alt_gt_footprint_weighted
- GT footprint total / extra Pred footprint: 21820.8726 / 6297.6135
- Chart-table eligible / auxiliary / matched: 0 / 0 / 0

### Table Matches
- primary GT table 0 -> Pred table 0: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 28, 'cols': 3}, Pred shape={'rows': 28, 'cols': 3}
- primary GT table 1 -> Pred table 1: pair=99.8681, structure=100.0000, content=99.6703, keywords=100.0000, match=99.9604, GT shape={'rows': 13, 'cols': 4}, Pred shape={'rows': 13, 'cols': 4}
- primary GT table 2 -> Pred table 2: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 6, 'cols': 3}, Pred shape={'rows': 6, 'cols': 3}
- primary GT table 3 -> Pred table 3: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 3, 'cols': 2}, Pred shape={'rows': 3, 'cols': 2}
- primary GT table 4 -> Pred table 4: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 3, 'cols': 2}, Pred shape={'rows': 3, 'cols': 2}
- primary GT table 5 -> Pred table 5: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 11, 'cols': 5}, Pred shape={'rows': 11, 'cols': 5}
- primary GT table 6 -> Pred table 6: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 5, 'cols': 5}, Pred shape={'rows': 5, 'cols': 5}
- primary GT table 7 -> Pred table 7: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 11, 'cols': 5}, Pred shape={'rows': 11, 'cols': 5}
- primary GT table 8 -> Pred table 8: pair=95.0365, structure=100.0000, content=87.5912, keywords=100.0000, match=98.5110, GT shape={'rows': 3, 'cols': 6}, Pred shape={'rows': 3, 'cols': 6}
- primary GT table 9 -> Pred table 9: pair=94.8169, structure=100.0000, content=87.0423, keywords=100.0000, match=98.4451, GT shape={'rows': 7, 'cols': 6}, Pred shape={'rows': 7, 'cols': 6}
- primary GT table 10 -> Pred table 10: pair=96.0920, structure=100.0000, content=90.2299, keywords=100.0000, match=98.8276, GT shape={'rows': 4, 'cols': 7}, Pred shape={'rows': 4, 'cols': 7}
- primary GT table 11 -> Pred table 11: pair=95.9570, structure=100.0000, content=89.8925, keywords=100.0000, match=98.7871, GT shape={'rows': 12, 'cols': 6}, Pred shape={'rows': 12, 'cols': 6}
- primary GT table 12 -> Pred table 12: pair=73.2789, structure=77.7778, content=66.5306, keywords=82.5000, match=78.7892, GT shape={'rows': 6, 'cols': 7}, Pred shape={'rows': 4, 'cols': 7}
- primary GT table 13 -> Pred table 14: pair=99.1837, structure=100.0000, content=97.9592, keywords=100.0000, match=99.7551, GT shape={'rows': 5, 'cols': 7}, Pred shape={'rows': 5, 'cols': 7}
- primary GT table 14 -> Pred table 15: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 3, 'cols': 2}, Pred shape={'rows': 3, 'cols': 2}
- primary GT table 15 -> Pred table 16: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 7, 'cols': 4}, Pred shape={'rows': 7, 'cols': 4}
- primary GT table 16 -> Pred table 17: pair=97.9167, structure=100.0000, content=94.7917, keywords=100.0000, match=99.3750, GT shape={'rows': 3, 'cols': 2}, Pred shape={'rows': 3, 'cols': 2}
- primary GT table 17 -> Pred table 18: pair=54.2563, structure=61.9048, content=42.7835, keywords=100.0000, match=78.6579, GT shape={'rows': 7, 'cols': 4}, Pred shape={'rows': 3, 'cols': 4}
- primary GT table 18 -> Pred table 20: pair=99.5676, structure=100.0000, content=98.9189, keywords=100.0000, match=99.8703, GT shape={'rows': 5, 'cols': 5}, Pred shape={'rows': 5, 'cols': 5}
- primary GT table 19 -> Pred table 21: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 11, 'cols': 4}, Pred shape={'rows': 11, 'cols': 4}
- primary GT table 20 -> Pred table 22: pair=95.7746, structure=100.0000, content=89.4366, keywords=100.0000, match=98.7324, GT shape={'rows': 5, 'cols': 5}, Pred shape={'rows': 5, 'cols': 5}
- primary GT table 21 -> Pred table 23: pair=96.3126, structure=100.0000, content=90.7816, keywords=100.0000, match=98.8938, GT shape={'rows': 10, 'cols': 7}, Pred shape={'rows': 10, 'cols': 7}
- primary GT table 22 -> Pred table 24: pair=99.6296, structure=100.0000, content=99.0741, keywords=81.6096, match=90.6937, GT shape={'rows': 2, 'cols': 9}, Pred shape={'rows': 2, 'cols': 9}
- primary GT table 23 -> Pred table 25: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 5, 'cols': 9}, Pred shape={'rows': 5, 'cols': 9}
- primary GT table 24 -> Pred table 26: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 2, 'cols': 3}, Pred shape={'rows': 2, 'cols': 3}
- primary GT table 25 -> Pred table 27: pair=74.6594, structure=77.7778, content=69.9819, keywords=96.5000, match=86.2034, GT shape={'rows': 9, 'cols': 15}, Pred shape={'rows': 6, 'cols': 15}
- primary GT table 26 -> Pred table 29: pair=95.8228, structure=100.0000, content=89.5570, keywords=100.0000, match=98.7468, GT shape={'rows': 4, 'cols': 9}, Pred shape={'rows': 4, 'cols': 9}
- primary GT table 27 -> Pred table 30: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 10, 'cols': 3}, Pred shape={'rows': 10, 'cols': 3}
- primary GT table 28 -> Pred table 31: pair=94.8387, structure=100.0000, content=87.0968, keywords=100.0000, match=98.4516, GT shape={'rows': 5, 'cols': 6}, Pred shape={'rows': 5, 'cols': 6}
- primary GT table 29 -> Pred table 32: pair=44.4720, structure=52.3810, content=32.6087, keywords=96.8182, match=72.2269, GT shape={'rows': 14, 'cols': 13}, Pred shape={'rows': 4, 'cols': 13}

## Title Layout Evaluation
- GT raw heading levels: `[1, 2, 2, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 3, 2, 3, 4, 4, 5, 5, 3, 4, 4, 4, 3, 4, 4, 4, 4, 3, 4, 5, 5, 4, 5, 5, 5, 5, 5, 5, 6, 6, 5, 5, 4, 4, 4, 3, 3, 4, 4, 4, 3, 4, 4, 4, 4, 5, 5, 4, 3, 4, 4, 3, 3, 3, 4, 5, 5, 4, 5, 5, 5, 5, 4, 5, 6, 6, 6, 5, 6, 6, 6, 3, 2, 3, 4, 4, 4, 4, 4, 4, 4, 3, 4, 4, 4, 4, 4, 3, 3, 4, 4, 3, 3, 3, 4, 4, 4, 3, 4, 4, 4, 4, 3] ... (460 total)`
- Pred raw heading levels: `[1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2] ... (455 total)`
- GT relative heading levels: `[1, 2, 2, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 3, 2, 3, 4, 4, 5, 5, 3, 4, 4, 4, 3, 4, 4, 4, 4, 3, 4, 5, 5, 4, 5, 5, 5, 5, 5, 5, 6, 6, 5, 5, 4, 4, 4, 3, 3, 4, 4, 4, 3, 4, 4, 4, 4, 5, 5, 4, 3, 4, 4, 3, 3, 3, 4, 5, 5, 4, 5, 5, 5, 5, 4, 5, 6, 6, 6, 5, 6, 6, 6, 3, 2, 3, 4, 4, 4, 4, 4, 4, 4, 3, 4, 4, 4, 4, 4, 3, 3, 4, 4, 3, 3, 3, 4, 4, 4, 3, 4, 4, 4, 4, 3] ... (460 total)`
- Pred relative heading levels: `[1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2] ... (455 total)`
- Title layout score: 92.5680
- Heading F1 score: 96.6120
- Level accuracy score: 56.6968
- Order score: 96.0870
- Main penalties:
  - 431 aligned headings have different relative levels.
  - 18 GT headings are missing.
  - 13 predicted headings are extra.

## Text Evaluation
- Text mode: body_edit_distance_plus_representation_neutral_chart_tokens
- Text score: 99.3268
- Body-only text score: 99.5346
- Chart score used by text module: 0.0000
- Average edit distance: 0.0047
- Matched / missing / extra blocks: 1 / 0 / 0
- GT / Pred block counts: 1 / 1

### Worst Match Samples
1. op=match, distance=0.0047, GT blocks 0+1, Pred blocks 0+1
   - GT: 福建紫天传媒科技股份有限公司\n\n2022年年度报告\n\n2023-035\n![]\nZTMT\n\n紫天传媒科技\n\n2023年4月28日\n\n2022年年度报告\n\n第一节重要提示目录和释义\n\n公司董事会监事会及董事监事高级管理人员保证年度报告内容的真实...
   - Pred: 福建紫天传媒科技股份有限公司\n\n2022年年度报告\n\n2023-035\n![]\nZTTMT\n\n紫天传媒科技\n\n2023年4月28日\n\n第一节重要提示目录和释义\n\n公司董事会监事会及董事监事高级管理人员保证年度报告内容的真实准确完整不存在虚假记载误...

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
