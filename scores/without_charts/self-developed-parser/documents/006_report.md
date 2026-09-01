# Financial Markdown Scoring Report

## Overall
- Final Score: 94.5388
- Table Score: 90.7435
- Title Layout Score: 88.5653
- Text Score: 97.7681

## Prediction Cleanup
- Mode: prediction_only_header_footer_cleanup
- Removed pred header/footer lines: 0
- Removed examples:
  - None

## Weights
- Mode: gt_content_information_share
- Table: 19.77%
- Title Layout: 20.00%
- Text: 60.23%
- GT table semantic tokens / grid slots / information units: 8850 / 4136 / 12986
- GT body / active chart / text information units: 39564 / 0 / 39564

## Configuration
- Remove pred header/footer: False
- Normalize images: True
- Score informative charts: False
- Normalize Chinese variants: t2s
- Normalize footnotes: True
- Normalize punctuation: True
- Table pair weights: structure=0.6, content=0.4
- Table aggregation: footprint
- Module weighting: content
- Title layout reserve: 0.2
- Chart scoring mode: excluded_from_scoring
- Detected primary GT / Pred chart blocks: 0 / 0
- Representation-neutral chart score: 100.0000
- GT chart token share inside text module: 0.0000
- Removed primary GT / alt GT / Pred chart blocks: 0 / 0 / 0

## Table Evaluation
- Table GT strategy result: per_table_max
- Primary table score: 81.1054
- Alt table score: 90.7485
- Per-table rule: each predicted table keeps its higher one-to-one pair score from primary or alt GT.
- Per-table selected primary / alt pairs: 49 / 4
- Per-table reference table count: 51
- Matched / missing / extra tables: 53 / 0 / 0
- Table content score: 84.7013
- Table structure score: 94.7716
- Table matrix score: 90.7435
- Table alignment strategy: per_table_best_of_primary_alt_gt_footprint_weighted
- GT footprint total / extra Pred footprint: 9460.2356 / 0.0000
- Chart-table eligible / auxiliary / matched: 0 / 0 / 0

### Table Matches
- primary GT table 0 -> Pred table 0: pair=86.9107, structure=100.0000, content=67.2766, keywords=98.8983, match=95.5224, GT shape={'rows': 18, 'cols': 5}, Pred shape={'rows': 18, 'cols': 5}
- primary GT table 1 -> Pred table 1: pair=90.9477, structure=96.8254, content=82.1311, keywords=87.7733, match=90.5360, GT shape={'rows': 20, 'cols': 5}, Pred shape={'rows': 21, 'cols': 5}
- primary GT table 2 -> Pred table 2: pair=93.7204, structure=95.5556, content=90.9677, keywords=90.3333, match=92.3939, GT shape={'rows': 14, 'cols': 5}, Pred shape={'rows': 15, 'cols': 5}
- primary GT table 3 -> Pred table 3: pair=93.3914, structure=97.2222, content=87.6452, keywords=84.8983, match=89.9110, GT shape={'rows': 23, 'cols': 7}, Pred shape={'rows': 24, 'cols': 7}
- primary GT table 4 -> Pred table 4: pair=82.1698, structure=91.6667, content=67.9245, keywords=72.0833, match=79.0259, GT shape={'rows': 7, 'cols': 5}, Pred shape={'rows': 8, 'cols': 5}
- primary GT table 5 -> Pred table 5: pair=83.1090, structure=93.3333, content=67.7725, keywords=72.0714, match=79.6351, GT shape={'rows': 9, 'cols': 4}, Pred shape={'rows': 10, 'cols': 4}
- primary GT table 6 -> Pred table 6: pair=93.5494, structure=96.2963, content=89.4292, keywords=87.6720, match=91.1601, GT shape={'rows': 17, 'cols': 4}, Pred shape={'rows': 18, 'cols': 4}
- primary GT table 7 -> Pred table 7: pair=88.5742, structure=94.8718, content=79.1277, keywords=83.2018, match=87.1475, GT shape={'rows': 12, 'cols': 4}, Pred shape={'rows': 13, 'cols': 4}
- primary GT table 8 -> Pred table 8: pair=89.4795, structure=95.5556, content=80.3653, keywords=89.6053, match=90.7576, GT shape={'rows': 14, 'cols': 4}, Pred shape={'rows': 15, 'cols': 4}
- primary GT table 9 -> Pred table 9: pair=86.0526, structure=91.6667, content=77.6316, keywords=79.8095, match=84.0539, GT shape={'rows': 7, 'cols': 4}, Pred shape={'rows': 8, 'cols': 4}
- primary GT table 10 -> Pred table 10: pair=79.8030, structure=100.0000, content=49.5074, keywords=100.0000, match=93.9409, GT shape={'rows': 11, 'cols': 3}, Pred shape={'rows': 11, 'cols': 3}
- primary GT table 11 -> Pred table 11: pair=78.6323, structure=90.4762, content=60.8665, keywords=97.4805, match=90.4252, GT shape={'rows': 21, 'cols': 5}, Pred shape={'rows': 18, 'cols': 5}
- primary GT table 12 -> Pred table 12: pair=61.3118, structure=71.0145, content=46.7577, keywords=100.0000, match=82.5964, GT shape={'rows': 23, 'cols': 5}, Pred shape={'rows': 13, 'cols': 5}
- primary GT table 13 -> Pred table 13: pair=81.8267, structure=94.4444, content=62.9002, keywords=83.9394, match=85.4066, GT shape={'rows': 11, 'cols': 10}, Pred shape={'rows': 12, 'cols': 10}
- primary GT table 14 -> Pred table 14: pair=84.7318, structure=93.3030, content=71.8750, keywords=95.6250, match=91.8926, GT shape={'rows': 10, 'cols': 10}, Pred shape={'rows': 9, 'cols': 11}
- primary GT table 15 -> Pred table 15: pair=72.1621, structure=86.6667, content=50.4052, keywords=89.7159, match=83.8399, GT shape={'rows': 4, 'cols': 9}, Pred shape={'rows': 5, 'cols': 9}
- primary GT table 16 -> Pred table 16: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 5, 'cols': 5}, Pred shape={'rows': 5, 'cols': 5}
- primary GT table 17 -> Pred table 17: pair=97.7186, structure=100.0000, content=94.2966, keywords=100.0000, match=99.3156, GT shape={'rows': 7, 'cols': 5}, Pred shape={'rows': 7, 'cols': 5}
- primary GT table 18 -> Pred table 18: pair=82.7097, structure=86.6667, content=76.7742, keywords=91.8548, match=88.0737, GT shape={'rows': 5, 'cols': 4}, Pred shape={'rows': 4, 'cols': 4}
- primary GT table 19 -> Pred table 19: pair=94.5122, structure=91.6667, content=98.7805, keywords=100.0000, match=96.6870, GT shape={'rows': 7, 'cols': 2}, Pred shape={'rows': 8, 'cols': 2}
- primary GT table 20 -> Pred table 20: pair=82.5991, structure=86.6667, content=76.4977, keywords=100.0000, match=92.1131, GT shape={'rows': 32, 'cols': 5}, Pred shape={'rows': 32, 'cols': 4}
- primary GT table 21 -> Pred table 21: pair=85.4477, structure=87.5000, content=82.3691, keywords=97.5000, match=91.8843, GT shape={'rows': 16, 'cols': 4}, Pred shape={'rows': 13, 'cols': 4}
- alt GT table 22 -> Pred table 22: pair=96.3584, structure=96.2963, content=96.4516, keywords=96.8182, match=96.5759, GT shape={'rows': 36, 'cols': 5}, Pred shape={'rows': 34, 'cols': 5}
- alt GT table 23 -> Pred table 23: pair=94.7000, structure=93.9394, content=95.8409, keywords=97.2106, match=95.8032, GT shape={'rows': 20, 'cols': 4}, Pred shape={'rows': 22, 'cols': 4}
- alt GT table 24 -> Pred table 24: pair=88.7743, structure=96.4912, content=77.1990, keywords=89.6987, match=90.7799, GT shape={'rows': 19, 'cols': 12}, Pred shape={'rows': 18, 'cols': 12}
- alt GT table 25 -> Pred table 25: pair=93.6370, structure=96.8254, content=88.8545, keywords=89.3712, match=92.1418, GT shape={'rows': 21, 'cols': 12}, Pred shape={'rows': 20, 'cols': 12}
- primary GT table 24 -> Pred table 26: pair=96.5090, structure=100.0000, content=91.2724, keywords=100.0000, match=98.9527, GT shape={'rows': 37, 'cols': 4}, Pred shape={'rows': 37, 'cols': 4}
- primary GT table 25 -> Pred table 27: pair=99.5376, structure=100.0000, content=98.8439, keywords=100.0000, match=99.8613, GT shape={'rows': 15, 'cols': 3}, Pred shape={'rows': 15, 'cols': 3}
- primary GT table 26 -> Pred table 28: pair=86.9968, structure=85.1852, content=89.7143, keywords=97.9688, match=92.1205, GT shape={'rows': 9, 'cols': 3}, Pred shape={'rows': 7, 'cols': 3}
- primary GT table 27 -> Pred table 29: pair=96.0000, structure=93.6508, content=99.5238, keywords=100.0000, match=97.5302, GT shape={'rows': 21, 'cols': 3}, Pred shape={'rows': 19, 'cols': 3}

## Title Layout Evaluation
- GT raw heading levels: `[1, 1, 1, 1, 1, 2, 2, 3, 4, 4, 3, 4, 4, 3, 4, 4, 3, 4, 4, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 2, 2, 3, 3, 3, 3, 3, 3, 1, 2, 3, 2, 1, 2, 2, 2, 1, 1, 2, 3, 3, 3, 2, 2, 3, 1, 2, 1, 2, 2, 3, 3, 3, 2, 2, 2, 2, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 4, 4, 3, 4, 3, 3, 3, 3, 3, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4] ... (133 total)`
- Pred raw heading levels: `[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3] ... (131 total)`
- GT relative heading levels: `[1, 1, 1, 1, 1, 2, 2, 3, 4, 4, 3, 4, 4, 3, 4, 4, 3, 4, 4, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 2, 2, 3, 3, 3, 3, 3, 3, 1, 2, 3, 2, 1, 2, 2, 2, 1, 1, 2, 3, 3, 3, 2, 2, 3, 1, 2, 1, 2, 2, 3, 3, 3, 2, 2, 2, 2, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 4, 4, 3, 4, 3, 3, 3, 3, 3, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4] ... (133 total)`
- Pred relative heading levels: `[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3] ... (131 total)`
- Title layout score: 88.5653
- Heading F1 score: 89.3939
- Level accuracy score: 81.7797
- Order score: 88.7218
- Main penalties:
  - 78 aligned headings have different relative levels.
  - 15 GT headings are missing.
  - 13 predicted headings are extra.

## Text Evaluation
- Text mode: normalized_full_text_preserve_newlines
- Text score: 97.7681
- Body-only text score: 97.7681
- Chart score used by text module: 100.0000
- Average edit distance: 0.0223
- Matched / missing / extra blocks: 1 / 0 / 0
- GT / Pred block counts: 1 / 1

### Worst Match Samples
1. op=match, distance=0.0223, GT blocks 0+1, Pred blocks 0+1
   - GT: ![]\n目录\n\n4管理层讨论与分析\n25董事及首席执行官\n29权益披露\n34股权激励计划\n38购买出售或回购本公司上市证券\n39其他信息\n42释义\n44财务报表\n\n不同投票权\n\n我们只有单一类别的股份每一股份对应一份表决权。然而根据《公司章程》,...
   - Pred: ![]\n阿里巴巴集团控股有限公司\n\n纽交所代码:BABA港交所代号:9988(港币柜台)89988(人民币柜台)\n\n2026财务年度中期报告\n\n目录\n\n4管理层讨论与分析\n\n25董事及首席执行官\n\n29权益披露\n\n34股权激励计划\n\n38购...

## Notes
- Table score compares extracted HTML and Markdown pipe tables after conversion to cell matrices.
- Table matching is Pred-driven semantic one-to-one: structure and header/row-label keywords select the highest-confidence unused GT candidate.
- Footprint aggregation weights each GT table by sqrt(expanded grid slots x normalized cell characters); unmatched GT footprint receives zero and unmatched Pred footprint enlarges the denominator.
- Content-aware module weighting reserves the configured title-layout share, then splits the remaining score budget between tables and text using Gold semantic tokens plus one structural unit per logical table grid slot.
- With max and two GT files, each predicted table keeps the higher pair score from the two independently one-to-one-matched GT variants.
- A chart-embedded table may match only a Gold table marked as chart-table; once routed, that payload is removed from chart scoring to prevent duplicate credit.
- Table pair score is 60% structure score and 40% content score; table content score uses exact normalized Levenshtein distance on complete flattened table text.
- Title layout score uses heading text only for anchor alignment, then combines heading F1, relative-level accuracy, and order coverage.
- Text score removes tables, keeps heading words, preserves newlines, and scores the full body as one character sequence.
- With score_charts=off, marked chart transcriptions are removed symmetrically before table extraction, heading layout, and body scoring.
- No-value page headers and footers are removed from prediction Markdown only; GT Markdown is kept as the reference answer.
- Current limitations: complex nested tables, heavily malformed HTML, and table semantic equivalence beyond cell text are only approximated.
