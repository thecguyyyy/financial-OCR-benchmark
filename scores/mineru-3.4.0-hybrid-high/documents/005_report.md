# Financial Markdown Scoring Report

## Overall
- Final Score: 90.8688
- Table Score: 97.0192
- Title Layout Score: 73.3610
- Text Score: 93.4724

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
- Primary table score: 86.3647
- Alt table score: 86.7494
- Per-table rule: each predicted table keeps its higher one-to-one pair score from primary or alt GT.
- Per-table selected primary / alt pairs: 183 / 25
- Per-table reference table count: 200
- Matched / missing / extra tables: 208 / 0 / 1
- Table content score: 95.2532
- Table structure score: 98.1966
- Table matrix score: 97.0192
- Table alignment strategy: per_table_best_of_primary_alt_one_to_one

### Table Matches
- primary GT table 0 -> Pred table 0: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 37, 'cols': 3}, Pred shape={'rows': 37, 'cols': 3}
- primary GT table 1 -> Pred table 1: pair=93.4545, structure=100.0000, content=83.6364, keywords=65.0000, match=80.5363, GT shape={'rows': 3, 'cols': 2}, Pred shape={'rows': 3, 'cols': 2}
- primary GT table 2 -> Pred table 2: pair=89.1667, structure=100.0000, content=72.9167, keywords=65.0000, match=79.2500, GT shape={'rows': 3, 'cols': 2}, Pred shape={'rows': 3, 'cols': 2}
- primary GT table 3 -> Pred table 3: pair=88.1818, structure=100.0000, content=70.4545, keywords=65.0000, match=78.9545, GT shape={'rows': 3, 'cols': 2}, Pred shape={'rows': 3, 'cols': 2}
- primary GT table 4 -> Pred table 4: pair=89.1667, structure=100.0000, content=72.9167, keywords=65.0000, match=79.2500, GT shape={'rows': 3, 'cols': 2}, Pred shape={'rows': 3, 'cols': 2}
- primary GT table 5 -> Pred table 5: pair=89.6000, structure=100.0000, content=74.0000, keywords=65.0000, match=79.3800, GT shape={'rows': 3, 'cols': 2}, Pred shape={'rows': 3, 'cols': 2}
- primary GT table 6 -> Pred table 6: pair=92.6531, structure=100.0000, content=81.6327, keywords=65.0000, match=80.2959, GT shape={'rows': 3, 'cols': 2}, Pred shape={'rows': 3, 'cols': 2}
- primary GT table 7 -> Pred table 7: pair=88.1818, structure=100.0000, content=70.4545, keywords=65.0000, match=78.9545, GT shape={'rows': 3, 'cols': 2}, Pred shape={'rows': 3, 'cols': 2}
- primary GT table 8 -> Pred table 8: pair=92.6531, structure=100.0000, content=81.6327, keywords=65.0000, match=80.2959, GT shape={'rows': 3, 'cols': 2}, Pred shape={'rows': 3, 'cols': 2}
- primary GT table 9 -> Pred table 9: pair=99.2000, structure=100.0000, content=98.0000, keywords=93.0000, match=96.2600, GT shape={'rows': 6, 'cols': 5}, Pred shape={'rows': 6, 'cols': 5}
- primary GT table 10 -> Pred table 10: pair=99.2278, structure=100.0000, content=98.0695, keywords=95.0000, match=97.2683, GT shape={'rows': 6, 'cols': 5}, Pred shape={'rows': 6, 'cols': 5}
- primary GT table 11 -> Pred table 11: pair=99.0847, structure=100.0000, content=97.7117, keywords=96.1111, match=97.7810, GT shape={'rows': 11, 'cols': 5}, Pred shape={'rows': 11, 'cols': 5}
- primary GT table 12 -> Pred table 12: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 7, 'cols': 3}, Pred shape={'rows': 7, 'cols': 3}
- primary GT table 13 -> Pred table 13: pair=99.9306, structure=100.0000, content=99.8264, keywords=100.0000, match=99.9792, GT shape={'rows': 37, 'cols': 4}, Pred shape={'rows': 37, 'cols': 4}
- primary GT table 16 -> Pred table 14: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 7, 'cols': 4}, Pred shape={'rows': 7, 'cols': 4}
- primary GT table 17 -> Pred table 15: pair=94.7368, structure=100.0000, content=86.8421, keywords=82.5000, match=89.6710, GT shape={'rows': 6, 'cols': 2}, Pred shape={'rows': 6, 'cols': 2}
- primary GT table 18 -> Pred table 16: pair=89.0909, structure=100.0000, content=72.7273, keywords=91.2500, match=92.3523, GT shape={'rows': 5, 'cols': 3}, Pred shape={'rows': 5, 'cols': 3}
- primary GT table 19 -> Pred table 17: pair=90.3557, structure=100.0000, content=75.8893, keywords=63.6667, match=78.9401, GT shape={'rows': 9, 'cols': 3}, Pred shape={'rows': 9, 'cols': 3}
- primary GT table 20 -> Pred table 18: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 5, 'cols': 2}, Pred shape={'rows': 5, 'cols': 2}
- primary GT table 21 -> Pred table 19: pair=84.0705, structure=86.6667, content=80.1762, keywords=100.0000, match=92.5545, GT shape={'rows': 6, 'cols': 5}, Pred shape={'rows': 6, 'cols': 4}
- primary GT table 22 -> Pred table 20: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 5, 'cols': 3}, Pred shape={'rows': 5, 'cols': 3}
- primary GT table 23 -> Pred table 21: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 5, 'cols': 3}, Pred shape={'rows': 5, 'cols': 3}
- primary GT table 24 -> Pred table 22: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 6, 'cols': 2}, Pred shape={'rows': 6, 'cols': 2}
- primary GT table 25 -> Pred table 23: pair=86.3838, structure=85.1852, content=88.1818, keywords=100.0000, match=92.9522, GT shape={'rows': 7, 'cols': 4}, Pred shape={'rows': 9, 'cols': 4}
- primary GT table 26 -> Pred table 24: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 11, 'cols': 8}, Pred shape={'rows': 11, 'cols': 8}
- primary GT table 27 -> Pred table 25: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 11, 'cols': 8}, Pred shape={'rows': 11, 'cols': 8}
- primary GT table 28 -> Pred table 26: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 8, 'cols': 4}, Pred shape={'rows': 8, 'cols': 4}
- primary GT table 29 -> Pred table 27: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 8, 'cols': 4}, Pred shape={'rows': 8, 'cols': 4}
- primary GT table 30 -> Pred table 28: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 8, 'cols': 4}, Pred shape={'rows': 8, 'cols': 4}
- primary GT table 31 -> Pred table 29: pair=99.6413, structure=100.0000, content=99.1031, keywords=100.0000, match=99.8924, GT shape={'rows': 5, 'cols': 5}, Pred shape={'rows': 5, 'cols': 5}

## Title Layout Evaluation
- GT raw heading levels: `[1, 1, 1, 2, 2, 2, 3, 2, 3, 1, 2, 3, 3, 3, 3, 3, 4, 4, 5, 6, 5, 6, 6, 5, 2, 3, 3, 4, 5, 5, 4, 4, 3, 2, 3, 4, 4, 3, 4, 4, 4, 4, 4, 4, 4, 3, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 4, 3, 4, 4, 4, 4, 4, 4, 4, 4, 3, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 4, 2, 3, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 4, 4, 4, 3, 2, 3, 3, 3, 3, 3, 3, 3, 2, 3, 4, 4, 4, 5, 5, 5, 4, 4, 3, 4, 5, 4, 4, 4] ... (304 total)`
- Pred raw heading levels: `[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 1, 2, 1, 1, 2, 2, 2, 1, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2] ... (477 total)`
- GT relative heading levels: `[1, 1, 1, 2, 2, 2, 3, 2, 3, 1, 2, 3, 3, 3, 3, 3, 4, 4, 5, 6, 5, 6, 6, 5, 2, 3, 3, 4, 5, 5, 4, 4, 3, 2, 3, 4, 4, 3, 4, 4, 4, 4, 4, 4, 4, 3, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 4, 3, 4, 4, 4, 4, 4, 4, 4, 4, 3, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 4, 2, 3, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 4, 4, 4, 3, 2, 3, 3, 3, 3, 3, 3, 3, 2, 3, 4, 4, 4, 5, 5, 5, 4, 4, 3, 4, 5, 4, 4, 4] ... (304 total)`
- Pred relative heading levels: `[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 1, 2, 1, 1, 2, 2, 2, 1, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2] ... (477 total)`
- Title layout score: 73.3610
- Heading F1 score: 76.0563
- Level accuracy score: 62.8956
- Order score: 62.2642
- Main penalties:
  - 282 aligned headings have different relative levels.
  - 7 GT headings are missing.
  - 180 predicted headings are extra.

## Text Evaluation
- Text mode: normalized_full_text_preserve_newlines
- Text score: 93.4724
- Average edit distance: 0.0653
- Matched / missing / extra blocks: 1 / 0 / 0
- GT / Pred block counts: 1 / 1

### Worst Match Samples
1. op=match, distance=0.0653, GT blocks 0+1, Pred blocks 0+1
   - GT: ![]\n二零二三年中报\n\n目录\n\n关于我们\n\n1重要提示及释义\n2公司概览\n5董事长致辞\n8财务摘要\n\n经营情况讨论及分析\n\n10综合金融\n14以医疗健康打造价值增长新引擎\n16主要业务经营分析\n16业绩综述\n20寿险及健康险业务\n26...
   - Pred: ![]\n关于我们\n\n1重要提示及释义\n2公司概览\n5董事长致辞\n8财务摘要\n\n经营情况讨论及分析\n\n10综合金融\n14以医疗健康打造价值增长新引擎\n16主要业务经营分析\n16业绩综述\n20寿险及健康险业务\n26财产保险业务\n30保险资金投资组...

## Notes
- Table score compares extracted HTML and Markdown pipe tables after conversion to cell matrices.
- With primary or alt strategy, table matching is GT-driven one-to-one: each GT table chooses one best unused Pred table.
- With max and two GT files, each predicted table keeps the higher pair score from the two independently one-to-one-matched GT variants.
- Table pair score is 60% structure score and 40% content score; table content score uses normalized edit distance on flattened table text.
- Title layout score uses heading text only for anchor alignment, then combines heading F1, relative-level accuracy, and order coverage.
- Text score removes tables, keeps heading words, preserves newlines, and scores the full body as one character sequence.
- No-value page headers and footers are removed from prediction Markdown only; GT Markdown is kept as the reference answer.
- Current limitations: complex nested tables, heavily malformed HTML, and table semantic equivalence beyond cell text are only approximated.
