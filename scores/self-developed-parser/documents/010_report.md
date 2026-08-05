# Financial Markdown Scoring Report

## Overall
- Final Score: 91.5469
- Table Score: 86.4177
- Title Layout Score: 93.3111
- Text Score: 95.7940

## Prediction Cleanup
- Mode: prediction_only_header_footer_cleanup
- Removed pred header/footer lines: 9
- Removed examples:
  - 广东万和新电气股份有限公司2020年年度报告全文
  - 广东万和新电气股份有限公司2020年年度报告全文
  - 广东万和新电气股份有限公司2020年年度报告全文
  - 广东万和新电气股份有限公司2020年年度报告全文
  - 广东万和新电气股份有限公司2020年年度报告全文
  - 广东万和新电气股份有限公司2020年年度报告全文
  - 广东万和新电气股份有限公司2020年年度报告全文
  - 广东万和新电气股份有限公司2020年年度报告全文
  - 广东万和新电气股份有限公司2020年年度报告全文

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
- Primary table score: 84.2868
- Alt table score: 81.5423
- Per-table rule: each predicted table keeps its higher one-to-one pair score from primary or alt GT.
- Per-table selected primary / alt pairs: 214 / 2
- Per-table reference table count: 215
- Matched / missing / extra tables: 216 / 0 / 25
- Table content score: 85.1465
- Table structure score: 87.2652
- Table matrix score: 86.4177
- Table alignment strategy: per_table_best_of_primary_alt_one_to_one

### Table Matches
- primary GT table 0 -> Pred table 1: pair=99.2011, structure=100.0000, content=98.0029, keywords=100.0000, match=99.7603, GT shape={'rows': 25, 'cols': 3}, Pred shape={'rows': 25, 'cols': 3}
- primary GT table 1 -> Pred table 2: pair=98.9189, structure=100.0000, content=97.2973, keywords=100.0000, match=99.6757, GT shape={'rows': 14, 'cols': 4}, Pred shape={'rows': 14, 'cols': 4}
- primary GT table 2 -> Pred table 3: pair=99.0303, structure=100.0000, content=97.5758, keywords=100.0000, match=99.7091, GT shape={'rows': 6, 'cols': 3}, Pred shape={'rows': 6, 'cols': 3}
- primary GT table 3 -> Pred table 4: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 3, 'cols': 2}, Pred shape={'rows': 3, 'cols': 2}
- primary GT table 4 -> Pred table 5: pair=95.7196, structure=100.0000, content=89.2989, keywords=97.6294, match=97.5306, GT shape={'rows': 3, 'cols': 2}, Pred shape={'rows': 3, 'cols': 2}
- primary GT table 5 -> Pred table 6: pair=98.9189, structure=100.0000, content=97.2973, keywords=100.0000, match=99.6757, GT shape={'rows': 3, 'cols': 2}, Pred shape={'rows': 3, 'cols': 2}
- primary GT table 6 -> Pred table 7: pair=81.8868, structure=87.8788, content=72.8988, keywords=95.6250, match=89.9543, GT shape={'rows': 11, 'cols': 5}, Pred shape={'rows': 9, 'cols': 5}
- primary GT table 7 -> Pred table 9: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 5, 'cols': 5}, Pred shape={'rows': 5, 'cols': 5}
- primary GT table 8 -> Pred table 10: pair=93.1643, structure=92.5926, content=94.0217, keywords=97.6667, match=95.3012, GT shape={'rows': 8, 'cols': 5}, Pred shape={'rows': 9, 'cols': 5}
- primary GT table 9 -> Pred table 11: pair=98.7487, structure=100.0000, content=96.8717, keywords=100.0000, match=99.6246, GT shape={'rows': 23, 'cols': 2}, Pred shape={'rows': 23, 'cols': 2}
- primary GT table 10 -> Pred table 12: pair=99.5634, structure=100.0000, content=98.9086, keywords=100.0000, match=99.8690, GT shape={'rows': 16, 'cols': 6}, Pred shape={'rows': 16, 'cols': 6}
- primary GT table 11 -> Pred table 13: pair=99.6859, structure=100.0000, content=99.2147, keywords=100.0000, match=99.9058, GT shape={'rows': 14, 'cols': 7}, Pred shape={'rows': 14, 'cols': 7}
- primary GT table 12 -> Pred table 14: pair=99.7838, structure=100.0000, content=99.4595, keywords=100.0000, match=99.9351, GT shape={'rows': 10, 'cols': 6}, Pred shape={'rows': 10, 'cols': 6}
- primary GT table 13 -> Pred table 15: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 3, 'cols': 7}, Pred shape={'rows': 3, 'cols': 7}
- primary GT table 14 -> Pred table 16: pair=99.7504, structure=100.0000, content=99.3760, keywords=100.0000, match=99.9251, GT shape={'rows': 12, 'cols': 7}, Pred shape={'rows': 12, 'cols': 7}
- primary GT table 15 -> Pred table 17: pair=99.1111, structure=100.0000, content=97.7778, keywords=100.0000, match=99.7333, GT shape={'rows': 3, 'cols': 2}, Pred shape={'rows': 3, 'cols': 2}
- primary GT table 16 -> Pred table 18: pair=99.5833, structure=100.0000, content=98.9583, keywords=100.0000, match=99.8750, GT shape={'rows': 7, 'cols': 4}, Pred shape={'rows': 7, 'cols': 4}
- primary GT table 17 -> Pred table 19: pair=99.1209, structure=100.0000, content=97.8022, keywords=100.0000, match=99.7363, GT shape={'rows': 3, 'cols': 2}, Pred shape={'rows': 3, 'cols': 2}
- primary GT table 18 -> Pred table 20: pair=99.5812, structure=100.0000, content=98.9529, keywords=100.0000, match=99.8744, GT shape={'rows': 7, 'cols': 4}, Pred shape={'rows': 7, 'cols': 4}
- primary GT table 19 -> Pred table 21: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 6, 'cols': 5}, Pred shape={'rows': 6, 'cols': 5}
- primary GT table 20 -> Pred table 22: pair=98.8732, structure=100.0000, content=97.1831, keywords=100.0000, match=99.6620, GT shape={'rows': 7, 'cols': 4}, Pred shape={'rows': 7, 'cols': 4}
- primary GT table 21 -> Pred table 23: pair=99.8505, structure=100.0000, content=99.6262, keywords=100.0000, match=99.9552, GT shape={'rows': 11, 'cols': 4}, Pred shape={'rows': 11, 'cols': 4}
- primary GT table 22 -> Pred table 24: pair=99.7315, structure=100.0000, content=99.3289, keywords=100.0000, match=99.9194, GT shape={'rows': 9, 'cols': 5}, Pred shape={'rows': 9, 'cols': 5}
- primary GT table 23 -> Pred table 25: pair=99.7193, structure=100.0000, content=99.2982, keywords=100.0000, match=99.9158, GT shape={'rows': 11, 'cols': 7}, Pred shape={'rows': 11, 'cols': 7}
- primary GT table 24 -> Pred table 26: pair=99.8574, structure=100.0000, content=99.6435, keywords=100.0000, match=99.9572, GT shape={'rows': 9, 'cols': 9}, Pred shape={'rows': 9, 'cols': 9}
- primary GT table 25 -> Pred table 27: pair=99.0164, structure=100.0000, content=97.5410, keywords=100.0000, match=99.7049, GT shape={'rows': 5, 'cols': 3}, Pred shape={'rows': 5, 'cols': 3}
- primary GT table 26 -> Pred table 28: pair=97.4194, structure=100.0000, content=93.5484, keywords=100.0000, match=99.2258, GT shape={'rows': 2, 'cols': 3}, Pred shape={'rows': 2, 'cols': 3}
- primary GT table 27 -> Pred table 29: pair=81.9766, structure=89.4737, content=70.7311, keywords=99.4068, match=92.1911, GT shape={'rows': 16, 'cols': 9}, Pred shape={'rows': 19, 'cols': 9}
- primary GT table 28 -> Pred table 30: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 3, 'cols': 3}, Pred shape={'rows': 3, 'cols': 3}
- primary GT table 29 -> Pred table 31: pair=99.3443, structure=100.0000, content=98.3607, keywords=96.1111, match=97.8588, GT shape={'rows': 3, 'cols': 7}, Pred shape={'rows': 3, 'cols': 7}

## Title Layout Evaluation
- GT raw heading levels: `[1, 2, 2, 2, 3, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 3, 3, 2, 3, 4, 4, 4, 5, 5, 5, 4, 5, 5, 3, 4, 3, 4, 4, 4, 4, 4, 2, 3, 4, 5, 5, 5, 5, 5, 4, 4, 5, 5, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 4, 4, 4, 3, 4, 4, 4, 4, 4, 4, 4, 3, 4, 4, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 4, 2, 3, 3, 3, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3] ... (504 total)`
- Pred raw heading levels: `[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2] ... (489 total)`
- GT relative heading levels: `[1, 2, 2, 2, 3, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 3, 3, 2, 3, 4, 4, 4, 5, 5, 5, 4, 5, 5, 3, 4, 3, 4, 4, 4, 4, 4, 2, 3, 4, 5, 5, 5, 5, 5, 4, 4, 5, 5, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 4, 4, 4, 3, 4, 4, 4, 4, 4, 4, 4, 3, 4, 4, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 4, 2, 3, 3, 3, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3] ... (504 total)`
- Pred relative heading levels: `[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2] ... (489 total)`
- Title layout score: 93.3111
- Heading F1 score: 97.8852
- Level accuracy score: 53.6008
- Order score: 96.4286
- Main penalties:
  - 471 aligned headings have different relative levels.
  - 18 GT headings are missing.
  - 3 predicted headings are extra.

## Text Evaluation
- Text mode: normalized_full_text_preserve_newlines
- Text score: 95.7940
- Average edit distance: 0.0421
- Matched / missing / extra blocks: 1 / 0 / 0
- GT / Pred block counts: 1 / 1

### Worst Match Samples
1. op=match, distance=0.0421, GT blocks 0+1, Pred blocks 0+1
   - GT: 广东万和新电气股份有限公司\n\n2020年年度报告\n![]\nvanward万和\n让家更温暖\n\n2021年4月29日\n\n第一节重要提示目录和释义\n\n公司董事会监事会及董事监事高级管理人员保证年度报告内容的真实准确完整不存在虚假记载误导性陈述或重大遗漏并承担...
   - Pred: 广东万和新电气股份有限公司\n\n2020年年度报告\n\n117346613\n\n2021年4月29日\n\n第一节重要提示目录和释义\n\n公司董事会监事会及董事监事高级管理人员保证年度报告内容的真实准确完整不存在虚假记载误导性陈述或重大遗漏并承担个别和连带的法律责任...

## Notes
- Table score compares extracted HTML and Markdown pipe tables after conversion to cell matrices.
- With primary or alt strategy, table matching is GT-driven one-to-one: each GT table chooses one best unused Pred table.
- With max and two GT files, each predicted table keeps the higher pair score from the two independently one-to-one-matched GT variants.
- Table pair score is 60% structure score and 40% content score; table content score uses normalized edit distance on flattened table text.
- Title layout score uses heading text only for anchor alignment, then combines heading F1, relative-level accuracy, and order coverage.
- Text score removes tables, keeps heading words, preserves newlines, and scores the full body as one character sequence.
- No-value page headers and footers are removed from prediction Markdown only; GT Markdown is kept as the reference answer.
- Current limitations: complex nested tables, heavily malformed HTML, and table semantic equivalence beyond cell text are only approximated.
