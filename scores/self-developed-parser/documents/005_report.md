# Financial Markdown Scoring Report

## Overall
- Final Score: 86.7706
- Table Score: 88.2781
- Title Layout Score: 71.7283
- Text Score: 92.7843

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
- Primary table score: 70.1541
- Alt table score: 65.1897
- Per-table rule: each predicted table keeps its higher one-to-one pair score from primary or alt GT.
- Per-table selected primary / alt pairs: 162 / 25
- Per-table reference table count: 196
- Matched / missing / extra tables: 187 / 9 / 0
- Table content score: 83.3667
- Table structure score: 91.5524
- Table matrix score: 88.2781
- Table alignment strategy: per_table_best_of_primary_alt_one_to_one

### Table Matches
- primary GT table 0 -> Pred table 0: pair=97.8929, structure=100.0000, content=94.7321, keywords=90.4324, match=94.5841, GT shape={'rows': 37, 'cols': 3}, Pred shape={'rows': 37, 'cols': 3}
- primary GT table 9 -> Pred table 1: pair=94.9388, structure=100.0000, content=87.3469, keywords=91.0882, match=94.0257, GT shape={'rows': 6, 'cols': 5}, Pred shape={'rows': 6, 'cols': 5}
- primary GT table 10 -> Pred table 2: pair=89.8616, structure=88.8889, content=91.3208, keywords=93.9167, match=91.6946, GT shape={'rows': 6, 'cols': 5}, Pred shape={'rows': 6, 'cols': 6}
- primary GT table 91 -> Pred table 3: pair=45.3333, structure=60.0000, content=23.3333, keywords=39.0000, match=45.1000, GT shape={'rows': 3, 'cols': 2}, Pred shape={'rows': 3, 'cols': 5}
- primary GT table 11 -> Pred table 4: pair=74.3341, structure=81.1111, content=64.1686, keywords=75.7131, match=76.3790, GT shape={'rows': 11, 'cols': 5}, Pred shape={'rows': 8, 'cols': 6}
- primary GT table 12 -> Pred table 5: pair=88.8732, structure=83.3333, content=97.1831, keywords=100.0000, match=93.3286, GT shape={'rows': 7, 'cols': 3}, Pred shape={'rows': 7, 'cols': 4}
- primary GT table 13 -> Pred table 6: pair=95.6680, structure=100.0000, content=89.1700, keywords=100.0000, match=98.7004, GT shape={'rows': 37, 'cols': 4}, Pred shape={'rows': 37, 'cols': 4}
- primary GT table 14 -> Pred table 7: pair=94.3689, structure=100.0000, content=85.9223, keywords=100.0000, match=98.3107, GT shape={'rows': 7, 'cols': 4}, Pred shape={'rows': 7, 'cols': 4}
- primary GT table 20 -> Pred table 8: pair=99.1304, structure=100.0000, content=97.8261, keywords=100.0000, match=99.7391, GT shape={'rows': 5, 'cols': 3}, Pred shape={'rows': 5, 'cols': 3}
- primary GT table 21 -> Pred table 9: pair=98.4000, structure=100.0000, content=96.0000, keywords=92.9688, match=96.0044, GT shape={'rows': 5, 'cols': 3}, Pred shape={'rows': 5, 'cols': 3}
- primary GT table 22 -> Pred table 10: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 6, 'cols': 2}, Pred shape={'rows': 6, 'cols': 2}
- primary GT table 23 -> Pred table 11: pair=85.7057, structure=85.1852, content=86.4865, keywords=100.0000, match=92.7488, GT shape={'rows': 7, 'cols': 4}, Pred shape={'rows': 9, 'cols': 4}
- primary GT table 24 -> Pred table 12: pair=97.3929, structure=100.0000, content=93.4823, keywords=100.0000, match=99.2179, GT shape={'rows': 11, 'cols': 8}, Pred shape={'rows': 11, 'cols': 8}
- primary GT table 25 -> Pred table 13: pair=97.5524, structure=100.0000, content=93.8811, keywords=100.0000, match=99.2657, GT shape={'rows': 11, 'cols': 8}, Pred shape={'rows': 11, 'cols': 8}
- primary GT table 26 -> Pred table 14: pair=99.6413, structure=100.0000, content=99.1031, keywords=100.0000, match=99.8924, GT shape={'rows': 8, 'cols': 4}, Pred shape={'rows': 8, 'cols': 4}
- primary GT table 27 -> Pred table 15: pair=85.0909, structure=86.6667, content=82.7273, keywords=100.0000, match=92.8606, GT shape={'rows': 8, 'cols': 4}, Pred shape={'rows': 8, 'cols': 5}
- primary GT table 28 -> Pred table 16: pair=96.7078, structure=100.0000, content=91.7695, keywords=100.0000, match=99.0123, GT shape={'rows': 8, 'cols': 4}, Pred shape={'rows': 8, 'cols': 4}
- primary GT table 29 -> Pred table 17: pair=98.9427, structure=100.0000, content=97.3568, keywords=100.0000, match=99.6828, GT shape={'rows': 5, 'cols': 5}, Pred shape={'rows': 5, 'cols': 5}
- primary GT table 30 -> Pred table 18: pair=99.2982, structure=100.0000, content=98.2456, keywords=100.0000, match=99.7895, GT shape={'rows': 11, 'cols': 5}, Pred shape={'rows': 11, 'cols': 5}
- primary GT table 31 -> Pred table 19: pair=93.3065, structure=100.0000, content=83.2661, keywords=99.1096, match=97.5468, GT shape={'rows': 14, 'cols': 4}, Pred shape={'rows': 14, 'cols': 4}
- primary GT table 32 -> Pred table 20: pair=87.1474, structure=94.4444, content=76.2019, keywords=100.0000, match=95.0331, GT shape={'rows': 12, 'cols': 4}, Pred shape={'rows': 11, 'cols': 4}
- primary GT table 15 -> Pred table 21: pair=38.9320, structure=50.0000, content=22.3301, keywords=53.6111, match=48.4852, GT shape={'rows': 6, 'cols': 2}, Pred shape={'rows': 2, 'cols': 4}
- primary GT table 33 -> Pred table 22: pair=86.3704, structure=100.0000, content=65.9259, keywords=94.1667, match=92.9945, GT shape={'rows': 4, 'cols': 4}, Pred shape={'rows': 4, 'cols': 4}
- primary GT table 34 -> Pred table 23: pair=98.6383, structure=100.0000, content=96.5957, keywords=100.0000, match=99.5915, GT shape={'rows': 16, 'cols': 4}, Pred shape={'rows': 16, 'cols': 4}
- primary GT table 35 -> Pred table 24: pair=94.0220, structure=94.4444, content=93.3884, keywords=100.0000, match=97.0955, GT shape={'rows': 11, 'cols': 4}, Pred shape={'rows': 12, 'cols': 4}
- primary GT table 36 -> Pred table 25: pair=98.7640, structure=100.0000, content=96.9101, keywords=100.0000, match=99.6292, GT shape={'rows': 7, 'cols': 7}, Pred shape={'rows': 7, 'cols': 7}
- primary GT table 37 -> Pred table 26: pair=99.1837, structure=100.0000, content=97.9592, keywords=100.0000, match=99.7551, GT shape={'rows': 4, 'cols': 3}, Pred shape={'rows': 4, 'cols': 3}
- primary GT table 38 -> Pred table 27: pair=99.1579, structure=100.0000, content=97.8947, keywords=100.0000, match=99.7474, GT shape={'rows': 4, 'cols': 3}, Pred shape={'rows': 4, 'cols': 3}
- primary GT table 39 -> Pred table 28: pair=99.2000, structure=100.0000, content=98.0000, keywords=100.0000, match=99.7600, GT shape={'rows': 17, 'cols': 3}, Pred shape={'rows': 17, 'cols': 3}
- primary GT table 40 -> Pred table 29: pair=99.1160, structure=100.0000, content=97.7901, keywords=100.0000, match=99.7348, GT shape={'rows': 9, 'cols': 3}, Pred shape={'rows': 9, 'cols': 3}

## Title Layout Evaluation
- GT raw heading levels: `[2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2] ... (299 total)`
- Pred raw heading levels: `[2, 2, 2, 3, 3, 3, 3, 3, 4, 2, 2, 2, 2, 2, 3, 2, 2, 3, 2, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 1, 2, 3, 2, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 2, 3, 2, 3, 3, 3, 2, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 2, 3, 3, 3, 2, 3, 3, 3, 2, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 2, 2, 2, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 2, 3, 3, 3] ... (517 total)`
- GT relative heading levels: `[2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2] ... (299 total)`
- Pred relative heading levels: `[2, 2, 2, 3, 3, 3, 3, 3, 4, 2, 2, 2, 2, 2, 3, 2, 2, 3, 2, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 1, 2, 3, 2, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 2, 3, 2, 3, 3, 3, 2, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 2, 3, 3, 3, 2, 3, 3, 3, 2, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 2, 2, 2, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 2, 3, 3, 3] ... (517 total)`
- Title layout score: 71.7283
- Heading F1 score: 72.0588
- Level accuracy score: 83.9456
- Order score: 56.8665
- Main penalties:
  - 221 aligned headings have different relative levels.
  - 5 GT headings are missing.
  - 223 predicted headings are extra.

## Text Evaluation
- Text mode: normalized_full_text_preserve_newlines
- Text score: 92.7843
- Average edit distance: 0.0722
- Matched / missing / extra blocks: 1 / 0 / 0
- GT / Pred block counts: 1 / 1

### Worst Match Samples
1. op=match, distance=0.0722, GT blocks 0+1, Pred blocks 0+1
   - GT: ![]\n关于我们\n\n1重要提示及释义\n2公司概览\n5董事长致辞\n8财务摘要\n\n经营情况讨论及分析\n\n10综合金融\n14以医疗健康打造价值增长新引擎\n16主要业务经营分析\n业绩综述\n20寿险及健康险业务\n26财产保险业务\n30保险资金投资组合\...
   - Pred: 中国平安PINGAN专业·价值\n\nth351988-2023中国平安成立35周年\n\n专业让生活更简单\n\n105219059\n\n112810907\n\n二零二三年中报\n\n目录\n\n关于我们\n\n重要提示及释义\n公司概览\n董事长致辞\n财务摘要\n...

## Notes
- Table score compares extracted HTML and Markdown pipe tables after conversion to cell matrices.
- With primary or alt strategy, table matching is GT-driven one-to-one: each GT table chooses one best unused Pred table.
- With max and two GT files, each predicted table keeps the higher pair score from the two independently one-to-one-matched GT variants.
- Table pair score is 60% structure score and 40% content score; table content score uses normalized edit distance on flattened table text.
- Title layout score uses heading text only for anchor alignment, then combines heading F1, relative-level accuracy, and order coverage.
- Text score removes tables, keeps heading words, preserves newlines, and scores the full body as one character sequence.
- No-value page headers and footers are removed from prediction Markdown only; GT Markdown is kept as the reference answer.
- Current limitations: complex nested tables, heavily malformed HTML, and table semantic equivalence beyond cell text are only approximated.
