# Financial Markdown Scoring Report

## Overall
- Final Score: 85.5406
- Table Score: 87.9700
- Title Layout Score: 71.8196
- Text Score: 89.9716

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
- Primary table score: 67.5256
- Alt table score: 62.6101
- Per-table rule: each predicted table keeps its higher one-to-one pair score from primary or alt GT.
- Per-table selected primary / alt pairs: 164 / 24
- Per-table reference table count: 200
- Matched / missing / extra tables: 188 / 12 / 1
- Table content score: 84.9015
- Table structure score: 90.0157
- Table matrix score: 87.9700
- Table alignment strategy: per_table_best_of_primary_alt_one_to_one

### Table Matches
- primary GT table 0 -> Pred table 0: pair=99.9627, structure=100.0000, content=99.9067, keywords=100.0000, match=99.9888, GT shape={'rows': 37, 'cols': 3}, Pred shape={'rows': 37, 'cols': 3}
- primary GT table 9 -> Pred table 1: pair=92.4898, structure=100.0000, content=81.2245, keywords=84.0882, match=89.7910, GT shape={'rows': 6, 'cols': 5}, Pred shape={'rows': 6, 'cols': 5}
- primary GT table 10 -> Pred table 2: pair=84.7559, structure=86.6667, content=81.8898, keywords=93.9167, match=89.7185, GT shape={'rows': 6, 'cols': 5}, Pred shape={'rows': 6, 'cols': 4}
- primary GT table 11 -> Pred table 3: pair=96.3805, structure=100.0000, content=90.9513, keywords=95.2986, match=96.5634, GT shape={'rows': 11, 'cols': 5}, Pred shape={'rows': 11, 'cols': 5}
- primary GT table 12 -> Pred table 4: pair=99.4366, structure=100.0000, content=98.5915, keywords=100.0000, match=99.8310, GT shape={'rows': 7, 'cols': 3}, Pred shape={'rows': 7, 'cols': 3}
- primary GT table 13 -> Pred table 5: pair=97.0968, structure=100.0000, content=92.7419, keywords=100.0000, match=99.1290, GT shape={'rows': 37, 'cols': 4}, Pred shape={'rows': 37, 'cols': 4}
- primary GT table 16 -> Pred table 6: pair=92.7451, structure=100.0000, content=81.8627, keywords=100.0000, match=97.8235, GT shape={'rows': 7, 'cols': 4}, Pred shape={'rows': 7, 'cols': 4}
- primary GT table 22 -> Pred table 7: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 5, 'cols': 3}, Pred shape={'rows': 5, 'cols': 3}
- primary GT table 23 -> Pred table 8: pair=98.4000, structure=100.0000, content=96.0000, keywords=92.9688, match=96.0044, GT shape={'rows': 5, 'cols': 3}, Pred shape={'rows': 5, 'cols': 3}
- primary GT table 24 -> Pred table 9: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 6, 'cols': 2}, Pred shape={'rows': 6, 'cols': 2}
- primary GT table 25 -> Pred table 10: pair=84.4143, structure=85.1852, content=83.2579, keywords=89.2778, match=87.0002, GT shape={'rows': 7, 'cols': 4}, Pred shape={'rows': 9, 'cols': 4}
- primary GT table 26 -> Pred table 11: pair=59.5985, structure=66.6667, content=48.9964, keywords=100.0000, match=81.2129, GT shape={'rows': 11, 'cols': 8}, Pred shape={'rows': 22, 'cols': 8}
- primary GT table 28 -> Pred table 12: pair=99.6413, structure=100.0000, content=99.1031, keywords=100.0000, match=99.8924, GT shape={'rows': 8, 'cols': 4}, Pred shape={'rows': 8, 'cols': 4}
- primary GT table 29 -> Pred table 13: pair=99.5652, structure=100.0000, content=98.9130, keywords=100.0000, match=99.8696, GT shape={'rows': 8, 'cols': 4}, Pred shape={'rows': 8, 'cols': 4}
- primary GT table 30 -> Pred table 14: pair=97.0732, structure=100.0000, content=92.6829, keywords=100.0000, match=99.1220, GT shape={'rows': 8, 'cols': 4}, Pred shape={'rows': 8, 'cols': 4}
- primary GT table 31 -> Pred table 15: pair=98.9427, structure=100.0000, content=97.3568, keywords=100.0000, match=99.6828, GT shape={'rows': 5, 'cols': 5}, Pred shape={'rows': 5, 'cols': 5}
- primary GT table 32 -> Pred table 16: pair=99.5294, structure=100.0000, content=98.8235, keywords=100.0000, match=99.8588, GT shape={'rows': 11, 'cols': 5}, Pred shape={'rows': 11, 'cols': 5}
- primary GT table 33 -> Pred table 17: pair=87.4066, structure=88.2353, content=86.1635, keywords=94.8810, match=91.3095, GT shape={'rows': 14, 'cols': 4}, Pred shape={'rows': 17, 'cols': 4}
- primary GT table 34 -> Pred table 18: pair=82.3454, structure=88.8889, content=72.5301, keywords=93.6855, match=89.3242, GT shape={'rows': 12, 'cols': 4}, Pred shape={'rows': 10, 'cols': 4}
- primary GT table 17 -> Pred table 19: pair=38.9320, structure=50.0000, content=22.3301, keywords=53.6111, match=48.4852, GT shape={'rows': 6, 'cols': 2}, Pred shape={'rows': 2, 'cols': 4}
- primary GT table 35 -> Pred table 20: pair=99.1304, structure=100.0000, content=97.8261, keywords=100.0000, match=99.7391, GT shape={'rows': 4, 'cols': 4}, Pred shape={'rows': 4, 'cols': 4}
- primary GT table 36 -> Pred table 21: pair=98.8211, structure=100.0000, content=97.0526, keywords=100.0000, match=99.6463, GT shape={'rows': 16, 'cols': 4}, Pred shape={'rows': 16, 'cols': 4}
- primary GT table 37 -> Pred table 22: pair=93.7319, structure=94.4444, content=92.6630, keywords=92.2222, match=93.1196, GT shape={'rows': 11, 'cols': 4}, Pred shape={'rows': 12, 'cols': 4}
- primary GT table 38 -> Pred table 23: pair=98.9888, structure=100.0000, content=97.4719, keywords=100.0000, match=99.6966, GT shape={'rows': 7, 'cols': 7}, Pred shape={'rows': 7, 'cols': 7}
- primary GT table 39 -> Pred table 24: pair=99.1837, structure=100.0000, content=97.9592, keywords=100.0000, match=99.7551, GT shape={'rows': 4, 'cols': 3}, Pred shape={'rows': 4, 'cols': 3}
- primary GT table 40 -> Pred table 25: pair=99.1579, structure=100.0000, content=97.8947, keywords=100.0000, match=99.7474, GT shape={'rows': 4, 'cols': 3}, Pred shape={'rows': 4, 'cols': 3}
- primary GT table 41 -> Pred table 26: pair=99.7701, structure=100.0000, content=99.4253, keywords=100.0000, match=99.9310, GT shape={'rows': 17, 'cols': 3}, Pred shape={'rows': 17, 'cols': 3}
- primary GT table 42 -> Pred table 27: pair=99.5580, structure=100.0000, content=98.8950, keywords=100.0000, match=99.8674, GT shape={'rows': 9, 'cols': 3}, Pred shape={'rows': 9, 'cols': 3}
- primary GT table 43 -> Pred table 28: pair=99.4872, structure=100.0000, content=98.7179, keywords=100.0000, match=99.8462, GT shape={'rows': 8, 'cols': 3}, Pred shape={'rows': 8, 'cols': 3}
- primary GT table 44 -> Pred table 29: pair=80.8837, structure=80.9524, content=80.7808, keywords=92.0282, match=86.4697, GT shape={'rows': 10, 'cols': 4}, Pred shape={'rows': 14, 'cols': 4}

## Title Layout Evaluation
- GT raw heading levels: `[1, 1, 1, 2, 2, 2, 3, 2, 3, 1, 2, 3, 3, 3, 3, 3, 4, 4, 5, 6, 5, 6, 6, 5, 2, 3, 3, 4, 5, 5, 4, 4, 3, 2, 3, 4, 4, 3, 4, 4, 4, 4, 4, 4, 4, 3, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 4, 3, 4, 4, 4, 4, 4, 4, 4, 4, 3, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 4, 2, 3, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 4, 4, 4, 3, 2, 3, 3, 3, 3, 3, 3, 3, 2, 3, 4, 4, 4, 5, 5, 5, 4, 4, 3, 4, 5, 4, 4, 4] ... (304 total)`
- Pred raw heading levels: `[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 1, 2] ... (511 total)`
- GT relative heading levels: `[1, 1, 1, 2, 2, 2, 3, 2, 3, 1, 2, 3, 3, 3, 3, 3, 4, 4, 5, 6, 5, 6, 6, 5, 2, 3, 3, 4, 5, 5, 4, 4, 3, 2, 3, 4, 4, 3, 4, 4, 4, 4, 4, 4, 4, 3, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 4, 3, 4, 4, 4, 4, 4, 4, 4, 4, 3, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 4, 2, 3, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 4, 4, 4, 3, 2, 3, 3, 3, 3, 3, 3, 3, 2, 3, 4, 4, 4, 5, 5, 5, 4, 4, 3, 4, 5, 4, 4, 4] ... (304 total)`
- Pred relative heading levels: `[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 1, 2] ... (511 total)`
- Title layout score: 71.8196
- Heading F1 score: 73.8650
- Level accuracy score: 68.3721
- Order score: 58.9041
- Main penalties:
  - 281 aligned headings have different relative levels.
  - 3 GT headings are missing.
  - 210 predicted headings are extra.

## Text Evaluation
- Text mode: normalized_full_text_preserve_newlines
- Text score: 89.9716
- Average edit distance: 0.1003
- Matched / missing / extra blocks: 1 / 0 / 0
- GT / Pred block counts: 1 / 1

### Worst Match Samples
1. op=match, distance=0.1003, GT blocks 0+1, Pred blocks 0+1
   - GT: ![]\n二零二三年中报\n\n目录\n\n关于我们\n\n1重要提示及释义\n2公司概览\n5董事长致辞\n8财务摘要\n\n经营情况讨论及分析\n\n10综合金融\n14以医疗健康打造价值增长新引擎\n16主要业务经营分析\n16业绩综述\n20寿险及健康险业务\n26...
   - Pred: ![]\n二零二三年中报\n\n目录\n\n关于我们\n\n重要提示及释义\n\n2公司概览\n\n5董事长致辞\n\n8财务摘要\n\n经营情况讨论及分析\n\n10综合金融\n\n14以医疗健康打造价值增长新引擎\n\n16主要业务经营分析\n\n16业绩综述\n\n2...

## Notes
- Table score compares extracted HTML and Markdown pipe tables after conversion to cell matrices.
- With primary or alt strategy, table matching is GT-driven one-to-one: each GT table chooses one best unused Pred table.
- With max and two GT files, each predicted table keeps the higher pair score from the two independently one-to-one-matched GT variants.
- Table pair score is 60% structure score and 40% content score; table content score uses normalized edit distance on flattened table text.
- Title layout score uses heading text only for anchor alignment, then combines heading F1, relative-level accuracy, and order coverage.
- Text score removes tables, keeps heading words, preserves newlines, and scores the full body as one character sequence.
- No-value page headers and footers are removed from prediction Markdown only; GT Markdown is kept as the reference answer.
- Current limitations: complex nested tables, heavily malformed HTML, and table semantic equivalence beyond cell text are only approximated.
