# Financial Markdown Scoring Report

## Overall
- Final Score: 93.8393
- Table Score: 91.9288
- Title Layout Score: 89.0672
- Text Score: 98.1359

## Prediction Cleanup
- Mode: prediction_only_header_footer_cleanup
- Removed pred header/footer lines: 7
- Removed examples:
  - 第二节公司简介和主要财务指标..... .... 8
  - 第三节管理层讨论与分析.... ..... 12
  - 第四节公司治理、环境和社会.... ....... 30
  - 第五节重要事项... ...41
  - 第六节股份变动及股东情况........ ...... 50
  - 第七节债券相关情况... .....55
  - 第八节财务报告.. ....56

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
- Primary table score: 87.0210
- Alt table score: 80.0275
- Per-table rule: each predicted table keeps its higher one-to-one pair score from primary or alt GT.
- Per-table selected primary / alt pairs: 215 / 1
- Per-table reference table count: 218
- Matched / missing / extra tables: 216 / 2 / 9
- Table content score: 90.2074
- Table structure score: 93.0764
- Table matrix score: 91.9288
- Table alignment strategy: per_table_best_of_primary_alt_one_to_one

### Table Matches
- primary GT table 0 -> Pred table 0: pair=98.9155, structure=100.0000, content=97.2887, keywords=100.0000, match=99.6746, GT shape={'rows': 21, 'cols': 3}, Pred shape={'rows': 21, 'cols': 3}
- primary GT table 1 -> Pred table 1: pair=99.7504, structure=100.0000, content=99.3760, keywords=100.0000, match=99.9251, GT shape={'rows': 13, 'cols': 4}, Pred shape={'rows': 13, 'cols': 4}
- primary GT table 2 -> Pred table 2: pair=99.7605, structure=100.0000, content=99.4012, keywords=100.0000, match=99.9281, GT shape={'rows': 6, 'cols': 3}, Pred shape={'rows': 6, 'cols': 3}
- primary GT table 3 -> Pred table 3: pair=99.4805, structure=100.0000, content=98.7013, keywords=100.0000, match=99.8441, GT shape={'rows': 3, 'cols': 2}, Pred shape={'rows': 3, 'cols': 2}
- primary GT table 4 -> Pred table 4: pair=99.0698, structure=100.0000, content=97.6744, keywords=100.0000, match=99.7209, GT shape={'rows': 3, 'cols': 2}, Pred shape={'rows': 3, 'cols': 2}
- primary GT table 5 -> Pred table 5: pair=98.9078, structure=100.0000, content=97.2696, keywords=100.0000, match=99.6723, GT shape={'rows': 11, 'cols': 5}, Pred shape={'rows': 11, 'cols': 5}
- primary GT table 6 -> Pred table 6: pair=98.9091, structure=100.0000, content=97.2727, keywords=100.0000, match=99.6727, GT shape={'rows': 5, 'cols': 4}, Pred shape={'rows': 5, 'cols': 4}
- primary GT table 7 -> Pred table 7: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 5, 'cols': 5}, Pred shape={'rows': 5, 'cols': 5}
- primary GT table 8 -> Pred table 8: pair=99.3256, structure=100.0000, content=98.3139, keywords=100.0000, match=99.7977, GT shape={'rows': 12, 'cols': 5}, Pred shape={'rows': 12, 'cols': 5}
- primary GT table 9 -> Pred table 9: pair=98.7037, structure=100.0000, content=96.7593, keywords=100.0000, match=99.6111, GT shape={'rows': 5, 'cols': 3}, Pred shape={'rows': 5, 'cols': 3}
- primary GT table 10 -> Pred table 10: pair=96.7862, structure=100.0000, content=91.9656, keywords=100.0000, match=99.0359, GT shape={'rows': 16, 'cols': 6}, Pred shape={'rows': 16, 'cols': 6}
- primary GT table 11 -> Pred table 11: pair=97.7077, structure=100.0000, content=94.2693, keywords=100.0000, match=99.3123, GT shape={'rows': 14, 'cols': 7}, Pred shape={'rows': 14, 'cols': 7}
- primary GT table 12 -> Pred table 12: pair=90.2609, structure=86.6667, content=95.6522, keywords=93.0000, match=90.9116, GT shape={'rows': 4, 'cols': 6}, Pred shape={'rows': 5, 'cols': 6}
- primary GT table 13 -> Pred table 13: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 4, 'cols': 7}, Pred shape={'rows': 4, 'cols': 7}
- primary GT table 14 -> Pred table 14: pair=99.1011, structure=100.0000, content=97.7528, keywords=100.0000, match=99.7303, GT shape={'rows': 3, 'cols': 2}, Pred shape={'rows': 3, 'cols': 2}
- primary GT table 15 -> Pred table 15: pair=99.5676, structure=100.0000, content=98.9189, keywords=100.0000, match=99.8703, GT shape={'rows': 7, 'cols': 4}, Pred shape={'rows': 7, 'cols': 4}
- primary GT table 16 -> Pred table 16: pair=99.1111, structure=100.0000, content=97.7778, keywords=100.0000, match=99.7333, GT shape={'rows': 3, 'cols': 2}, Pred shape={'rows': 3, 'cols': 2}
- primary GT table 17 -> Pred table 17: pair=93.4762, structure=91.6667, content=96.1905, keywords=88.3333, match=90.5429, GT shape={'rows': 7, 'cols': 4}, Pred shape={'rows': 8, 'cols': 4}
- primary GT table 18 -> Pred table 18: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 5, 'cols': 5}, Pred shape={'rows': 5, 'cols': 5}
- primary GT table 19 -> Pred table 19: pair=87.0869, structure=86.6667, content=87.7173, keywords=96.8815, match=91.9002, GT shape={'rows': 8, 'cols': 5}, Pred shape={'rows': 10, 'cols': 5}
- primary GT table 20 -> Pred table 20: pair=92.6809, structure=100.0000, content=81.7021, keywords=100.0000, match=97.8043, GT shape={'rows': 11, 'cols': 4}, Pred shape={'rows': 11, 'cols': 4}
- primary GT table 21 -> Pred table 21: pair=99.5897, structure=100.0000, content=98.9744, keywords=100.0000, match=99.8769, GT shape={'rows': 6, 'cols': 4}, Pred shape={'rows': 6, 'cols': 4}
- primary GT table 22 -> Pred table 22: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 11, 'cols': 4}, Pred shape={'rows': 11, 'cols': 4}
- primary GT table 23 -> Pred table 23: pair=99.7122, structure=100.0000, content=99.2806, keywords=100.0000, match=99.9137, GT shape={'rows': 8, 'cols': 5}, Pred shape={'rows': 8, 'cols': 5}
- primary GT table 24 -> Pred table 24: pair=99.9368, structure=100.0000, content=99.8420, keywords=100.0000, match=99.9810, GT shape={'rows': 20, 'cols': 7}, Pred shape={'rows': 20, 'cols': 7}
- primary GT table 25 -> Pred table 25: pair=97.3840, structure=100.0000, content=93.4599, keywords=94.1667, match=96.2986, GT shape={'rows': 8, 'cols': 9}, Pred shape={'rows': 8, 'cols': 9}
- primary GT table 26 -> Pred table 26: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 3, 'cols': 3}, Pred shape={'rows': 3, 'cols': 3}
- primary GT table 27 -> Pred table 27: pair=99.2453, structure=100.0000, content=98.1132, keywords=100.0000, match=99.7736, GT shape={'rows': 2, 'cols': 15}, Pred shape={'rows': 2, 'cols': 15}
- primary GT table 28 -> Pred table 28: pair=98.1963, structure=100.0000, content=95.4907, keywords=100.0000, match=99.4589, GT shape={'rows': 2, 'cols': 14}, Pred shape={'rows': 2, 'cols': 14}
- primary GT table 29 -> Pred table 29: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 8, 'cols': 9}, Pred shape={'rows': 8, 'cols': 9}

## Title Layout Evaluation
- GT raw heading levels: `[1, 3, 2, 4, 4, 4, 4, 4, 4, 2, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 3, 2, 3, 4, 4, 4, 3, 3, 4, 4, 4, 4, 3, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 3, 3, 4, 4, 4, 3, 4, 4, 4, 4, 5, 5, 3, 4, 4, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 2, 3, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 4, 3, 4, 4, 4, 3, 3, 3, 4, 4, 4, 4, 3, 3, 3, 4] ... (429 total)`
- Pred raw heading levels: `[1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2] ... (445 total)`
- GT relative heading levels: `[1, 3, 2, 4, 4, 4, 4, 4, 4, 2, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 3, 2, 3, 4, 4, 4, 3, 3, 4, 4, 4, 4, 3, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 3, 3, 4, 4, 4, 3, 4, 4, 4, 4, 5, 5, 3, 4, 4, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 2, 3, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 4, 3, 4, 4, 4, 3, 3, 3, 4, 4, 4, 4, 3, 3, 3, 4] ... (429 total)`
- Pred relative heading levels: `[1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2] ... (445 total)`
- Title layout score: 89.0672
- Heading F1 score: 92.4485
- Level accuracy score: 60.2970
- Order score: 90.7865
- Main penalties:
  - 393 aligned headings have different relative levels.
  - 25 GT headings are missing.
  - 41 predicted headings are extra.

## Text Evaluation
- Text mode: normalized_full_text_preserve_newlines
- Text score: 98.1359
- Average edit distance: 0.0186
- Matched / missing / extra blocks: 1 / 0 / 0
- GT / Pred block counts: 1 / 1

### Worst Match Samples
1. op=match, distance=0.0186, GT blocks 0+1, Pred blocks 0+1
   - GT: 宁波先锋新材料股份有限公司\n\n2025年年度报告\n\n2026年4月\n\n2025年年度报告\n\n第一节重要提示目录和释义\n\n公司董事会及董事高级管理人员保证年度报告内容的真实准确完整不存在虚假记载误导性陈述或者重大遗漏并承担个别和连带的法律责任。\n\n公司...
   - Pred: 宁波先锋新材料股份有限公司\n\n2025年年度报告\n\n2026年4月\n\n2025年年度报告\n\n第一节重要提示目录和释义\n\n公司董事会及董事高级管理人员保证年度报告内容的真实准确完整不存在虚假记载误导性陈述或者重大遗漏并承担个别和连带的法律责任。\n\n公司...

## Notes
- Table score compares extracted HTML and Markdown pipe tables after conversion to cell matrices.
- With primary or alt strategy, table matching is GT-driven one-to-one: each GT table chooses one best unused Pred table.
- With max and two GT files, each predicted table keeps the higher pair score from the two independently one-to-one-matched GT variants.
- Table pair score is 60% structure score and 40% content score; table content score uses normalized edit distance on flattened table text.
- Title layout score uses heading text only for anchor alignment, then combines heading F1, relative-level accuracy, and order coverage.
- Text score removes tables, keeps heading words, preserves newlines, and scores the full body as one character sequence.
- No-value page headers and footers are removed from prediction Markdown only; GT Markdown is kept as the reference answer.
- Current limitations: complex nested tables, heavily malformed HTML, and table semantic equivalence beyond cell text are only approximated.
