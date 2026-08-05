# Financial Markdown Scoring Report

## Overall
- Final Score: 85.6674
- Table Score: 82.6554
- Title Layout Score: 78.3123
- Text Score: 92.3570

## Prediction Cleanup
- Mode: prediction_only_header_footer_cleanup
- Removed pred header/footer lines: 0
- Removed examples:
  - None

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
- Primary table score: 62.0625
- Alt table score: 58.2872
- Per-table rule: each predicted table keeps its higher one-to-one pair score from primary or alt GT.
- Per-table selected primary / alt pairs: 160 / 22
- Per-table reference table count: 196
- Matched / missing / extra tables: 182 / 14 / 0
- Table content score: 79.7423
- Table structure score: 84.5975
- Table matrix score: 82.6554
- Table alignment strategy: per_table_best_of_primary_alt_one_to_one

### Table Matches
- primary GT table 0 -> Pred table 0: pair=79.4105, structure=77.7778, content=81.8596, keywords=52.3270, match=65.5422, GT shape={'rows': 37, 'cols': 3}, Pred shape={'rows': 37, 'cols': 2}
- primary GT table 9 -> Pred table 1: pair=97.9845, structure=100.0000, content=94.9612, keywords=96.2857, match=97.5382, GT shape={'rows': 6, 'cols': 5}, Pred shape={'rows': 6, 'cols': 5}
- primary GT table 10 -> Pred table 2: pair=97.0079, structure=100.0000, content=92.5197, keywords=97.8333, match=98.0190, GT shape={'rows': 6, 'cols': 5}, Pred shape={'rows': 6, 'cols': 5}
- primary GT table 11 -> Pred table 3: pair=90.9405, structure=94.4444, content=85.6846, keywords=93.7037, match=93.0229, GT shape={'rows': 11, 'cols': 5}, Pred shape={'rows': 12, 'cols': 5}
- primary GT table 12 -> Pred table 4: pair=84.6296, structure=91.6667, content=74.0741, keywords=88.3333, match=87.8889, GT shape={'rows': 7, 'cols': 3}, Pred shape={'rows': 8, 'cols': 3}
- primary GT table 13 -> Pred table 5: pair=96.5519, structure=98.1982, content=94.0823, keywords=97.8635, match=97.5370, GT shape={'rows': 37, 'cols': 4}, Pred shape={'rows': 36, 'cols': 4}
- primary GT table 14 -> Pred table 6: pair=77.7444, structure=100.0000, content=44.3609, keywords=93.2759, match=89.9613, GT shape={'rows': 7, 'cols': 4}, Pred shape={'rows': 7, 'cols': 4}
- primary GT table 20 -> Pred table 7: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 5, 'cols': 3}, Pred shape={'rows': 5, 'cols': 3}
- primary GT table 21 -> Pred table 8: pair=99.3443, structure=100.0000, content=98.3607, keywords=100.0000, match=99.8033, GT shape={'rows': 5, 'cols': 3}, Pred shape={'rows': 5, 'cols': 3}
- primary GT table 22 -> Pred table 9: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 6, 'cols': 2}, Pred shape={'rows': 6, 'cols': 2}
- primary GT table 23 -> Pred table 10: pair=85.8622, structure=85.1852, content=86.8778, keywords=100.0000, match=92.7957, GT shape={'rows': 7, 'cols': 4}, Pred shape={'rows': 9, 'cols': 4}
- primary GT table 24 -> Pred table 11: pair=95.7542, structure=100.0000, content=89.3855, keywords=99.2935, match=98.3730, GT shape={'rows': 11, 'cols': 8}, Pred shape={'rows': 11, 'cols': 8}
- primary GT table 25 -> Pred table 12: pair=86.1538, structure=93.9394, content=74.4755, keywords=93.6364, match=91.4522, GT shape={'rows': 11, 'cols': 8}, Pred shape={'rows': 10, 'cols': 8}
- primary GT table 26 -> Pred table 13: pair=89.8198, structure=83.3333, content=99.5495, keywords=95.0000, match=91.1126, GT shape={'rows': 8, 'cols': 4}, Pred shape={'rows': 8, 'cols': 3}
- primary GT table 76 -> Pred table 14: pair=63.7874, structure=47.3380, content=88.4615, keywords=74.2222, match=65.7149, GT shape={'rows': 8, 'cols': 4}, Pred shape={'rows': 9, 'cols': 1}
- primary GT table 28 -> Pred table 15: pair=87.9310, structure=83.3333, content=94.8276, keywords=91.4524, match=88.7722, GT shape={'rows': 8, 'cols': 4}, Pred shape={'rows': 8, 'cols': 3}
- primary GT table 29 -> Pred table 16: pair=99.6413, structure=100.0000, content=99.1031, keywords=100.0000, match=99.8924, GT shape={'rows': 5, 'cols': 5}, Pred shape={'rows': 5, 'cols': 5}
- primary GT table 30 -> Pred table 17: pair=88.1890, structure=100.0000, content=70.4724, keywords=82.8675, match=87.8905, GT shape={'rows': 11, 'cols': 5}, Pred shape={'rows': 11, 'cols': 5}
- primary GT table 31 -> Pred table 18: pair=81.7618, structure=82.4561, content=80.7203, keywords=96.7763, match=89.4079, GT shape={'rows': 14, 'cols': 4}, Pred shape={'rows': 19, 'cols': 4}
- primary GT table 32 -> Pred table 19: pair=82.5557, structure=94.8718, content=64.0816, keywords=94.0514, match=90.7668, GT shape={'rows': 12, 'cols': 4}, Pred shape={'rows': 13, 'cols': 4}
- primary GT table 33 -> Pred table 20: pair=91.1209, structure=86.6667, content=97.8022, keywords=100.0000, match=94.6696, GT shape={'rows': 4, 'cols': 4}, Pred shape={'rows': 5, 'cols': 4}
- primary GT table 34 -> Pred table 21: pair=83.2450, structure=86.6667, content=78.1124, keywords=96.8182, match=90.7159, GT shape={'rows': 16, 'cols': 4}, Pred shape={'rows': 20, 'cols': 4}
- primary GT table 35 -> Pred table 22: pair=86.1108, structure=89.7436, content=80.6616, keywords=95.6250, match=91.5945, GT shape={'rows': 11, 'cols': 4}, Pred shape={'rows': 13, 'cols': 4}
- primary GT table 36 -> Pred table 23: pair=98.3146, structure=100.0000, content=95.7865, keywords=100.0000, match=99.4944, GT shape={'rows': 7, 'cols': 7}, Pred shape={'rows': 7, 'cols': 7}
- primary GT table 37 -> Pred table 24: pair=99.5876, structure=100.0000, content=98.9691, keywords=100.0000, match=99.8763, GT shape={'rows': 4, 'cols': 3}, Pred shape={'rows': 4, 'cols': 3}
- primary GT table 38 -> Pred table 25: pair=99.5745, structure=100.0000, content=98.9362, keywords=100.0000, match=99.8723, GT shape={'rows': 4, 'cols': 3}, Pred shape={'rows': 4, 'cols': 3}
- primary GT table 39 -> Pred table 26: pair=84.1667, structure=77.7778, content=93.7500, keywords=100.0000, match=90.8056, GT shape={'rows': 17, 'cols': 3}, Pred shape={'rows': 17, 'cols': 2}
- primary GT table 40 -> Pred table 27: pair=62.5180, structure=83.3333, content=31.2950, keywords=94.1667, match=82.5054, GT shape={'rows': 9, 'cols': 3}, Pred shape={'rows': 9, 'cols': 4}
- primary GT table 41 -> Pred table 28: pair=85.4545, structure=100.0000, content=63.6364, keywords=88.3333, match=89.8030, GT shape={'rows': 8, 'cols': 3}, Pred shape={'rows': 8, 'cols': 3}
- primary GT table 42 -> Pred table 29: pair=83.5883, structure=88.8889, content=75.6374, keywords=94.4699, match=90.0892, GT shape={'rows': 10, 'cols': 4}, Pred shape={'rows': 12, 'cols': 4}

## Title Layout Evaluation
- GT raw heading levels: `[2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2] ... (299 total)`
- Pred raw heading levels: `[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 1, 2, 1, 2, 2, 2, 1, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2] ... (457 total)`
- GT relative heading levels: `[2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2] ... (299 total)`
- Pred relative heading levels: `[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 1, 2, 1, 2, 2, 2, 1, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2] ... (457 total)`
- Title layout score: 78.3123
- Heading F1 score: 78.5714
- Level accuracy score: 89.5623
- Order score: 64.9891
- Main penalties:
  - 100 aligned headings have different relative levels.
  - 2 GT headings are missing.
  - 160 predicted headings are extra.

## Text Evaluation
- Text mode: normalized_full_text_preserve_newlines
- Text score: 92.3570
- Average edit distance: 0.0764
- Matched / missing / extra blocks: 1 / 0 / 0
- GT / Pred block counts: 1 / 1

### Worst Match Samples
1. op=match, distance=0.0764, GT blocks 0+1, Pred blocks 0+1
   - GT: ![]\n关于我们\n\n1重要提示及释义\n2公司概览\n5董事长致辞\n8财务摘要\n\n经营情况讨论及分析\n\n10综合金融\n14以医疗健康打造价值增长新引擎\n16主要业务经营分析\n业绩综述\n20寿险及健康险业务\n26财产保险业务\n30保险资金投资组合\...
   - Pred: ![]\n目录\n\n关于我们\n\n重要提示及释义\n\n2公司概览\n\n5董事长致辞\n\n8财务摘要\n\n经营情况讨论及分析\n\n10综合金融\n\n14以医疗健康打造价值增长新引擎\n\n16主要业务经营分析\n\n16业绩综述\n\n20寿险及健康险业务\n...

## Notes
- Table score compares extracted HTML and Markdown pipe tables after conversion to cell matrices.
- With primary or alt strategy, table matching is GT-driven one-to-one: each GT table chooses one best unused Pred table.
- With max and two GT files, each predicted table keeps the higher pair score from the two independently one-to-one-matched GT variants.
- Table pair score is 60% structure score and 40% content score; table content score uses normalized edit distance on flattened table text.
- Title layout score uses heading text only for anchor alignment, then combines heading F1, relative-level accuracy, and order coverage.
- Text score removes tables, keeps heading words, preserves newlines, and scores the full body as one character sequence.
- No-value page headers and footers are removed from prediction Markdown only; GT Markdown is kept as the reference answer.
- Current limitations: complex nested tables, heavily malformed HTML, and table semantic equivalence beyond cell text are only approximated.
