# Financial Markdown Scoring Report

## Overall
- Final Score: 96.8289
- Table Score: 96.2588
- Title Layout Score: 92.4885
- Text Score: 99.5692

## Prediction Cleanup
- Mode: prediction_only_header_footer_cleanup
- Removed pred header/footer lines: 9
- Removed examples:
  - 第二节 公司简介和主要财务指标. .. 5
  - 第三节 公司业务概要 ... 9
  - 第四节 经营情况讨论与分析. ... 14
  - 第五节 重要事项. ... 35
  - 第六节 股份变动及股东情况. .. 57
  - 第七节 优先股相关情况. ... 63
  - 第八节 可转换公司债券相关情况. ... 64
  - 第九节 董事、监事、高级管理人员和员工情况. .. 65
  - 第十节 公司治理 ... 77

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
- Primary table score: 95.9386
- Alt table score: 87.2669
- Per-table rule: each predicted table keeps its higher one-to-one pair score from primary or alt GT.
- Per-table selected primary / alt pairs: 215 / 0
- Per-table reference table count: 215
- Matched / missing / extra tables: 215 / 0 / 4
- Table content score: 95.2703
- Table structure score: 96.9178
- Table matrix score: 96.2588
- Table alignment strategy: per_table_best_of_primary_alt_one_to_one

### Table Matches
- primary GT table 0 -> Pred table 0: pair=94.0086, structure=100.0000, content=85.0214, keywords=100.0000, match=98.2026, GT shape={'rows': 25, 'cols': 3}, Pred shape={'rows': 25, 'cols': 3}
- primary GT table 1 -> Pred table 1: pair=98.9189, structure=100.0000, content=97.2973, keywords=100.0000, match=99.6757, GT shape={'rows': 14, 'cols': 4}, Pred shape={'rows': 14, 'cols': 4}
- primary GT table 2 -> Pred table 2: pair=99.0303, structure=100.0000, content=97.5758, keywords=100.0000, match=99.7091, GT shape={'rows': 6, 'cols': 3}, Pred shape={'rows': 6, 'cols': 3}
- primary GT table 3 -> Pred table 3: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 3, 'cols': 2}, Pred shape={'rows': 3, 'cols': 2}
- primary GT table 4 -> Pred table 4: pair=97.9688, structure=100.0000, content=94.9219, keywords=100.0000, match=99.3906, GT shape={'rows': 3, 'cols': 2}, Pred shape={'rows': 3, 'cols': 2}
- primary GT table 5 -> Pred table 5: pair=98.9189, structure=100.0000, content=97.2973, keywords=100.0000, match=99.6757, GT shape={'rows': 3, 'cols': 2}, Pred shape={'rows': 3, 'cols': 2}
- primary GT table 6 -> Pred table 6: pair=95.7763, structure=94.4444, content=97.7740, keywords=100.0000, match=97.6218, GT shape={'rows': 11, 'cols': 5}, Pred shape={'rows': 12, 'cols': 5}
- primary GT table 7 -> Pred table 7: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 5, 'cols': 5}, Pred shape={'rows': 5, 'cols': 5}
- primary GT table 8 -> Pred table 8: pair=93.3698, structure=92.5926, content=94.5355, keywords=97.6667, match=95.3628, GT shape={'rows': 8, 'cols': 5}, Pred shape={'rows': 9, 'cols': 5}
- primary GT table 9 -> Pred table 9: pair=98.8297, structure=100.0000, content=97.0742, keywords=100.0000, match=99.6489, GT shape={'rows': 23, 'cols': 2}, Pred shape={'rows': 23, 'cols': 2}
- primary GT table 10 -> Pred table 10: pair=96.6529, structure=100.0000, content=91.6324, keywords=100.0000, match=98.9959, GT shape={'rows': 16, 'cols': 6}, Pred shape={'rows': 16, 'cols': 6}
- primary GT table 11 -> Pred table 11: pair=99.6859, structure=100.0000, content=99.2147, keywords=100.0000, match=99.9058, GT shape={'rows': 14, 'cols': 7}, Pred shape={'rows': 14, 'cols': 7}
- primary GT table 12 -> Pred table 12: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 10, 'cols': 6}, Pred shape={'rows': 10, 'cols': 6}
- primary GT table 13 -> Pred table 13: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 3, 'cols': 7}, Pred shape={'rows': 3, 'cols': 7}
- primary GT table 14 -> Pred table 14: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 12, 'cols': 7}, Pred shape={'rows': 12, 'cols': 7}
- primary GT table 15 -> Pred table 15: pair=99.1111, structure=100.0000, content=97.7778, keywords=100.0000, match=99.7333, GT shape={'rows': 3, 'cols': 2}, Pred shape={'rows': 3, 'cols': 2}
- primary GT table 16 -> Pred table 16: pair=99.5833, structure=100.0000, content=98.9583, keywords=100.0000, match=99.8750, GT shape={'rows': 7, 'cols': 4}, Pred shape={'rows': 7, 'cols': 4}
- primary GT table 17 -> Pred table 17: pair=99.1209, structure=100.0000, content=97.8022, keywords=100.0000, match=99.7363, GT shape={'rows': 3, 'cols': 2}, Pred shape={'rows': 3, 'cols': 2}
- primary GT table 18 -> Pred table 18: pair=99.5812, structure=100.0000, content=98.9529, keywords=100.0000, match=99.8744, GT shape={'rows': 7, 'cols': 4}, Pred shape={'rows': 7, 'cols': 4}
- primary GT table 19 -> Pred table 19: pair=99.6863, structure=100.0000, content=99.2157, keywords=100.0000, match=99.9059, GT shape={'rows': 6, 'cols': 5}, Pred shape={'rows': 6, 'cols': 5}
- primary GT table 20 -> Pred table 20: pair=99.2417, structure=100.0000, content=98.1043, keywords=100.0000, match=99.7725, GT shape={'rows': 7, 'cols': 4}, Pred shape={'rows': 7, 'cols': 4}
- primary GT table 21 -> Pred table 21: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 11, 'cols': 4}, Pred shape={'rows': 11, 'cols': 4}
- primary GT table 22 -> Pred table 22: pair=99.7315, structure=100.0000, content=99.3289, keywords=100.0000, match=99.9194, GT shape={'rows': 9, 'cols': 5}, Pred shape={'rows': 9, 'cols': 5}
- primary GT table 23 -> Pred table 23: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 11, 'cols': 7}, Pred shape={'rows': 11, 'cols': 7}
- primary GT table 24 -> Pred table 24: pair=99.8574, structure=100.0000, content=99.6435, keywords=100.0000, match=99.9572, GT shape={'rows': 9, 'cols': 9}, Pred shape={'rows': 9, 'cols': 9}
- primary GT table 25 -> Pred table 25: pair=99.0164, structure=100.0000, content=97.5410, keywords=100.0000, match=99.7049, GT shape={'rows': 5, 'cols': 3}, Pred shape={'rows': 5, 'cols': 3}
- primary GT table 26 -> Pred table 26: pair=97.4194, structure=100.0000, content=93.5484, keywords=100.0000, match=99.2258, GT shape={'rows': 2, 'cols': 3}, Pred shape={'rows': 2, 'cols': 3}
- primary GT table 27 -> Pred table 27: pair=82.3742, structure=89.4737, content=71.7250, keywords=99.4068, match=92.3104, GT shape={'rows': 16, 'cols': 9}, Pred shape={'rows': 19, 'cols': 9}
- primary GT table 28 -> Pred table 28: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 3, 'cols': 3}, Pred shape={'rows': 3, 'cols': 3}
- primary GT table 29 -> Pred table 29: pair=99.3443, structure=100.0000, content=98.3607, keywords=100.0000, match=99.8033, GT shape={'rows': 3, 'cols': 7}, Pred shape={'rows': 3, 'cols': 7}

## Title Layout Evaluation
- GT raw heading levels: `[1, 2, 2, 2, 3, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 3, 3, 2, 3, 4, 4, 4, 5, 5, 5, 4, 5, 5, 3, 4, 3, 4, 4, 4, 4, 4, 2, 3, 4, 5, 5, 5, 5, 5, 4, 4, 5, 5, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 4, 4, 4, 3, 4, 4, 4, 4, 4, 4, 4, 3, 4, 4, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 4, 2, 3, 3, 3, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3] ... (504 total)`
- Pred raw heading levels: `[1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2] ... (508 total)`
- GT relative heading levels: `[1, 2, 2, 2, 3, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 3, 3, 2, 3, 4, 4, 4, 5, 5, 5, 4, 5, 5, 3, 4, 3, 4, 4, 4, 4, 4, 2, 3, 4, 5, 5, 5, 5, 5, 4, 4, 5, 5, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 4, 4, 4, 3, 4, 4, 4, 4, 4, 4, 4, 3, 4, 4, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 4, 2, 3, 3, 3, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3] ... (504 total)`
- Pred relative heading levels: `[1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2] ... (508 total)`
- Title layout score: 92.4885
- Heading F1 score: 96.8379
- Level accuracy score: 53.7245
- Order score: 96.4567
- Main penalties:
  - 475 aligned headings have different relative levels.
  - 14 GT headings are missing.
  - 18 predicted headings are extra.

## Text Evaluation
- Text mode: normalized_full_text_preserve_newlines
- Text score: 99.5692
- Average edit distance: 0.0043
- Matched / missing / extra blocks: 1 / 0 / 0
- GT / Pred block counts: 1 / 1

### Worst Match Samples
1. op=match, distance=0.0043, GT blocks 0+1, Pred blocks 0+1
   - GT: 广东万和新电气股份有限公司\n\n2020年年度报告\n![]\nvanward万和\n让家更温暖\n\n2021年4月29日\n\n第一节重要提示目录和释义\n\n公司董事会监事会及董事监事高级管理人员保证年度报告内容的真实准确完整不存在虚假记载误导性陈述或重大遗漏并承担...
   - Pred: 广东万和新电气股份有限公司\n\n2020年年度报告\n\nVanward万和让家更温暖\n\n2021年4月29日\n\n第一节重要提示目录和释义\n\n公司董事会监事会及董事监事高级管理人员保证年度报告内容的真实准确完整不存在虚假记载误导性陈述或重大遗漏并承担个别和连带...

## Notes
- Table score compares extracted HTML and Markdown pipe tables after conversion to cell matrices.
- With primary or alt strategy, table matching is GT-driven one-to-one: each GT table chooses one best unused Pred table.
- With max and two GT files, each predicted table keeps the higher pair score from the two independently one-to-one-matched GT variants.
- Table pair score is 60% structure score and 40% content score; table content score uses normalized edit distance on flattened table text.
- Title layout score uses heading text only for anchor alignment, then combines heading F1, relative-level accuracy, and order coverage.
- Text score removes tables, keeps heading words, preserves newlines, and scores the full body as one character sequence.
- No-value page headers and footers are removed from prediction Markdown only; GT Markdown is kept as the reference answer.
- Current limitations: complex nested tables, heavily malformed HTML, and table semantic equivalence beyond cell text are only approximated.
