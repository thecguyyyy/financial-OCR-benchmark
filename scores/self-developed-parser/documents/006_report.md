# Financial Markdown Scoring Report

## Overall
- Final Score: 92.6013
- Table Score: 91.5834
- Title Layout Score: 87.3769
- Text Score: 96.2313

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
- Primary table score: 83.5568
- Alt table score: 87.9249
- Per-table rule: each predicted table keeps its higher one-to-one pair score from primary or alt GT.
- Per-table selected primary / alt pairs: 49 / 4
- Per-table reference table count: 51
- Matched / missing / extra tables: 53 / 0 / 0
- Table content score: 87.5147
- Table structure score: 94.2959
- Table matrix score: 91.5834
- Table alignment strategy: per_table_best_of_primary_alt_one_to_one

### Table Matches
- primary GT table 0 -> Pred table 0: pair=92.0102, structure=100.0000, content=80.0256, keywords=90.8214, match=93.0138, GT shape={'rows': 18, 'cols': 5}, Pred shape={'rows': 18, 'cols': 5}
- primary GT table 1 -> Pred table 1: pair=92.2932, structure=96.8254, content=85.4949, keywords=87.7733, match=90.9397, GT shape={'rows': 20, 'cols': 5}, Pred shape={'rows': 21, 'cols': 5}
- primary GT table 2 -> Pred table 2: pair=93.7204, structure=95.5556, content=90.9677, keywords=90.3333, match=92.3939, GT shape={'rows': 14, 'cols': 5}, Pred shape={'rows': 15, 'cols': 5}
- primary GT table 3 -> Pred table 3: pair=93.5401, structure=97.2222, content=88.0170, keywords=75.1761, match=85.0945, GT shape={'rows': 23, 'cols': 7}, Pred shape={'rows': 24, 'cols': 7}
- primary GT table 4 -> Pred table 4: pair=84.8755, structure=91.6667, content=74.6888, keywords=72.0833, match=79.8376, GT shape={'rows': 7, 'cols': 5}, Pred shape={'rows': 8, 'cols': 5}
- primary GT table 5 -> Pred table 5: pair=84.1773, structure=93.3333, content=70.4433, keywords=72.0714, match=79.9555, GT shape={'rows': 9, 'cols': 4}, Pred shape={'rows': 10, 'cols': 4}
- primary GT table 6 -> Pred table 6: pair=93.5494, structure=96.2963, content=89.4292, keywords=87.6720, match=91.1601, GT shape={'rows': 17, 'cols': 4}, Pred shape={'rows': 18, 'cols': 4}
- primary GT table 7 -> Pred table 7: pair=89.3831, structure=94.8718, content=81.1502, keywords=83.2018, match=87.3902, GT shape={'rows': 12, 'cols': 4}, Pred shape={'rows': 13, 'cols': 4}
- primary GT table 8 -> Pred table 8: pair=92.0131, structure=95.5556, content=86.6995, keywords=89.6053, match=91.5177, GT shape={'rows': 14, 'cols': 4}, Pred shape={'rows': 15, 'cols': 4}
- primary GT table 9 -> Pred table 9: pair=86.0526, structure=91.6667, content=77.6316, keywords=79.8095, match=84.0539, GT shape={'rows': 7, 'cols': 4}, Pred shape={'rows': 8, 'cols': 4}
- primary GT table 10 -> Pred table 10: pair=85.6051, structure=100.0000, content=64.0127, keywords=100.0000, match=95.6815, GT shape={'rows': 11, 'cols': 3}, Pred shape={'rows': 11, 'cols': 3}
- primary GT table 11 -> Pred table 11: pair=80.1611, structure=90.4762, content=64.6884, keywords=99.0714, match=91.6793, GT shape={'rows': 21, 'cols': 5}, Pred shape={'rows': 18, 'cols': 5}
- primary GT table 12 -> Pred table 12: pair=63.3595, structure=71.0145, content=51.8771, keywords=100.0000, match=83.2107, GT shape={'rows': 23, 'cols': 5}, Pred shape={'rows': 13, 'cols': 5}
- primary GT table 13 -> Pred table 13: pair=83.9598, structure=94.4444, content=68.2329, keywords=74.3939, match=81.2738, GT shape={'rows': 11, 'cols': 10}, Pred shape={'rows': 12, 'cols': 10}
- primary GT table 14 -> Pred table 14: pair=87.6604, structure=93.3030, content=79.1966, keywords=95.6250, match=92.7712, GT shape={'rows': 10, 'cols': 10}, Pred shape={'rows': 9, 'cols': 11}
- primary GT table 15 -> Pred table 15: pair=73.7794, structure=86.6667, content=54.4484, keywords=76.5909, match=77.7626, GT shape={'rows': 4, 'cols': 9}, Pred shape={'rows': 5, 'cols': 9}
- primary GT table 16 -> Pred table 16: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 5, 'cols': 5}, Pred shape={'rows': 5, 'cols': 5}
- primary GT table 17 -> Pred table 17: pair=98.9020, structure=100.0000, content=97.2549, keywords=100.0000, match=99.6706, GT shape={'rows': 7, 'cols': 5}, Pred shape={'rows': 7, 'cols': 5}
- primary GT table 18 -> Pred table 18: pair=81.0244, structure=86.6667, content=72.5610, keywords=91.8548, match=87.5681, GT shape={'rows': 5, 'cols': 4}, Pred shape={'rows': 4, 'cols': 4}
- primary GT table 19 -> Pred table 19: pair=94.5122, structure=91.6667, content=98.7805, keywords=100.0000, match=96.6870, GT shape={'rows': 7, 'cols': 2}, Pred shape={'rows': 8, 'cols': 2}
- primary GT table 20 -> Pred table 20: pair=82.6912, structure=86.6667, content=76.7281, keywords=100.0000, match=92.1407, GT shape={'rows': 32, 'cols': 5}, Pred shape={'rows': 32, 'cols': 4}
- primary GT table 21 -> Pred table 21: pair=85.3767, structure=87.5000, content=82.1918, keywords=97.5000, match=91.8630, GT shape={'rows': 16, 'cols': 4}, Pred shape={'rows': 13, 'cols': 4}
- alt GT table 22 -> Pred table 22: pair=96.3584, structure=96.2963, content=96.4516, keywords=96.8182, match=96.5759, GT shape={'rows': 36, 'cols': 5}, Pred shape={'rows': 34, 'cols': 5}
- alt GT table 23 -> Pred table 23: pair=94.5553, structure=93.9394, content=95.4792, keywords=97.2106, match=95.7598, GT shape={'rows': 20, 'cols': 4}, Pred shape={'rows': 22, 'cols': 4}
- alt GT table 24 -> Pred table 24: pair=88.7743, structure=96.4912, content=77.1990, keywords=89.6987, match=90.7799, GT shape={'rows': 19, 'cols': 12}, Pred shape={'rows': 18, 'cols': 12}
- alt GT table 25 -> Pred table 25: pair=93.6370, structure=96.8254, content=88.8545, keywords=89.3712, match=92.1418, GT shape={'rows': 21, 'cols': 12}, Pred shape={'rows': 20, 'cols': 12}
- primary GT table 24 -> Pred table 26: pair=96.6585, structure=100.0000, content=91.6462, keywords=100.0000, match=98.9976, GT shape={'rows': 37, 'cols': 4}, Pred shape={'rows': 37, 'cols': 4}
- primary GT table 25 -> Pred table 27: pair=99.5376, structure=100.0000, content=98.8439, keywords=100.0000, match=99.8613, GT shape={'rows': 15, 'cols': 3}, Pred shape={'rows': 15, 'cols': 3}
- primary GT table 26 -> Pred table 28: pair=86.9968, structure=85.1852, content=89.7143, keywords=97.9688, match=92.1205, GT shape={'rows': 9, 'cols': 3}, Pred shape={'rows': 7, 'cols': 3}
- primary GT table 27 -> Pred table 29: pair=95.8113, structure=93.6508, content=99.0521, keywords=100.0000, match=97.4736, GT shape={'rows': 21, 'cols': 3}, Pred shape={'rows': 19, 'cols': 3}

## Title Layout Evaluation
- GT raw heading levels: `[1, 1, 1, 1, 1, 2, 2, 3, 4, 4, 3, 4, 4, 3, 4, 4, 3, 4, 4, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 2, 2, 3, 3, 3, 3, 3, 3, 1, 2, 3, 2, 1, 2, 2, 2, 1, 1, 2, 3, 3, 3, 2, 2, 3, 1, 2, 1, 2, 2, 3, 3, 3, 2, 2, 2, 2, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 4, 4, 3, 4, 3, 3, 3, 3, 3, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4] ... (133 total)`
- Pred raw heading levels: `[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3] ... (137 total)`
- GT relative heading levels: `[1, 1, 1, 1, 1, 2, 2, 3, 4, 4, 3, 4, 4, 3, 4, 4, 3, 4, 4, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 2, 2, 3, 3, 3, 3, 3, 3, 1, 2, 3, 2, 1, 2, 2, 2, 1, 1, 2, 3, 3, 3, 2, 2, 3, 1, 2, 1, 2, 2, 3, 3, 3, 2, 2, 2, 2, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 4, 4, 3, 4, 3, 3, 3, 3, 3, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4] ... (133 total)`
- Pred relative heading levels: `[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3] ... (137 total)`
- Title layout score: 87.3769
- Heading F1 score: 88.1481
- Level accuracy score: 81.7227
- Order score: 86.8613
- Main penalties:
  - 79 aligned headings have different relative levels.
  - 14 GT headings are missing.
  - 18 predicted headings are extra.

## Text Evaluation
- Text mode: normalized_full_text_preserve_newlines
- Text score: 96.2313
- Average edit distance: 0.0377
- Matched / missing / extra blocks: 1 / 0 / 0
- GT / Pred block counts: 1 / 1

### Worst Match Samples
1. op=match, distance=0.0377, GT blocks 0+1, Pred blocks 0+1
   - GT: ![]\n目录\n\n4管理层讨论与分析\n25董事及首席执行官\n29权益披露\n34股权激励计划\n38购买出售或回购本公司上市证券\n39其他信息\n42释义\n44财务报表\n\n不同投票权\n\n我们只有单一类别的股份每一股份对应一份表决权。然而根据《公司章程》,...
   - Pred: ![]\n阿里巴巴集团控股有限公司\n\n纽交所代码:BABA港交所代号:9988(港币柜台)89988(人民币柜台)\n\n2026财务年度中期报告\n\n目录\n\n4管理层讨论与分析\n\n25董事及首席执行官\n\n29权益披露\n\n34股权激励计划\n\n38购...

## Notes
- Table score compares extracted HTML and Markdown pipe tables after conversion to cell matrices.
- With primary or alt strategy, table matching is GT-driven one-to-one: each GT table chooses one best unused Pred table.
- With max and two GT files, each predicted table keeps the higher pair score from the two independently one-to-one-matched GT variants.
- Table pair score is 60% structure score and 40% content score; table content score uses normalized edit distance on flattened table text.
- Title layout score uses heading text only for anchor alignment, then combines heading F1, relative-level accuracy, and order coverage.
- Text score removes tables, keeps heading words, preserves newlines, and scores the full body as one character sequence.
- No-value page headers and footers are removed from prediction Markdown only; GT Markdown is kept as the reference answer.
- Current limitations: complex nested tables, heavily malformed HTML, and table semantic equivalence beyond cell text are only approximated.
