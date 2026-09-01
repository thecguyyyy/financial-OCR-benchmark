# Financial Markdown Scoring Report

## Overall
- Final Score: 87.2301
- Table Score: 88.4493
- Title Layout Score: 75.7551
- Text Score: 90.9426

## Prediction Cleanup
- Mode: prediction_only_header_footer_cleanup
- Removed pred header/footer lines: 0
- Removed examples:
  - None

## Weights
- Mode: gt_content_information_share
- Table: 27.07%
- Title Layout: 20.00%
- Text: 52.93%
- GT table semantic tokens / grid slots / information units: 29953 / 10988 / 40941
- GT body / active chart / text information units: 78195 / 1841 / 80036

## Configuration
- Remove pred header/footer: False
- Normalize images: True
- Score informative charts: True
- Normalize Chinese variants: t2s
- Normalize footnotes: True
- Normalize punctuation: True
- Table pair weights: structure=0.6, content=0.4
- Table aggregation: footprint
- Module weighting: content
- Title layout reserve: 0.2
- Chart scoring mode: included_as_order_aware_numeric_first_token_score
- Detected primary GT / Pred chart blocks: 21 / 0
- Representation-neutral chart score: 0.0000
- GT chart token share inside text module: 0.0230
- Removed primary GT / alt GT / Pred chart blocks: 0 / 0 / 0

## Table Evaluation
- Table GT strategy result: per_table_max
- Primary table score: 72.6802
- Alt table score: 85.9154
- Per-table rule: each predicted table keeps its higher one-to-one pair score from primary or alt GT.
- Per-table selected primary / alt pairs: 160 / 21
- Per-table reference table count: 178
- Matched / missing / extra tables: 181 / 0 / 1
- Table content score: 84.5103
- Table structure score: 91.0752
- Table matrix score: 88.4493
- Table alignment strategy: per_table_best_of_primary_alt_gt_footprint_weighted
- GT footprint total / extra Pred footprint: 25868.0877 / 37.6962
- Chart-table eligible / auxiliary / matched: 0 / 0 / 0

### Table Matches
- primary GT table 0 -> Pred table 0: pair=80.2488, structure=77.7778, content=83.9552, keywords=52.3270, match=65.7937, GT shape={'rows': 37, 'cols': 3}, Pred shape={'rows': 37, 'cols': 2}
- primary GT table 1 -> Pred table 1: pair=97.9845, structure=100.0000, content=94.9612, keywords=96.2857, match=97.5382, GT shape={'rows': 6, 'cols': 5}, Pred shape={'rows': 6, 'cols': 5}
- primary GT table 2 -> Pred table 2: pair=97.0079, structure=100.0000, content=92.5197, keywords=97.8333, match=98.0190, GT shape={'rows': 6, 'cols': 5}, Pred shape={'rows': 6, 'cols': 5}
- primary GT table 3 -> Pred table 3: pair=91.1065, structure=94.4444, content=86.0996, keywords=93.7037, match=93.0727, GT shape={'rows': 11, 'cols': 5}, Pred shape={'rows': 12, 'cols': 5}
- primary GT table 4 -> Pred table 4: pair=84.6296, structure=91.6667, content=74.0741, keywords=88.3333, match=87.8889, GT shape={'rows': 7, 'cols': 3}, Pred shape={'rows': 8, 'cols': 3}
- primary GT table 5 -> Pred table 5: pair=97.6711, structure=98.1982, content=96.8804, keywords=97.8635, match=97.8727, GT shape={'rows': 37, 'cols': 4}, Pred shape={'rows': 36, 'cols': 4}
- primary GT table 6 -> Pred table 6: pair=77.7444, structure=100.0000, content=44.3609, keywords=93.2759, match=89.9613, GT shape={'rows': 7, 'cols': 4}, Pred shape={'rows': 7, 'cols': 4}
- primary GT table 7 -> Pred table 7: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 5, 'cols': 3}, Pred shape={'rows': 5, 'cols': 3}
- primary GT table 8 -> Pred table 8: pair=99.3443, structure=100.0000, content=98.3607, keywords=100.0000, match=99.8033, GT shape={'rows': 5, 'cols': 3}, Pred shape={'rows': 5, 'cols': 3}
- primary GT table 9 -> Pred table 9: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 6, 'cols': 2}, Pred shape={'rows': 6, 'cols': 2}
- primary GT table 10 -> Pred table 10: pair=86.2242, structure=85.1852, content=87.7828, keywords=100.0000, match=92.9043, GT shape={'rows': 7, 'cols': 4}, Pred shape={'rows': 9, 'cols': 4}
- primary GT table 11 -> Pred table 11: pair=95.9032, structure=100.0000, content=89.7579, keywords=99.2935, match=98.4177, GT shape={'rows': 11, 'cols': 8}, Pred shape={'rows': 11, 'cols': 8}
- primary GT table 12 -> Pred table 12: pair=86.2238, structure=93.9394, content=74.6503, keywords=93.6364, match=91.4732, GT shape={'rows': 11, 'cols': 8}, Pred shape={'rows': 10, 'cols': 8}
- primary GT table 13 -> Pred table 13: pair=89.8198, structure=83.3333, content=99.5495, keywords=95.0000, match=91.1126, GT shape={'rows': 8, 'cols': 4}, Pred shape={'rows': 8, 'cols': 3}
- primary GT table 63 -> Pred table 14: pair=63.7874, structure=47.3380, content=88.4615, keywords=74.2222, match=65.7149, GT shape={'rows': 8, 'cols': 4}, Pred shape={'rows': 9, 'cols': 1}
- primary GT table 15 -> Pred table 15: pair=87.9310, structure=83.3333, content=94.8276, keywords=91.4524, match=88.7722, GT shape={'rows': 8, 'cols': 4}, Pred shape={'rows': 8, 'cols': 3}
- primary GT table 16 -> Pred table 16: pair=99.6413, structure=100.0000, content=99.1031, keywords=100.0000, match=99.8924, GT shape={'rows': 5, 'cols': 5}, Pred shape={'rows': 5, 'cols': 5}
- primary GT table 17 -> Pred table 17: pair=88.3004, structure=100.0000, content=70.7510, keywords=82.8675, match=87.9239, GT shape={'rows': 11, 'cols': 5}, Pred shape={'rows': 11, 'cols': 5}
- primary GT table 18 -> Pred table 18: pair=82.0161, structure=82.4561, content=81.3559, keywords=96.7763, match=89.4842, GT shape={'rows': 14, 'cols': 4}, Pred shape={'rows': 19, 'cols': 4}
- primary GT table 19 -> Pred table 19: pair=83.7533, structure=94.8718, content=67.0757, keywords=94.0514, match=91.1261, GT shape={'rows': 12, 'cols': 4}, Pred shape={'rows': 13, 'cols': 4}
- primary GT table 20 -> Pred table 20: pair=91.1209, structure=86.6667, content=97.8022, keywords=100.0000, match=94.6696, GT shape={'rows': 4, 'cols': 4}, Pred shape={'rows': 5, 'cols': 4}
- primary GT table 21 -> Pred table 21: pair=83.4056, structure=86.6667, content=78.5141, keywords=96.8182, match=90.7641, GT shape={'rows': 16, 'cols': 4}, Pred shape={'rows': 20, 'cols': 4}
- primary GT table 22 -> Pred table 22: pair=86.1108, structure=89.7436, content=80.6616, keywords=95.6250, match=91.5945, GT shape={'rows': 11, 'cols': 4}, Pred shape={'rows': 13, 'cols': 4}
- primary GT table 23 -> Pred table 23: pair=98.3146, structure=100.0000, content=95.7865, keywords=100.0000, match=99.4944, GT shape={'rows': 7, 'cols': 7}, Pred shape={'rows': 7, 'cols': 7}
- primary GT table 24 -> Pred table 24: pair=99.5876, structure=100.0000, content=98.9691, keywords=100.0000, match=99.8763, GT shape={'rows': 4, 'cols': 3}, Pred shape={'rows': 4, 'cols': 3}
- primary GT table 25 -> Pred table 25: pair=99.5745, structure=100.0000, content=98.9362, keywords=100.0000, match=99.8723, GT shape={'rows': 4, 'cols': 3}, Pred shape={'rows': 4, 'cols': 3}
- primary GT table 26 -> Pred table 26: pair=84.4809, structure=77.7778, content=94.5355, keywords=100.0000, match=90.8998, GT shape={'rows': 17, 'cols': 3}, Pred shape={'rows': 17, 'cols': 2}
- primary GT table 27 -> Pred table 27: pair=62.5180, structure=83.3333, content=31.2950, keywords=94.1667, match=82.5054, GT shape={'rows': 9, 'cols': 3}, Pred shape={'rows': 9, 'cols': 4}
- primary GT table 28 -> Pred table 28: pair=85.4545, structure=100.0000, content=63.6364, keywords=88.3333, match=89.8030, GT shape={'rows': 8, 'cols': 3}, Pred shape={'rows': 8, 'cols': 3}
- primary GT table 29 -> Pred table 29: pair=84.0415, structure=88.8889, content=76.7705, keywords=94.4699, match=90.2252, GT shape={'rows': 10, 'cols': 4}, Pred shape={'rows': 12, 'cols': 4}

## Title Layout Evaluation
- GT raw heading levels: `[1, 1, 1, 2, 2, 2, 3, 2, 3, 1, 2, 3, 3, 3, 3, 3, 4, 4, 5, 6, 5, 6, 6, 5, 2, 3, 3, 4, 5, 5, 4, 4, 3, 2, 3, 4, 4, 3, 4, 4, 4, 4, 4, 4, 4, 3, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 4, 3, 4, 4, 4, 4, 4, 4, 4, 4, 3, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 4, 2, 3, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 4, 4, 4, 3, 2, 3, 3, 3, 3, 3, 3, 3, 2, 3, 4, 4, 4, 5, 5, 5, 4, 4, 3, 4, 5, 4, 4, 4] ... (304 total)`
- Pred raw heading levels: `[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 1, 2, 1, 2, 2, 2, 1, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2] ... (457 total)`
- GT relative heading levels: `[1, 1, 1, 2, 2, 2, 3, 2, 3, 1, 2, 3, 3, 3, 3, 3, 4, 4, 5, 6, 5, 6, 6, 5, 2, 3, 3, 4, 5, 5, 4, 4, 3, 2, 3, 4, 4, 3, 4, 4, 4, 4, 4, 4, 4, 3, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 4, 3, 4, 4, 4, 4, 4, 4, 4, 4, 3, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 4, 2, 3, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 4, 4, 4, 3, 2, 3, 3, 3, 3, 3, 3, 3, 2, 3, 4, 4, 4, 5, 5, 5, 4, 4, 3, 4, 5, 4, 4, 4] ... (304 total)`
- Pred relative heading levels: `[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 1, 2, 1, 2, 2, 2, 1, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2] ... (457 total)`
- Title layout score: 75.7551
- Heading F1 score: 78.5808
- Level accuracy score: 63.4783
- Order score: 65.4267
- Main penalties:
  - 282 aligned headings have different relative levels.
  - 5 GT headings are missing.
  - 158 predicted headings are extra.

## Text Evaluation
- Text mode: body_edit_distance_plus_representation_neutral_chart_tokens
- Text score: 90.9426
- Body-only text score: 93.0837
- Chart score used by text module: 0.0000
- Average edit distance: 0.0692
- Matched / missing / extra blocks: 1 / 0 / 0
- GT / Pred block counts: 1 / 1

### Worst Match Samples
1. op=match, distance=0.0692, GT blocks 0+1, Pred blocks 0+1
   - GT: ![]\n二零二三年中报\n\n目录\n\n关于我们\n\n1重要提示及释义\n2公司概览\n5董事长致辞\n8财务摘要\n\n经营情况讨论及分析\n\n10综合金融\n14以医疗健康打造价值增长新引擎\n16主要业务经营分析\n16业绩综述\n20寿险及健康险业务\n26...
   - Pred: ![]\n目录\n\n关于我们\n\n重要提示及释义\n\n2公司概览\n\n5董事长致辞\n\n8财务摘要\n\n经营情况讨论及分析\n\n10综合金融\n\n14以医疗健康打造价值增长新引擎\n\n16主要业务经营分析\n\n16业绩综述\n\n20寿险及健康险业务\n...

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
