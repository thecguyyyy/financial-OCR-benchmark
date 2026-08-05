# Financial Markdown Scoring Report

## Overall
- Final Score: 83.3663
- Table Score: 85.1511
- Title Layout Score: 65.0539
- Text Score: 90.7376

## Prediction Cleanup
- Mode: prediction_only_header_footer_cleanup
- Removed pred header/footer lines: 64
- Removed examples:
  - ## 主席報告
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
- Primary table score: 65.2941
- Alt table score: 58.0736
- Per-table rule: each predicted table keeps its higher one-to-one pair score from primary or alt GT.
- Per-table selected primary / alt pairs: 120 / 41
- Per-table reference table count: 141
- Matched / missing / extra tables: 161 / 0 / 0
- Table content score: 79.6431
- Table structure score: 88.8230
- Table matrix score: 85.1511
- Table alignment strategy: per_table_best_of_primary_alt_one_to_one

### Table Matches
- primary GT table 0 -> Pred table 0: pair=94.6840, structure=100.0000, content=86.7099, keywords=91.2500, match=94.0302, GT shape={'rows': 10, 'cols': 6}, Pred shape={'rows': 10, 'cols': 6}
- primary GT table 1 -> Pred table 1: pair=86.7838, structure=88.6574, content=83.9735, keywords=80.8333, match=84.1833, GT shape={'rows': 16, 'cols': 6}, Pred shape={'rows': 18, 'cols': 5}
- alt GT table 3 -> Pred table 2: pair=56.1173, structure=61.2821, content=48.3703, keywords=92.4375, match=75.3104, GT shape={'rows': 12, 'cols': 5}, Pred shape={'rows': 26, 'cols': 4}
- alt GT table 5 -> Pred table 3: pair=60.9010, structure=62.6667, content=58.2524, keywords=84.2398, match=72.9235, GT shape={'rows': 12, 'cols': 5}, Pred shape={'rows': 25, 'cols': 4}
- alt GT table 6 -> Pred table 4: pair=59.7970, structure=65.3333, content=51.4925, keywords=91.5497, match=76.7806, GT shape={'rows': 12, 'cols': 5}, Pred shape={'rows': 25, 'cols': 5}
- primary GT table 7 -> Pred table 5: pair=87.2317, structure=94.8718, content=75.7716, keywords=94.7183, match=92.5030, GT shape={'rows': 24, 'cols': 3}, Pred shape={'rows': 26, 'cols': 3}
- primary GT table 4 -> Pred table 6: pair=86.7757, structure=87.8788, content=85.1211, keywords=100.0000, match=93.6085, GT shape={'rows': 18, 'cols': 4}, Pred shape={'rows': 22, 'cols': 4}
- primary GT table 5 -> Pred table 7: pair=91.2707, structure=100.0000, content=78.1768, keywords=76.2403, match=85.5014, GT shape={'rows': 10, 'cols': 5}, Pred shape={'rows': 10, 'cols': 5}
- primary GT table 10 -> Pred table 8: pair=82.7708, structure=93.3333, content=66.9271, keywords=80.9048, match=83.9503, GT shape={'rows': 9, 'cols': 5}, Pred shape={'rows': 10, 'cols': 5}
- primary GT table 3 -> Pred table 9: pair=88.0637, structure=94.6667, content=78.1591, keywords=100.0000, match=95.3525, GT shape={'rows': 23, 'cols': 3}, Pred shape={'rows': 25, 'cols': 3}
- primary GT table 8 -> Pred table 10: pair=56.7551, structure=87.8788, content=10.0694, keywords=100.0000, match=84.6023, GT shape={'rows': 18, 'cols': 4}, Pred shape={'rows': 22, 'cols': 4}
- primary GT table 9 -> Pred table 11: pair=88.5556, structure=100.0000, content=71.3889, keywords=76.2403, match=84.6868, GT shape={'rows': 10, 'cols': 5}, Pred shape={'rows': 10, 'cols': 5}
- primary GT table 6 -> Pred table 12: pair=70.1707, structure=86.6667, content=45.4268, keywords=54.3810, match=65.5751, GT shape={'rows': 8, 'cols': 5}, Pred shape={'rows': 10, 'cols': 4}
- primary GT table 11 -> Pred table 13: pair=86.2632, structure=100.0000, content=65.6581, keywords=100.0000, match=95.8790, GT shape={'rows': 23, 'cols': 3}, Pred shape={'rows': 23, 'cols': 3}
- alt GT table 17 -> Pred table 14: pair=33.4615, structure=43.4343, content=18.5022, keywords=87.8289, match=62.6398, GT shape={'rows': 18, 'cols': 4}, Pred shape={'rows': 22, 'cols': 15}
- primary GT table 13 -> Pred table 15: pair=82.2391, structure=93.3333, content=65.5977, keywords=51.4583, match=69.0675, GT shape={'rows': 9, 'cols': 5}, Pred shape={'rows': 10, 'cols': 5}
- primary GT table 14 -> Pred table 16: pair=84.9129, structure=86.6667, content=82.2823, keywords=80.9470, match=83.2807, GT shape={'rows': 8, 'cols': 5}, Pred shape={'rows': 10, 'cols': 5}
- primary GT table 15 -> Pred table 17: pair=90.7584, structure=97.2222, content=81.0627, keywords=86.1015, match=89.7227, GT shape={'rows': 23, 'cols': 4}, Pred shape={'rows': 24, 'cols': 4}
- primary GT table 16 -> Pred table 18: pair=96.0727, structure=100.0000, content=90.1818, keywords=100.0000, match=98.8218, GT shape={'rows': 21, 'cols': 3}, Pred shape={'rows': 21, 'cols': 3}
- primary GT table 17 -> Pred table 19: pair=88.6882, structure=88.8889, content=88.3871, keywords=100.0000, match=94.3842, GT shape={'rows': 10, 'cols': 3}, Pred shape={'rows': 12, 'cols': 3}
- alt GT table 23 -> Pred table 20: pair=61.8729, structure=56.7251, content=69.5946, keywords=53.3333, match=56.5735, GT shape={'rows': 9, 'cols': 5}, Pred shape={'rows': 19, 'cols': 6}
- primary GT table 18 -> Pred table 21: pair=65.8202, structure=91.6667, content=27.0506, keywords=56.8750, match=66.5169, GT shape={'rows': 24, 'cols': 5}, Pred shape={'rows': 21, 'cols': 5}
- alt GT table 25 -> Pred table 22: pair=54.7074, structure=55.5556, content=53.4351, keywords=51.2500, match=53.1483, GT shape={'rows': 5, 'cols': 5}, Pred shape={'rows': 15, 'cols': 5}
- primary GT table 19 -> Pred table 23: pair=97.0556, structure=100.0000, content=92.6389, keywords=94.3174, match=96.2754, GT shape={'rows': 18, 'cols': 4}, Pred shape={'rows': 18, 'cols': 4}
- primary GT table 20 -> Pred table 24: pair=66.9935, structure=67.6768, content=65.9686, keywords=79.7177, match=73.4923, GT shape={'rows': 8, 'cols': 9}, Pred shape={'rows': 12, 'cols': 11}
- primary GT table 21 -> Pred table 25: pair=62.3607, structure=73.3333, content=45.9016, keywords=69.5797, match=68.1647, GT shape={'rows': 6, 'cols': 9}, Pred shape={'rows': 10, 'cols': 9}
- primary GT table 22 -> Pred table 26: pair=76.4268, structure=88.6574, content=58.0808, keywords=55.5208, match=68.4199, GT shape={'rows': 5, 'cols': 9}, Pred shape={'rows': 6, 'cols': 8}
- primary GT table 23 -> Pred table 27: pair=72.5185, structure=73.3333, content=71.2963, keywords=51.5094, match=62.1769, GT shape={'rows': 6, 'cols': 11}, Pred shape={'rows': 10, 'cols': 11}
- primary GT table 24 -> Pred table 28: pair=84.8012, structure=90.4762, content=76.2887, keywords=52.8125, match=69.9419, GT shape={'rows': 6, 'cols': 9}, Pred shape={'rows': 7, 'cols': 9}
- primary GT table 25 -> Pred table 29: pair=65.7937, structure=70.3704, content=58.9286, keywords=41.9792, match=54.8018, GT shape={'rows': 5, 'cols': 9}, Pred shape={'rows': 9, 'cols': 9}

## Title Layout Evaluation
- GT raw heading levels: `[1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2] ... (502 total)`
- Pred raw heading levels: `[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2] ... (859 total)`
- GT relative heading levels: `[1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2] ... (502 total)`
- Pred relative heading levels: `[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] ... (859 total)`
- Title layout score: 65.0539
- Heading F1 score: 68.3321
- Level accuracy score: 49.7491
- Order score: 54.1327
- Main penalties:
  - 465 aligned headings have different relative levels.
  - 37 GT headings are missing.
  - 394 predicted headings are extra.

## Text Evaluation
- Text mode: normalized_full_text_preserve_newlines
- Text score: 90.7376
- Average edit distance: 0.0926
- Matched / missing / extra blocks: 1 / 0 / 0
- GT / Pred block counts: 1 / 1

### Worst Match Samples
1. op=match, distance=0.0926, GT blocks 0+1, Pred blocks 0+1
   - GT: 美团\n\nMeituan\n\n(于开曼群岛注册成立以不同投票权控制的有限公司)\n\n港币柜台股份代号:3690\n\n人民币柜台股份代号:83690\n![]\n#EatBetterLiveBetter\n年度报告\n\n目录\n\n公司资料\n\n财务概要6\n\n...
   - Pred: 美团美团Meituan\n\n(于开曼群岛注册成立以不同投票权控制的有限公司)\n港币柜台股份代号:3690\n人民币柜台股份代号:83690\n\n2024年度报告\n\n目录\n\n公司资料2\n财务概要6\n主席报告10\n管理层讨论及分析14\n董事及高级管理层38...

## Notes
- Table score compares extracted HTML and Markdown pipe tables after conversion to cell matrices.
- With primary or alt strategy, table matching is GT-driven one-to-one: each GT table chooses one best unused Pred table.
- With max and two GT files, each predicted table keeps the higher pair score from the two independently one-to-one-matched GT variants.
- Table pair score is 60% structure score and 40% content score; table content score uses normalized edit distance on flattened table text.
- Title layout score uses heading text only for anchor alignment, then combines heading F1, relative-level accuracy, and order coverage.
- Text score removes tables, keeps heading words, preserves newlines, and scores the full body as one character sequence.
- No-value page headers and footers are removed from prediction Markdown only; GT Markdown is kept as the reference answer.
- Current limitations: complex nested tables, heavily malformed HTML, and table semantic equivalence beyond cell text are only approximated.
