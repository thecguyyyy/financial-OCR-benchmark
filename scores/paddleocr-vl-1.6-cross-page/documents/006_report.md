# Financial Markdown Scoring Report

## Overall
- Final Score: 93.7977
- Table Score: 90.7101
- Title Layout Score: 92.5390
- Text Score: 97.5146

## Prediction Cleanup
- Mode: prediction_only_header_footer_cleanup
- Removed pred header/footer lines: 4
- Removed examples:
  - 阿里巴巴集團控股有限公司
  - 阿里巴巴集團控股有限公司
  - 阿里巴巴集團控股有限公司
  - 阿里巴巴集團控股有限公司

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
- Primary table score: 86.8118
- Alt table score: 65.8045
- Per-table rule: each predicted table keeps its higher one-to-one pair score from primary or alt GT.
- Per-table selected primary / alt pairs: 49 / 0
- Per-table reference table count: 50
- Matched / missing / extra tables: 49 / 1 / 0
- Table content score: 85.9800
- Table structure score: 93.8636
- Table matrix score: 90.7101
- Table alignment strategy: per_table_best_of_primary_alt_one_to_one

### Table Matches
- primary GT table 0 -> Pred table 0: pair=85.7433, structure=96.2963, content=69.9137, keywords=85.0252, match=87.4948, GT shape={'rows': 18, 'cols': 5}, Pred shape={'rows': 17, 'cols': 5}
- primary GT table 1 -> Pred table 1: pair=91.8816, structure=96.8254, content=84.4660, keywords=87.7733, match=90.8162, GT shape={'rows': 20, 'cols': 5}, Pred shape={'rows': 21, 'cols': 5}
- primary GT table 2 -> Pred table 2: pair=91.1073, structure=95.5556, content=84.4350, keywords=90.3333, match=91.6100, GT shape={'rows': 14, 'cols': 5}, Pred shape={'rows': 15, 'cols': 5}
- primary GT table 3 -> Pred table 3: pair=97.6153, structure=100.0000, content=94.0382, keywords=100.0000, match=99.2846, GT shape={'rows': 23, 'cols': 7}, Pred shape={'rows': 23, 'cols': 7}
- primary GT table 4 -> Pred table 4: pair=80.0000, structure=91.6667, content=62.5000, keywords=72.0833, match=78.3750, GT shape={'rows': 7, 'cols': 5}, Pred shape={'rows': 8, 'cols': 5}
- primary GT table 5 -> Pred table 5: pair=96.6061, structure=100.0000, content=91.5152, keywords=100.0000, match=98.9818, GT shape={'rows': 9, 'cols': 4}, Pred shape={'rows': 9, 'cols': 4}
- primary GT table 6 -> Pred table 6: pair=93.5889, structure=96.2963, content=89.5277, keywords=88.2407, match=91.4563, GT shape={'rows': 17, 'cols': 4}, Pred shape={'rows': 18, 'cols': 4}
- primary GT table 7 -> Pred table 7: pair=86.0413, structure=89.7436, content=80.4878, keywords=84.8667, match=86.1945, GT shape={'rows': 11, 'cols': 4}, Pred shape={'rows': 13, 'cols': 4}
- primary GT table 8 -> Pred table 8: pair=90.9152, structure=95.5556, content=83.9546, keywords=89.6053, match=91.1883, GT shape={'rows': 14, 'cols': 4}, Pred shape={'rows': 15, 'cols': 4}
- primary GT table 9 -> Pred table 9: pair=80.5394, structure=83.3333, content=76.3485, keywords=81.8065, match=81.7317, GT shape={'rows': 6, 'cols': 4}, Pred shape={'rows': 8, 'cols': 4}
- primary GT table 10 -> Pred table 10: pair=86.9799, structure=100.0000, content=67.4497, keywords=100.0000, match=96.0940, GT shape={'rows': 11, 'cols': 3}, Pred shape={'rows': 11, 'cols': 3}
- primary GT table 11 -> Pred table 11: pair=94.8123, structure=100.0000, content=87.0307, keywords=100.0000, match=98.4437, GT shape={'rows': 21, 'cols': 5}, Pred shape={'rows': 21, 'cols': 5}
- primary GT table 12 -> Pred table 12: pair=94.6222, structure=100.0000, content=86.5556, keywords=100.0000, match=98.3867, GT shape={'rows': 23, 'cols': 5}, Pred shape={'rows': 23, 'cols': 5}
- primary GT table 13 -> Pred table 13: pair=88.2051, structure=87.8788, content=88.6945, keywords=80.0758, match=84.0752, GT shape={'rows': 11, 'cols': 10}, Pred shape={'rows': 9, 'cols': 10}
- primary GT table 14 -> Pred table 14: pair=92.7878, structure=100.0000, content=81.9695, keywords=90.4545, match=93.0636, GT shape={'rows': 10, 'cols': 10}, Pred shape={'rows': 10, 'cols': 10}
- primary GT table 15 -> Pred table 15: pair=74.2648, structure=86.6667, content=55.6619, keywords=86.8750, match=83.0503, GT shape={'rows': 4, 'cols': 9}, Pred shape={'rows': 5, 'cols': 9}
- primary GT table 16 -> Pred table 16: pair=99.2793, structure=100.0000, content=98.1982, keywords=100.0000, match=99.7838, GT shape={'rows': 5, 'cols': 5}, Pred shape={'rows': 5, 'cols': 5}
- primary GT table 17 -> Pred table 17: pair=97.4340, structure=100.0000, content=93.5849, keywords=94.1667, match=96.3135, GT shape={'rows': 7, 'cols': 5}, Pred shape={'rows': 7, 'cols': 5}
- primary GT table 18 -> Pred table 18: pair=94.9133, structure=100.0000, content=87.2832, keywords=86.8750, match=91.9115, GT shape={'rows': 4, 'cols': 4}, Pred shape={'rows': 4, 'cols': 4}
- primary GT table 19 -> Pred table 19: pair=94.5122, structure=91.6667, content=98.7805, keywords=100.0000, match=96.6870, GT shape={'rows': 7, 'cols': 2}, Pred shape={'rows': 8, 'cols': 2}
- primary GT table 20 -> Pred table 20: pair=76.2821, structure=80.2381, content=70.3481, keywords=93.6364, match=85.7505, GT shape={'rows': 30, 'cols': 5}, Pred shape={'rows': 42, 'cols': 4}
- primary GT table 21 -> Pred table 21: pair=81.5467, structure=92.1569, content=65.6315, keywords=88.3725, match=87.0816, GT shape={'rows': 15, 'cols': 4}, Pred shape={'rows': 17, 'cols': 4}
- primary GT table 22 -> Pred table 22: pair=83.5053, structure=86.3095, content=79.2990, keywords=96.8182, match=90.7226, GT shape={'rows': 35, 'cols': 5}, Pred shape={'rows': 40, 'cols': 4}
- primary GT table 23 -> Pred table 23: pair=93.9782, structure=91.3043, content=97.9890, keywords=100.0000, match=96.4543, GT shape={'rows': 20, 'cols': 4}, Pred shape={'rows': 23, 'cols': 4}
- primary GT table 24 -> Pred table 24: pair=97.1000, structure=100.0000, content=92.7500, keywords=88.5650, match=93.4125, GT shape={'rows': 19, 'cols': 12}, Pred shape={'rows': 19, 'cols': 12}
- primary GT table 25 -> Pred table 25: pair=97.0755, structure=100.0000, content=92.6887, keywords=88.6080, match=93.4266, GT shape={'rows': 21, 'cols': 12}, Pred shape={'rows': 21, 'cols': 12}
- primary GT table 26 -> Pred table 26: pair=93.8166, structure=98.1982, content=87.2441, keywords=98.6538, match=97.1115, GT shape={'rows': 36, 'cols': 4}, Pred shape={'rows': 37, 'cols': 4}
- primary GT table 27 -> Pred table 27: pair=98.9210, structure=100.0000, content=97.3025, keywords=100.0000, match=99.6763, GT shape={'rows': 24, 'cols': 3}, Pred shape={'rows': 24, 'cols': 3}
- primary GT table 28 -> Pred table 28: pair=98.9598, structure=100.0000, content=97.3995, keywords=100.0000, match=99.6879, GT shape={'rows': 21, 'cols': 3}, Pred shape={'rows': 21, 'cols': 3}
- primary GT table 29 -> Pred table 29: pair=99.1960, structure=100.0000, content=97.9899, keywords=100.0000, match=99.7588, GT shape={'rows': 11, 'cols': 3}, Pred shape={'rows': 11, 'cols': 3}

## Title Layout Evaluation
- GT raw heading levels: `[1, 3, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 3, 4, 4, 3, 4, 4, 3, 4, 4, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 2, 3, 3, 3, 2, 2, 3, 3, 3, 3, 3, 3, 3, 2, 3, 2, 3, 2, 3, 3, 3, 3, 3, 3, 3, 4, 3, 4, 4, 3, 4, 4, 4, 3, 4, 4, 3, 4, 3, 3, 3, 3, 3, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3] ... (146 total)`
- Pred raw heading levels: `[2, 3, 5, 5, 5, 5, 5, 4, 5, 4, 5, 5, 4, 3, 3, 5, 4, 4, 3, 3, 4, 5, 3, 4, 4, 4, 3, 3, 3, 3, 3, 3, 4, 3, 4, 4, 3, 4, 4, 4, 5, 3, 3, 3, 3, 5, 5, 5, 5, 3, 4, 4, 4, 3, 4, 3, 5, 4, 5, 3, 3, 4, 4, 5, 5, 5, 5, 4, 5, 3, 3, 3, 5, 5, 5, 5, 5, 5, 5, 4, 3, 5, 4, 2, 5, 5, 5, 5, 3, 3, 4, 3, 3, 3, 3, 4, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 3, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3] ... (152 total)`
- GT relative heading levels: `[1, 3, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 3, 4, 4, 3, 4, 4, 3, 4, 4, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 2, 3, 3, 3, 2, 2, 3, 3, 3, 3, 3, 3, 3, 2, 3, 2, 3, 2, 3, 3, 3, 3, 3, 3, 3, 4, 3, 4, 4, 3, 4, 4, 4, 3, 4, 4, 3, 4, 3, 3, 3, 3, 3, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3] ... (146 total)`
- Pred relative heading levels: `[2, 3, 5, 5, 5, 5, 5, 4, 5, 4, 5, 5, 4, 3, 3, 5, 4, 4, 3, 3, 4, 5, 3, 4, 4, 4, 3, 3, 3, 3, 3, 3, 4, 3, 4, 4, 3, 4, 4, 4, 5, 3, 3, 3, 3, 5, 5, 5, 5, 3, 4, 4, 4, 3, 4, 3, 5, 4, 5, 3, 3, 4, 4, 5, 5, 5, 5, 4, 5, 3, 3, 3, 5, 5, 5, 5, 5, 5, 5, 4, 3, 5, 4, 2, 5, 5, 5, 5, 3, 3, 4, 3, 3, 3, 3, 4, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 3, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3] ... (152 total)`
- Title layout score: 92.5390
- Heading F1 score: 93.9597
- Level accuracy score: 81.6071
- Order score: 92.1053
- Main penalties:
  - 63 aligned headings have different relative levels.
  - 6 GT headings are missing.
  - 12 predicted headings are extra.

## Text Evaluation
- Text mode: normalized_full_text_preserve_newlines
- Text score: 97.5146
- Average edit distance: 0.0249
- Matched / missing / extra blocks: 1 / 0 / 0
- GT / Pred block counts: 1 / 1

### Worst Match Samples
1. op=match, distance=0.0249, GT blocks 0+1, Pred blocks 0+1
   - GT: ![]\n2026财务年度中期报告\n阿里巴巴\n\n阿里巴巴集团控股有限公司\n\n纽交所代码:BABA港交所代号:9988(港币柜台)89988(人民币柜台)\n\n目录\n\n4管理层讨论与分析\n25董事及首席执行官\n29权益披露\n34股权激励计划\n38购买出...
   - Pred: E阿里巴巴\n\n阿里巴巴集团控股有限公司\n\n纽交所代码:BABA港交所代号:9988(港币柜台)89988(人民币柜台)\n\n目录\n\n4管理层讨论与分析\n25董事及首席执行官\n29权益披露\n34股权激励计划\n38购买出售或回购本公司上市证券\n39其他信...

## Notes
- Table score compares extracted HTML and Markdown pipe tables after conversion to cell matrices.
- With primary or alt strategy, table matching is GT-driven one-to-one: each GT table chooses one best unused Pred table.
- With max and two GT files, each predicted table keeps the higher pair score from the two independently one-to-one-matched GT variants.
- Table pair score is 60% structure score and 40% content score; table content score uses normalized edit distance on flattened table text.
- Title layout score uses heading text only for anchor alignment, then combines heading F1, relative-level accuracy, and order coverage.
- Text score removes tables, keeps heading words, preserves newlines, and scores the full body as one character sequence.
- No-value page headers and footers are removed from prediction Markdown only; GT Markdown is kept as the reference answer.
- Current limitations: complex nested tables, heavily malformed HTML, and table semantic equivalence beyond cell text are only approximated.
