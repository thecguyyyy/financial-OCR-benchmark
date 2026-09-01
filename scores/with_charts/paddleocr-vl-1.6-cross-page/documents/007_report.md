# Financial Markdown Scoring Report

## Overall
- Final Score: 85.1932
- Table Score: 86.5648
- Title Layout Score: 66.6624
- Text Score: 90.7435

## Prediction Cleanup
- Mode: prediction_only_header_footer_cleanup
- Removed pred header/footer lines: 0
- Removed examples:
  - None

## Weights
- Mode: gt_content_information_share
- Table: 17.57%
- Title Layout: 20.00%
- Text: 62.43%
- GT table semantic tokens / grid slots / information units: 27398 / 7850 / 35248
- GT body / active chart / text information units: 125260 / 0 / 125260

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
- Detected primary GT / Pred chart blocks: 3 / 0
- Representation-neutral chart score: 0.0000
- GT chart token share inside text module: 0.0000
- Removed primary GT / alt GT / Pred chart blocks: 0 / 0 / 0

## Table Evaluation
- Table GT strategy result: per_table_max
- Primary table score: 71.1499
- Alt table score: 83.0074
- Per-table rule: each predicted table keeps its higher one-to-one pair score from primary or alt GT.
- Per-table selected primary / alt pairs: 120 / 39
- Per-table reference table count: 144
- Matched / missing / extra tables: 159 / 0 / 2
- Table content score: 84.3838
- Table structure score: 88.0188
- Table matrix score: 86.5648
- Table alignment strategy: per_table_best_of_primary_alt_gt_footprint_weighted
- GT footprint total / extra Pred footprint: 21114.2958 / 16.2448
- Chart-table eligible / auxiliary / matched: 0 / 0 / 0

### Table Matches
- primary GT table 1 -> Pred table 0: pair=66.3128, structure=74.3590, content=54.2435, keywords=75.8333, match=72.6823, GT shape={'rows': 16, 'cols': 6}, Pred shape={'rows': 26, 'cols': 6}
- alt GT table 3 -> Pred table 1: pair=62.6042, structure=69.6970, content=51.9651, keywords=93.9444, match=79.6929, GT shape={'rows': 12, 'cols': 5}, Pred shape={'rows': 22, 'cols': 5}
- alt GT table 5 -> Pred table 2: pair=67.9051, structure=69.6970, content=65.2174, keywords=83.0994, match=75.8606, GT shape={'rows': 12, 'cols': 5}, Pred shape={'rows': 22, 'cols': 5}
- alt GT table 6 -> Pred table 3: pair=65.5717, structure=69.6970, content=59.3838, keywords=98.8596, match=83.0407, GT shape={'rows': 12, 'cols': 5}, Pred shape={'rows': 22, 'cols': 5}
- primary GT table 3 -> Pred table 4: pair=97.7083, structure=97.2222, content=98.4375, keywords=99.5185, match=98.5162, GT shape={'rows': 23, 'cols': 3}, Pred shape={'rows': 24, 'cols': 3}
- primary GT table 4 -> Pred table 5: pair=95.7494, structure=96.4912, content=94.6367, keywords=89.6646, match=92.8554, GT shape={'rows': 18, 'cols': 4}, Pred shape={'rows': 19, 'cols': 4}
- primary GT table 13 -> Pred table 6: pair=80.4076, structure=92.5926, content=62.1302, keywords=98.2895, match=91.7856, GT shape={'rows': 9, 'cols': 5}, Pred shape={'rows': 8, 'cols': 5}
- primary GT table 6 -> Pred table 7: pair=90.0236, structure=92.5926, content=86.1702, keywords=85.3788, match=88.2150, GT shape={'rows': 8, 'cols': 5}, Pred shape={'rows': 9, 'cols': 5}
- primary GT table 7 -> Pred table 8: pair=96.0629, structure=94.8718, content=97.8495, keywords=95.1691, match=95.3778, GT shape={'rows': 24, 'cols': 3}, Pred shape={'rows': 26, 'cols': 3}
- primary GT table 8 -> Pred table 9: pair=93.3883, structure=93.3333, content=93.4708, keywords=84.5556, match=88.9609, GT shape={'rows': 18, 'cols': 4}, Pred shape={'rows': 20, 'cols': 4}
- primary GT table 9 -> Pred table 10: pair=83.3239, structure=86.6667, content=78.3099, keywords=75.8553, match=80.2582, GT shape={'rows': 10, 'cols': 5}, Pred shape={'rows': 8, 'cols': 5}
- primary GT table 10 -> Pred table 11: pair=98.3158, structure=100.0000, content=95.7895, keywords=98.7500, match=98.8697, GT shape={'rows': 9, 'cols': 5}, Pred shape={'rows': 9, 'cols': 5}
- primary GT table 11 -> Pred table 12: pair=96.0771, structure=94.6667, content=98.1928, keywords=93.6705, match=94.5917, GT shape={'rows': 23, 'cols': 3}, Pred shape={'rows': 25, 'cols': 3}
- primary GT table 12 -> Pred table 13: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 18, 'cols': 4}, Pred shape={'rows': 18, 'cols': 4}
- primary GT table 5 -> Pred table 14: pair=65.9272, structure=80.0000, content=44.8179, keywords=66.6892, match=69.1228, GT shape={'rows': 10, 'cols': 5}, Pred shape={'rows': 7, 'cols': 5}
- primary GT table 14 -> Pred table 15: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 8, 'cols': 5}, Pred shape={'rows': 8, 'cols': 5}
- primary GT table 15 -> Pred table 16: pair=97.4614, structure=97.2222, content=97.8202, keywords=97.1295, match=97.2476, GT shape={'rows': 23, 'cols': 4}, Pred shape={'rows': 24, 'cols': 4}
- primary GT table 16 -> Pred table 17: pair=97.3833, structure=96.9697, content=98.0036, keywords=97.0833, match=97.1506, GT shape={'rows': 21, 'cols': 3}, Pred shape={'rows': 22, 'cols': 3}
- primary GT table 17 -> Pred table 18: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 10, 'cols': 3}, Pred shape={'rows': 10, 'cols': 3}
- alt GT table 23 -> Pred table 19: pair=87.5421, structure=100.0000, content=68.8552, keywords=100.0000, match=96.2626, GT shape={'rows': 9, 'cols': 5}, Pred shape={'rows': 9, 'cols': 5}
- alt GT table 24 -> Pred table 20: pair=61.5143, structure=73.3333, content=43.7859, keywords=100.0000, match=83.1209, GT shape={'rows': 10, 'cols': 5}, Pred shape={'rows': 6, 'cols': 5}
- alt GT table 25 -> Pred table 21: pair=92.6267, structure=100.0000, content=81.5668, keywords=100.0000, match=97.7880, GT shape={'rows': 5, 'cols': 5}, Pred shape={'rows': 5, 'cols': 5}
- alt GT table 26 -> Pred table 22: pair=90.8666, structure=100.0000, content=77.1664, keywords=96.7857, match=95.6528, GT shape={'rows': 14, 'cols': 4}, Pred shape={'rows': 14, 'cols': 4}
- alt GT table 27 -> Pred table 23: pair=89.6447, structure=100.0000, content=74.1117, keywords=100.0000, match=96.8934, GT shape={'rows': 4, 'cols': 4}, Pred shape={'rows': 4, 'cols': 4}
- primary GT table 20 -> Pred table 24: pair=92.5800, structure=100.0000, content=81.4499, keywords=87.2704, match=91.4092, GT shape={'rows': 8, 'cols': 9}, Pred shape={'rows': 8, 'cols': 9}
- primary GT table 21 -> Pred table 25: pair=85.8197, structure=100.0000, content=64.5492, keywords=93.0000, match=92.2459, GT shape={'rows': 6, 'cols': 9}, Pred shape={'rows': 6, 'cols': 9}
- primary GT table 22 -> Pred table 26: pair=84.8485, structure=92.5926, content=73.2323, keywords=65.0000, match=76.4731, GT shape={'rows': 5, 'cols': 9}, Pred shape={'rows': 5, 'cols': 8}
- primary GT table 23 -> Pred table 27: pair=90.1162, structure=93.9394, content=84.3813, keywords=93.7963, match=92.7209, GT shape={'rows': 6, 'cols': 11}, Pred shape={'rows': 6, 'cols': 10}
- primary GT table 24 -> Pred table 28: pair=65.4390, structure=77.7778, content=46.9309, keywords=81.9643, match=76.1694, GT shape={'rows': 6, 'cols': 9}, Pred shape={'rows': 9, 'cols': 9}
- primary GT table 26 -> Pred table 29: pair=81.8626, structure=88.8095, content=71.4423, keywords=89.9048, match=87.2731, GT shape={'rows': 13, 'cols': 9}, Pred shape={'rows': 14, 'cols': 10}

## Title Layout Evaluation
- GT raw heading levels: `[1, 2, 1, 1, 2, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 3, 3, 2, 1, 2, 3, 3, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 2, 3, 3, 2, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 2, 3, 3, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3] ... (554 total)`
- Pred raw heading levels: `[2, 3, 5, 5, 5, 4, 5, 5, 5, 5, 4, 5, 5, 5, 4, 5, 5, 4, 5, 5, 4, 5, 4, 4, 4, 4, 5, 5, 5, 5, 4, 4, 5, 2, 4, 2, 4, 5, 4, 5, 4, 5, 5, 5, 5, 5, 5, 5, 5, 4, 5, 5, 5, 4, 2, 4, 5, 4, 5, 4, 5, 5, 5, 5, 5, 5, 5, 5, 4, 5, 5, 5, 4, 5, 4, 5, 4, 5, 4, 5, 5, 5, 5, 5, 4, 5, 5, 5, 4, 5, 5, 5, 5, 4, 4, 4, 5, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 4, 5, 5, 4, 5, 5, 4, 5, 4, 4, 4, 5, 4] ... (1034 total)`
- GT relative heading levels: `[1, 2, 1, 1, 2, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 3, 3, 2, 1, 2, 3, 3, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 2, 3, 3, 2, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 2, 3, 3, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3] ... (554 total)`
- Pred relative heading levels: `[1, 2, 4, 4, 4, 3, 4, 4, 4, 4, 3, 4, 4, 4, 3, 4, 4, 3, 4, 4, 3, 4, 3, 3, 3, 3, 4, 4, 4, 4, 3, 3, 4, 1, 3, 1, 3, 4, 3, 4, 3, 4, 4, 4, 4, 4, 4, 4, 4, 3, 4, 4, 4, 3, 1, 3, 4, 3, 4, 3, 4, 4, 4, 4, 4, 4, 4, 4, 3, 4, 4, 4, 3, 4, 3, 4, 3, 4, 3, 4, 4, 4, 4, 4, 3, 4, 4, 4, 3, 4, 4, 4, 4, 3, 3, 3, 4, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 3, 4, 4, 3, 4, 4, 3, 4, 3, 3, 3, 4, 3] ... (1034 total)`
- Title layout score: 66.6624
- Heading F1 score: 67.1285
- Level accuracy score: 78.0488
- Order score: 51.5474
- Main penalties:
  - 450 aligned headings have different relative levels.
  - 21 GT headings are missing.
  - 501 predicted headings are extra.

## Text Evaluation
- Text mode: body_edit_distance_plus_representation_neutral_chart_tokens
- Text score: 90.7435
- Body-only text score: 90.7435
- Chart score used by text module: 0.0000
- Average edit distance: 0.0926
- Matched / missing / extra blocks: 1 / 0 / 0
- GT / Pred block counts: 1 / 1

### Worst Match Samples
1. op=match, distance=0.0926, GT blocks 0+1, Pred blocks 0+1
   - GT: 美团\n\nMeituan\n\n(于开曼群岛注册成立以不同投票权控制的有限公司)\n\n港币柜台股份代号:3690\n\n人民币柜台股份代号:83690\n![]\nEatBetterLiveBetter\n年度报告\n\n目录\n\n公司资料\n\n财务概要6\n\n主...
   - Pred: 美团Meituan\n\n(于开曼群岛注册成立以不同投票权控制的有限公司)\n\n港币柜台股份代号:3690\n\n人民币柜台股份代号:83690\n![]\n2024年度报告\n\n目录\n\n公司资料2\n财务概要6\n主席报告10\n管理层讨论及分析14\n董事及高级...

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
