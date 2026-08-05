# Financial Markdown Scoring Report

## Overall
- Final Score: 89.3031
- Table Score: 93.5882
- Title Layout Score: 69.2578
- Text Score: 95.0407

## Prediction Cleanup
- Mode: prediction_only_header_footer_cleanup
- Removed pred header/footer lines: 81
- Removed examples:
  - ## 主席報告
  - ## 主席報告
  - ## 主席報告
  - ## 企業管治報告
  - ## 企業管治報告
  - ## 企業管治報告
  - ## 企業管治報告
  - ## 企業管治報告
  - ## 企業管治報告
  - ## 企業管治報告

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
- Primary table score: 70.8109
- Alt table score: 81.5377
- Per-table rule: each predicted table keeps its higher one-to-one pair score from primary or alt GT.
- Per-table selected primary / alt pairs: 125 / 46
- Per-table reference table count: 141
- Matched / missing / extra tables: 171 / 0 / 6
- Table content score: 92.2879
- Table structure score: 94.4550
- Table matrix score: 93.5882
- Table alignment strategy: per_table_best_of_primary_alt_one_to_one

### Table Matches
- primary GT table 0 -> Pred table 0: pair=98.7034, structure=100.0000, content=96.7585, keywords=100.0000, match=99.6110, GT shape={'rows': 10, 'cols': 6}, Pred shape={'rows': 10, 'cols': 6}
- primary GT table 1 -> Pred table 1: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 16, 'cols': 6}, Pred shape={'rows': 16, 'cols': 6}
- alt GT table 3 -> Pred table 2: pair=62.2539, structure=69.6970, content=51.0893, keywords=98.9844, match=82.1078, GT shape={'rows': 12, 'cols': 5}, Pred shape={'rows': 22, 'cols': 5}
- alt GT table 4 -> Pred table 3: pair=55.5960, structure=69.6970, content=34.4444, keywords=93.8304, match=77.5334, GT shape={'rows': 12, 'cols': 5}, Pred shape={'rows': 22, 'cols': 5}
- alt GT table 6 -> Pred table 4: pair=65.1143, structure=69.6970, content=58.2402, keywords=98.8596, match=82.9035, GT shape={'rows': 12, 'cols': 5}, Pred shape={'rows': 22, 'cols': 5}
- primary GT table 3 -> Pred table 5: pair=99.6875, structure=100.0000, content=99.2188, keywords=100.0000, match=99.9062, GT shape={'rows': 23, 'cols': 3}, Pred shape={'rows': 23, 'cols': 3}
- primary GT table 4 -> Pred table 6: pair=99.8616, structure=100.0000, content=99.6540, keywords=100.0000, match=99.9585, GT shape={'rows': 18, 'cols': 4}, Pred shape={'rows': 18, 'cols': 4}
- primary GT table 13 -> Pred table 7: pair=31.8134, structure=40.0000, content=19.5335, keywords=100.0000, match=67.5440, GT shape={'rows': 9, 'cols': 5}, Pred shape={'rows': 2, 'cols': 4}
- primary GT table 5 -> Pred table 8: pair=52.9061, structure=60.0000, content=42.2652, keywords=65.0000, match=60.3718, GT shape={'rows': 10, 'cols': 5}, Pred shape={'rows': 4, 'cols': 5}
- primary GT table 6 -> Pred table 9: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 8, 'cols': 5}, Pred shape={'rows': 8, 'cols': 5}
- primary GT table 7 -> Pred table 10: pair=99.6914, structure=100.0000, content=99.2284, keywords=100.0000, match=99.9074, GT shape={'rows': 24, 'cols': 3}, Pred shape={'rows': 24, 'cols': 3}
- primary GT table 8 -> Pred table 11: pair=99.8611, structure=100.0000, content=99.6528, keywords=100.0000, match=99.9583, GT shape={'rows': 18, 'cols': 4}, Pred shape={'rows': 18, 'cols': 4}
- primary GT table 9 -> Pred table 13: pair=53.0000, structure=60.0000, content=42.5000, keywords=65.0000, match=60.4000, GT shape={'rows': 10, 'cols': 5}, Pred shape={'rows': 4, 'cols': 5}
- primary GT table 10 -> Pred table 14: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 9, 'cols': 5}, Pred shape={'rows': 9, 'cols': 5}
- primary GT table 11 -> Pred table 15: pair=99.6983, structure=100.0000, content=99.2459, keywords=100.0000, match=99.9095, GT shape={'rows': 23, 'cols': 3}, Pred shape={'rows': 23, 'cols': 3}
- primary GT table 12 -> Pred table 16: pair=99.8566, structure=100.0000, content=99.6416, keywords=100.0000, match=99.9570, GT shape={'rows': 18, 'cols': 4}, Pred shape={'rows': 18, 'cols': 4}
- primary GT table 14 -> Pred table 19: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 8, 'cols': 5}, Pred shape={'rows': 8, 'cols': 5}
- primary GT table 15 -> Pred table 20: pair=99.8365, structure=100.0000, content=99.5913, keywords=100.0000, match=99.9510, GT shape={'rows': 23, 'cols': 4}, Pred shape={'rows': 23, 'cols': 4}
- primary GT table 16 -> Pred table 21: pair=99.6364, structure=100.0000, content=99.0909, keywords=100.0000, match=99.8909, GT shape={'rows': 21, 'cols': 3}, Pred shape={'rows': 21, 'cols': 3}
- primary GT table 17 -> Pred table 22: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 10, 'cols': 3}, Pred shape={'rows': 10, 'cols': 3}
- alt GT table 23 -> Pred table 23: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 9, 'cols': 5}, Pred shape={'rows': 9, 'cols': 5}
- alt GT table 24 -> Pred table 24: pair=99.9235, structure=100.0000, content=99.8088, keywords=100.0000, match=99.9770, GT shape={'rows': 10, 'cols': 5}, Pred shape={'rows': 10, 'cols': 5}
- alt GT table 25 -> Pred table 25: pair=99.0960, structure=100.0000, content=97.7401, keywords=100.0000, match=99.7288, GT shape={'rows': 5, 'cols': 5}, Pred shape={'rows': 5, 'cols': 5}
- alt GT table 26 -> Pred table 26: pair=99.5855, structure=100.0000, content=98.9637, keywords=100.0000, match=99.8756, GT shape={'rows': 14, 'cols': 4}, Pred shape={'rows': 14, 'cols': 4}
- alt GT table 27 -> Pred table 27: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 4, 'cols': 4}, Pred shape={'rows': 4, 'cols': 4}
- primary GT table 20 -> Pred table 28: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 8, 'cols': 9}, Pred shape={'rows': 8, 'cols': 9}
- primary GT table 21 -> Pred table 29: pair=63.0222, structure=72.2222, content=49.2221, keywords=63.1061, match=64.9042, GT shape={'rows': 6, 'cols': 9}, Pred shape={'rows': 9, 'cols': 10}
- primary GT table 22 -> Pred table 30: pair=89.4949, structure=92.5926, content=84.8485, keywords=65.0000, match=77.8670, GT shape={'rows': 5, 'cols': 9}, Pred shape={'rows': 5, 'cols': 8}
- primary GT table 23 -> Pred table 31: pair=99.2048, structure=100.0000, content=98.0119, keywords=100.0000, match=99.7614, GT shape={'rows': 6, 'cols': 11}, Pred shape={'rows': 6, 'cols': 11}
- primary GT table 24 -> Pred table 32: pair=98.2041, structure=100.0000, content=95.5102, keywords=100.0000, match=99.4612, GT shape={'rows': 6, 'cols': 9}, Pred shape={'rows': 6, 'cols': 9}

## Title Layout Evaluation
- GT raw heading levels: `[1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2] ... (502 total)`
- Pred raw heading levels: `[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2] ... (873 total)`
- GT relative heading levels: `[1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2] ... (502 total)`
- Pred relative heading levels: `[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] ... (873 total)`
- Title layout score: 69.2578
- Heading F1 score: 73.0182
- Level accuracy score: 50.9296
- Order score: 57.5029
- Main penalties:
  - 501 aligned headings have different relative levels.
  - 371 predicted headings are extra.

## Text Evaluation
- Text mode: normalized_full_text_preserve_newlines
- Text score: 95.0407
- Average edit distance: 0.0496
- Matched / missing / extra blocks: 1 / 0 / 0
- GT / Pred block counts: 1 / 1

### Worst Match Samples
1. op=match, distance=0.0496, GT blocks 0+1, Pred blocks 0+1
   - GT: 美团\n\nMeituan\n\n(于开曼群岛注册成立以不同投票权控制的有限公司)\n\n港币柜台股份代号:3690\n\n人民币柜台股份代号:83690\n![]\n#EatBetterLiveBetter\n年度报告\n\n目录\n\n公司资料\n\n财务概要6\n\n...
   - Pred: 美团美团\n\nMeituan\n\n(于开曼群岛注册成立以不同投票权控制的有限公司)\n\n港币柜台股份代号:3690\n\n人民币柜台股份代号:83690\n![]\n#EatBetterLiveBetter\n年度报告\n\n目录\n\n公司资料\n\n财务概要6\n...

## Notes
- Table score compares extracted HTML and Markdown pipe tables after conversion to cell matrices.
- With primary or alt strategy, table matching is GT-driven one-to-one: each GT table chooses one best unused Pred table.
- With max and two GT files, each predicted table keeps the higher pair score from the two independently one-to-one-matched GT variants.
- Table pair score is 60% structure score and 40% content score; table content score uses normalized edit distance on flattened table text.
- Title layout score uses heading text only for anchor alignment, then combines heading F1, relative-level accuracy, and order coverage.
- Text score removes tables, keeps heading words, preserves newlines, and scores the full body as one character sequence.
- No-value page headers and footers are removed from prediction Markdown only; GT Markdown is kept as the reference answer.
- Current limitations: complex nested tables, heavily malformed HTML, and table semantic equivalence beyond cell text are only approximated.
