# Financial Markdown Scoring Report

## Overall
- Final Score: 85.8498
- Table Score: 91.1077
- Title Layout Score: 63.9466
- Text Score: 91.5436

## Prediction Cleanup
- Mode: prediction_only_header_footer_cleanup
- Removed pred header/footer lines: 98
- Removed examples:
  - ## 企業管治報告
  - ## 企業管治報告
  - ## 企業管治報告
  - ## 企業管治報告
  - ## 企業管治報告
  - ## 企業管治報告
  - ## 企業管治報告
  - ## 企業管治報告
  - ## 企業管治報告
  - ## 企業管治報告

## Weights
- Table: 40%
- Title Layout: 20%
- Text: 40%

## Configuration
- Remove pred header/footer: True
- Normalize images: True
- Normalize Chinese variants: t2s
- Normalize footnotes: True
- Normalize punctuation: True
- Table pair weights: structure=0.6, content=0.4

## Table Evaluation
- Table GT strategy result: per_table_max
- Primary table score: 67.3094
- Alt table score: 82.6478
- Per-table rule: each predicted table keeps its higher one-to-one pair score from primary or alt GT.
- Per-table selected primary / alt pairs: 123 / 47
- Per-table reference table count: 141
- Matched / missing / extra tables: 170 / 0 / 5
- Table content score: 87.9569
- Table structure score: 93.2083
- Table matrix score: 91.1077
- Table alignment strategy: per_table_best_of_primary_alt_one_to_one

### Table Matches
- primary GT table 0 -> Pred table 1: pair=98.9015, structure=100.0000, content=97.2536, keywords=95.6250, match=97.4830, GT shape={'rows': 10, 'cols': 6}, Pred shape={'rows': 10, 'cols': 6}
- primary GT table 1 -> Pred table 2: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 16, 'cols': 6}, Pred shape={'rows': 16, 'cols': 6}
- alt GT table 2 -> Pred table 3: pair=92.5229, structure=94.4444, content=89.6406, keywords=91.9683, match=92.6299, GT shape={'rows': 11, 'cols': 5}, Pred shape={'rows': 12, 'cols': 5}
- alt GT table 3 -> Pred table 4: pair=92.6499, structure=94.4444, content=89.9582, keywords=95.4844, match=94.4261, GT shape={'rows': 12, 'cols': 5}, Pred shape={'rows': 11, 'cols': 5}
- alt GT table 4 -> Pred table 5: pair=92.2981, structure=94.4444, content=89.0785, keywords=89.9415, match=91.5491, GT shape={'rows': 12, 'cols': 5}, Pred shape={'rows': 11, 'cols': 5}
- alt GT table 5 -> Pred table 6: pair=92.9915, structure=94.4444, content=90.8120, keywords=98.8596, match=96.2161, GT shape={'rows': 12, 'cols': 5}, Pred shape={'rows': 11, 'cols': 5}
- alt GT table 6 -> Pred table 7: pair=93.8462, structure=94.4444, content=92.9487, keywords=100.0000, match=97.0427, GT shape={'rows': 12, 'cols': 5}, Pred shape={'rows': 11, 'cols': 5}
- alt GT table 7 -> Pred table 8: pair=93.2065, structure=94.4444, content=91.3495, keywords=89.9415, match=91.8216, GT shape={'rows': 12, 'cols': 5}, Pred shape={'rows': 11, 'cols': 5}
- primary GT table 3 -> Pred table 9: pair=97.4017, structure=97.2222, content=97.6708, keywords=85.5324, match=91.4312, GT shape={'rows': 23, 'cols': 3}, Pred shape={'rows': 24, 'cols': 3}
- primary GT table 4 -> Pred table 11: pair=61.0458, structure=70.3704, content=47.0588, keywords=83.1111, match=73.9434, GT shape={'rows': 18, 'cols': 4}, Pred shape={'rows': 10, 'cols': 4}
- primary GT table 5 -> Pred table 12: pair=90.1436, structure=93.3333, content=85.3591, keywords=70.1364, match=80.7779, GT shape={'rows': 10, 'cols': 5}, Pred shape={'rows': 9, 'cols': 5}
- primary GT table 6 -> Pred table 13: pair=88.1818, structure=92.5926, content=81.5657, keywords=72.0851, match=81.0156, GT shape={'rows': 8, 'cols': 5}, Pred shape={'rows': 9, 'cols': 5}
- primary GT table 7 -> Pred table 14: pair=99.6923, structure=100.0000, content=99.2308, keywords=96.1111, match=97.9632, GT shape={'rows': 24, 'cols': 3}, Pred shape={'rows': 24, 'cols': 3}
- primary GT table 8 -> Pred table 16: pair=62.0833, structure=70.3704, content=49.6528, keywords=83.1111, match=74.2546, GT shape={'rows': 18, 'cols': 4}, Pred shape={'rows': 10, 'cols': 4}
- primary GT table 9 -> Pred table 17: pair=90.1111, structure=93.3333, content=85.2778, keywords=70.1364, match=80.7682, GT shape={'rows': 10, 'cols': 5}, Pred shape={'rows': 9, 'cols': 5}
- primary GT table 10 -> Pred table 18: pair=98.6735, structure=100.0000, content=96.6837, keywords=100.0000, match=99.6020, GT shape={'rows': 9, 'cols': 5}, Pred shape={'rows': 9, 'cols': 5}
- primary GT table 11 -> Pred table 19: pair=99.7587, structure=100.0000, content=99.3967, keywords=94.1667, match=97.0110, GT shape={'rows': 23, 'cols': 3}, Pred shape={'rows': 23, 'cols': 3}
- primary GT table 12 -> Pred table 20: pair=59.7849, structure=66.6667, content=49.4624, keywords=100.0000, match=81.2688, GT shape={'rows': 18, 'cols': 4}, Pred shape={'rows': 9, 'cols': 4}
- primary GT table 13 -> Pred table 22: pair=97.4344, structure=100.0000, content=93.5860, keywords=86.7083, match=92.5845, GT shape={'rows': 9, 'cols': 5}, Pred shape={'rows': 9, 'cols': 5}
- primary GT table 14 -> Pred table 23: pair=90.7298, structure=92.5926, content=87.9357, keywords=75.5851, match=83.5300, GT shape={'rows': 8, 'cols': 5}, Pred shape={'rows': 9, 'cols': 5}
- primary GT table 15 -> Pred table 24: pair=95.8136, structure=97.2222, content=93.7008, keywords=97.6667, match=97.0219, GT shape={'rows': 23, 'cols': 4}, Pred shape={'rows': 24, 'cols': 4}
- primary GT table 16 -> Pred table 25: pair=99.2727, structure=100.0000, content=98.1818, keywords=100.0000, match=99.7818, GT shape={'rows': 21, 'cols': 3}, Pred shape={'rows': 21, 'cols': 3}
- primary GT table 17 -> Pred table 26: pair=92.7105, structure=93.3333, content=91.7763, keywords=91.2500, match=92.1048, GT shape={'rows': 10, 'cols': 3}, Pred shape={'rows': 9, 'cols': 3}
- alt GT table 23 -> Pred table 27: pair=91.5873, structure=100.0000, content=78.9683, keywords=100.0000, match=97.4762, GT shape={'rows': 9, 'cols': 5}, Pred shape={'rows': 9, 'cols': 5}
- alt GT table 24 -> Pred table 28: pair=66.0268, structure=73.3333, content=55.0669, keywords=100.0000, match=84.4747, GT shape={'rows': 10, 'cols': 5}, Pred shape={'rows': 6, 'cols': 5}
- alt GT table 25 -> Pred table 29: pair=94.7739, structure=100.0000, content=86.9347, keywords=100.0000, match=98.4322, GT shape={'rows': 5, 'cols': 5}, Pred shape={'rows': 5, 'cols': 5}
- alt GT table 26 -> Pred table 30: pair=95.0693, structure=100.0000, content=87.6733, keywords=100.0000, match=98.5208, GT shape={'rows': 14, 'cols': 4}, Pred shape={'rows': 14, 'cols': 4}
- alt GT table 27 -> Pred table 31: pair=78.6019, structure=86.6667, content=66.5049, keywords=84.0278, match=82.9278, GT shape={'rows': 4, 'cols': 4}, Pred shape={'rows': 5, 'cols': 4}
- primary GT table 20 -> Pred table 32: pair=94.2964, structure=92.5926, content=96.8520, keywords=96.5000, match=95.0574, GT shape={'rows': 8, 'cols': 9}, Pred shape={'rows': 9, 'cols': 9}
- primary GT table 21 -> Pred table 33: pair=80.9563, structure=88.8889, content=69.0574, keywords=93.0000, match=88.5647, GT shape={'rows': 6, 'cols': 9}, Pred shape={'rows': 5, 'cols': 9}

## Title Layout Evaluation
- GT raw heading levels: `[1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2] ... (502 total)`
- Pred raw heading levels: `[1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2] ... (996 total)`
- GT relative heading levels: `[1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2] ... (502 total)`
- Pred relative heading levels: `[1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2] ... (996 total)`
- Title layout score: 63.9466
- Heading F1 score: 63.5514
- Level accuracy score: 83.2633
- Order score: 47.7912
- Main penalties:
  - 128 aligned headings have different relative levels.
  - 26 GT headings are missing.
  - 520 predicted headings are extra.

## Text Evaluation
- Text mode: normalized_full_text_preserve_newlines
- Text score: 91.5436
- Average edit distance: 0.0846
- Matched / missing / extra blocks: 1 / 0 / 0
- GT / Pred block counts: 1 / 1

### Worst Match Samples
1. op=match, distance=0.0846, GT blocks 0+1, Pred blocks 0+1
   - GT: 美团\n\nMeituan\n\n(于开曼群岛注册成立以不同投票权控制的有限公司)\n\n港币柜台股份代号:3690\n\n人民币柜台股份代号:83690\n![]\n#EatBetterLiveBetter\n年度报告\n\n目录\n\n公司资料\n\n财务概要6\n\n...
   - Pred: 110110705\n\n美团\n\nMeituan\n\n(于开曼群岛注册成立以不同投票权控制的有限公司)\n\n港币柜台股份代号:3690\n\n人民币柜台股份代号:83690\n\n119322209\n\n120451405\n\n132612430\n\n1067...

## Notes
- Table score compares extracted HTML and Markdown pipe tables after conversion to cell matrices.
- With primary or alt strategy, table matching is GT-driven one-to-one: each GT table chooses one best unused Pred table.
- With max and two GT files, each predicted table keeps the higher pair score from the two independently one-to-one-matched GT variants.
- Table pair score is 60% structure score and 40% content score; table content score uses normalized edit distance on flattened table text.
- Title layout score uses heading text only for anchor alignment, then combines heading F1, relative-level accuracy, and order coverage.
- Text score removes tables, keeps heading words, preserves newlines, and scores the full body as one character sequence.
- No-value page headers and footers are removed from prediction Markdown only; GT Markdown is kept as the reference answer.
- Current limitations: complex nested tables, heavily malformed HTML, and table semantic equivalence beyond cell text are only approximated.
