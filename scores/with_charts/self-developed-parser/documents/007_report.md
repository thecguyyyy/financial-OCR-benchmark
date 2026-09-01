# Financial Markdown Scoring Report

## Overall
- Final Score: 91.7965
- Table Score: 90.8057
- Title Layout Score: 85.9054
- Text Score: 93.9278

## Prediction Cleanup
- Mode: prediction_only_header_footer_cleanup
- Removed pred header/footer lines: 0
- Removed examples:
  - None

## Weights
- Mode: gt_content_information_share
- Table: 16.87%
- Title Layout: 20.00%
- Text: 63.13%
- GT table semantic tokens / grid slots / information units: 26334 / 7679 / 34013
- GT body / active chart / text information units: 125258 / 1978 / 127236

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
- GT chart token share inside text module: 0.0155
- Removed primary GT / alt GT / Pred chart blocks: 0 / 0 / 0

## Table Evaluation
- Table GT strategy result: per_table_max
- Primary table score: 70.2285
- Alt table score: 89.8036
- Per-table rule: each predicted table keeps its higher one-to-one pair score from primary or alt GT.
- Per-table selected primary / alt pairs: 123 / 47
- Per-table reference table count: 141
- Matched / missing / extra tables: 170 / 0 / 5
- Table content score: 88.8165
- Table structure score: 92.1319
- Table matrix score: 90.8057
- Table alignment strategy: per_table_best_of_primary_alt_gt_footprint_weighted
- GT footprint total / extra Pred footprint: 20692.7558 / 381.7836
- Chart-table eligible / auxiliary / matched: 0 / 0 / 0

### Table Matches
- primary GT table 0 -> Pred table 1: pair=99.6759, structure=100.0000, content=99.1896, keywords=100.0000, match=99.9028, GT shape={'rows': 10, 'cols': 6}, Pred shape={'rows': 10, 'cols': 6}
- primary GT table 1 -> Pred table 2: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 16, 'cols': 6}, Pred shape={'rows': 16, 'cols': 6}
- alt GT table 2 -> Pred table 3: pair=92.9847, structure=94.4444, content=90.7950, keywords=91.9683, match=92.7684, GT shape={'rows': 11, 'cols': 5}, Pred shape={'rows': 12, 'cols': 5}
- alt GT table 3 -> Pred table 4: pair=93.5639, structure=94.4444, content=92.2432, keywords=95.4844, match=94.7002, GT shape={'rows': 12, 'cols': 5}, Pred shape={'rows': 11, 'cols': 5}
- alt GT table 4 -> Pred table 5: pair=92.9680, structure=94.4444, content=90.7534, keywords=89.9415, match=91.7500, GT shape={'rows': 12, 'cols': 5}, Pred shape={'rows': 11, 'cols': 5}
- alt GT table 5 -> Pred table 6: pair=93.9258, structure=94.4444, content=93.1478, keywords=98.8596, match=96.4964, GT shape={'rows': 12, 'cols': 5}, Pred shape={'rows': 11, 'cols': 5}
- alt GT table 6 -> Pred table 7: pair=94.7823, structure=94.4444, content=95.2891, keywords=100.0000, match=97.3236, GT shape={'rows': 12, 'cols': 5}, Pred shape={'rows': 11, 'cols': 5}
- alt GT table 7 -> Pred table 8: pair=93.8889, structure=94.4444, content=93.0556, keywords=89.9415, match=92.0263, GT shape={'rows': 12, 'cols': 5}, Pred shape={'rows': 11, 'cols': 5}
- primary GT table 3 -> Pred table 9: pair=97.6480, structure=97.2222, content=98.2866, keywords=91.7546, match=94.6161, GT shape={'rows': 23, 'cols': 3}, Pred shape={'rows': 24, 'cols': 3}
- primary GT table 4 -> Pred table 11: pair=61.2534, structure=70.3704, content=47.5779, keywords=83.1111, match=74.0057, GT shape={'rows': 18, 'cols': 4}, Pred shape={'rows': 10, 'cols': 4}
- primary GT table 5 -> Pred table 12: pair=91.6303, structure=93.3333, content=89.0756, keywords=70.1364, match=81.2240, GT shape={'rows': 10, 'cols': 5}, Pred shape={'rows': 9, 'cols': 5}
- primary GT table 6 -> Pred table 13: pair=89.3056, structure=92.5926, content=84.3750, keywords=72.0851, match=81.3528, GT shape={'rows': 8, 'cols': 5}, Pred shape={'rows': 9, 'cols': 5}
- primary GT table 7 -> Pred table 14: pair=99.9383, structure=100.0000, content=99.8457, keywords=100.0000, match=99.9815, GT shape={'rows': 24, 'cols': 3}, Pred shape={'rows': 24, 'cols': 3}
- primary GT table 8 -> Pred table 16: pair=62.2917, structure=70.3704, content=50.1736, keywords=83.1111, match=74.3171, GT shape={'rows': 18, 'cols': 4}, Pred shape={'rows': 10, 'cols': 4}
- primary GT table 9 -> Pred table 17: pair=91.6056, structure=93.3333, content=89.0141, keywords=70.1364, match=81.2165, GT shape={'rows': 10, 'cols': 5}, Pred shape={'rows': 9, 'cols': 5}
- primary GT table 10 -> Pred table 18: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 9, 'cols': 5}, Pred shape={'rows': 9, 'cols': 5}
- primary GT table 11 -> Pred table 19: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 23, 'cols': 3}, Pred shape={'rows': 23, 'cols': 3}
- primary GT table 12 -> Pred table 20: pair=60.0000, structure=66.6667, content=50.0000, keywords=100.0000, match=81.3333, GT shape={'rows': 18, 'cols': 4}, Pred shape={'rows': 9, 'cols': 4}
- primary GT table 13 -> Pred table 22: pair=98.4615, structure=100.0000, content=96.1538, keywords=86.7083, match=92.8926, GT shape={'rows': 9, 'cols': 5}, Pred shape={'rows': 9, 'cols': 5}
- primary GT table 14 -> Pred table 23: pair=91.2195, structure=92.5926, content=89.1599, keywords=75.5851, match=83.6769, GT shape={'rows': 8, 'cols': 5}, Pred shape={'rows': 9, 'cols': 5}
- primary GT table 15 -> Pred table 24: pair=95.9530, structure=97.2222, content=94.0492, keywords=97.6667, match=97.0637, GT shape={'rows': 23, 'cols': 4}, Pred shape={'rows': 24, 'cols': 4}
- primary GT table 16 -> Pred table 25: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 21, 'cols': 3}, Pred shape={'rows': 21, 'cols': 3}
- primary GT table 17 -> Pred table 26: pair=92.9737, structure=93.3333, content=92.4342, keywords=91.2500, match=92.1838, GT shape={'rows': 10, 'cols': 3}, Pred shape={'rows': 9, 'cols': 3}
- alt GT table 23 -> Pred table 27: pair=88.2639, structure=100.0000, content=70.6597, keywords=100.0000, match=96.4792, GT shape={'rows': 9, 'cols': 5}, Pred shape={'rows': 9, 'cols': 5}
- alt GT table 24 -> Pred table 28: pair=62.5086, structure=73.3333, content=46.2715, keywords=100.0000, match=83.4192, GT shape={'rows': 10, 'cols': 5}, Pred shape={'rows': 6, 'cols': 5}
- alt GT table 25 -> Pred table 29: pair=93.5545, structure=100.0000, content=83.8863, keywords=100.0000, match=98.0663, GT shape={'rows': 5, 'cols': 5}, Pred shape={'rows': 5, 'cols': 5}
- alt GT table 26 -> Pred table 30: pair=91.4403, structure=100.0000, content=78.6008, keywords=100.0000, match=97.4321, GT shape={'rows': 14, 'cols': 4}, Pred shape={'rows': 14, 'cols': 4}
- alt GT table 27 -> Pred table 31: pair=75.8261, structure=86.6667, content=59.5652, keywords=84.0278, match=82.0951, GT shape={'rows': 4, 'cols': 4}, Pred shape={'rows': 5, 'cols': 4}
- primary GT table 20 -> Pred table 32: pair=95.4280, structure=92.5926, content=99.6812, keywords=98.2500, match=96.2719, GT shape={'rows': 8, 'cols': 9}, Pred shape={'rows': 9, 'cols': 9}
- primary GT table 21 -> Pred table 33: pair=81.7760, structure=88.8889, content=71.1066, keywords=96.5000, match=90.5606, GT shape={'rows': 6, 'cols': 9}, Pred shape={'rows': 5, 'cols': 9}

## Title Layout Evaluation
- GT raw heading levels: `[1, 2, 1, 1, 2, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 3, 3, 2, 1, 2, 3, 3, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 2, 3, 3, 2, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 2, 3, 3, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3] ... (554 total)`
- Pred raw heading levels: `[1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2] ... (639 total)`
- GT relative heading levels: `[1, 2, 1, 1, 2, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 3, 3, 2, 1, 2, 3, 3, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 2, 3, 3, 2, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 2, 3, 3, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3] ... (554 total)`
- Pred relative heading levels: `[1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2] ... (639 total)`
- Title layout score: 85.9054
- Heading F1 score: 87.5105
- Level accuracy score: 77.2797
- Order score: 81.6901
- Main penalties:
  - 372 aligned headings have different relative levels.
  - 32 GT headings are missing.
  - 117 predicted headings are extra.

## Text Evaluation
- Text mode: body_edit_distance_plus_representation_neutral_chart_tokens
- Text score: 93.9278
- Body-only text score: 95.4111
- Chart score used by text module: 0.0000
- Average edit distance: 0.0459
- Matched / missing / extra blocks: 1 / 0 / 0
- GT / Pred block counts: 1 / 1

### Worst Match Samples
1. op=match, distance=0.0459, GT blocks 0+1, Pred blocks 0+1
   - GT: 美团\n\nMeituan\n\n(于开曼群岛注册成立以不同投票权控制的有限公司)\n\n港币柜台股份代号:3690\n\n人民币柜台股份代号:83690\n![]\nEatBetterLiveBetter\n年度报告\n\n目录\n\n公司资料\n\n财务概要6\n\n主...
   - Pred: ![]\n美团\n\nMeituan\n\n(于开曼群岛注册成立以不同投票权控制的有限公司)\n\n港币柜台股份代号:3690\n\n人民币柜台股份代号:83690\n![]\n年度报告\n\n目录\n\n公司资料\n\n董事会\n\n执行董事\n\n王兴先生(董事长兼首席...

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
