# Financial Markdown Scoring Report

## Overall
- Final Score: 83.6275
- Table Score: 85.2803
- Title Layout Score: 69.7916
- Text Score: 88.8926

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
- Primary table score: 65.7180
- Alt table score: 57.4717
- Per-table rule: each predicted table keeps its higher one-to-one pair score from primary or alt GT.
- Per-table selected primary / alt pairs: 121 / 39
- Per-table reference table count: 144
- Matched / missing / extra tables: 160 / 0 / 1
- Table content score: 80.0283
- Table structure score: 88.7817
- Table matrix score: 85.2803
- Table alignment strategy: per_table_best_of_primary_alt_one_to_one

### Table Matches
- primary GT table 0 -> Pred table 0: pair=95.2026, structure=100.0000, content=88.0065, keywords=91.2500, match=94.1858, GT shape={'rows': 10, 'cols': 6}, Pred shape={'rows': 10, 'cols': 6}
- primary GT table 1 -> Pred table 1: pair=86.7838, structure=88.6574, content=83.9735, keywords=80.8333, match=84.1833, GT shape={'rows': 16, 'cols': 6}, Pred shape={'rows': 18, 'cols': 5}
- alt GT table 3 -> Pred table 2: pair=53.3444, structure=61.2821, content=41.4379, keywords=92.4375, match=74.4785, GT shape={'rows': 12, 'cols': 5}, Pred shape={'rows': 26, 'cols': 4}
- alt GT table 5 -> Pred table 3: pair=60.9766, structure=62.6667, content=58.4416, keywords=84.2398, match=72.9462, GT shape={'rows': 12, 'cols': 5}, Pred shape={'rows': 25, 'cols': 4}
- alt GT table 6 -> Pred table 4: pair=42.3737, structure=65.3333, content=7.9341, keywords=91.5497, match=71.5536, GT shape={'rows': 12, 'cols': 5}, Pred shape={'rows': 25, 'cols': 5}
- primary GT table 7 -> Pred table 5: pair=87.6021, structure=94.8718, content=76.6975, keywords=94.7183, match=92.6141, GT shape={'rows': 24, 'cols': 3}, Pred shape={'rows': 26, 'cols': 3}
- primary GT table 4 -> Pred table 6: pair=87.0525, structure=87.8788, content=85.8131, keywords=100.0000, match=93.6915, GT shape={'rows': 18, 'cols': 4}, Pred shape={'rows': 22, 'cols': 4}
- primary GT table 5 -> Pred table 7: pair=91.8207, structure=100.0000, content=79.5518, keywords=76.2403, match=85.6664, GT shape={'rows': 10, 'cols': 5}, Pred shape={'rows': 10, 'cols': 5}
- primary GT table 10 -> Pred table 8: pair=83.1579, structure=93.3333, content=67.8947, keywords=80.9048, match=84.0664, GT shape={'rows': 9, 'cols': 5}, Pred shape={'rows': 10, 'cols': 5}
- primary GT table 3 -> Pred table 9: pair=88.4381, structure=94.6667, content=79.0952, keywords=100.0000, match=95.4648, GT shape={'rows': 23, 'cols': 3}, Pred shape={'rows': 25, 'cols': 3}
- primary GT table 8 -> Pred table 10: pair=86.5467, structure=87.8788, content=84.5486, keywords=100.0000, match=93.5398, GT shape={'rows': 18, 'cols': 4}, Pred shape={'rows': 22, 'cols': 4}
- primary GT table 9 -> Pred table 11: pair=89.0704, structure=100.0000, content=72.6761, keywords=76.2403, match=84.8413, GT shape={'rows': 10, 'cols': 5}, Pred shape={'rows': 10, 'cols': 5}
- primary GT table 6 -> Pred table 12: pair=70.3951, structure=86.6667, content=45.9877, keywords=54.3810, match=65.6424, GT shape={'rows': 8, 'cols': 5}, Pred shape={'rows': 10, 'cols': 4}
- primary GT table 11 -> Pred table 13: pair=86.3843, structure=100.0000, content=65.9607, keywords=100.0000, match=95.9153, GT shape={'rows': 23, 'cols': 3}, Pred shape={'rows': 23, 'cols': 3}
- alt GT table 17 -> Pred table 14: pair=33.4615, structure=43.4343, content=18.5022, keywords=87.8289, match=62.6398, GT shape={'rows': 18, 'cols': 4}, Pred shape={'rows': 22, 'cols': 15}
- primary GT table 13 -> Pred table 15: pair=82.7456, structure=93.3333, content=66.8639, keywords=51.4583, match=69.2195, GT shape={'rows': 9, 'cols': 5}, Pred shape={'rows': 10, 'cols': 5}
- primary GT table 14 -> Pred table 16: pair=85.4347, structure=86.6667, content=83.5866, keywords=80.9470, match=83.4373, GT shape={'rows': 8, 'cols': 5}, Pred shape={'rows': 10, 'cols': 5}
- primary GT table 15 -> Pred table 17: pair=91.0755, structure=97.2222, content=81.8554, keywords=86.1015, match=89.8178, GT shape={'rows': 23, 'cols': 4}, Pred shape={'rows': 24, 'cols': 4}
- primary GT table 16 -> Pred table 18: pair=96.5756, structure=100.0000, content=91.4390, keywords=100.0000, match=98.9727, GT shape={'rows': 21, 'cols': 3}, Pred shape={'rows': 21, 'cols': 3}
- primary GT table 17 -> Pred table 19: pair=89.2043, structure=88.8889, content=89.6774, keywords=100.0000, match=94.5391, GT shape={'rows': 10, 'cols': 3}, Pred shape={'rows': 12, 'cols': 3}
- alt GT table 23 -> Pred table 20: pair=61.8729, structure=56.7251, content=69.5946, keywords=53.3333, match=56.5735, GT shape={'rows': 9, 'cols': 5}, Pred shape={'rows': 19, 'cols': 6}
- primary GT table 18 -> Pred table 21: pair=65.8202, structure=91.6667, content=27.0506, keywords=56.8750, match=66.5169, GT shape={'rows': 24, 'cols': 5}, Pred shape={'rows': 21, 'cols': 5}
- alt GT table 25 -> Pred table 22: pair=54.7074, structure=55.5556, content=53.4351, keywords=51.2500, match=53.1483, GT shape={'rows': 5, 'cols': 5}, Pred shape={'rows': 15, 'cols': 5}
- primary GT table 19 -> Pred table 23: pair=97.5556, structure=100.0000, content=93.8889, keywords=94.3174, match=96.4254, GT shape={'rows': 18, 'cols': 4}, Pred shape={'rows': 18, 'cols': 4}
- primary GT table 20 -> Pred table 24: pair=67.2029, structure=67.6768, content=66.4921, keywords=79.7177, match=73.5551, GT shape={'rows': 8, 'cols': 9}, Pred shape={'rows': 12, 'cols': 11}
- primary GT table 21 -> Pred table 25: pair=62.5246, structure=73.3333, content=46.3115, keywords=69.5797, match=68.2139, GT shape={'rows': 6, 'cols': 9}, Pred shape={'rows': 10, 'cols': 9}
- primary GT table 22 -> Pred table 26: pair=76.4268, structure=88.6574, content=58.0808, keywords=55.5208, match=68.4199, GT shape={'rows': 5, 'cols': 9}, Pred shape={'rows': 6, 'cols': 8}
- primary GT table 23 -> Pred table 27: pair=72.5185, structure=73.3333, content=71.2963, keywords=51.5094, match=62.1769, GT shape={'rows': 6, 'cols': 11}, Pred shape={'rows': 10, 'cols': 11}
- primary GT table 24 -> Pred table 28: pair=84.8012, structure=90.4762, content=76.2887, keywords=52.8125, match=69.9419, GT shape={'rows': 6, 'cols': 9}, Pred shape={'rows': 7, 'cols': 9}
- primary GT table 25 -> Pred table 29: pair=65.7937, structure=70.3704, content=58.9286, keywords=41.9792, match=54.8018, GT shape={'rows': 5, 'cols': 9}, Pred shape={'rows': 9, 'cols': 9}

## Title Layout Evaluation
- GT raw heading levels: `[1, 2, 1, 1, 2, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 3, 3, 2, 1, 2, 3, 3, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 2, 3, 3, 2, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 2, 3, 3, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3] ... (554 total)`
- Pred raw heading levels: `[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2] ... (923 total)`
- GT relative heading levels: `[1, 2, 1, 1, 2, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 3, 3, 2, 1, 2, 3, 3, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 2, 3, 3, 2, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 2, 3, 3, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3] ... (554 total)`
- Pred relative heading levels: `[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2] ... (923 total)`
- Title layout score: 69.7916
- Heading F1 score: 70.5484
- Level accuracy score: 77.0825
- Order score: 56.4464
- Main penalties:
  - 374 aligned headings have different relative levels.
  - 33 GT headings are missing.
  - 402 predicted headings are extra.

## Text Evaluation
- Text mode: normalized_full_text_preserve_newlines
- Text score: 88.8926
- Average edit distance: 0.1111
- Matched / missing / extra blocks: 1 / 0 / 0
- GT / Pred block counts: 1 / 1

### Worst Match Samples
1. op=match, distance=0.1111, GT blocks 0+1, Pred blocks 0+1
   - GT: 美团\n\nMeituan\n\n(于开曼群岛注册成立以不同投票权控制的有限公司)\n\n港币柜台股份代号:3690\n\n人民币柜台股份代号:83690\n![]\nEatBetterLiveBetter\n年度报告\n\n目录\n\n公司资料\n\n财务概要6\n\n主...
   - Pred: 美团美团Meituan\n\n(于开曼群岛注册成立以不同投票权控制的有限公司)\n港币柜台股份代号:3690\n人民币柜台股份代号:83690\n\n2024年度报告\n\n目录\n\n公司资料2\n财务概要6\n主席报告10\n管理层讨论及分析14\n董事及高级管理层38...

## Notes
- Table score compares extracted HTML and Markdown pipe tables after conversion to cell matrices.
- With primary or alt strategy, table matching is GT-driven one-to-one: each GT table chooses one best unused Pred table.
- With max and two GT files, each predicted table keeps the higher pair score from the two independently one-to-one-matched GT variants.
- Table pair score is 60% structure score and 40% content score; table content score uses normalized edit distance on flattened table text.
- Title layout score uses heading text only for anchor alignment, then combines heading F1, relative-level accuracy, and order coverage.
- Text score removes tables, keeps heading words, preserves newlines, and scores the full body as one character sequence.
- No-value page headers and footers are removed from prediction Markdown only; GT Markdown is kept as the reference answer.
- Current limitations: complex nested tables, heavily malformed HTML, and table semantic equivalence beyond cell text are only approximated.
