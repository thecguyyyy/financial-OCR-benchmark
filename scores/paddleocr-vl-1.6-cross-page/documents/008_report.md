# Financial Markdown Scoring Report

## Overall
- Final Score: 95.7242
- Table Score: 94.5590
- Title Layout Score: 91.8526
- Text Score: 98.8253

## Prediction Cleanup
- Mode: prediction_only_header_footer_cleanup
- Removed pred header/footer lines: 8
- Removed examples:
  - 第一节 重要提示、目录和释义..... 2
  - 第二节 公司简介和主要财务指标..... 8
  - 第三节 管理层讨论与分析..... 12
  - 第四节 公司治理、环境和社会..... 30
  - 第五节 重要事项..... 41
  - 第六节 股份变动及股东情况..... 50
  - 第七节 债券相关情况..... 55
  - 第八节 财务报告..... 56

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
- Primary table score: 90.1503
- Alt table score: 84.8169
- Per-table rule: each predicted table keeps its higher one-to-one pair score from primary or alt GT.
- Per-table selected primary / alt pairs: 216 / 5
- Per-table reference table count: 218
- Matched / missing / extra tables: 221 / 0 / 7
- Table content score: 93.3871
- Table structure score: 95.3402
- Table matrix score: 94.5590
- Table alignment strategy: per_table_best_of_primary_alt_one_to_one

### Table Matches
- primary GT table 0 -> Pred table 0: pair=98.9155, structure=100.0000, content=97.2887, keywords=100.0000, match=99.6746, GT shape={'rows': 21, 'cols': 3}, Pred shape={'rows': 21, 'cols': 3}
- primary GT table 1 -> Pred table 1: pair=99.3818, structure=100.0000, content=98.4544, keywords=100.0000, match=99.8145, GT shape={'rows': 13, 'cols': 4}, Pred shape={'rows': 13, 'cols': 4}
- primary GT table 2 -> Pred table 2: pair=98.8304, structure=100.0000, content=97.0760, keywords=100.0000, match=99.6491, GT shape={'rows': 6, 'cols': 3}, Pred shape={'rows': 6, 'cols': 3}
- primary GT table 3 -> Pred table 3: pair=98.9744, structure=100.0000, content=97.4359, keywords=100.0000, match=99.6923, GT shape={'rows': 3, 'cols': 2}, Pred shape={'rows': 3, 'cols': 2}
- primary GT table 4 -> Pred table 4: pair=97.3333, structure=100.0000, content=93.3333, keywords=100.0000, match=99.2000, GT shape={'rows': 3, 'cols': 2}, Pred shape={'rows': 3, 'cols': 2}
- primary GT table 5 -> Pred table 5: pair=98.5135, structure=100.0000, content=96.2838, keywords=100.0000, match=99.5540, GT shape={'rows': 11, 'cols': 5}, Pred shape={'rows': 11, 'cols': 5}
- primary GT table 6 -> Pred table 6: pair=98.3784, structure=100.0000, content=95.9459, keywords=100.0000, match=99.5135, GT shape={'rows': 5, 'cols': 4}, Pred shape={'rows': 5, 'cols': 4}
- primary GT table 7 -> Pred table 7: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 5, 'cols': 5}, Pred shape={'rows': 5, 'cols': 5}
- primary GT table 8 -> Pred table 8: pair=99.4812, structure=100.0000, content=98.7030, keywords=100.0000, match=99.8444, GT shape={'rows': 12, 'cols': 5}, Pred shape={'rows': 12, 'cols': 5}
- primary GT table 9 -> Pred table 9: pair=98.8889, structure=100.0000, content=97.2222, keywords=100.0000, match=99.6667, GT shape={'rows': 5, 'cols': 3}, Pred shape={'rows': 5, 'cols': 3}
- primary GT table 10 -> Pred table 10: pair=99.7718, structure=100.0000, content=99.4294, keywords=100.0000, match=99.9315, GT shape={'rows': 16, 'cols': 6}, Pred shape={'rows': 16, 'cols': 6}
- primary GT table 11 -> Pred table 11: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 14, 'cols': 7}, Pred shape={'rows': 14, 'cols': 7}
- primary GT table 12 -> Pred table 12: pair=90.2609, structure=86.6667, content=95.6522, keywords=93.0000, match=90.9116, GT shape={'rows': 4, 'cols': 6}, Pred shape={'rows': 5, 'cols': 6}
- primary GT table 13 -> Pred table 13: pair=99.2271, structure=100.0000, content=98.0676, keywords=100.0000, match=99.7681, GT shape={'rows': 4, 'cols': 7}, Pred shape={'rows': 4, 'cols': 7}
- primary GT table 14 -> Pred table 14: pair=99.1011, structure=100.0000, content=97.7528, keywords=100.0000, match=99.7303, GT shape={'rows': 3, 'cols': 2}, Pred shape={'rows': 3, 'cols': 2}
- primary GT table 15 -> Pred table 15: pair=98.5263, structure=100.0000, content=96.3158, keywords=100.0000, match=99.5579, GT shape={'rows': 7, 'cols': 4}, Pred shape={'rows': 7, 'cols': 4}
- primary GT table 16 -> Pred table 16: pair=99.1111, structure=100.0000, content=97.7778, keywords=100.0000, match=99.7333, GT shape={'rows': 3, 'cols': 2}, Pred shape={'rows': 3, 'cols': 2}
- primary GT table 17 -> Pred table 17: pair=94.0521, structure=91.6667, content=97.6303, keywords=88.3333, match=90.7156, GT shape={'rows': 7, 'cols': 4}, Pred shape={'rows': 8, 'cols': 4}
- primary GT table 18 -> Pred table 18: pair=99.6887, structure=100.0000, content=99.2218, keywords=100.0000, match=99.9066, GT shape={'rows': 5, 'cols': 5}, Pred shape={'rows': 5, 'cols': 5}
- primary GT table 19 -> Pred table 19: pair=87.0116, structure=86.6667, content=87.5290, keywords=96.8815, match=91.8776, GT shape={'rows': 8, 'cols': 5}, Pred shape={'rows': 10, 'cols': 5}
- primary GT table 20 -> Pred table 20: pair=98.8333, structure=100.0000, content=97.0833, keywords=100.0000, match=99.6500, GT shape={'rows': 11, 'cols': 4}, Pred shape={'rows': 11, 'cols': 4}
- primary GT table 21 -> Pred table 21: pair=98.5859, structure=100.0000, content=96.4646, keywords=100.0000, match=99.5758, GT shape={'rows': 6, 'cols': 4}, Pred shape={'rows': 6, 'cols': 4}
- primary GT table 22 -> Pred table 22: pair=99.8135, structure=100.0000, content=99.5338, keywords=100.0000, match=99.9441, GT shape={'rows': 11, 'cols': 4}, Pred shape={'rows': 11, 'cols': 4}
- primary GT table 23 -> Pred table 23: pair=99.6163, structure=100.0000, content=99.0408, keywords=100.0000, match=99.8849, GT shape={'rows': 8, 'cols': 5}, Pred shape={'rows': 8, 'cols': 5}
- primary GT table 24 -> Pred table 24: pair=99.8110, structure=100.0000, content=99.5276, keywords=100.0000, match=99.9433, GT shape={'rows': 20, 'cols': 7}, Pred shape={'rows': 20, 'cols': 7}
- primary GT table 25 -> Pred table 25: pair=99.8312, structure=100.0000, content=99.5781, keywords=100.0000, match=99.9494, GT shape={'rows': 8, 'cols': 9}, Pred shape={'rows': 8, 'cols': 9}
- primary GT table 26 -> Pred table 26: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 3, 'cols': 3}, Pred shape={'rows': 3, 'cols': 3}
- primary GT table 27 -> Pred table 27: pair=98.5882, structure=100.0000, content=96.4706, keywords=100.0000, match=99.5765, GT shape={'rows': 2, 'cols': 15}, Pred shape={'rows': 2, 'cols': 15}
- primary GT table 28 -> Pred table 28: pair=97.6842, structure=100.0000, content=94.2105, keywords=100.0000, match=99.3053, GT shape={'rows': 2, 'cols': 14}, Pred shape={'rows': 2, 'cols': 14}
- primary GT table 29 -> Pred table 29: pair=99.5994, structure=100.0000, content=98.9986, keywords=100.0000, match=99.8798, GT shape={'rows': 8, 'cols': 9}, Pred shape={'rows': 8, 'cols': 9}

## Title Layout Evaluation
- GT raw heading levels: `[1, 3, 2, 4, 4, 4, 4, 4, 4, 2, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 3, 2, 3, 4, 4, 4, 3, 3, 4, 4, 4, 4, 3, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 3, 3, 4, 4, 4, 3, 4, 4, 4, 4, 5, 5, 3, 4, 4, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 2, 3, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 4, 3, 4, 4, 4, 3, 3, 3, 4, 4, 4, 4, 3, 3, 3, 4] ... (429 total)`
- Pred raw heading levels: `[1, 2, 3, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 5, 3, 3, 2, 2, 3, 5, 5, 3, 3, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 4, 5, 5, 5, 5, 5, 5, 5, 5, 2, 2, 2, 3, 3, 2, 2, 5, 2, 3, 2, 2, 2, 2, 5, 5, 3, 2, 2, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 3, 5, 3, 3, 1, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 2, 2, 2, 2, 2, 3, 2, 2, 2, 3, 3, 3, 2, 2, 2, 2, 3] ... (440 total)`
- GT relative heading levels: `[1, 3, 2, 4, 4, 4, 4, 4, 4, 2, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 3, 2, 3, 4, 4, 4, 3, 3, 4, 4, 4, 4, 3, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 3, 3, 4, 4, 4, 3, 4, 4, 4, 4, 5, 5, 3, 4, 4, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 2, 3, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 4, 3, 4, 4, 4, 3, 3, 3, 4, 4, 4, 4, 3, 3, 3, 4] ... (429 total)`
- Pred relative heading levels: `[1, 2, 3, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 5, 3, 3, 2, 2, 3, 5, 5, 3, 3, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 4, 5, 5, 5, 5, 5, 5, 5, 5, 2, 2, 2, 3, 3, 2, 2, 5, 2, 3, 2, 2, 2, 2, 5, 5, 3, 2, 2, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 3, 5, 3, 3, 1, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 2, 2, 2, 2, 2, 3, 2, 2, 2, 3, 3, 3, 2, 2, 2, 2, 3] ... (440 total)`
- Title layout score: 91.8526
- Heading F1 score: 93.6709
- Level accuracy score: 76.6585
- Order score: 92.5000
- Main penalties:
  - 282 aligned headings have different relative levels.
  - 22 GT headings are missing.
  - 33 predicted headings are extra.

## Text Evaluation
- Text mode: normalized_full_text_preserve_newlines
- Text score: 98.8253
- Average edit distance: 0.0117
- Matched / missing / extra blocks: 1 / 0 / 0
- GT / Pred block counts: 1 / 1

### Worst Match Samples
1. op=match, distance=0.0117, GT blocks 0+1, Pred blocks 0+1
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
