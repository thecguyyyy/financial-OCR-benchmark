# Financial Markdown Scoring Report

## Overall
- Final Score: 86.8413
- Table Score: 93.2212
- Title Layout Score: 62.9119
- Text Score: 92.4262

## Prediction Cleanup
- Mode: prediction_only_header_footer_cleanup
- Removed pred header/footer lines: 87
- Removed examples:
  - ## 主席報告
  - ## 主席報告
  - ## 企業管治報告
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
- Primary table score: 72.2133
- Alt table score: 71.8689
- Per-table rule: each predicted table keeps its higher one-to-one pair score from primary or alt GT.
- Per-table selected primary / alt pairs: 119 / 42
- Per-table reference table count: 141
- Matched / missing / extra tables: 161 / 0 / 2
- Table content score: 90.3082
- Table structure score: 95.1632
- Table matrix score: 93.2212
- Table alignment strategy: per_table_best_of_primary_alt_one_to_one

### Table Matches
- primary GT table 1 -> Pred table 0: pair=64.2464, structure=74.3590, content=49.0775, keywords=75.8333, match=72.0624, GT shape={'rows': 16, 'cols': 6}, Pred shape={'rows': 26, 'cols': 6}
- alt GT table 3 -> Pred table 1: pair=62.4619, structure=69.6970, content=51.6093, keywords=93.9444, match=79.6502, GT shape={'rows': 12, 'cols': 5}, Pred shape={'rows': 22, 'cols': 5}
- alt GT table 5 -> Pred table 2: pair=67.2727, structure=69.6970, content=63.6364, keywords=83.0994, match=75.6709, GT shape={'rows': 12, 'cols': 5}, Pred shape={'rows': 22, 'cols': 5}
- alt GT table 6 -> Pred table 3: pair=64.9467, structure=69.6970, content=57.8212, keywords=98.8596, match=82.8532, GT shape={'rows': 12, 'cols': 5}, Pred shape={'rows': 22, 'cols': 5}
- primary GT table 3 -> Pred table 4: pair=97.4583, structure=97.2222, content=97.8125, keywords=99.5185, match=98.4412, GT shape={'rows': 23, 'cols': 3}, Pred shape={'rows': 24, 'cols': 3}
- primary GT table 4 -> Pred table 5: pair=95.3342, structure=96.4912, content=93.5986, keywords=89.6646, match=92.7308, GT shape={'rows': 18, 'cols': 4}, Pred shape={'rows': 19, 'cols': 4}
- primary GT table 13 -> Pred table 6: pair=79.5789, structure=92.5926, content=60.0583, keywords=98.2895, match=91.5369, GT shape={'rows': 9, 'cols': 5}, Pred shape={'rows': 8, 'cols': 5}
- primary GT table 6 -> Pred table 7: pair=89.5556, structure=92.5926, content=85.0000, keywords=85.3788, match=88.0746, GT shape={'rows': 8, 'cols': 5}, Pred shape={'rows': 9, 'cols': 5}
- primary GT table 7 -> Pred table 8: pair=95.9400, structure=94.8718, content=97.5422, keywords=95.1691, match=95.3409, GT shape={'rows': 24, 'cols': 3}, Pred shape={'rows': 26, 'cols': 3}
- primary GT table 8 -> Pred table 9: pair=92.9759, structure=93.3333, content=92.4399, keywords=84.5556, match=88.8372, GT shape={'rows': 18, 'cols': 4}, Pred shape={'rows': 20, 'cols': 4}
- primary GT table 9 -> Pred table 10: pair=82.4444, structure=86.6667, content=76.1111, keywords=75.8553, match=79.9943, GT shape={'rows': 10, 'cols': 5}, Pred shape={'rows': 8, 'cols': 5}
- primary GT table 10 -> Pred table 11: pair=97.8125, structure=100.0000, content=94.5312, keywords=98.7500, match=98.7188, GT shape={'rows': 9, 'cols': 5}, Pred shape={'rows': 9, 'cols': 5}
- primary GT table 11 -> Pred table 12: pair=95.9566, structure=94.6667, content=97.8916, keywords=93.6705, match=94.5556, GT shape={'rows': 23, 'cols': 3}, Pred shape={'rows': 25, 'cols': 3}
- primary GT table 12 -> Pred table 13: pair=99.5699, structure=100.0000, content=98.9247, keywords=100.0000, match=99.8710, GT shape={'rows': 18, 'cols': 4}, Pred shape={'rows': 18, 'cols': 4}
- primary GT table 5 -> Pred table 14: pair=64.3536, structure=80.0000, content=40.8840, keywords=66.6892, match=68.6507, GT shape={'rows': 10, 'cols': 5}, Pred shape={'rows': 7, 'cols': 5}
- primary GT table 14 -> Pred table 15: pair=99.3994, structure=100.0000, content=98.4985, keywords=100.0000, match=99.8198, GT shape={'rows': 8, 'cols': 5}, Pred shape={'rows': 8, 'cols': 5}
- primary GT table 15 -> Pred table 16: pair=97.1361, structure=97.2222, content=97.0068, keywords=97.1295, match=97.1500, GT shape={'rows': 23, 'cols': 4}, Pred shape={'rows': 24, 'cols': 4}
- primary GT table 16 -> Pred table 17: pair=97.1673, structure=96.9697, content=97.4638, keywords=97.0833, match=97.0858, GT shape={'rows': 21, 'cols': 3}, Pred shape={'rows': 22, 'cols': 3}
- primary GT table 17 -> Pred table 18: pair=99.8684, structure=100.0000, content=99.6711, keywords=100.0000, match=99.9605, GT shape={'rows': 10, 'cols': 3}, Pred shape={'rows': 10, 'cols': 3}
- alt GT table 23 -> Pred table 19: pair=91.2062, structure=100.0000, content=78.0156, keywords=100.0000, match=97.3619, GT shape={'rows': 9, 'cols': 5}, Pred shape={'rows': 9, 'cols': 5}
- alt GT table 24 -> Pred table 20: pair=65.4914, structure=73.3333, content=53.7285, keywords=100.0000, match=84.3141, GT shape={'rows': 10, 'cols': 5}, Pred shape={'rows': 6, 'cols': 5}
- alt GT table 25 -> Pred table 21: pair=94.4279, structure=100.0000, content=86.0697, keywords=100.0000, match=98.3284, GT shape={'rows': 5, 'cols': 5}, Pred shape={'rows': 5, 'cols': 5}
- alt GT table 26 -> Pred table 22: pair=94.4359, structure=100.0000, content=86.0896, keywords=96.7857, match=96.7236, GT shape={'rows': 14, 'cols': 4}, Pred shape={'rows': 14, 'cols': 4}
- alt GT table 27 -> Pred table 23: pair=92.2652, structure=100.0000, content=80.6630, keywords=100.0000, match=97.6796, GT shape={'rows': 4, 'cols': 4}, Pred shape={'rows': 4, 'cols': 4}
- primary GT table 20 -> Pred table 24: pair=92.5373, structure=100.0000, content=81.3433, keywords=87.2704, match=91.3964, GT shape={'rows': 8, 'cols': 9}, Pred shape={'rows': 8, 'cols': 9}
- primary GT table 21 -> Pred table 25: pair=86.3115, structure=100.0000, content=65.7787, keywords=93.0000, match=92.3935, GT shape={'rows': 6, 'cols': 9}, Pred shape={'rows': 6, 'cols': 9}
- primary GT table 22 -> Pred table 26: pair=84.8485, structure=92.5926, content=73.2323, keywords=65.0000, match=76.4731, GT shape={'rows': 5, 'cols': 9}, Pred shape={'rows': 5, 'cols': 8}
- primary GT table 23 -> Pred table 27: pair=91.2521, structure=93.9394, content=87.2211, keywords=93.7963, match=93.0617, GT shape={'rows': 6, 'cols': 11}, Pred shape={'rows': 6, 'cols': 10}
- primary GT table 24 -> Pred table 28: pair=84.1614, structure=88.8889, content=77.0701, keywords=89.9235, match=87.9880, GT shape={'rows': 6, 'cols': 9}, Pred shape={'rows': 5, 'cols': 9}
- primary GT table 25 -> Pred table 29: pair=97.4468, structure=100.0000, content=93.6170, keywords=100.0000, match=99.2340, GT shape={'rows': 5, 'cols': 9}, Pred shape={'rows': 5, 'cols': 9}

## Title Layout Evaluation
- GT raw heading levels: `[1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2] ... (502 total)`
- Pred raw heading levels: `[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2] ... (948 total)`
- GT relative heading levels: `[1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2] ... (502 total)`
- Pred relative heading levels: `[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] ... (948 total)`
- Title layout score: 62.9119
- Heading F1 score: 65.2414
- Level accuracy score: 57.2939
- Order score: 49.8945
- Main penalties:
  - 468 aligned headings have different relative levels.
  - 29 GT headings are missing.
  - 475 predicted headings are extra.

## Text Evaluation
- Text mode: normalized_full_text_preserve_newlines
- Text score: 92.4262
- Average edit distance: 0.0757
- Matched / missing / extra blocks: 1 / 0 / 0
- GT / Pred block counts: 1 / 1

### Worst Match Samples
1. op=match, distance=0.0757, GT blocks 0+1, Pred blocks 0+1
   - GT: 美团\n\nMeituan\n\n(于开曼群岛注册成立以不同投票权控制的有限公司)\n\n港币柜台股份代号:3690\n\n人民币柜台股份代号:83690\n![]\n#EatBetterLiveBetter\n年度报告\n\n目录\n\n公司资料\n\n财务概要6\n\n...
   - Pred: 美团Meituan\n\n(于开曼群岛注册成立以不同投票权控制的有限公司)\n\n港币柜台股份代号:3690\n\n人民币柜台股份代号:83690\n![]\n2024年度报告\n\n目录\n\n公司资料2\n财务概要6\n主席报告10\n管理层讨论及分析14\n董事及高级...

## Notes
- Table score compares extracted HTML and Markdown pipe tables after conversion to cell matrices.
- With primary or alt strategy, table matching is GT-driven one-to-one: each GT table chooses one best unused Pred table.
- With max and two GT files, each predicted table keeps the higher pair score from the two independently one-to-one-matched GT variants.
- Table pair score is 60% structure score and 40% content score; table content score uses normalized edit distance on flattened table text.
- Title layout score uses heading text only for anchor alignment, then combines heading F1, relative-level accuracy, and order coverage.
- Text score removes tables, keeps heading words, preserves newlines, and scores the full body as one character sequence.
- No-value page headers and footers are removed from prediction Markdown only; GT Markdown is kept as the reference answer.
- Current limitations: complex nested tables, heavily malformed HTML, and table semantic equivalence beyond cell text are only approximated.
