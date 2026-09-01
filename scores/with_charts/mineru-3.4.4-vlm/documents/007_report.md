# Financial Markdown Scoring Report

## Overall
- Final Score: 87.4467
- Table Score: 92.0829
- Title Layout Score: 67.6369
- Text Score: 92.4882

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
- Detected primary GT / Pred chart blocks: 3 / 2
- Representation-neutral chart score: 33.3333
- GT chart token share inside text module: 0.0000
- Removed primary GT / alt GT / Pred chart blocks: 0 / 0 / 0

## Table Evaluation
- Table GT strategy result: per_table_max
- Primary table score: 71.9612
- Alt table score: 90.0211
- Per-table rule: each predicted table keeps its higher one-to-one pair score from primary or alt GT.
- Per-table selected primary / alt pairs: 124 / 45
- Per-table reference table count: 144
- Matched / missing / extra tables: 169 / 0 / 7
- Table content score: 91.0309
- Table structure score: 92.7842
- Table matrix score: 92.0829
- Table alignment strategy: per_table_best_of_primary_alt_gt_footprint_weighted
- GT footprint total / extra Pred footprint: 21114.2958 / 171.9901
- Chart-table eligible / auxiliary / matched: 0 / 1 / 0

### Table Matches
- primary GT table 0 -> Pred table 0: pair=99.6759, structure=100.0000, content=99.1896, keywords=100.0000, match=99.9028, GT shape={'rows': 10, 'cols': 6}, Pred shape={'rows': 10, 'cols': 6}
- primary GT table 1 -> Pred table 1: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 16, 'cols': 6}, Pred shape={'rows': 16, 'cols': 6}
- alt GT table 3 -> Pred table 2: pair=62.6042, structure=69.6970, content=51.9651, keywords=98.9844, match=82.2129, GT shape={'rows': 12, 'cols': 5}, Pred shape={'rows': 22, 'cols': 5}
- alt GT table 4 -> Pred table 3: pair=55.6900, structure=69.6970, content=34.6797, keywords=93.8304, match=77.5616, GT shape={'rows': 12, 'cols': 5}, Pred shape={'rows': 22, 'cols': 5}
- alt GT table 6 -> Pred table 4: pair=65.5717, structure=69.6970, content=59.3838, keywords=98.8596, match=83.0407, GT shape={'rows': 12, 'cols': 5}, Pred shape={'rows': 22, 'cols': 5}
- primary GT table 3 -> Pred table 5: pair=99.9375, structure=100.0000, content=99.8438, keywords=100.0000, match=99.9813, GT shape={'rows': 23, 'cols': 3}, Pred shape={'rows': 23, 'cols': 3}
- primary GT table 4 -> Pred table 6: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 18, 'cols': 4}, Pred shape={'rows': 18, 'cols': 4}
- primary GT table 13 -> Pred table 7: pair=31.9290, structure=40.0000, content=19.8225, keywords=100.0000, match=67.5787, GT shape={'rows': 9, 'cols': 5}, Pred shape={'rows': 2, 'cols': 4}
- primary GT table 5 -> Pred table 8: pair=53.1429, structure=60.0000, content=42.8571, keywords=65.0000, match=60.4429, GT shape={'rows': 10, 'cols': 5}, Pred shape={'rows': 4, 'cols': 5}
- primary GT table 6 -> Pred table 9: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 8, 'cols': 5}, Pred shape={'rows': 8, 'cols': 5}
- primary GT table 7 -> Pred table 10: pair=99.9383, structure=100.0000, content=99.8457, keywords=100.0000, match=99.9815, GT shape={'rows': 24, 'cols': 3}, Pred shape={'rows': 24, 'cols': 3}
- primary GT table 8 -> Pred table 11: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 18, 'cols': 4}, Pred shape={'rows': 18, 'cols': 4}
- primary GT table 9 -> Pred table 13: pair=53.2394, structure=60.0000, content=43.0986, keywords=65.0000, match=60.4718, GT shape={'rows': 10, 'cols': 5}, Pred shape={'rows': 4, 'cols': 5}
- primary GT table 10 -> Pred table 14: pair=89.2398, structure=92.5926, content=84.2105, keywords=72.0851, match=81.3330, GT shape={'rows': 9, 'cols': 5}, Pred shape={'rows': 8, 'cols': 5}
- primary GT table 11 -> Pred table 15: pair=99.8793, structure=100.0000, content=99.6983, keywords=100.0000, match=99.9638, GT shape={'rows': 23, 'cols': 3}, Pred shape={'rows': 23, 'cols': 3}
- primary GT table 12 -> Pred table 16: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 18, 'cols': 4}, Pred shape={'rows': 18, 'cols': 4}
- primary GT table 14 -> Pred table 19: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 8, 'cols': 5}, Pred shape={'rows': 8, 'cols': 5}
- primary GT table 15 -> Pred table 20: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 23, 'cols': 4}, Pred shape={'rows': 23, 'cols': 4}
- primary GT table 16 -> Pred table 21: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 21, 'cols': 3}, Pred shape={'rows': 21, 'cols': 3}
- primary GT table 17 -> Pred table 22: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 10, 'cols': 3}, Pred shape={'rows': 10, 'cols': 3}
- alt GT table 23 -> Pred table 23: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 9, 'cols': 5}, Pred shape={'rows': 9, 'cols': 5}
- alt GT table 24 -> Pred table 24: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 10, 'cols': 5}, Pred shape={'rows': 10, 'cols': 5}
- alt GT table 25 -> Pred table 25: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 5, 'cols': 5}, Pred shape={'rows': 5, 'cols': 5}
- alt GT table 26 -> Pred table 26: pair=99.5855, structure=100.0000, content=98.9637, keywords=100.0000, match=99.8756, GT shape={'rows': 14, 'cols': 4}, Pred shape={'rows': 14, 'cols': 4}
- alt GT table 27 -> Pred table 27: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 4, 'cols': 4}, Pred shape={'rows': 4, 'cols': 4}
- primary GT table 20 -> Pred table 28: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 8, 'cols': 9}, Pred shape={'rows': 8, 'cols': 9}
- primary GT table 21 -> Pred table 29: pair=61.9697, structure=72.2222, content=46.5909, keywords=63.1061, match=64.5884, GT shape={'rows': 6, 'cols': 9}, Pred shape={'rows': 9, 'cols': 10}
- primary GT table 22 -> Pred table 30: pair=89.4949, structure=92.5926, content=84.8485, keywords=65.0000, match=77.8670, GT shape={'rows': 5, 'cols': 9}, Pred shape={'rows': 5, 'cols': 8}
- primary GT table 23 -> Pred table 31: pair=97.7055, structure=100.0000, content=94.2639, keywords=100.0000, match=99.3117, GT shape={'rows': 6, 'cols': 11}, Pred shape={'rows': 6, 'cols': 11}
- primary GT table 24 -> Pred table 32: pair=95.3208, structure=100.0000, content=88.3019, keywords=100.0000, match=98.5962, GT shape={'rows': 6, 'cols': 9}, Pred shape={'rows': 6, 'cols': 9}

## Title Layout Evaluation
- GT raw heading levels: `[1, 2, 1, 1, 2, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 3, 3, 2, 1, 2, 3, 3, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 2, 3, 3, 2, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 2, 3, 3, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3] ... (554 total)`
- Pred raw heading levels: `[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] ... (957 total)`
- GT relative heading levels: `[1, 2, 1, 1, 2, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 3, 3, 2, 1, 2, 3, 3, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 2, 3, 3, 2, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 2, 3, 3, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3] ... (554 total)`
- Pred relative heading levels: `[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] ... (957 total)`
- Title layout score: 67.6369
- Heading F1 score: 70.2846
- Level accuracy score: 58.6064
- Order score: 55.4859
- Main penalties:
  - 515 aligned headings have different relative levels.
  - 23 GT headings are missing.
  - 426 predicted headings are extra.

## Text Evaluation
- Text mode: body_edit_distance_plus_representation_neutral_chart_tokens
- Text score: 92.4882
- Body-only text score: 92.4882
- Chart score used by text module: 33.3333
- Average edit distance: 0.0751
- Matched / missing / extra blocks: 1 / 0 / 0
- GT / Pred block counts: 1 / 1

### Worst Match Samples
1. op=match, distance=0.0751, GT blocks 0+1, Pred blocks 0+1
   - GT: 美团\n\nMeituan\n\n(于开曼群岛注册成立以不同投票权控制的有限公司)\n\n港币柜台股份代号:3690\n\n人民币柜台股份代号:83690\n![]\nEatBetterLiveBetter\n年度报告\n\n目录\n\n公司资料\n\n财务概要6\n\n主...
   - Pred: 美团美团\n\nMeituan\n\n(于开曼群岛注册成立以不同投票权控制的有限公司)\n\n港币柜台股份代号:3690\n\n人民币柜台股份代号:83690\n![]\n#EatBetterLiveBetter\n年度报告\n\n目录\n\n公司资料\n\n财务概要6\n...

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
