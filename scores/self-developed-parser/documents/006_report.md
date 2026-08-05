# Financial Markdown Scoring Report

## Overall
- Final Score: 93.8860
- Table Score: 91.1985
- Title Layout Score: 93.0066
- Text Score: 97.0131

## Prediction Cleanup
- Mode: prediction_only_header_footer_cleanup
- Removed pred header/footer lines: 12
- Removed examples:
  - 阿里巴巴集團控股有限公司
  - 阿里巴巴集團控股有限公司
  - 阿里巴巴集團控股有限公司
  - 阿里巴巴集團控股有限公司
  - 阿里巴巴集團控股有限公司
  - ### 阿里巴巴集團控股有限公司
  - ### 阿里巴巴集團控股有限公司
  - ### 阿里巴巴集團控股有限公司
  - ### 阿里巴巴集團控股有限公司
  - ### 阿里巴巴集團控股有限公司

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
- Primary table score: 81.0496
- Alt table score: 75.3778
- Per-table rule: each predicted table keeps its higher one-to-one pair score from primary or alt GT.
- Per-table selected primary / alt pairs: 47 / 6
- Per-table reference table count: 50
- Matched / missing / extra tables: 53 / 0 / 0
- Table content score: 86.4626
- Table structure score: 94.3558
- Table matrix score: 91.1985
- Table alignment strategy: per_table_best_of_primary_alt_one_to_one

### Table Matches
- primary GT table 0 -> Pred table 0: pair=91.7962, structure=100.0000, content=79.4904, keywords=90.8214, match=92.9496, GT shape={'rows': 18, 'cols': 5}, Pred shape={'rows': 18, 'cols': 5}
- primary GT table 1 -> Pred table 1: pair=93.2735, structure=96.8254, content=87.9457, keywords=87.7733, match=91.2338, GT shape={'rows': 20, 'cols': 5}, Pred shape={'rows': 21, 'cols': 5}
- primary GT table 2 -> Pred table 2: pair=91.1073, structure=95.5556, content=84.4350, keywords=90.3333, match=91.6100, GT shape={'rows': 14, 'cols': 5}, Pred shape={'rows': 15, 'cols': 5}
- primary GT table 3 -> Pred table 3: pair=93.6822, structure=97.2222, content=88.3721, keywords=75.1761, match=85.1372, GT shape={'rows': 23, 'cols': 7}, Pred shape={'rows': 24, 'cols': 7}
- primary GT table 4 -> Pred table 4: pair=80.3061, structure=91.6667, content=63.2653, keywords=72.0833, match=78.4668, GT shape={'rows': 7, 'cols': 5}, Pred shape={'rows': 8, 'cols': 5}
- primary GT table 5 -> Pred table 5: pair=86.1478, structure=93.3333, content=75.3695, keywords=73.9630, match=81.4925, GT shape={'rows': 9, 'cols': 4}, Pred shape={'rows': 10, 'cols': 4}
- primary GT table 6 -> Pred table 6: pair=94.4797, structure=96.2963, content=91.7548, keywords=88.2407, match=91.7235, GT shape={'rows': 17, 'cols': 4}, Pred shape={'rows': 18, 'cols': 4}
- primary GT table 7 -> Pred table 7: pair=86.5618, structure=89.7436, content=81.7891, keywords=84.8667, match=86.3506, GT shape={'rows': 11, 'cols': 4}, Pred shape={'rows': 13, 'cols': 4}
- primary GT table 8 -> Pred table 8: pair=91.3203, structure=95.5556, content=84.9673, keywords=89.6053, match=91.3099, GT shape={'rows': 14, 'cols': 4}, Pred shape={'rows': 15, 'cols': 4}
- primary GT table 9 -> Pred table 9: pair=81.5789, structure=83.3333, content=78.9474, keywords=81.8065, match=82.0436, GT shape={'rows': 6, 'cols': 4}, Pred shape={'rows': 8, 'cols': 4}
- primary GT table 10 -> Pred table 10: pair=85.6051, structure=100.0000, content=64.0127, keywords=100.0000, match=95.6815, GT shape={'rows': 11, 'cols': 3}, Pred shape={'rows': 11, 'cols': 3}
- primary GT table 11 -> Pred table 11: pair=80.0721, structure=90.4762, content=64.4659, keywords=99.0714, match=91.6526, GT shape={'rows': 21, 'cols': 5}, Pred shape={'rows': 18, 'cols': 5}
- primary GT table 12 -> Pred table 12: pair=63.2503, structure=71.0145, content=51.6041, keywords=100.0000, match=83.1780, GT shape={'rows': 23, 'cols': 5}, Pred shape={'rows': 13, 'cols': 5}
- primary GT table 13 -> Pred table 13: pair=83.6738, structure=94.4444, content=67.5179, keywords=74.3939, match=81.1880, GT shape={'rows': 11, 'cols': 10}, Pred shape={'rows': 12, 'cols': 10}
- primary GT table 14 -> Pred table 14: pair=87.4883, structure=93.3030, content=78.7661, keywords=95.6250, match=92.7196, GT shape={'rows': 10, 'cols': 10}, Pred shape={'rows': 9, 'cols': 11}
- primary GT table 15 -> Pred table 15: pair=73.4947, structure=86.6667, content=53.7367, keywords=76.5909, match=77.6772, GT shape={'rows': 4, 'cols': 9}, Pred shape={'rows': 5, 'cols': 9}
- primary GT table 16 -> Pred table 16: pair=99.2793, structure=100.0000, content=98.1982, keywords=100.0000, match=99.7838, GT shape={'rows': 5, 'cols': 5}, Pred shape={'rows': 5, 'cols': 5}
- primary GT table 17 -> Pred table 17: pair=97.8125, structure=100.0000, content=94.5312, keywords=100.0000, match=99.3438, GT shape={'rows': 7, 'cols': 5}, Pred shape={'rows': 7, 'cols': 5}
- primary GT table 18 -> Pred table 18: pair=96.1677, structure=100.0000, content=90.4192, keywords=91.2500, match=94.4753, GT shape={'rows': 4, 'cols': 4}, Pred shape={'rows': 4, 'cols': 4}
- primary GT table 19 -> Pred table 19: pair=94.5122, structure=91.6667, content=98.7805, keywords=100.0000, match=96.6870, GT shape={'rows': 7, 'cols': 2}, Pred shape={'rows': 8, 'cols': 2}
- primary GT table 20 -> Pred table 20: pair=81.1084, structure=86.3611, content=73.2293, keywords=93.6364, match=88.4229, GT shape={'rows': 30, 'cols': 5}, Pred shape={'rows': 32, 'cols': 4}
- primary GT table 21 -> Pred table 21: pair=87.6530, structure=91.1111, content=82.4658, keywords=93.0392, match=91.0377, GT shape={'rows': 15, 'cols': 4}, Pred shape={'rows': 13, 'cols': 4}
- primary GT table 22 -> Pred table 22: pair=96.9299, structure=98.0952, content=95.1820, keywords=96.8182, match=97.1071, GT shape={'rows': 35, 'cols': 5}, Pred shape={'rows': 34, 'cols': 5}
- primary GT table 23 -> Pred table 23: pair=95.3436, structure=93.9394, content=97.4499, keywords=97.2106, match=95.9963, GT shape={'rows': 20, 'cols': 4}, Pred shape={'rows': 22, 'cols': 4}
- primary GT table 24 -> Pred table 24: pair=87.8281, structure=96.4912, content=74.8333, keywords=87.4352, match=89.3643, GT shape={'rows': 19, 'cols': 12}, Pred shape={'rows': 18, 'cols': 12}
- primary GT table 25 -> Pred table 25: pair=93.1528, structure=96.8254, content=87.6439, keywords=91.2352, match=92.9285, GT shape={'rows': 21, 'cols': 12}, Pred shape={'rows': 20, 'cols': 12}
- primary GT table 26 -> Pred table 26: pair=94.7427, structure=98.1982, content=89.5595, keywords=97.8861, match=97.0055, GT shape={'rows': 36, 'cols': 4}, Pred shape={'rows': 37, 'cols': 4}
- alt GT table 29 -> Pred table 27: pair=99.3084, structure=100.0000, content=98.2709, keywords=100.0000, match=99.7925, GT shape={'rows': 15, 'cols': 3}, Pred shape={'rows': 15, 'cols': 3}
- alt GT table 30 -> Pred table 28: pair=86.0825, structure=85.1852, content=87.4286, keywords=97.9688, match=91.8462, GT shape={'rows': 9, 'cols': 3}, Pred shape={'rows': 7, 'cols': 3}
- primary GT table 28 -> Pred table 29: pair=94.9612, structure=93.6508, content=96.9267, keywords=100.0000, match=97.2185, GT shape={'rows': 21, 'cols': 3}, Pred shape={'rows': 19, 'cols': 3}

## Title Layout Evaluation
- GT raw heading levels: `[1, 3, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 3, 4, 4, 3, 4, 4, 3, 4, 4, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 2, 3, 3, 3, 2, 2, 3, 3, 3, 3, 3, 3, 3, 2, 3, 2, 3, 2, 3, 3, 3, 3, 3, 3, 3, 4, 3, 4, 4, 3, 4, 4, 4, 3, 4, 4, 3, 4, 3, 3, 3, 3, 3, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3] ... (146 total)`
- Pred raw heading levels: `[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3] ... (138 total)`
- GT relative heading levels: `[1, 3, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 3, 4, 4, 3, 4, 4, 3, 4, 4, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 2, 3, 3, 3, 2, 2, 3, 3, 3, 3, 3, 3, 3, 2, 3, 2, 3, 2, 3, 3, 3, 3, 3, 3, 3, 4, 3, 4, 4, 3, 4, 4, 4, 3, 4, 4, 3, 4, 3, 3, 3, 3, 3, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3] ... (146 total)`
- Pred relative heading levels: `[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3] ... (138 total)`
- Title layout score: 93.0066
- Heading F1 score: 95.0704
- Level accuracy score: 77.0370
- Order score: 92.4658
- Main penalties:
  - 86 aligned headings have different relative levels.
  - 11 GT headings are missing.
  - 3 predicted headings are extra.

## Text Evaluation
- Text mode: normalized_full_text_preserve_newlines
- Text score: 97.0131
- Average edit distance: 0.0299
- Matched / missing / extra blocks: 1 / 0 / 0
- GT / Pred block counts: 1 / 1

### Worst Match Samples
1. op=match, distance=0.0299, GT blocks 0+1, Pred blocks 0+1
   - GT: ![]\n2026财务年度中期报告\n阿里巴巴\n\n阿里巴巴集团控股有限公司\n\n纽交所代码:BABA港交所代号:9988(港币柜台)89988(人民币柜台)\n\n目录\n\n4管理层讨论与分析\n25董事及首席执行官\n29权益披露\n34股权激励计划\n38购买出...
   - Pred: 133343412\n\n阿里巴巴集团控股有限公司\n\n纽交所代码:BABA港交所代号:9988(港币柜台)89988(人民币柜台)\n\n2026财务年度中期报告\n\n目录\n\n4管理层讨论与分析\n\n25董事及首席执行官\n\n29权益披露\n\n34股权激励计...

## Notes
- Table score compares extracted HTML and Markdown pipe tables after conversion to cell matrices.
- With primary or alt strategy, table matching is GT-driven one-to-one: each GT table chooses one best unused Pred table.
- With max and two GT files, each predicted table keeps the higher pair score from the two independently one-to-one-matched GT variants.
- Table pair score is 60% structure score and 40% content score; table content score uses normalized edit distance on flattened table text.
- Title layout score uses heading text only for anchor alignment, then combines heading F1, relative-level accuracy, and order coverage.
- Text score removes tables, keeps heading words, preserves newlines, and scores the full body as one character sequence.
- No-value page headers and footers are removed from prediction Markdown only; GT Markdown is kept as the reference answer.
- Current limitations: complex nested tables, heavily malformed HTML, and table semantic equivalence beyond cell text are only approximated.
