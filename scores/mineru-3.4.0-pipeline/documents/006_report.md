# Financial Markdown Scoring Report

## Overall
- Final Score: 88.2190
- Table Score: 83.9838
- Title Layout Score: 88.1754
- Text Score: 92.4760

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
- Primary table score: 81.2189
- Alt table score: 62.4212
- Per-table rule: each predicted table keeps its higher one-to-one pair score from primary or alt GT.
- Per-table selected primary / alt pairs: 49 / 0
- Per-table reference table count: 50
- Matched / missing / extra tables: 49 / 1 / 0
- Table content score: 73.9023
- Table structure score: 90.7048
- Table matrix score: 83.9838
- Table alignment strategy: per_table_best_of_primary_alt_one_to_one

### Table Matches
- primary GT table 0 -> Pred table 0: pair=82.0030, structure=93.3333, content=65.0075, keywords=82.8941, match=84.7146, GT shape={'rows': 18, 'cols': 5}, Pred shape={'rows': 20, 'cols': 5}
- primary GT table 1 -> Pred table 1: pair=90.6041, structure=96.8254, content=81.2721, keywords=80.6875, match=86.8901, GT shape={'rows': 20, 'cols': 5}, Pred shape={'rows': 21, 'cols': 5}
- primary GT table 2 -> Pred table 2: pair=93.1127, structure=95.5556, content=89.4484, keywords=98.6170, match=96.3534, GT shape={'rows': 14, 'cols': 5}, Pred shape={'rows': 15, 'cols': 5}
- primary GT table 3 -> Pred table 3: pair=96.8606, structure=97.2222, content=96.3183, keywords=100.0000, match=98.5026, GT shape={'rows': 23, 'cols': 7}, Pred shape={'rows': 24, 'cols': 7}
- primary GT table 4 -> Pred table 4: pair=96.4286, structure=100.0000, content=91.0714, keywords=100.0000, match=98.9286, GT shape={'rows': 7, 'cols': 5}, Pred shape={'rows': 7, 'cols': 5}
- primary GT table 5 -> Pred table 5: pair=98.2166, structure=100.0000, content=95.5414, keywords=88.1852, match=93.5576, GT shape={'rows': 9, 'cols': 4}, Pred shape={'rows': 9, 'cols': 4}
- primary GT table 6 -> Pred table 6: pair=86.6810, structure=96.2963, content=72.2581, keywords=100.0000, match=95.2636, GT shape={'rows': 17, 'cols': 4}, Pred shape={'rows': 18, 'cols': 4}
- primary GT table 7 -> Pred table 7: pair=86.0609, structure=89.7436, content=80.5369, keywords=88.2667, match=87.9003, GT shape={'rows': 11, 'cols': 4}, Pred shape={'rows': 13, 'cols': 4}
- primary GT table 8 -> Pred table 8: pair=92.4211, structure=100.0000, content=81.0526, keywords=86.1423, match=90.7975, GT shape={'rows': 14, 'cols': 4}, Pred shape={'rows': 14, 'cols': 4}
- primary GT table 9 -> Pred table 9: pair=76.0658, structure=90.4762, content=54.4503, keywords=90.9032, match=86.3666, GT shape={'rows': 6, 'cols': 4}, Pred shape={'rows': 7, 'cols': 4}
- primary GT table 10 -> Pred table 10: pair=99.8058, structure=100.0000, content=99.5146, keywords=100.0000, match=99.9417, GT shape={'rows': 11, 'cols': 3}, Pred shape={'rows': 11, 'cols': 3}
- primary GT table 11 -> Pred table 11: pair=86.6443, structure=96.8254, content=71.3725, keywords=85.2500, match=87.9834, GT shape={'rows': 21, 'cols': 5}, Pred shape={'rows': 20, 'cols': 5}
- primary GT table 12 -> Pred table 12: pair=72.1568, structure=88.7022, content=47.3388, keywords=76.6463, match=77.7106, GT shape={'rows': 23, 'cols': 5}, Pred shape={'rows': 22, 'cols': 6}
- primary GT table 13 -> Pred table 13: pair=76.7810, structure=94.4444, content=50.2857, keywords=68.1250, match=75.9857, GT shape={'rows': 11, 'cols': 10}, Pred shape={'rows': 12, 'cols': 10}
- primary GT table 14 -> Pred table 14: pair=88.9172, structure=100.0000, content=72.2930, keywords=73.6909, match=83.5206, GT shape={'rows': 10, 'cols': 10}, Pred shape={'rows': 10, 'cols': 10}
- primary GT table 15 -> Pred table 15: pair=68.3223, structure=72.2222, content=62.4724, keywords=64.8295, match=67.3559, GT shape={'rows': 4, 'cols': 9}, Pred shape={'rows': 6, 'cols': 10}
- primary GT table 16 -> Pred table 16: pair=78.8323, structure=80.9524, content=75.6522, keywords=70.9444, match=75.3124, GT shape={'rows': 5, 'cols': 5}, Pred shape={'rows': 7, 'cols': 5}
- primary GT table 17 -> Pred table 17: pair=87.0235, structure=85.1852, content=89.7810, keywords=90.4524, match=88.3703, GT shape={'rows': 7, 'cols': 5}, Pred shape={'rows': 9, 'cols': 5}
- primary GT table 18 -> Pred table 18: pair=68.2646, structure=74.6667, content=58.6614, keywords=100.0000, match=85.4127, GT shape={'rows': 4, 'cols': 4}, Pred shape={'rows': 5, 'cols': 5}
- primary GT table 19 -> Pred table 19: pair=94.3496, structure=91.6667, content=98.3740, keywords=100.0000, match=96.6382, GT shape={'rows': 7, 'cols': 2}, Pred shape={'rows': 8, 'cols': 2}
- primary GT table 20 -> Pred table 20: pair=82.6123, structure=85.8772, content=77.7149, keywords=93.6364, match=88.7773, GT shape={'rows': 30, 'cols': 5}, Pred shape={'rows': 38, 'cols': 4}
- primary GT table 21 -> Pred table 21: pair=86.0952, structure=91.1111, content=78.5714, keywords=88.3725, match=88.2370, GT shape={'rows': 15, 'cols': 4}, Pred shape={'rows': 13, 'cols': 4}
- primary GT table 22 -> Pred table 22: pair=93.2687, structure=93.1624, content=93.4283, keywords=100.0000, match=96.6131, GT shape={'rows': 35, 'cols': 5}, Pred shape={'rows': 39, 'cols': 5}
- primary GT table 23 -> Pred table 23: pair=77.4706, structure=93.3333, content=53.6765, keywords=75.6313, match=79.7235, GT shape={'rows': 20, 'cols': 4}, Pred shape={'rows': 18, 'cols': 4}
- primary GT table 24 -> Pred table 24: pair=80.0788, structure=90.9091, content=63.8333, keywords=79.9096, match=82.1603, GT shape={'rows': 19, 'cols': 12}, Pred shape={'rows': 22, 'cols': 12}
- primary GT table 25 -> Pred table 25: pair=77.8133, structure=84.6154, content=67.6101, keywords=90.8212, match=85.6777, GT shape={'rows': 21, 'cols': 12}, Pred shape={'rows': 25, 'cols': 13}
- primary GT table 26 -> Pred table 26: pair=94.1213, structure=93.3333, content=95.3032, keywords=100.0000, match=96.9031, GT shape={'rows': 36, 'cols': 4}, Pred shape={'rows': 40, 'cols': 4}
- primary GT table 27 -> Pred table 27: pair=84.9749, structure=97.3333, content=66.4372, keywords=97.0833, match=93.5008, GT shape={'rows': 24, 'cols': 3}, Pred shape={'rows': 25, 'cols': 3}
- primary GT table 28 -> Pred table 28: pair=96.1866, structure=96.9697, content=95.0119, keywords=98.8596, match=97.6797, GT shape={'rows': 21, 'cols': 3}, Pred shape={'rows': 22, 'cols': 3}
- primary GT table 29 -> Pred table 29: pair=96.4667, structure=94.4444, content=99.5000, keywords=100.0000, match=97.8289, GT shape={'rows': 11, 'cols': 3}, Pred shape={'rows': 12, 'cols': 3}

## Title Layout Evaluation
- GT raw heading levels: `[1, 3, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 3, 4, 4, 3, 4, 4, 3, 4, 4, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 2, 3, 3, 3, 2, 2, 3, 3, 3, 3, 3, 3, 3, 2, 3, 2, 3, 2, 3, 3, 3, 3, 3, 3, 3, 4, 3, 4, 4, 3, 4, 4, 4, 3, 4, 4, 3, 4, 3, 3, 3, 3, 3, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3] ... (146 total)`
- Pred raw heading levels: `[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2] ... (143 total)`
- GT relative heading levels: `[1, 3, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 3, 4, 4, 3, 4, 4, 3, 4, 4, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 2, 3, 3, 3, 2, 2, 3, 3, 3, 3, 3, 3, 3, 2, 3, 2, 3, 2, 3, 3, 3, 3, 3, 3, 3, 4, 3, 4, 4, 3, 4, 4, 4, 3, 4, 4, 3, 4, 3, 3, 3, 3, 3, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3] ... (146 total)`
- Pred relative heading levels: `[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] ... (143 total)`
- Title layout score: 88.1754
- Heading F1 score: 94.8097
- Level accuracy score: 29.4404
- Order score: 93.8356
- Main penalties:
  - 137 aligned headings have different relative levels.
  - 9 GT headings are missing.
  - 6 predicted headings are extra.

## Text Evaluation
- Text mode: normalized_full_text_preserve_newlines
- Text score: 92.4760
- Average edit distance: 0.0752
- Matched / missing / extra blocks: 1 / 0 / 0
- GT / Pred block counts: 1 / 1

### Worst Match Samples
1. op=match, distance=0.0752, GT blocks 0+1, Pred blocks 0+1
   - GT: ![]\n2026财务年度中期报告\n阿里巴巴\n\n阿里巴巴集团控股有限公司\n\n纽交所代码:BABA港交所代号:9988(港币柜台)89988(人民币柜台)\n\n目录\n\n4管理层讨论与分析\n25董事及首席执行官\n29权益披露\n34股权激励计划\n38购买出...
   - Pred: E阿里巴巴\n\n阿里巴巴集团控股有限公司纽交所代码:BABA港交所代号:9988(港币柜台)89988(人民币柜台)\n\n2026财务年度中期报告\n\n目录\n\n4管理层讨论与分析\n25董事及首席执行官\n29权益披露\n34股权激励计划\n38购买出售或回购本公...

## Notes
- Table score compares extracted HTML and Markdown pipe tables after conversion to cell matrices.
- With primary or alt strategy, table matching is GT-driven one-to-one: each GT table chooses one best unused Pred table.
- With max and two GT files, each predicted table keeps the higher pair score from the two independently one-to-one-matched GT variants.
- Table pair score is 60% structure score and 40% content score; table content score uses normalized edit distance on flattened table text.
- Title layout score uses heading text only for anchor alignment, then combines heading F1, relative-level accuracy, and order coverage.
- Text score removes tables, keeps heading words, preserves newlines, and scores the full body as one character sequence.
- No-value page headers and footers are removed from prediction Markdown only; GT Markdown is kept as the reference answer.
- Current limitations: complex nested tables, heavily malformed HTML, and table semantic equivalence beyond cell text are only approximated.
