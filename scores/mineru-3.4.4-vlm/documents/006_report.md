# Financial Markdown Scoring Report

## Overall
- Final Score: 92.2179
- Table Score: 93.7883
- Title Layout Score: 82.4568
- Text Score: 95.5280

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
- Primary table score: 82.2601
- Alt table score: 80.5507
- Per-table rule: each predicted table keeps its higher one-to-one pair score from primary or alt GT.
- Per-table selected primary / alt pairs: 46 / 4
- Per-table reference table count: 51
- Matched / missing / extra tables: 50 / 1 / 0
- Table content score: 92.2492
- Table structure score: 94.8144
- Table matrix score: 93.7883
- Table alignment strategy: per_table_best_of_primary_alt_one_to_one

### Table Matches
- primary GT table 0 -> Pred table 0: pair=99.3930, structure=100.0000, content=98.4825, keywords=100.0000, match=99.8179, GT shape={'rows': 18, 'cols': 5}, Pred shape={'rows': 18, 'cols': 5}
- primary GT table 1 -> Pred table 1: pair=98.2826, structure=100.0000, content=95.7066, keywords=100.0000, match=99.4848, GT shape={'rows': 20, 'cols': 5}, Pred shape={'rows': 20, 'cols': 5}
- primary GT table 2 -> Pred table 2: pair=97.8082, structure=100.0000, content=94.5205, keywords=100.0000, match=99.3425, GT shape={'rows': 14, 'cols': 5}, Pred shape={'rows': 14, 'cols': 5}
- primary GT table 3 -> Pred table 3: pair=94.7866, structure=97.1014, content=91.3143, keywords=93.8288, match=94.7707, GT shape={'rows': 23, 'cols': 7}, Pred shape={'rows': 22, 'cols': 7}
- primary GT table 4 -> Pred table 4: pair=91.7895, structure=100.0000, content=79.4737, keywords=100.0000, match=97.5369, GT shape={'rows': 7, 'cols': 5}, Pred shape={'rows': 7, 'cols': 5}
- primary GT table 5 -> Pred table 5: pair=90.4094, structure=92.5926, content=87.1345, keywords=77.6852, match=84.4839, GT shape={'rows': 9, 'cols': 4}, Pred shape={'rows': 8, 'cols': 4}
- primary GT table 6 -> Pred table 6: pair=96.1393, structure=96.0784, content=96.2306, keywords=91.0185, match=93.5667, GT shape={'rows': 17, 'cols': 4}, Pred shape={'rows': 16, 'cols': 4}
- primary GT table 7 -> Pred table 7: pair=93.9906, structure=94.4444, content=93.3099, keywords=88.2667, match=91.2194, GT shape={'rows': 12, 'cols': 4}, Pred shape={'rows': 11, 'cols': 4}
- primary GT table 8 -> Pred table 8: pair=99.8491, structure=100.0000, content=99.6226, keywords=100.0000, match=99.9547, GT shape={'rows': 14, 'cols': 4}, Pred shape={'rows': 14, 'cols': 4}
- primary GT table 9 -> Pred table 9: pair=90.9686, structure=90.4762, content=91.7073, keywords=90.9032, match=90.8374, GT shape={'rows': 7, 'cols': 4}, Pred shape={'rows': 6, 'cols': 4}
- primary GT table 10 -> Pred table 10: pair=99.8058, structure=100.0000, content=99.5146, keywords=100.0000, match=99.9417, GT shape={'rows': 11, 'cols': 3}, Pred shape={'rows': 11, 'cols': 3}
- primary GT table 11 -> Pred table 11: pair=99.7647, structure=100.0000, content=99.4118, keywords=100.0000, match=99.9294, GT shape={'rows': 21, 'cols': 5}, Pred shape={'rows': 21, 'cols': 5}
- primary GT table 12 -> Pred table 12: pair=96.9776, structure=97.1014, content=96.7918, keywords=94.0909, match=95.5590, GT shape={'rows': 23, 'cols': 5}, Pred shape={'rows': 22, 'cols': 5}
- primary GT table 13 -> Pred table 13: pair=99.9429, structure=100.0000, content=99.8571, keywords=100.0000, match=99.9829, GT shape={'rows': 11, 'cols': 10}, Pred shape={'rows': 11, 'cols': 10}
- primary GT table 14 -> Pred table 14: pair=99.8089, structure=100.0000, content=99.5223, keywords=100.0000, match=99.9427, GT shape={'rows': 10, 'cols': 10}, Pred shape={'rows': 10, 'cols': 10}
- primary GT table 15 -> Pred table 15: pair=99.8867, structure=100.0000, content=99.7167, keywords=100.0000, match=99.9660, GT shape={'rows': 4, 'cols': 9}, Pred shape={'rows': 4, 'cols': 9}
- primary GT table 16 -> Pred table 16: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 5, 'cols': 5}, Pred shape={'rows': 5, 'cols': 5}
- primary GT table 17 -> Pred table 17: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 7, 'cols': 5}, Pred shape={'rows': 7, 'cols': 5}
- primary GT table 18 -> Pred table 18: pair=82.9677, structure=86.6667, content=77.4194, keywords=91.8548, match=88.1510, GT shape={'rows': 5, 'cols': 4}, Pred shape={'rows': 4, 'cols': 4}
- primary GT table 19 -> Pred table 19: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 7, 'cols': 2}, Pred shape={'rows': 7, 'cols': 2}
- primary GT table 20 -> Pred table 20: pair=95.2880, structure=95.8333, content=94.4700, keywords=96.5000, match=96.0031, GT shape={'rows': 32, 'cols': 5}, Pred shape={'rows': 30, 'cols': 5}
- primary GT table 21 -> Pred table 21: pair=95.5403, structure=95.8333, content=95.1009, keywords=100.0000, match=97.8288, GT shape={'rows': 16, 'cols': 4}, Pred shape={'rows': 15, 'cols': 4}
- alt GT table 22 -> Pred table 22: pair=96.6051, structure=96.2963, content=97.0684, keywords=96.8182, match=96.6499, GT shape={'rows': 36, 'cols': 5}, Pred shape={'rows': 34, 'cols': 5}
- alt GT table 23 -> Pred table 23: pair=96.4810, structure=96.6667, content=96.2025, keywords=100.0000, match=98.2776, GT shape={'rows': 20, 'cols': 4}, Pred shape={'rows': 19, 'cols': 4}
- alt GT table 24 -> Pred table 24: pair=95.3991, structure=100.0000, content=88.4979, keywords=89.6987, match=93.4691, GT shape={'rows': 19, 'cols': 12}, Pred shape={'rows': 19, 'cols': 12}
- alt GT table 25 -> Pred table 25: pair=97.0530, structure=100.0000, content=92.6324, keywords=89.7323, match=93.9820, GT shape={'rows': 21, 'cols': 12}, Pred shape={'rows': 21, 'cols': 12}
- primary GT table 24 -> Pred table 26: pair=98.3357, structure=98.1982, content=98.5420, keywords=100.0000, match=99.1403, GT shape={'rows': 37, 'cols': 4}, Pred shape={'rows': 36, 'cols': 4}
- primary GT table 25 -> Pred table 27: pair=71.4093, structure=75.0000, content=66.0232, keywords=96.8182, match=84.8319, GT shape={'rows': 15, 'cols': 3}, Pred shape={'rows': 24, 'cols': 3}
- primary GT table 27 -> Pred table 28: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 21, 'cols': 3}, Pred shape={'rows': 21, 'cols': 3}
- primary GT table 28 -> Pred table 29: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 11, 'cols': 3}, Pred shape={'rows': 11, 'cols': 3}

## Title Layout Evaluation
- GT raw heading levels: `[1, 1, 1, 1, 1, 2, 2, 3, 4, 4, 3, 4, 4, 3, 4, 4, 3, 4, 4, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 2, 2, 3, 3, 3, 3, 3, 3, 1, 2, 3, 2, 1, 2, 2, 2, 1, 1, 2, 3, 3, 3, 2, 2, 3, 1, 2, 1, 2, 2, 3, 3, 3, 2, 2, 2, 2, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 4, 4, 3, 4, 3, 3, 3, 3, 3, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4] ... (133 total)`
- Pred raw heading levels: `[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] ... (147 total)`
- GT relative heading levels: `[1, 1, 1, 1, 1, 2, 2, 3, 4, 4, 3, 4, 4, 3, 4, 4, 3, 4, 4, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 2, 2, 3, 3, 3, 3, 3, 3, 1, 2, 3, 2, 1, 2, 2, 2, 1, 1, 2, 3, 3, 3, 2, 2, 3, 1, 2, 1, 2, 2, 3, 3, 3, 2, 2, 2, 2, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 4, 4, 3, 4, 3, 3, 3, 3, 3, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4] ... (133 total)`
- Pred relative heading levels: `[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] ... (147 total)`
- Title layout score: 82.4568
- Heading F1 score: 86.4286
- Level accuracy score: 50.8264
- Order score: 82.3129
- Main penalties:
  - 111 aligned headings have different relative levels.
  - 12 GT headings are missing.
  - 26 predicted headings are extra.

## Text Evaluation
- Text mode: normalized_full_text_preserve_newlines
- Text score: 95.5280
- Average edit distance: 0.0447
- Matched / missing / extra blocks: 1 / 0 / 0
- GT / Pred block counts: 1 / 1

### Worst Match Samples
1. op=match, distance=0.0447, GT blocks 0+1, Pred blocks 0+1
   - GT: ![]\n目录\n\n4管理层讨论与分析\n25董事及首席执行官\n29权益披露\n34股权激励计划\n38购买出售或回购本公司上市证券\n39其他信息\n42释义\n44财务报表\n\n不同投票权\n\n我们只有单一类别的股份每一股份对应一份表决权。然而根据《公司章程》,...
   - Pred: ![]\n阿里巴巴\n\n阿里巴巴集团控股有限公司\n\n纽交所代码:BABA港交所代号:9988(港币柜台)89988(人民币柜台)\n\n目录\n\n4管理层讨论与分析\n25董事及首席执行官\n29权益披露\n34股权激励计划\n38购买出售或回购本公司上市证券\n3...

## Notes
- Table score compares extracted HTML and Markdown pipe tables after conversion to cell matrices.
- With primary or alt strategy, table matching is GT-driven one-to-one: each GT table chooses one best unused Pred table.
- With max and two GT files, each predicted table keeps the higher pair score from the two independently one-to-one-matched GT variants.
- Table pair score is 60% structure score and 40% content score; table content score uses normalized edit distance on flattened table text.
- Title layout score uses heading text only for anchor alignment, then combines heading F1, relative-level accuracy, and order coverage.
- Text score removes tables, keeps heading words, preserves newlines, and scores the full body as one character sequence.
- No-value page headers and footers are removed from prediction Markdown only; GT Markdown is kept as the reference answer.
- Current limitations: complex nested tables, heavily malformed HTML, and table semantic equivalence beyond cell text are only approximated.
