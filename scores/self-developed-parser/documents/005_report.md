# Financial Markdown Scoring Report

## Overall
- Final Score: 86.7523
- Table Score: 87.4070
- Title Layout Score: 71.7735
- Text Score: 93.5870

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
- Primary table score: 67.5020
- Alt table score: 63.2232
- Per-table rule: each predicted table keeps its higher one-to-one pair score from primary or alt GT.
- Per-table selected primary / alt pairs: 163 / 24
- Per-table reference table count: 200
- Matched / missing / extra tables: 187 / 13 / 0
- Table content score: 83.6799
- Table structure score: 89.8917
- Table matrix score: 87.4070
- Table alignment strategy: per_table_best_of_primary_alt_one_to_one

### Table Matches
- primary GT table 0 -> Pred table 0: pair=99.1185, structure=100.0000, content=97.7961, keywords=90.4324, match=94.9518, GT shape={'rows': 37, 'cols': 3}, Pred shape={'rows': 37, 'cols': 3}
- primary GT table 9 -> Pred table 1: pair=95.2653, structure=100.0000, content=88.1633, keywords=91.0882, match=94.1237, GT shape={'rows': 6, 'cols': 5}, Pred shape={'rows': 6, 'cols': 5}
- primary GT table 10 -> Pred table 2: pair=89.8616, structure=88.8889, content=91.3208, keywords=93.9167, match=91.6946, GT shape={'rows': 6, 'cols': 5}, Pred shape={'rows': 6, 'cols': 6}
- primary GT table 95 -> Pred table 3: pair=45.3333, structure=60.0000, content=23.3333, keywords=39.0000, match=45.1000, GT shape={'rows': 3, 'cols': 2}, Pred shape={'rows': 3, 'cols': 5}
- primary GT table 11 -> Pred table 4: pair=74.3341, structure=81.1111, content=64.1686, keywords=75.7131, match=76.3790, GT shape={'rows': 11, 'cols': 5}, Pred shape={'rows': 8, 'cols': 6}
- primary GT table 12 -> Pred table 5: pair=89.4366, structure=83.3333, content=98.5915, keywords=100.0000, match=93.4976, GT shape={'rows': 7, 'cols': 3}, Pred shape={'rows': 7, 'cols': 4}
- primary GT table 13 -> Pred table 6: pair=96.7119, structure=100.0000, content=91.7797, keywords=100.0000, match=99.0136, GT shape={'rows': 37, 'cols': 4}, Pred shape={'rows': 37, 'cols': 4}
- primary GT table 16 -> Pred table 7: pair=94.3689, structure=100.0000, content=85.9223, keywords=100.0000, match=98.3107, GT shape={'rows': 7, 'cols': 4}, Pred shape={'rows': 7, 'cols': 4}
- primary GT table 22 -> Pred table 8: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 5, 'cols': 3}, Pred shape={'rows': 5, 'cols': 3}
- primary GT table 23 -> Pred table 9: pair=98.4000, structure=100.0000, content=96.0000, keywords=92.9688, match=96.0044, GT shape={'rows': 5, 'cols': 3}, Pred shape={'rows': 5, 'cols': 3}
- primary GT table 24 -> Pred table 10: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 6, 'cols': 2}, Pred shape={'rows': 6, 'cols': 2}
- primary GT table 25 -> Pred table 11: pair=86.0661, structure=85.1852, content=87.3874, keywords=100.0000, match=92.8569, GT shape={'rows': 7, 'cols': 4}, Pred shape={'rows': 9, 'cols': 4}
- primary GT table 26 -> Pred table 12: pair=98.2123, structure=100.0000, content=95.5307, keywords=100.0000, match=99.4637, GT shape={'rows': 11, 'cols': 8}, Pred shape={'rows': 11, 'cols': 8}
- primary GT table 27 -> Pred table 13: pair=98.3217, structure=100.0000, content=95.8042, keywords=100.0000, match=99.4965, GT shape={'rows': 11, 'cols': 8}, Pred shape={'rows': 11, 'cols': 8}
- primary GT table 28 -> Pred table 14: pair=99.6413, structure=100.0000, content=99.1031, keywords=100.0000, match=99.8924, GT shape={'rows': 8, 'cols': 4}, Pred shape={'rows': 8, 'cols': 4}
- primary GT table 29 -> Pred table 15: pair=85.0909, structure=86.6667, content=82.7273, keywords=100.0000, match=92.8606, GT shape={'rows': 8, 'cols': 4}, Pred shape={'rows': 8, 'cols': 5}
- primary GT table 30 -> Pred table 16: pair=97.0370, structure=100.0000, content=92.5926, keywords=100.0000, match=99.1111, GT shape={'rows': 8, 'cols': 4}, Pred shape={'rows': 8, 'cols': 4}
- primary GT table 31 -> Pred table 17: pair=98.9427, structure=100.0000, content=97.3568, keywords=100.0000, match=99.6828, GT shape={'rows': 5, 'cols': 5}, Pred shape={'rows': 5, 'cols': 5}
- primary GT table 32 -> Pred table 18: pair=99.4521, structure=100.0000, content=98.6301, keywords=100.0000, match=99.8356, GT shape={'rows': 11, 'cols': 5}, Pred shape={'rows': 11, 'cols': 5}
- primary GT table 33 -> Pred table 19: pair=93.7903, structure=100.0000, content=84.4758, keywords=99.1096, match=97.6919, GT shape={'rows': 14, 'cols': 4}, Pred shape={'rows': 14, 'cols': 4}
- primary GT table 34 -> Pred table 20: pair=87.1245, structure=94.4444, content=76.1446, keywords=100.0000, match=95.0262, GT shape={'rows': 12, 'cols': 4}, Pred shape={'rows': 11, 'cols': 4}
- primary GT table 17 -> Pred table 21: pair=38.9320, structure=50.0000, content=22.3301, keywords=53.6111, match=48.4852, GT shape={'rows': 6, 'cols': 2}, Pred shape={'rows': 2, 'cols': 4}
- primary GT table 35 -> Pred table 22: pair=86.6667, structure=100.0000, content=66.6667, keywords=94.1667, match=93.0834, GT shape={'rows': 4, 'cols': 4}, Pred shape={'rows': 4, 'cols': 4}
- primary GT table 36 -> Pred table 23: pair=99.2340, structure=100.0000, content=98.0851, keywords=100.0000, match=99.7702, GT shape={'rows': 16, 'cols': 4}, Pred shape={'rows': 16, 'cols': 4}
- primary GT table 37 -> Pred table 24: pair=94.2424, structure=94.4444, content=93.9394, keywords=100.0000, match=97.1616, GT shape={'rows': 11, 'cols': 4}, Pred shape={'rows': 12, 'cols': 4}
- primary GT table 38 -> Pred table 25: pair=98.9888, structure=100.0000, content=97.4719, keywords=100.0000, match=99.6966, GT shape={'rows': 7, 'cols': 7}, Pred shape={'rows': 7, 'cols': 7}
- primary GT table 39 -> Pred table 26: pair=99.1837, structure=100.0000, content=97.9592, keywords=100.0000, match=99.7551, GT shape={'rows': 4, 'cols': 3}, Pred shape={'rows': 4, 'cols': 3}
- primary GT table 40 -> Pred table 27: pair=99.1579, structure=100.0000, content=97.8947, keywords=100.0000, match=99.7474, GT shape={'rows': 4, 'cols': 3}, Pred shape={'rows': 4, 'cols': 3}
- primary GT table 41 -> Pred table 28: pair=99.7701, structure=100.0000, content=99.4253, keywords=100.0000, match=99.9310, GT shape={'rows': 17, 'cols': 3}, Pred shape={'rows': 17, 'cols': 3}
- primary GT table 42 -> Pred table 29: pair=99.5580, structure=100.0000, content=98.8950, keywords=100.0000, match=99.8674, GT shape={'rows': 9, 'cols': 3}, Pred shape={'rows': 9, 'cols': 3}

## Title Layout Evaluation
- GT raw heading levels: `[1, 1, 1, 2, 2, 2, 3, 2, 3, 1, 2, 3, 3, 3, 3, 3, 4, 4, 5, 6, 5, 6, 6, 5, 2, 3, 3, 4, 5, 5, 4, 4, 3, 2, 3, 4, 4, 3, 4, 4, 4, 4, 4, 4, 4, 3, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 4, 3, 4, 4, 4, 4, 4, 4, 4, 4, 3, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 4, 2, 3, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 4, 4, 4, 3, 2, 3, 3, 3, 3, 3, 3, 3, 2, 3, 4, 4, 4, 5, 5, 5, 4, 4, 3, 4, 5, 4, 4, 4] ... (304 total)`
- Pred raw heading levels: `[2, 2, 2, 3, 3, 3, 3, 3, 4, 2, 2, 2, 2, 2, 3, 2, 2, 3, 2, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 1, 2, 3, 2, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 2, 3, 2, 3, 3, 3, 2, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 2, 3, 3, 3, 2, 3, 3, 3, 2, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 2, 2, 2, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 2, 3, 3, 3] ... (517 total)`
- GT relative heading levels: `[1, 1, 1, 2, 2, 2, 3, 2, 3, 1, 2, 3, 3, 3, 3, 3, 4, 4, 5, 6, 5, 6, 6, 5, 2, 3, 3, 4, 5, 5, 4, 4, 3, 2, 3, 4, 4, 3, 4, 4, 4, 4, 4, 4, 4, 3, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 4, 3, 4, 4, 4, 4, 4, 4, 4, 4, 3, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 4, 2, 3, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 4, 4, 4, 3, 2, 3, 3, 3, 3, 3, 3, 3, 2, 3, 4, 4, 4, 5, 5, 5, 4, 4, 3, 4, 5, 4, 4, 4] ... (304 total)`
- Pred relative heading levels: `[2, 2, 2, 3, 3, 3, 3, 3, 4, 2, 2, 2, 2, 2, 3, 2, 2, 3, 2, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 1, 2, 3, 2, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 2, 3, 2, 3, 3, 3, 2, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 2, 3, 3, 3, 2, 3, 3, 3, 2, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 2, 2, 2, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 2, 3, 3, 3] ... (517 total)`
- Title layout score: 71.7735
- Heading F1 score: 72.3508
- Level accuracy score: 81.4815
- Order score: 57.4468
- Main penalties:
  - 196 aligned headings have different relative levels.
  - 7 GT headings are missing.
  - 220 predicted headings are extra.

## Text Evaluation
- Text mode: normalized_full_text_preserve_newlines
- Text score: 93.5870
- Average edit distance: 0.0641
- Matched / missing / extra blocks: 1 / 0 / 0
- GT / Pred block counts: 1 / 1

### Worst Match Samples
1. op=match, distance=0.0641, GT blocks 0+1, Pred blocks 0+1
   - GT: ![]\n二零二三年中报\n\n目录\n\n关于我们\n\n1重要提示及释义\n2公司概览\n5董事长致辞\n8财务摘要\n\n经营情况讨论及分析\n\n10综合金融\n14以医疗健康打造价值增长新引擎\n16主要业务经营分析\n16业绩综述\n20寿险及健康险业务\n26...
   - Pred: 中国平安PINGAN专业·价值\n\nth351988-2023中国平安成立35周年\n\n专业让生活更简单\n![]\n二零二三年中报\n\n目录\n\n关于我们\n\n重要提示及释义\n公司概览\n董事长致辞\n财务摘要\n\n经营情况讨论及分析\n\n10综合金融\n...

## Notes
- Table score compares extracted HTML and Markdown pipe tables after conversion to cell matrices.
- With primary or alt strategy, table matching is GT-driven one-to-one: each GT table chooses one best unused Pred table.
- With max and two GT files, each predicted table keeps the higher pair score from the two independently one-to-one-matched GT variants.
- Table pair score is 60% structure score and 40% content score; table content score uses normalized edit distance on flattened table text.
- Title layout score uses heading text only for anchor alignment, then combines heading F1, relative-level accuracy, and order coverage.
- Text score removes tables, keeps heading words, preserves newlines, and scores the full body as one character sequence.
- No-value page headers and footers are removed from prediction Markdown only; GT Markdown is kept as the reference answer.
- Current limitations: complex nested tables, heavily malformed HTML, and table semantic equivalence beyond cell text are only approximated.
