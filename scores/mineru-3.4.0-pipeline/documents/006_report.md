# Financial Markdown Scoring Report

## Overall
- Final Score: 85.9595
- Table Score: 80.9389
- Title Layout Score: 84.3791
- Text Score: 91.7702

## Prediction Cleanup
- Mode: disabled_after_explicit_adapter
- Removed pred header/footer lines: 0
- Removed examples:
  - None

## Weights
- Table: 40%
- Title Layout: 20%
- Text: 40%

## Configuration
- Remove pred header/footer: False
- Normalize images: True
- Normalize Chinese variants: t2s
- Normalize footnotes: True
- Normalize punctuation: True
- Table pair weights: structure=0.6, content=0.4

## Table Evaluation
- Table GT strategy result: per_table_max
- Primary table score: 72.1910
- Alt table score: 69.6562
- Per-table rule: each predicted table keeps its higher one-to-one pair score from primary or alt GT.
- Per-table selected primary / alt pairs: 45 / 4
- Per-table reference table count: 51
- Matched / missing / extra tables: 49 / 2 / 0
- Table content score: 70.6699
- Table structure score: 87.7849
- Table matrix score: 80.9389
- Table alignment strategy: per_table_best_of_primary_alt_one_to_one

### Table Matches
- primary GT table 0 -> Pred table 0: pair=82.6256, structure=93.3333, content=66.5639, keywords=82.8941, match=84.9014, GT shape={'rows': 18, 'cols': 5}, Pred shape={'rows': 20, 'cols': 5}
- primary GT table 1 -> Pred table 1: pair=89.3009, structure=96.8254, content=78.0142, keywords=80.6875, match=86.4991, GT shape={'rows': 20, 'cols': 5}, Pred shape={'rows': 21, 'cols': 5}
- primary GT table 2 -> Pred table 2: pair=92.4932, structure=95.5556, content=87.8995, keywords=98.6170, match=96.1676, GT shape={'rows': 14, 'cols': 5}, Pred shape={'rows': 15, 'cols': 5}
- primary GT table 3 -> Pred table 3: pair=95.5448, structure=97.2222, content=93.0286, keywords=100.0000, match=98.1079, GT shape={'rows': 23, 'cols': 7}, Pred shape={'rows': 24, 'cols': 7}
- primary GT table 4 -> Pred table 4: pair=92.4211, structure=100.0000, content=81.0526, keywords=100.0000, match=97.7263, GT shape={'rows': 7, 'cols': 5}, Pred shape={'rows': 7, 'cols': 5}
- primary GT table 5 -> Pred table 5: pair=95.0877, structure=100.0000, content=87.7193, keywords=86.0357, match=91.5442, GT shape={'rows': 9, 'cols': 4}, Pred shape={'rows': 9, 'cols': 4}
- primary GT table 6 -> Pred table 6: pair=86.4229, structure=96.2963, content=71.6129, keywords=99.4037, match=94.8880, GT shape={'rows': 17, 'cols': 4}, Pred shape={'rows': 18, 'cols': 4}
- primary GT table 7 -> Pred table 7: pair=89.2721, structure=94.8718, content=80.8725, keywords=99.1447, match=95.3283, GT shape={'rows': 12, 'cols': 4}, Pred shape={'rows': 13, 'cols': 4}
- primary GT table 8 -> Pred table 8: pair=93.4392, structure=100.0000, content=83.5979, keywords=86.1423, match=91.1029, GT shape={'rows': 14, 'cols': 4}, Pred shape={'rows': 14, 'cols': 4}
- primary GT table 9 -> Pred table 9: pair=81.8537, structure=100.0000, content=54.6341, keywords=100.0000, match=94.5561, GT shape={'rows': 7, 'cols': 4}, Pred shape={'rows': 7, 'cols': 4}
- primary GT table 10 -> Pred table 10: pair=99.8058, structure=100.0000, content=99.5146, keywords=100.0000, match=99.9417, GT shape={'rows': 11, 'cols': 3}, Pred shape={'rows': 11, 'cols': 3}
- primary GT table 11 -> Pred table 11: pair=86.6835, structure=96.8254, content=71.4706, keywords=85.2500, match=87.9951, GT shape={'rows': 21, 'cols': 5}, Pred shape={'rows': 20, 'cols': 5}
- primary GT table 12 -> Pred table 12: pair=72.1568, structure=88.7022, content=47.3388, keywords=76.6463, match=77.7106, GT shape={'rows': 23, 'cols': 5}, Pred shape={'rows': 22, 'cols': 6}
- primary GT table 13 -> Pred table 13: pair=76.8381, structure=94.4444, content=50.4286, keywords=68.1250, match=76.0028, GT shape={'rows': 11, 'cols': 10}, Pred shape={'rows': 12, 'cols': 10}
- primary GT table 14 -> Pred table 14: pair=88.9809, structure=100.0000, content=72.4522, keywords=73.6909, match=83.5397, GT shape={'rows': 10, 'cols': 10}, Pred shape={'rows': 10, 'cols': 10}
- primary GT table 15 -> Pred table 15: pair=68.4106, structure=72.2222, content=62.6932, keywords=64.8295, match=67.3824, GT shape={'rows': 4, 'cols': 9}, Pred shape={'rows': 6, 'cols': 10}
- primary GT table 16 -> Pred table 16: pair=78.8323, structure=80.9524, content=75.6522, keywords=70.9444, match=75.3124, GT shape={'rows': 5, 'cols': 5}, Pred shape={'rows': 7, 'cols': 5}
- primary GT table 17 -> Pred table 17: pair=87.1551, structure=85.1852, content=90.1099, keywords=90.4524, match=88.4098, GT shape={'rows': 7, 'cols': 5}, Pred shape={'rows': 9, 'cols': 5}
- primary GT table 18 -> Pred table 18: pair=77.0000, structure=86.6667, content=62.5000, keywords=91.8548, match=86.3607, GT shape={'rows': 5, 'cols': 4}, Pred shape={'rows': 5, 'cols': 5}
- primary GT table 19 -> Pred table 19: pair=94.5122, structure=91.6667, content=98.7805, keywords=100.0000, match=96.6870, GT shape={'rows': 7, 'cols': 2}, Pred shape={'rows': 8, 'cols': 2}
- primary GT table 20 -> Pred table 20: pair=82.6915, structure=86.4035, content=77.1234, keywords=96.5000, match=90.3381, GT shape={'rows': 32, 'cols': 5}, Pred shape={'rows': 38, 'cols': 4}
- primary GT table 21 -> Pred table 21: pair=83.1593, structure=87.5000, content=76.6484, keywords=87.6220, match=86.2588, GT shape={'rows': 16, 'cols': 4}, Pred shape={'rows': 13, 'cols': 4}
- alt GT table 22 -> Pred table 22: pair=93.7960, structure=94.8718, content=92.1824, keywords=100.0000, match=97.1132, GT shape={'rows': 36, 'cols': 5}, Pred shape={'rows': 39, 'cols': 5}
- alt GT table 23 -> Pred table 23: pair=77.2658, structure=93.3333, content=53.1646, keywords=75.6313, match=79.6620, GT shape={'rows': 20, 'cols': 4}, Pred shape={'rows': 18, 'cols': 4}
- alt GT table 24 -> Pred table 24: pair=80.9489, structure=90.9091, content=66.0086, keywords=83.8517, match=84.3923, GT shape={'rows': 19, 'cols': 12}, Pred shape={'rows': 22, 'cols': 12}
- alt GT table 25 -> Pred table 25: pair=78.6333, structure=84.6154, content=69.6602, keywords=91.1844, match=86.1053, GT shape={'rows': 21, 'cols': 12}, Pred shape={'rows': 25, 'cols': 13}
- primary GT table 24 -> Pred table 26: pair=95.3877, structure=95.0000, content=95.9691, keywords=100.0000, match=97.6163, GT shape={'rows': 37, 'cols': 4}, Pred shape={'rows': 40, 'cols': 4}
- primary GT table 25 -> Pred table 27: pair=61.8238, structure=73.3333, content=44.5596, keywords=93.6364, match=80.0320, GT shape={'rows': 15, 'cols': 3}, Pred shape={'rows': 25, 'cols': 3}
- primary GT table 27 -> Pred table 28: pair=96.4675, structure=96.9697, content=95.7143, keywords=98.8596, match=97.7640, GT shape={'rows': 21, 'cols': 3}, Pred shape={'rows': 22, 'cols': 3}
- primary GT table 28 -> Pred table 29: pair=96.4667, structure=94.4444, content=99.5000, keywords=100.0000, match=97.8289, GT shape={'rows': 11, 'cols': 3}, Pred shape={'rows': 12, 'cols': 3}

## Title Layout Evaluation
- GT raw heading levels: `[1, 1, 1, 1, 1, 2, 2, 3, 4, 4, 3, 4, 4, 3, 4, 4, 3, 4, 4, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 2, 2, 3, 3, 3, 3, 3, 3, 1, 2, 3, 2, 1, 2, 2, 2, 1, 1, 2, 3, 3, 3, 2, 2, 3, 1, 2, 1, 2, 2, 3, 3, 3, 2, 2, 2, 2, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 4, 4, 3, 4, 3, 3, 3, 3, 3, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4] ... (133 total)`
- Pred raw heading levels: `[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2] ... (143 total)`
- GT relative heading levels: `[1, 1, 1, 1, 1, 2, 2, 3, 4, 4, 3, 4, 4, 3, 4, 4, 3, 4, 4, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 2, 2, 3, 3, 3, 3, 3, 3, 1, 2, 3, 2, 1, 2, 2, 2, 1, 1, 2, 3, 3, 3, 2, 2, 3, 1, 2, 1, 2, 2, 3, 3, 3, 2, 2, 2, 2, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 4, 4, 3, 4, 3, 3, 3, 3, 3, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4] ... (133 total)`
- Pred relative heading levels: `[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] ... (143 total)`
- Title layout score: 84.3791
- Heading F1 score: 88.4058
- Level accuracy score: 51.2295
- Order score: 85.3147
- Main penalties:
  - 111 aligned headings have different relative levels.
  - 11 GT headings are missing.
  - 21 predicted headings are extra.

## Text Evaluation
- Text mode: normalized_full_text_preserve_newlines
- Text score: 91.7702
- Average edit distance: 0.0823
- Matched / missing / extra blocks: 1 / 0 / 0
- GT / Pred block counts: 1 / 1

### Worst Match Samples
1. op=match, distance=0.0823, GT blocks 0+1, Pred blocks 0+1
   - GT: ![]\n目录\n\n4管理层讨论与分析\n25董事及首席执行官\n29权益披露\n34股权激励计划\n38购买出售或回购本公司上市证券\n39其他信息\n42释义\n44财务报表\n\n不同投票权\n\n我们只有单一类别的股份每一股份对应一份表决权。然而根据《公司章程》,...
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
