# Financial Markdown Scoring Report

## Overall
- Final Score: 96.4510
- Table Score: 99.0752
- Title Layout Score: 89.8078
- Text Score: 97.1483

## Prediction Cleanup
- Mode: prediction_only_header_footer_cleanup
- Removed pred header/footer lines: 3
- Removed examples:
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
- Primary table score: 99.0752
- Alt table score: 73.1567
- Per-table rule: each predicted table keeps its higher one-to-one pair score from primary or alt GT.
- Per-table selected primary / alt pairs: 50 / 0
- Per-table reference table count: 50
- Matched / missing / extra tables: 50 / 0 / 0
- Table content score: 98.6089
- Table structure score: 99.3860
- Table matrix score: 99.0752
- Table alignment strategy: per_table_best_of_primary_alt_one_to_one

### Table Matches
- primary GT table 0 -> Pred table 0: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 18, 'cols': 5}, Pred shape={'rows': 18, 'cols': 5}
- primary GT table 1 -> Pred table 1: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 20, 'cols': 5}, Pred shape={'rows': 20, 'cols': 5}
- primary GT table 2 -> Pred table 2: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 14, 'cols': 5}, Pred shape={'rows': 14, 'cols': 5}
- primary GT table 3 -> Pred table 3: pair=96.1706, structure=97.1014, content=94.7743, keywords=93.8288, match=95.1859, GT shape={'rows': 23, 'cols': 7}, Pred shape={'rows': 22, 'cols': 7}
- primary GT table 4 -> Pred table 4: pair=96.7213, structure=100.0000, content=91.8033, keywords=100.0000, match=99.0164, GT shape={'rows': 7, 'cols': 5}, Pred shape={'rows': 7, 'cols': 5}
- primary GT table 5 -> Pred table 5: pair=92.5742, structure=92.5926, content=92.5466, keywords=77.6852, match=85.1334, GT shape={'rows': 9, 'cols': 4}, Pred shape={'rows': 8, 'cols': 4}
- primary GT table 6 -> Pred table 6: pair=96.9148, structure=96.0784, content=98.1693, keywords=91.0185, match=93.7994, GT shape={'rows': 17, 'cols': 4}, Pred shape={'rows': 16, 'cols': 4}
- primary GT table 7 -> Pred table 7: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 11, 'cols': 4}, Pred shape={'rows': 11, 'cols': 4}
- primary GT table 8 -> Pred table 8: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 14, 'cols': 4}, Pred shape={'rows': 14, 'cols': 4}
- primary GT table 9 -> Pred table 9: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 6, 'cols': 4}, Pred shape={'rows': 6, 'cols': 4}
- primary GT table 10 -> Pred table 10: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 11, 'cols': 3}, Pred shape={'rows': 11, 'cols': 3}
- primary GT table 11 -> Pred table 11: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 21, 'cols': 5}, Pred shape={'rows': 21, 'cols': 5}
- primary GT table 12 -> Pred table 12: pair=97.0595, structure=97.1014, content=96.9966, keywords=94.0909, match=95.5836, GT shape={'rows': 23, 'cols': 5}, Pred shape={'rows': 22, 'cols': 5}
- primary GT table 13 -> Pred table 13: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 11, 'cols': 10}, Pred shape={'rows': 11, 'cols': 10}
- primary GT table 14 -> Pred table 14: pair=99.8726, structure=100.0000, content=99.6815, keywords=100.0000, match=99.9618, GT shape={'rows': 10, 'cols': 10}, Pred shape={'rows': 10, 'cols': 10}
- primary GT table 15 -> Pred table 15: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 4, 'cols': 9}, Pred shape={'rows': 4, 'cols': 9}
- primary GT table 16 -> Pred table 16: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 5, 'cols': 5}, Pred shape={'rows': 5, 'cols': 5}
- primary GT table 17 -> Pred table 17: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 7, 'cols': 5}, Pred shape={'rows': 7, 'cols': 5}
- primary GT table 18 -> Pred table 18: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 4, 'cols': 4}, Pred shape={'rows': 4, 'cols': 4}
- primary GT table 19 -> Pred table 19: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 7, 'cols': 2}, Pred shape={'rows': 7, 'cols': 2}
- primary GT table 20 -> Pred table 20: pair=99.9520, structure=100.0000, content=99.8801, keywords=100.0000, match=99.9856, GT shape={'rows': 30, 'cols': 5}, Pred shape={'rows': 30, 'cols': 5}
- primary GT table 21 -> Pred table 21: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 15, 'cols': 4}, Pred shape={'rows': 15, 'cols': 4}
- primary GT table 22 -> Pred table 22: pair=97.7678, structure=98.0952, content=97.2767, keywords=96.8182, match=97.3585, GT shape={'rows': 35, 'cols': 5}, Pred shape={'rows': 34, 'cols': 5}
- primary GT table 23 -> Pred table 23: pair=97.7075, structure=96.6667, content=99.2687, keywords=100.0000, match=98.6456, GT shape={'rows': 20, 'cols': 4}, Pred shape={'rows': 19, 'cols': 4}
- primary GT table 24 -> Pred table 24: pair=94.3000, structure=100.0000, content=85.7500, keywords=85.7698, match=91.1749, GT shape={'rows': 19, 'cols': 12}, Pred shape={'rows': 19, 'cols': 12}
- primary GT table 25 -> Pred table 25: pair=96.7123, structure=100.0000, content=91.7808, keywords=89.3772, match=93.7023, GT shape={'rows': 21, 'cols': 12}, Pred shape={'rows': 21, 'cols': 12}
- primary GT table 26 -> Pred table 26: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 36, 'cols': 4}, Pred shape={'rows': 36, 'cols': 4}
- primary GT table 27 -> Pred table 27: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 24, 'cols': 3}, Pred shape={'rows': 24, 'cols': 3}
- primary GT table 28 -> Pred table 28: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 21, 'cols': 3}, Pred shape={'rows': 21, 'cols': 3}
- primary GT table 29 -> Pred table 29: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 11, 'cols': 3}, Pred shape={'rows': 11, 'cols': 3}

## Title Layout Evaluation
- GT raw heading levels: `[1, 3, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 3, 4, 4, 3, 4, 4, 3, 4, 4, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 2, 3, 3, 3, 2, 2, 3, 3, 3, 3, 3, 3, 3, 2, 3, 2, 3, 2, 3, 3, 3, 3, 3, 3, 3, 4, 3, 4, 4, 3, 4, 4, 4, 3, 4, 4, 3, 4, 3, 3, 3, 3, 3, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3] ... (146 total)`
- Pred raw heading levels: `[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] ... (148 total)`
- GT relative heading levels: `[1, 3, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 3, 4, 4, 3, 4, 4, 3, 4, 4, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 2, 3, 3, 3, 2, 2, 3, 3, 3, 3, 3, 3, 3, 2, 3, 2, 3, 2, 3, 3, 3, 3, 3, 3, 3, 4, 3, 4, 4, 3, 4, 4, 4, 3, 4, 4, 3, 4, 3, 3, 3, 3, 3, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3] ... (146 total)`
- Pred relative heading levels: `[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] ... (148 total)`
- Title layout score: 89.8078
- Heading F1 score: 96.5986
- Level accuracy score: 29.3427
- Order score: 95.9459
- Main penalties:
  - 142 aligned headings have different relative levels.
  - 4 GT headings are missing.
  - 6 predicted headings are extra.

## Text Evaluation
- Text mode: normalized_full_text_preserve_newlines
- Text score: 97.1483
- Average edit distance: 0.0285
- Matched / missing / extra blocks: 1 / 0 / 0
- GT / Pred block counts: 1 / 1

### Worst Match Samples
1. op=match, distance=0.0285, GT blocks 0+1, Pred blocks 0+1
   - GT: ![]\n2026财务年度中期报告\n阿里巴巴\n\n阿里巴巴集团控股有限公司\n\n纽交所代码:BABA港交所代号:9988(港币柜台)89988(人民币柜台)\n\n目录\n\n4管理层讨论与分析\n25董事及首席执行官\n29权益披露\n34股权激励计划\n38购买出...
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
