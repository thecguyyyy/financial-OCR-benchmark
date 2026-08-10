# Financial Markdown Scoring Report

## Overall
- Final Score: 86.2809
- Table Score: 91.6940
- Title Layout Score: 65.7222
- Text Score: 91.1472

## Prediction Cleanup
- Mode: disabled_after_explicit_adapter
- Removed pred header/footer lines: 0
- Removed examples:
  - None

## Weights
- Table: 40%
- Title Layout: 20%
- Text: 40%

## Configuration
- Remove pred header/footer: False
- Normalize images: True
- Normalize Chinese variants: t2s
- Normalize footnotes: True
- Normalize punctuation: True
- Table pair weights: structure=0.6, content=0.4

## Table Evaluation
- Table GT strategy result: per_table_max
- Primary table score: 69.4647
- Alt table score: 81.9448
- Per-table rule: each predicted table keeps its higher one-to-one pair score from primary or alt GT.
- Per-table selected primary / alt pairs: 123 / 47
- Per-table reference table count: 144
- Matched / missing / extra tables: 170 / 0 / 5
- Table content score: 89.5417
- Table structure score: 93.1289
- Table matrix score: 91.6940
- Table alignment strategy: per_table_best_of_primary_alt_one_to_one

### Table Matches
- primary GT table 0 -> Pred table 1: pair=99.5477, structure=100.0000, content=98.8691, keywords=95.6250, match=97.6768, GT shape={'rows': 10, 'cols': 6}, Pred shape={'rows': 10, 'cols': 6}
- primary GT table 1 -> Pred table 2: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 16, 'cols': 6}, Pred shape={'rows': 16, 'cols': 6}
- alt GT table 2 -> Pred table 3: pair=93.4463, structure=94.4444, content=91.9492, keywords=91.9683, match=92.9069, GT shape={'rows': 11, 'cols': 5}, Pred shape={'rows': 12, 'cols': 5}
- alt GT table 3 -> Pred table 4: pair=93.5639, structure=94.4444, content=92.2432, keywords=95.4844, match=94.7002, GT shape={'rows': 12, 'cols': 5}, Pred shape={'rows': 11, 'cols': 5}
- alt GT table 4 -> Pred table 5: pair=92.9680, structure=94.4444, content=90.7534, keywords=89.9415, match=91.7500, GT shape={'rows': 12, 'cols': 5}, Pred shape={'rows': 11, 'cols': 5}
- alt GT table 5 -> Pred table 6: pair=93.9258, structure=94.4444, content=93.1478, keywords=98.8596, match=96.4964, GT shape={'rows': 12, 'cols': 5}, Pred shape={'rows': 11, 'cols': 5}
- alt GT table 6 -> Pred table 7: pair=94.7823, structure=94.4444, content=95.2891, keywords=100.0000, match=97.3236, GT shape={'rows': 12, 'cols': 5}, Pred shape={'rows': 11, 'cols': 5}
- alt GT table 7 -> Pred table 8: pair=93.8889, structure=94.4444, content=93.0556, keywords=89.9415, match=92.0263, GT shape={'rows': 12, 'cols': 5}, Pred shape={'rows': 11, 'cols': 5}
- primary GT table 3 -> Pred table 9: pair=97.5259, structure=97.2222, content=97.9814, keywords=85.5324, match=91.4684, GT shape={'rows': 23, 'cols': 3}, Pred shape={'rows': 24, 'cols': 3}
- primary GT table 4 -> Pred table 11: pair=61.2534, structure=70.3704, content=47.5779, keywords=83.1111, match=74.0057, GT shape={'rows': 18, 'cols': 4}, Pred shape={'rows': 10, 'cols': 4}
- primary GT table 5 -> Pred table 12: pair=91.0700, structure=93.3333, content=87.6751, keywords=70.1364, match=81.0559, GT shape={'rows': 10, 'cols': 5}, Pred shape={'rows': 9, 'cols': 5}
- primary GT table 6 -> Pred table 13: pair=88.6168, structure=92.5926, content=82.6531, keywords=72.0851, match=81.1461, GT shape={'rows': 8, 'cols': 5}, Pred shape={'rows': 9, 'cols': 5}
- primary GT table 7 -> Pred table 14: pair=99.8154, structure=100.0000, content=99.5385, keywords=96.1111, match=98.0002, GT shape={'rows': 24, 'cols': 3}, Pred shape={'rows': 24, 'cols': 3}
- primary GT table 8 -> Pred table 16: pair=62.2917, structure=70.3704, content=50.1736, keywords=83.1111, match=74.3171, GT shape={'rows': 18, 'cols': 4}, Pred shape={'rows': 10, 'cols': 4}
- primary GT table 9 -> Pred table 17: pair=91.0423, structure=93.3333, content=87.6056, keywords=70.1364, match=81.0476, GT shape={'rows': 10, 'cols': 5}, Pred shape={'rows': 9, 'cols': 5}
- primary GT table 10 -> Pred table 18: pair=99.1753, structure=100.0000, content=97.9381, keywords=100.0000, match=99.7526, GT shape={'rows': 9, 'cols': 5}, Pred shape={'rows': 9, 'cols': 5}
- primary GT table 11 -> Pred table 19: pair=99.8793, structure=100.0000, content=99.6983, keywords=94.1667, match=97.0471, GT shape={'rows': 23, 'cols': 3}, Pred shape={'rows': 23, 'cols': 3}
- primary GT table 12 -> Pred table 20: pair=60.0000, structure=66.6667, content=50.0000, keywords=100.0000, match=81.3333, GT shape={'rows': 18, 'cols': 4}, Pred shape={'rows': 9, 'cols': 4}
- primary GT table 13 -> Pred table 22: pair=98.4615, structure=100.0000, content=96.1538, keywords=86.7083, match=92.8926, GT shape={'rows': 9, 'cols': 5}, Pred shape={'rows': 9, 'cols': 5}
- primary GT table 14 -> Pred table 23: pair=91.2195, structure=92.5926, content=89.1599, keywords=75.5851, match=83.6769, GT shape={'rows': 8, 'cols': 5}, Pred shape={'rows': 9, 'cols': 5}
- primary GT table 15 -> Pred table 24: pair=96.5462, structure=97.2222, content=95.5322, keywords=97.6667, match=97.2417, GT shape={'rows': 23, 'cols': 4}, Pred shape={'rows': 24, 'cols': 4}
- primary GT table 16 -> Pred table 25: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 21, 'cols': 3}, Pred shape={'rows': 21, 'cols': 3}
- primary GT table 17 -> Pred table 26: pair=92.8421, structure=93.3333, content=92.1053, keywords=91.2500, match=92.1443, GT shape={'rows': 10, 'cols': 3}, Pred shape={'rows': 9, 'cols': 3}
- alt GT table 23 -> Pred table 27: pair=91.5873, structure=100.0000, content=78.9683, keywords=100.0000, match=97.4762, GT shape={'rows': 9, 'cols': 5}, Pred shape={'rows': 9, 'cols': 5}
- alt GT table 24 -> Pred table 28: pair=66.1033, structure=73.3333, content=55.2581, keywords=100.0000, match=84.4976, GT shape={'rows': 10, 'cols': 5}, Pred shape={'rows': 6, 'cols': 5}
- alt GT table 25 -> Pred table 29: pair=95.5779, structure=100.0000, content=88.9447, keywords=100.0000, match=98.6734, GT shape={'rows': 5, 'cols': 5}, Pred shape={'rows': 5, 'cols': 5}
- alt GT table 26 -> Pred table 30: pair=95.3159, structure=100.0000, content=88.2897, keywords=100.0000, match=98.5948, GT shape={'rows': 14, 'cols': 4}, Pred shape={'rows': 14, 'cols': 4}
- alt GT table 27 -> Pred table 31: pair=78.6019, structure=86.6667, content=66.5049, keywords=84.0278, match=82.9278, GT shape={'rows': 4, 'cols': 4}, Pred shape={'rows': 5, 'cols': 4}
- primary GT table 20 -> Pred table 32: pair=94.9260, structure=92.5926, content=98.4260, keywords=96.5000, match=95.2463, GT shape={'rows': 8, 'cols': 9}, Pred shape={'rows': 9, 'cols': 9}
- primary GT table 21 -> Pred table 33: pair=81.1202, structure=88.8889, content=69.4672, keywords=93.0000, match=88.6138, GT shape={'rows': 6, 'cols': 9}, Pred shape={'rows': 5, 'cols': 9}

## Title Layout Evaluation
- GT raw heading levels: `[1, 2, 1, 1, 2, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 3, 3, 2, 1, 2, 3, 3, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 2, 3, 3, 2, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 2, 3, 3, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3] ... (554 total)`
- Pred raw heading levels: `[1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2] ... (1094 total)`
- GT relative heading levels: `[1, 2, 1, 1, 2, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 3, 3, 2, 1, 2, 3, 3, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 2, 3, 3, 2, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 2, 3, 3, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3] ... (554 total)`
- Pred relative heading levels: `[1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2] ... (1094 total)`
- Title layout score: 65.7222
- Heading F1 score: 66.2621
- Level accuracy score: 77.2161
- Order score: 49.9086
- Main penalties:
  - 392 aligned headings have different relative levels.
  - 8 GT headings are missing.
  - 548 predicted headings are extra.

## Text Evaluation
- Text mode: normalized_full_text_preserve_newlines
- Text score: 91.1472
- Average edit distance: 0.0885
- Matched / missing / extra blocks: 1 / 0 / 0
- GT / Pred block counts: 1 / 1

### Worst Match Samples
1. op=match, distance=0.0885, GT blocks 0+1, Pred blocks 0+1
   - GT: 美团\n\nMeituan\n\n(于开曼群岛注册成立以不同投票权控制的有限公司)\n\n港币柜台股份代号:3690\n\n人民币柜台股份代号:83690\n![]\nEatBetterLiveBetter\n年度报告\n\n目录\n\n公司资料\n\n财务概要6\n\n主...
   - Pred: ![]\n美团\n\nMeituan\n\n(于开曼群岛注册成立以不同投票权控制的有限公司)\n\n港币柜台股份代号:3690\n\n人民币柜台股份代号:83690\n![]\n年度报告\n\n目录\n\n公司资料\n\n董事会\n\n执行董事\n\n王兴先生(董事长兼首席...

## Notes
- Table score compares extracted HTML and Markdown pipe tables after conversion to cell matrices.
- With primary or alt strategy, table matching is GT-driven one-to-one: each GT table chooses one best unused Pred table.
- With max and two GT files, each predicted table keeps the higher pair score from the two independently one-to-one-matched GT variants.
- Table pair score is 60% structure score and 40% content score; table content score uses normalized edit distance on flattened table text.
- Title layout score uses heading text only for anchor alignment, then combines heading F1, relative-level accuracy, and order coverage.
- Text score removes tables, keeps heading words, preserves newlines, and scores the full body as one character sequence.
- No-value page headers and footers are removed from prediction Markdown only; GT Markdown is kept as the reference answer.
- Current limitations: complex nested tables, heavily malformed HTML, and table semantic equivalence beyond cell text are only approximated.
