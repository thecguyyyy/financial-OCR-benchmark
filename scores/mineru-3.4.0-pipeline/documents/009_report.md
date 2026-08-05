# Financial Markdown Scoring Report

## Overall
- Final Score: 96.6793
- Table Score: 96.2029
- Title Layout Score: 92.7303
- Text Score: 99.1303

## Prediction Cleanup
- Mode: prediction_only_header_footer_cleanup
- Removed pred header/footer lines: 8
- Removed examples:
  - 第三节 管理层讨论与分析. .... 10
  - 第四节 公司治理. .. 26
  - 第五节 环境和社会责任. ... 42
  - 第六节 重要事项... .. 44
  - 第七节 股份变动及股东情况.. .. 56
  - 第八节 优先股相关情况... .... 62
  - 第九节 债券相关情况.. ... 63
  - 第十节 财务报告.... ..... 64

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
- Primary table score: 95.2998
- Alt table score: 90.9400
- Per-table rule: each predicted table keeps its higher one-to-one pair score from primary or alt GT.
- Per-table selected primary / alt pairs: 182 / 1
- Per-table reference table count: 182
- Matched / missing / extra tables: 183 / 0 / 3
- Table content score: 95.1376
- Table structure score: 96.9131
- Table matrix score: 96.2029
- Table alignment strategy: per_table_best_of_primary_alt_one_to_one

### Table Matches
- primary GT table 0 -> Pred table 0: pair=99.2583, structure=100.0000, content=98.1457, keywords=100.0000, match=99.7775, GT shape={'rows': 28, 'cols': 3}, Pred shape={'rows': 28, 'cols': 3}
- primary GT table 1 -> Pred table 1: pair=99.2944, structure=100.0000, content=98.2359, keywords=100.0000, match=99.7883, GT shape={'rows': 13, 'cols': 4}, Pred shape={'rows': 13, 'cols': 4}
- primary GT table 2 -> Pred table 2: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 6, 'cols': 3}, Pred shape={'rows': 6, 'cols': 3}
- primary GT table 3 -> Pred table 3: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 3, 'cols': 2}, Pred shape={'rows': 3, 'cols': 2}
- primary GT table 4 -> Pred table 4: pair=98.1609, structure=100.0000, content=95.4023, keywords=100.0000, match=99.4483, GT shape={'rows': 3, 'cols': 2}, Pred shape={'rows': 3, 'cols': 2}
- primary GT table 5 -> Pred table 5: pair=98.9316, structure=100.0000, content=97.3289, keywords=100.0000, match=99.6795, GT shape={'rows': 11, 'cols': 5}, Pred shape={'rows': 11, 'cols': 5}
- primary GT table 6 -> Pred table 6: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 5, 'cols': 5}, Pred shape={'rows': 5, 'cols': 5}
- primary GT table 7 -> Pred table 7: pair=99.0370, structure=100.0000, content=97.5926, keywords=100.0000, match=99.7111, GT shape={'rows': 11, 'cols': 5}, Pred shape={'rows': 11, 'cols': 5}
- primary GT table 8 -> Pred table 8: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 3, 'cols': 6}, Pred shape={'rows': 3, 'cols': 6}
- primary GT table 9 -> Pred table 9: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 7, 'cols': 6}, Pred shape={'rows': 7, 'cols': 6}
- primary GT table 10 -> Pred table 10: pair=98.9809, structure=100.0000, content=97.4522, keywords=100.0000, match=99.6943, GT shape={'rows': 4, 'cols': 7}, Pred shape={'rows': 4, 'cols': 7}
- primary GT table 11 -> Pred table 11: pair=99.9045, structure=100.0000, content=99.7613, keywords=100.0000, match=99.9714, GT shape={'rows': 12, 'cols': 6}, Pred shape={'rows': 12, 'cols': 6}
- primary GT table 12 -> Pred table 12: pair=97.3878, structure=100.0000, content=93.4694, keywords=82.5000, match=90.4663, GT shape={'rows': 6, 'cols': 7}, Pred shape={'rows': 6, 'cols': 7}
- primary GT table 13 -> Pred table 13: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 5, 'cols': 7}, Pred shape={'rows': 5, 'cols': 7}
- primary GT table 14 -> Pred table 14: pair=99.0909, structure=100.0000, content=97.7273, keywords=100.0000, match=99.7273, GT shape={'rows': 3, 'cols': 2}, Pred shape={'rows': 3, 'cols': 2}
- primary GT table 15 -> Pred table 15: pair=98.9362, structure=100.0000, content=97.3404, keywords=100.0000, match=99.6809, GT shape={'rows': 7, 'cols': 4}, Pred shape={'rows': 7, 'cols': 4}
- primary GT table 16 -> Pred table 16: pair=99.1209, structure=100.0000, content=97.8022, keywords=100.0000, match=99.7363, GT shape={'rows': 3, 'cols': 2}, Pred shape={'rows': 3, 'cols': 2}
- primary GT table 17 -> Pred table 17: pair=98.9744, structure=100.0000, content=97.4359, keywords=100.0000, match=99.6923, GT shape={'rows': 7, 'cols': 4}, Pred shape={'rows': 7, 'cols': 4}
- primary GT table 18 -> Pred table 18: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 5, 'cols': 5}, Pred shape={'rows': 5, 'cols': 5}
- primary GT table 19 -> Pred table 19: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 11, 'cols': 4}, Pred shape={'rows': 11, 'cols': 4}
- primary GT table 20 -> Pred table 20: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 5, 'cols': 5}, Pred shape={'rows': 5, 'cols': 5}
- primary GT table 21 -> Pred table 21: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 10, 'cols': 7}, Pred shape={'rows': 10, 'cols': 7}
- primary GT table 22 -> Pred table 22: pair=99.6262, structure=100.0000, content=99.0654, keywords=100.0000, match=99.8879, GT shape={'rows': 2, 'cols': 9}, Pred shape={'rows': 2, 'cols': 9}
- primary GT table 23 -> Pred table 23: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 5, 'cols': 9}, Pred shape={'rows': 5, 'cols': 9}
- primary GT table 24 -> Pred table 24: pair=96.8627, structure=100.0000, content=92.1569, keywords=100.0000, match=99.0588, GT shape={'rows': 2, 'cols': 3}, Pred shape={'rows': 2, 'cols': 3}
- primary GT table 25 -> Pred table 25: pair=91.3191, structure=93.3333, content=88.2979, keywords=100.0000, match=96.0624, GT shape={'rows': 9, 'cols': 15}, Pred shape={'rows': 10, 'cols': 15}
- primary GT table 26 -> Pred table 26: pair=99.8606, structure=100.0000, content=99.6516, keywords=100.0000, match=99.9582, GT shape={'rows': 4, 'cols': 9}, Pred shape={'rows': 4, 'cols': 9}
- primary GT table 27 -> Pred table 27: pair=99.5506, structure=100.0000, content=98.8764, keywords=100.0000, match=99.8652, GT shape={'rows': 10, 'cols': 3}, Pred shape={'rows': 10, 'cols': 3}
- primary GT table 28 -> Pred table 28: pair=99.4613, structure=100.0000, content=98.6532, keywords=100.0000, match=99.8384, GT shape={'rows': 5, 'cols': 6}, Pred shape={'rows': 5, 'cols': 6}
- primary GT table 29 -> Pred table 29: pair=93.7456, structure=95.5556, content=91.0308, keywords=100.0000, match=97.2348, GT shape={'rows': 14, 'cols': 13}, Pred shape={'rows': 15, 'cols': 13}

## Title Layout Evaluation
- GT raw heading levels: `[1, 2, 2, 5, 5, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 3, 2, 3, 4, 4, 5, 5, 3, 5, 5, 5, 3, 4, 4, 4, 4, 3, 4, 5, 5, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 3, 3, 4, 4, 4, 3, 4, 4, 4, 4, 5, 5, 4, 3, 4, 4, 3, 3, 3, 4, 5, 5, 4, 5, 5, 5, 5, 4, 5, 5, 5, 5, 5, 5, 5, 5, 3, 2, 3, 4, 4, 4, 4, 4, 4, 4, 3, 4, 4, 4, 4, 4, 3, 3, 4, 4, 3, 3, 3, 4, 4, 4, 3, 4, 4, 4, 4, 3] ... (437 total)`
- Pred raw heading levels: `[1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2] ... (439 total)`
- GT relative heading levels: `[1, 2, 2, 5, 5, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 3, 2, 3, 4, 4, 5, 5, 3, 5, 5, 5, 3, 4, 4, 4, 4, 3, 4, 5, 5, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 3, 3, 4, 4, 4, 3, 4, 4, 4, 4, 5, 5, 4, 3, 4, 4, 3, 3, 3, 4, 5, 5, 4, 5, 5, 5, 5, 4, 5, 5, 5, 5, 5, 5, 5, 5, 3, 2, 3, 4, 4, 4, 4, 4, 4, 4, 3, 4, 4, 4, 4, 4, 3, 3, 4, 4, 3, 3, 3, 4, 4, 4, 3, 4, 4, 4, 4, 3] ... (437 total)`
- Pred relative heading levels: `[1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2] ... (439 total)`
- Title layout score: 92.7303
- Heading F1 score: 96.5753
- Level accuracy score: 58.3452
- Order score: 96.3554
- Main penalties:
  - 411 aligned headings have different relative levels.
  - 14 GT headings are missing.
  - 16 predicted headings are extra.

## Text Evaluation
- Text mode: normalized_full_text_preserve_newlines
- Text score: 99.1303
- Average edit distance: 0.0087
- Matched / missing / extra blocks: 1 / 0 / 0
- GT / Pred block counts: 1 / 1

### Worst Match Samples
1. op=match, distance=0.0087, GT blocks 0+1, Pred blocks 0+1
   - GT: 福建紫天传媒科技股份有限公司\n\n2022年年度报告\n\n2023-035\n![]\nZTMT\n\n紫天传媒科技\n\n2023年4月28日\n\n2022年年度报告\n\n第一节重要提示目录和释义\n\n公司董事会监事会及董事监事高级管理人员保证年度报告内容的真实...
   - Pred: 福建紫天传媒科技股份有限公司\n\n2022年年度报告\n\n2023-035\n![]\nZTMT\n\n紫天传媒科技\n\n2023年4月28日\n\n2022年年度报告\n\n第一节重要提示目录和释义\n\n公司董事会监事会及董事监事高级管理人员保证年度报告内容的真实...

## Notes
- Table score compares extracted HTML and Markdown pipe tables after conversion to cell matrices.
- With primary or alt strategy, table matching is GT-driven one-to-one: each GT table chooses one best unused Pred table.
- With max and two GT files, each predicted table keeps the higher pair score from the two independently one-to-one-matched GT variants.
- Table pair score is 60% structure score and 40% content score; table content score uses normalized edit distance on flattened table text.
- Title layout score uses heading text only for anchor alignment, then combines heading F1, relative-level accuracy, and order coverage.
- Text score removes tables, keeps heading words, preserves newlines, and scores the full body as one character sequence.
- No-value page headers and footers are removed from prediction Markdown only; GT Markdown is kept as the reference answer.
- Current limitations: complex nested tables, heavily malformed HTML, and table semantic equivalence beyond cell text are only approximated.
