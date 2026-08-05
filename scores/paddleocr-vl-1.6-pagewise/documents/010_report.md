# Financial Markdown Scoring Report

## Overall
- Final Score: 83.8440
- Table Score: 64.2778
- Title Layout Score: 92.5988
- Text Score: 99.0328

## Prediction Cleanup
- Mode: prediction_only_header_footer_cleanup
- Removed pred header/footer lines: 13
- Removed examples:
  - 第一节 重要提示、目录和释义.....2
  - 第二节 公司简介和主要财务指标.....5
  - 第三节 公司业务概要.....9
  - 第四节 经营情况讨论与分析.....14
  - 第五节 重要事项.....35
  - 第六节 股份变动及股东情况.....57
  - 第七节 优先股相关情况.....63
  - 第八节 可转换公司债券相关情况.....64
  - 第九节 董事、监事、高级管理人员和员工情况.....65
  - 第十节 公司治理.....77

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
- Primary table score: 61.3847
- Alt table score: 61.6704
- Per-table rule: each predicted table keeps its higher one-to-one pair score from primary or alt GT.
- Per-table selected primary / alt pairs: 214 / 4
- Per-table reference table count: 215
- Matched / missing / extra tables: 218 / 0 / 88
- Table content score: 61.8766
- Table structure score: 65.8785
- Table matrix score: 64.2778
- Table alignment strategy: per_table_best_of_primary_alt_one_to_one

### Table Matches
- primary GT table 0 -> Pred table 0: pair=99.2582, structure=100.0000, content=98.1455, keywords=100.0000, match=99.7775, GT shape={'rows': 25, 'cols': 3}, Pred shape={'rows': 25, 'cols': 3}
- primary GT table 1 -> Pred table 1: pair=98.2301, structure=100.0000, content=95.5752, keywords=100.0000, match=99.4690, GT shape={'rows': 14, 'cols': 4}, Pred shape={'rows': 14, 'cols': 4}
- primary GT table 2 -> Pred table 2: pair=99.0303, structure=100.0000, content=97.5758, keywords=100.0000, match=99.7091, GT shape={'rows': 6, 'cols': 3}, Pred shape={'rows': 6, 'cols': 3}
- primary GT table 3 -> Pred table 3: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 3, 'cols': 2}, Pred shape={'rows': 3, 'cols': 2}
- primary GT table 4 -> Pred table 4: pair=96.1481, structure=100.0000, content=90.3704, keywords=100.0000, match=98.8444, GT shape={'rows': 3, 'cols': 2}, Pred shape={'rows': 3, 'cols': 2}
- primary GT table 5 -> Pred table 5: pair=97.8947, structure=100.0000, content=94.7368, keywords=100.0000, match=99.3684, GT shape={'rows': 3, 'cols': 2}, Pred shape={'rows': 3, 'cols': 2}
- primary GT table 6 -> Pred table 6: pair=81.8868, structure=87.8788, content=72.8988, keywords=95.6250, match=89.9543, GT shape={'rows': 11, 'cols': 5}, Pred shape={'rows': 9, 'cols': 5}
- primary GT table 7 -> Pred table 8: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 5, 'cols': 5}, Pred shape={'rows': 5, 'cols': 5}
- primary GT table 8 -> Pred table 10: pair=88.1387, structure=91.6667, content=82.8467, keywords=92.5000, match=91.0250, GT shape={'rows': 8, 'cols': 5}, Pred shape={'rows': 7, 'cols': 5}
- primary GT table 9 -> Pred table 11: pair=98.0738, structure=100.0000, content=95.1844, keywords=100.0000, match=99.4221, GT shape={'rows': 23, 'cols': 2}, Pred shape={'rows': 23, 'cols': 2}
- primary GT table 10 -> Pred table 12: pair=99.4543, structure=100.0000, content=98.6357, keywords=100.0000, match=99.8363, GT shape={'rows': 16, 'cols': 6}, Pred shape={'rows': 16, 'cols': 6}
- alt GT table 13 -> Pred table 13: pair=64.9224, structure=71.4286, content=55.1630, keywords=100.0000, match=83.7624, GT shape={'rows': 4, 'cols': 7}, Pred shape={'rows': 7, 'cols': 7}
- alt GT table 12 -> Pred table 14: pair=64.3720, structure=81.6327, content=38.4810, keywords=57.0652, match=64.1707, GT shape={'rows': 6, 'cols': 6}, Pred shape={'rows': 7, 'cols': 7}
- primary GT table 12 -> Pred table 15: pair=99.7838, structure=100.0000, content=99.4595, keywords=100.0000, match=99.9351, GT shape={'rows': 10, 'cols': 6}, Pred shape={'rows': 10, 'cols': 6}
- primary GT table 13 -> Pred table 16: pair=98.8489, structure=100.0000, content=97.1223, keywords=100.0000, match=99.6547, GT shape={'rows': 3, 'cols': 7}, Pred shape={'rows': 3, 'cols': 7}
- primary GT table 14 -> Pred table 17: pair=99.7504, structure=100.0000, content=99.3760, keywords=100.0000, match=99.9251, GT shape={'rows': 12, 'cols': 7}, Pred shape={'rows': 12, 'cols': 7}
- primary GT table 15 -> Pred table 18: pair=99.1111, structure=100.0000, content=97.7778, keywords=100.0000, match=99.7333, GT shape={'rows': 3, 'cols': 2}, Pred shape={'rows': 3, 'cols': 2}
- primary GT table 16 -> Pred table 19: pair=99.5833, structure=100.0000, content=98.9583, keywords=100.0000, match=99.8750, GT shape={'rows': 7, 'cols': 4}, Pred shape={'rows': 7, 'cols': 4}
- primary GT table 17 -> Pred table 20: pair=99.1209, structure=100.0000, content=97.8022, keywords=100.0000, match=99.7363, GT shape={'rows': 3, 'cols': 2}, Pred shape={'rows': 3, 'cols': 2}
- primary GT table 18 -> Pred table 21: pair=99.5812, structure=100.0000, content=98.9529, keywords=100.0000, match=99.8744, GT shape={'rows': 7, 'cols': 4}, Pred shape={'rows': 7, 'cols': 4}
- primary GT table 19 -> Pred table 22: pair=57.2549, structure=66.6667, content=43.1373, keywords=100.0000, match=80.5098, GT shape={'rows': 6, 'cols': 5}, Pred shape={'rows': 3, 'cols': 5}
- primary GT table 20 -> Pred table 24: pair=98.4977, structure=100.0000, content=96.2441, keywords=100.0000, match=99.5493, GT shape={'rows': 7, 'cols': 4}, Pred shape={'rows': 7, 'cols': 4}
- primary GT table 21 -> Pred table 25: pair=77.1585, structure=81.8182, content=70.1689, keywords=88.3333, match=83.6778, GT shape={'rows': 11, 'cols': 4}, Pred shape={'rows': 8, 'cols': 4}
- primary GT table 22 -> Pred table 27: pair=99.7315, structure=100.0000, content=99.3289, keywords=100.0000, match=99.9194, GT shape={'rows': 9, 'cols': 5}, Pred shape={'rows': 9, 'cols': 5}
- primary GT table 23 -> Pred table 28: pair=99.7193, structure=100.0000, content=99.2982, keywords=100.0000, match=99.9158, GT shape={'rows': 11, 'cols': 7}, Pred shape={'rows': 11, 'cols': 7}
- primary GT table 24 -> Pred table 29: pair=73.6898, structure=77.7778, content=67.5579, keywords=91.2500, match=83.2875, GT shape={'rows': 9, 'cols': 9}, Pred shape={'rows': 6, 'cols': 9}
- primary GT table 25 -> Pred table 31: pair=99.0164, structure=100.0000, content=97.5410, keywords=100.0000, match=99.7049, GT shape={'rows': 5, 'cols': 3}, Pred shape={'rows': 5, 'cols': 3}
- primary GT table 26 -> Pred table 32: pair=97.4194, structure=100.0000, content=93.5484, keywords=100.0000, match=99.2258, GT shape={'rows': 2, 'cols': 3}, Pred shape={'rows': 2, 'cols': 3}
- primary GT table 27 -> Pred table 33: pair=27.2863, structure=41.6667, content=5.7158, keywords=100.0000, match=66.5192, GT shape={'rows': 16, 'cols': 9}, Pred shape={'rows': 2, 'cols': 9}
- primary GT table 28 -> Pred table 38: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 3, 'cols': 3}, Pred shape={'rows': 3, 'cols': 3}

## Title Layout Evaluation
- GT raw heading levels: `[1, 2, 2, 2, 3, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 3, 3, 2, 3, 4, 4, 4, 5, 5, 5, 4, 5, 5, 3, 4, 3, 4, 4, 4, 4, 4, 2, 3, 4, 5, 5, 5, 5, 5, 4, 4, 5, 5, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 4, 4, 4, 3, 4, 4, 4, 4, 4, 4, 4, 3, 4, 4, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 4, 2, 3, 3, 3, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3] ... (504 total)`
- Pred raw heading levels: `[1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 2, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 4, 4, 3, 3, 2, 2, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2] ... (530 total)`
- GT relative heading levels: `[1, 2, 2, 2, 3, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 3, 3, 2, 3, 4, 4, 4, 5, 5, 5, 4, 5, 5, 3, 4, 3, 4, 4, 4, 4, 4, 2, 3, 4, 5, 5, 5, 5, 5, 4, 4, 5, 5, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 4, 4, 4, 3, 4, 4, 4, 4, 4, 4, 4, 3, 4, 4, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 4, 2, 3, 3, 3, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3] ... (504 total)`
- Pred relative heading levels: `[1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 2, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 4, 4, 3, 3, 2, 2, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2] ... (530 total)`
- Title layout score: 92.5988
- Heading F1 score: 97.0986
- Level accuracy score: 54.4821
- Order score: 94.7170
- Main penalties:
  - 487 aligned headings have different relative levels.
  - 2 GT headings are missing.
  - 28 predicted headings are extra.

## Text Evaluation
- Text mode: normalized_full_text_preserve_newlines
- Text score: 99.0328
- Average edit distance: 0.0097
- Matched / missing / extra blocks: 1 / 0 / 0
- GT / Pred block counts: 1 / 1

### Worst Match Samples
1. op=match, distance=0.0097, GT blocks 0+1, Pred blocks 0+1
   - GT: 广东万和新电气股份有限公司\n\n2020年年度报告\n![]\nvanward万和\n让家更温暖\n\n2021年4月29日\n\n第一节重要提示目录和释义\n\n公司董事会监事会及董事监事高级管理人员保证年度报告内容的真实准确完整不存在虚假记载误导性陈述或重大遗漏并承担...
   - Pred: 广东万和新电气股份有限公司\n\n2020年年度报告\n\nanward万和让家更温暖\n\n2021年4月29日\n\n第一节重要提示目录和释义\n\n公司董事会监事会及董事监事高级管理人员保证年度报告内容的真实准确完整不存在虚假记载误导性陈述或重大遗漏并承担个别和连带的...

## Notes
- Table score compares extracted HTML and Markdown pipe tables after conversion to cell matrices.
- With primary or alt strategy, table matching is GT-driven one-to-one: each GT table chooses one best unused Pred table.
- With max and two GT files, each predicted table keeps the higher pair score from the two independently one-to-one-matched GT variants.
- Table pair score is 60% structure score and 40% content score; table content score uses normalized edit distance on flattened table text.
- Title layout score uses heading text only for anchor alignment, then combines heading F1, relative-level accuracy, and order coverage.
- Text score removes tables, keeps heading words, preserves newlines, and scores the full body as one character sequence.
- No-value page headers and footers are removed from prediction Markdown only; GT Markdown is kept as the reference answer.
- Current limitations: complex nested tables, heavily malformed HTML, and table semantic equivalence beyond cell text are only approximated.
