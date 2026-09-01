# Financial Markdown Scoring Report

## Overall
- Final Score: 82.1168
- Table Score: 55.7417
- Title Layout Score: 92.4943
- Text Score: 98.8072

## Prediction Cleanup
- Mode: prediction_only_header_footer_cleanup
- Removed pred header/footer lines: 0
- Removed examples:
  - None

## Weights
- Mode: gt_content_information_share
- Table: 35.82%
- Title Layout: 20.00%
- Text: 44.18%
- GT table semantic tokens / grid slots / information units: 39051 / 12002 / 51053
- GT body / active chart / text information units: 62756 / 199 / 62955

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
- GT chart token share inside text module: 0.0032
- Removed primary GT / alt GT / Pred chart blocks: 0 / 0 / 0

## Table Evaluation
- Table GT strategy result: per_table_max
- Primary table score: 55.7417
- Alt table score: 55.7417
- Per-table rule: each predicted table keeps its higher one-to-one pair score from primary or alt GT.
- Per-table selected primary / alt pairs: 215 / 0
- Per-table reference table count: 215
- Matched / missing / extra tables: 215 / 0 / 91
- Table content score: 50.0530
- Table structure score: 59.5341
- Table matrix score: 55.7417
- Table alignment strategy: per_table_best_of_primary_alt_gt_footprint_weighted
- GT footprint total / extra Pred footprint: 31133.6739 / 10085.7829
- Chart-table eligible / auxiliary / matched: 0 / 0 / 0

### Table Matches
- primary GT table 0 -> Pred table 0: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 25, 'cols': 3}, Pred shape={'rows': 25, 'cols': 3}
- primary GT table 1 -> Pred table 1: pair=99.2920, structure=100.0000, content=98.2301, keywords=100.0000, match=99.7876, GT shape={'rows': 14, 'cols': 4}, Pred shape={'rows': 14, 'cols': 4}
- primary GT table 2 -> Pred table 2: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 6, 'cols': 3}, Pred shape={'rows': 6, 'cols': 3}
- primary GT table 3 -> Pred table 3: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 3, 'cols': 2}, Pred shape={'rows': 3, 'cols': 2}
- primary GT table 4 -> Pred table 4: pair=97.9026, structure=100.0000, content=94.7566, keywords=100.0000, match=99.3708, GT shape={'rows': 3, 'cols': 2}, Pred shape={'rows': 3, 'cols': 2}
- primary GT table 5 -> Pred table 5: pair=98.9333, structure=100.0000, content=97.3333, keywords=100.0000, match=99.6800, GT shape={'rows': 3, 'cols': 2}, Pred shape={'rows': 3, 'cols': 2}
- primary GT table 6 -> Pred table 6: pair=82.7101, structure=87.8788, content=74.9571, keywords=95.6250, match=90.2013, GT shape={'rows': 11, 'cols': 5}, Pred shape={'rows': 9, 'cols': 5}
- primary GT table 7 -> Pred table 8: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 5, 'cols': 5}, Pred shape={'rows': 5, 'cols': 5}
- primary GT table 8 -> Pred table 10: pair=88.6803, structure=91.6667, content=84.2007, keywords=92.5000, match=91.1874, GT shape={'rows': 8, 'cols': 5}, Pred shape={'rows': 7, 'cols': 5}
- primary GT table 9 -> Pred table 11: pair=99.2173, structure=100.0000, content=98.0433, keywords=100.0000, match=99.7652, GT shape={'rows': 23, 'cols': 2}, Pred shape={'rows': 23, 'cols': 2}
- primary GT table 10 -> Pred table 12: pair=99.7817, structure=100.0000, content=99.4543, keywords=100.0000, match=99.9345, GT shape={'rows': 16, 'cols': 6}, Pred shape={'rows': 16, 'cols': 6}
- primary GT table 11 -> Pred table 14: pair=60.6806, structure=66.6667, content=51.7016, keywords=93.0000, match=78.0375, GT shape={'rows': 14, 'cols': 7}, Pred shape={'rows': 7, 'cols': 7}
- primary GT table 12 -> Pred table 15: pair=99.7838, structure=100.0000, content=99.4595, keywords=100.0000, match=99.9351, GT shape={'rows': 10, 'cols': 6}, Pred shape={'rows': 10, 'cols': 6}
- primary GT table 13 -> Pred table 16: pair=98.8489, structure=100.0000, content=97.1223, keywords=100.0000, match=99.6547, GT shape={'rows': 3, 'cols': 7}, Pred shape={'rows': 3, 'cols': 7}
- primary GT table 14 -> Pred table 17: pair=99.7504, structure=100.0000, content=99.3760, keywords=100.0000, match=99.9251, GT shape={'rows': 12, 'cols': 7}, Pred shape={'rows': 12, 'cols': 7}
- primary GT table 15 -> Pred table 18: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 3, 'cols': 2}, Pred shape={'rows': 3, 'cols': 2}
- primary GT table 16 -> Pred table 19: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 7, 'cols': 4}, Pred shape={'rows': 7, 'cols': 4}
- primary GT table 17 -> Pred table 20: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 3, 'cols': 2}, Pred shape={'rows': 3, 'cols': 2}
- primary GT table 18 -> Pred table 21: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 7, 'cols': 4}, Pred shape={'rows': 7, 'cols': 4}
- primary GT table 19 -> Pred table 22: pair=57.2549, structure=66.6667, content=43.1373, keywords=100.0000, match=80.5098, GT shape={'rows': 6, 'cols': 5}, Pred shape={'rows': 3, 'cols': 5}
- primary GT table 20 -> Pred table 24: pair=99.6244, structure=100.0000, content=99.0610, keywords=100.0000, match=99.8873, GT shape={'rows': 7, 'cols': 4}, Pred shape={'rows': 7, 'cols': 4}
- primary GT table 21 -> Pred table 25: pair=77.1585, structure=81.8182, content=70.1689, keywords=88.3333, match=83.6778, GT shape={'rows': 11, 'cols': 4}, Pred shape={'rows': 8, 'cols': 4}
- primary GT table 22 -> Pred table 27: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 9, 'cols': 5}, Pred shape={'rows': 9, 'cols': 5}
- primary GT table 23 -> Pred table 28: pair=99.7193, structure=100.0000, content=99.2982, keywords=100.0000, match=99.9158, GT shape={'rows': 11, 'cols': 7}, Pred shape={'rows': 11, 'cols': 7}
- primary GT table 24 -> Pred table 29: pair=73.8324, structure=77.7778, content=67.9144, keywords=91.2500, match=83.3303, GT shape={'rows': 9, 'cols': 9}, Pred shape={'rows': 6, 'cols': 9}
- primary GT table 25 -> Pred table 31: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 5, 'cols': 3}, Pred shape={'rows': 5, 'cols': 3}
- primary GT table 26 -> Pred table 32: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 2, 'cols': 3}, Pred shape={'rows': 2, 'cols': 3}
- primary GT table 27 -> Pred table 33: pair=27.3091, structure=41.6667, content=5.7729, keywords=100.0000, match=66.5261, GT shape={'rows': 16, 'cols': 9}, Pred shape={'rows': 2, 'cols': 9}
- primary GT table 28 -> Pred table 38: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 3, 'cols': 3}, Pred shape={'rows': 3, 'cols': 3}
- primary GT table 29 -> Pred table 39: pair=99.3388, structure=100.0000, content=98.3471, keywords=96.1111, match=97.8572, GT shape={'rows': 3, 'cols': 7}, Pred shape={'rows': 3, 'cols': 7}

## Title Layout Evaluation
- GT raw heading levels: `[1, 2, 2, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 3, 3, 2, 3, 4, 4, 4, 5, 5, 5, 4, 5, 5, 3, 4, 4, 3, 4, 4, 4, 4, 4, 2, 3, 4, 5, 6, 6, 5, 5, 4, 4, 5, 5, 3, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 3, 3, 4, 4, 4, 3, 4, 4, 4, 4, 5, 5, 4, 3, 4, 4, 3, 3, 3, 4, 4, 5, 5, 5, 5, 6, 6, 6, 5, 4, 4, 5, 5, 5, 5, 5, 5, 3, 4, 2, 3, 3, 3, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3] ... (512 total)`
- Pred raw heading levels: `[1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 2, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 4, 4, 3, 3, 2, 2, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2] ... (530 total)`
- GT relative heading levels: `[1, 2, 2, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 3, 3, 2, 3, 4, 4, 4, 5, 5, 5, 4, 5, 5, 3, 4, 4, 3, 4, 4, 4, 4, 4, 2, 3, 4, 5, 6, 6, 5, 5, 4, 4, 5, 5, 3, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 3, 3, 4, 4, 4, 3, 4, 4, 4, 4, 5, 5, 4, 3, 4, 4, 3, 3, 3, 4, 4, 5, 5, 5, 5, 6, 6, 6, 5, 4, 4, 5, 5, 5, 5, 5, 5, 3, 4, 2, 3, 3, 3, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3] ... (512 total)`
- Pred relative heading levels: `[1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 2, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 4, 4, 3, 3, 2, 2, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2] ... (530 total)`
- Title layout score: 92.4943
- Heading F1 score: 96.7370
- Level accuracy score: 55.9524
- Order score: 95.0943
- Main penalties:
  - 490 aligned headings have different relative levels.
  - 8 GT headings are missing.
  - 26 predicted headings are extra.

## Text Evaluation
- Text mode: body_edit_distance_plus_representation_neutral_chart_tokens
- Text score: 98.8072
- Body-only text score: 99.1205
- Chart score used by text module: 0.0000
- Average edit distance: 0.0088
- Matched / missing / extra blocks: 1 / 0 / 0
- GT / Pred block counts: 1 / 1

### Worst Match Samples
1. op=match, distance=0.0088, GT blocks 0+1, Pred blocks 0+1
   - GT: 广东万和新电气股份有限公司\n\n2020年年度报告\n![]\nvanward万和\n让家更温暖\n\n2021年4月29日\n\n第一节重要提示目录和释义\n\n公司董事会监事会及董事监事高级管理人员保证年度报告内容的真实准确完整不存在虚假记载误导性陈述或重大遗漏并承担...
   - Pred: 广东万和新电气股份有限公司\n\n2020年年度报告\n\nanward万和让家更温暖\n\n2021年4月29日\n\n第一节重要提示目录和释义\n\n公司董事会监事会及董事监事高级管理人员保证年度报告内容的真实准确完整不存在虚假记载误导性陈述或重大遗漏并承担个别和连带的...

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
