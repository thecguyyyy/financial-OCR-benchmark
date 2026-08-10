# Financial Markdown Scoring Report

## Overall
- Final Score: 90.7004
- Table Score: 87.6058
- Title Layout Score: 85.4032
- Text Score: 96.4435

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
- Primary table score: 75.2938
- Alt table score: 73.4036
- Per-table rule: each predicted table keeps its higher one-to-one pair score from primary or alt GT.
- Per-table selected primary / alt pairs: 45 / 4
- Per-table reference table count: 51
- Matched / missing / extra tables: 49 / 2 / 0
- Table content score: 83.3238
- Table structure score: 90.4605
- Table matrix score: 87.6058
- Table alignment strategy: per_table_best_of_primary_alt_one_to_one

### Table Matches
- primary GT table 0 -> Pred table 0: pair=85.7827, structure=96.2963, content=70.0124, keywords=85.0252, match=87.5067, GT shape={'rows': 18, 'cols': 5}, Pred shape={'rows': 17, 'cols': 5}
- primary GT table 1 -> Pred table 1: pair=93.9191, structure=96.8254, content=89.5595, keywords=87.7733, match=91.4275, GT shape={'rows': 20, 'cols': 5}, Pred shape={'rows': 21, 'cols': 5}
- primary GT table 2 -> Pred table 2: pair=93.7204, structure=95.5556, content=90.9677, keywords=90.3333, match=92.3939, GT shape={'rows': 14, 'cols': 5}, Pred shape={'rows': 15, 'cols': 5}
- primary GT table 3 -> Pred table 3: pair=99.6376, structure=100.0000, content=99.0940, keywords=100.0000, match=99.8913, GT shape={'rows': 23, 'cols': 7}, Pred shape={'rows': 23, 'cols': 7}
- primary GT table 4 -> Pred table 4: pair=84.5082, structure=91.6667, content=73.7705, keywords=72.0833, match=79.7275, GT shape={'rows': 7, 'cols': 5}, Pred shape={'rows': 8, 'cols': 5}
- primary GT table 5 -> Pred table 5: pair=94.8538, structure=100.0000, content=87.1345, keywords=100.0000, match=98.4561, GT shape={'rows': 9, 'cols': 4}, Pred shape={'rows': 9, 'cols': 4}
- primary GT table 6 -> Pred table 6: pair=94.8209, structure=96.2963, content=92.6078, keywords=87.6720, match=91.5415, GT shape={'rows': 17, 'cols': 4}, Pred shape={'rows': 18, 'cols': 4}
- primary GT table 7 -> Pred table 7: pair=91.3133, structure=94.8718, content=85.9756, keywords=83.2018, match=87.9693, GT shape={'rows': 12, 'cols': 4}, Pred shape={'rows': 13, 'cols': 4}
- primary GT table 8 -> Pred table 8: pair=91.7307, structure=95.5556, content=85.9935, keywords=89.6053, match=91.4330, GT shape={'rows': 14, 'cols': 4}, Pred shape={'rows': 15, 'cols': 4}
- primary GT table 9 -> Pred table 9: pair=89.0249, structure=91.6667, content=85.0622, keywords=79.8095, match=84.9456, GT shape={'rows': 7, 'cols': 4}, Pred shape={'rows': 8, 'cols': 4}
- primary GT table 10 -> Pred table 10: pair=86.9799, structure=100.0000, content=67.4497, keywords=100.0000, match=96.0940, GT shape={'rows': 11, 'cols': 3}, Pred shape={'rows': 11, 'cols': 3}
- primary GT table 11 -> Pred table 11: pair=94.6075, structure=100.0000, content=86.5188, keywords=100.0000, match=98.3822, GT shape={'rows': 21, 'cols': 5}, Pred shape={'rows': 21, 'cols': 5}
- primary GT table 12 -> Pred table 12: pair=94.7650, structure=100.0000, content=86.9126, keywords=100.0000, match=98.4295, GT shape={'rows': 23, 'cols': 5}, Pred shape={'rows': 23, 'cols': 5}
- primary GT table 13 -> Pred table 13: pair=88.5281, structure=87.8788, content=89.5020, keywords=80.0758, match=84.1721, GT shape={'rows': 11, 'cols': 10}, Pred shape={'rows': 9, 'cols': 10}
- primary GT table 14 -> Pred table 14: pair=92.8988, structure=100.0000, content=82.2469, keywords=90.4545, match=93.0969, GT shape={'rows': 10, 'cols': 10}, Pred shape={'rows': 10, 'cols': 10}
- primary GT table 15 -> Pred table 15: pair=74.4561, structure=86.6667, content=56.1404, keywords=86.8750, match=83.1077, GT shape={'rows': 4, 'cols': 9}, Pred shape={'rows': 5, 'cols': 9}
- primary GT table 16 -> Pred table 16: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 5, 'cols': 5}, Pred shape={'rows': 5, 'cols': 5}
- primary GT table 17 -> Pred table 17: pair=97.5758, structure=100.0000, content=93.9394, keywords=94.1667, match=96.3561, GT shape={'rows': 7, 'cols': 5}, Pred shape={'rows': 7, 'cols': 5}
- primary GT table 18 -> Pred table 18: pair=80.0000, structure=86.6667, content=70.0000, keywords=86.8548, match=84.7607, GT shape={'rows': 5, 'cols': 4}, Pred shape={'rows': 4, 'cols': 4}
- primary GT table 19 -> Pred table 19: pair=94.5122, structure=91.6667, content=98.7805, keywords=100.0000, match=96.6870, GT shape={'rows': 7, 'cols': 2}, Pred shape={'rows': 8, 'cols': 2}
- primary GT table 20 -> Pred table 20: pair=81.2995, structure=83.8095, content=77.5346, keywords=100.0000, match=91.1517, GT shape={'rows': 32, 'cols': 5}, Pred shape={'rows': 42, 'cols': 4}
- primary GT table 21 -> Pred table 21: pair=83.9825, structure=96.0784, content=65.8385, keywords=92.5000, match=90.6604, GT shape={'rows': 16, 'cols': 4}, Pred shape={'rows': 17, 'cols': 4}
- alt GT table 22 -> Pred table 22: pair=83.2653, structure=86.2963, content=78.7188, keywords=96.8182, match=90.6479, GT shape={'rows': 36, 'cols': 5}, Pred shape={'rows': 40, 'cols': 4}
- alt GT table 23 -> Pred table 23: pair=93.2636, structure=91.3043, content=96.2025, keywords=100.0000, match=96.2399, GT shape={'rows': 20, 'cols': 4}, Pred shape={'rows': 23, 'cols': 4}
- alt GT table 24 -> Pred table 24: pair=98.2146, structure=100.0000, content=95.5365, keywords=92.5026, match=95.7157, GT shape={'rows': 19, 'cols': 12}, Pred shape={'rows': 19, 'cols': 12}
- alt GT table 25 -> Pred table 25: pair=97.9935, structure=100.0000, content=94.9838, keywords=88.9773, match=93.8867, GT shape={'rows': 21, 'cols': 12}, Pred shape={'rows': 21, 'cols': 12}
- primary GT table 24 -> Pred table 26: pair=94.4980, structure=100.0000, content=86.2451, keywords=98.6000, match=97.6494, GT shape={'rows': 37, 'cols': 4}, Pred shape={'rows': 37, 'cols': 4}
- primary GT table 25 -> Pred table 27: pair=71.4093, structure=75.0000, content=66.0232, keywords=96.8182, match=84.8319, GT shape={'rows': 15, 'cols': 3}, Pred shape={'rows': 24, 'cols': 3}
- primary GT table 27 -> Pred table 28: pair=99.8104, structure=100.0000, content=99.5261, keywords=100.0000, match=99.9431, GT shape={'rows': 21, 'cols': 3}, Pred shape={'rows': 21, 'cols': 3}
- primary GT table 28 -> Pred table 29: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 11, 'cols': 3}, Pred shape={'rows': 11, 'cols': 3}

## Title Layout Evaluation
- GT raw heading levels: `[1, 1, 1, 1, 1, 2, 2, 3, 4, 4, 3, 4, 4, 3, 4, 4, 3, 4, 4, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 2, 2, 3, 3, 3, 3, 3, 3, 1, 2, 3, 2, 1, 2, 2, 2, 1, 1, 2, 3, 3, 3, 2, 2, 3, 1, 2, 1, 2, 2, 3, 3, 3, 2, 2, 2, 2, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 4, 4, 3, 4, 3, 3, 3, 3, 3, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4] ... (133 total)`
- Pred raw heading levels: `[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 2, 3, 2, 2, 3, 2, 2, 2, 3, 2, 2, 3, 2, 2, 3, 3, 3, 3, 3, 1, 3, 2, 2, 3, 3, 3, 3, 3, 3, 3, 1, 3] ... (150 total)`
- GT relative heading levels: `[1, 1, 1, 1, 1, 2, 2, 3, 4, 4, 3, 4, 4, 3, 4, 4, 3, 4, 4, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 2, 2, 3, 3, 3, 3, 3, 3, 1, 2, 3, 2, 1, 2, 2, 2, 1, 1, 2, 3, 3, 3, 2, 2, 3, 1, 2, 1, 2, 2, 3, 3, 3, 2, 2, 2, 2, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 4, 4, 3, 4, 3, 3, 3, 3, 3, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4] ... (133 total)`
- Pred relative heading levels: `[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 2, 3, 2, 2, 3, 2, 2, 2, 3, 2, 2, 3, 2, 2, 3, 3, 3, 3, 3, 1, 3, 2, 2, 3, 3, 3, 3, 3, 3, 3, 1, 3] ... (150 total)`
- Title layout score: 85.4032
- Heading F1 score: 86.9258
- Level accuracy score: 76.6260
- Order score: 82.0000
- Main penalties:
  - 85 aligned headings have different relative levels.
  - 10 GT headings are missing.
  - 27 predicted headings are extra.

## Text Evaluation
- Text mode: normalized_full_text_preserve_newlines
- Text score: 96.4435
- Average edit distance: 0.0356
- Matched / missing / extra blocks: 1 / 0 / 0
- GT / Pred block counts: 1 / 1

### Worst Match Samples
1. op=match, distance=0.0356, GT blocks 0+1, Pred blocks 0+1
   - GT: ![]\n目录\n\n4管理层讨论与分析\n25董事及首席执行官\n29权益披露\n34股权激励计划\n38购买出售或回购本公司上市证券\n39其他信息\n42释义\n44财务报表\n\n不同投票权\n\n我们只有单一类别的股份每一股份对应一份表决权。然而根据《公司章程》,...
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
