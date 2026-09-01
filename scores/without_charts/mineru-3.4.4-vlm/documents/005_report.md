# Financial Markdown Scoring Report

## Overall
- Final Score: 90.3098
- Table Score: 96.5892
- Title Layout Score: 71.6760
- Text Score: 94.1195

## Prediction Cleanup
- Mode: prediction_only_header_footer_cleanup
- Removed pred header/footer lines: 0
- Removed examples:
  - None

## Weights
- Mode: gt_content_information_share
- Table: 27.49%
- Title Layout: 20.00%
- Text: 52.51%
- GT table semantic tokens / grid slots / information units: 29953 / 10988 / 40941
- GT body / active chart / text information units: 78195 / 0 / 78195

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
- Detected primary GT / Pred chart blocks: 21 / 20
- Representation-neutral chart score: 57.5681
- GT chart token share inside text module: 0.0230
- Removed primary GT / alt GT / Pred chart blocks: 21 / 21 / 20

## Table Evaluation
- Table GT strategy result: per_table_max
- Primary table score: 77.7064
- Alt table score: 95.9427
- Per-table rule: each predicted table keeps its higher one-to-one pair score from primary or alt GT.
- Per-table selected primary / alt pairs: 166 / 25
- Per-table reference table count: 178
- Matched / missing / extra tables: 191 / 0 / 1
- Table content score: 95.4906
- Table structure score: 97.3215
- Table matrix score: 96.5892
- Table alignment strategy: per_table_best_of_primary_alt_gt_footprint_weighted
- GT footprint total / extra Pred footprint: 25868.0877 / 33.3167
- Chart-table eligible / auxiliary / matched: 0 / 17 / 0

### Table Matches
- primary GT table 0 -> Pred table 0: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 37, 'cols': 3}, Pred shape={'rows': 37, 'cols': 3}
- primary GT table 1 -> Pred table 1: pair=97.6923, structure=100.0000, content=94.2308, keywords=93.0000, match=95.8077, GT shape={'rows': 6, 'cols': 5}, Pred shape={'rows': 6, 'cols': 5}
- primary GT table 2 -> Pred table 2: pair=97.7695, structure=100.0000, content=94.4238, keywords=95.0000, match=96.8308, GT shape={'rows': 6, 'cols': 5}, Pred shape={'rows': 6, 'cols': 5}
- primary GT table 3 -> Pred table 3: pair=97.3742, structure=100.0000, content=93.4354, keywords=96.1111, match=97.2678, GT shape={'rows': 11, 'cols': 5}, Pred shape={'rows': 11, 'cols': 5}
- primary GT table 4 -> Pred table 4: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 7, 'cols': 3}, Pred shape={'rows': 7, 'cols': 3}
- primary GT table 5 -> Pred table 5: pair=99.9306, structure=100.0000, content=99.8264, keywords=100.0000, match=99.9792, GT shape={'rows': 37, 'cols': 4}, Pred shape={'rows': 37, 'cols': 4}
- primary GT table 6 -> Pred table 6: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 7, 'cols': 4}, Pred shape={'rows': 7, 'cols': 4}
- primary GT table 7 -> Pred table 8: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 5, 'cols': 3}, Pred shape={'rows': 5, 'cols': 3}
- primary GT table 8 -> Pred table 9: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 5, 'cols': 3}, Pred shape={'rows': 5, 'cols': 3}
- primary GT table 9 -> Pred table 10: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 6, 'cols': 2}, Pred shape={'rows': 6, 'cols': 2}
- primary GT table 10 -> Pred table 11: pair=86.3838, structure=85.1852, content=88.1818, keywords=100.0000, match=92.9522, GT shape={'rows': 7, 'cols': 4}, Pred shape={'rows': 9, 'cols': 4}
- primary GT table 11 -> Pred table 12: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 11, 'cols': 8}, Pred shape={'rows': 11, 'cols': 8}
- primary GT table 12 -> Pred table 13: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 11, 'cols': 8}, Pred shape={'rows': 11, 'cols': 8}
- primary GT table 13 -> Pred table 14: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 8, 'cols': 4}, Pred shape={'rows': 8, 'cols': 4}
- primary GT table 14 -> Pred table 15: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 8, 'cols': 4}, Pred shape={'rows': 8, 'cols': 4}
- primary GT table 15 -> Pred table 16: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 8, 'cols': 4}, Pred shape={'rows': 8, 'cols': 4}
- primary GT table 16 -> Pred table 17: pair=99.6413, structure=100.0000, content=99.1031, keywords=100.0000, match=99.8924, GT shape={'rows': 5, 'cols': 5}, Pred shape={'rows': 5, 'cols': 5}
- primary GT table 17 -> Pred table 18: pair=99.8419, structure=100.0000, content=99.6047, keywords=100.0000, match=99.9526, GT shape={'rows': 11, 'cols': 5}, Pred shape={'rows': 11, 'cols': 5}
- primary GT table 18 -> Pred table 19: pair=87.6613, structure=91.6667, content=81.6532, keywords=94.8810, match=92.0722, GT shape={'rows': 14, 'cols': 4}, Pred shape={'rows': 16, 'cols': 4}
- primary GT table 19 -> Pred table 20: pair=92.9713, structure=94.8718, content=90.1205, keywords=97.9412, match=95.8363, GT shape={'rows': 12, 'cols': 4}, Pred shape={'rows': 13, 'cols': 4}
- primary GT table 20 -> Pred table 21: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 4, 'cols': 4}, Pred shape={'rows': 4, 'cols': 4}
- primary GT table 21 -> Pred table 22: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 16, 'cols': 4}, Pred shape={'rows': 16, 'cols': 4}
- primary GT table 22 -> Pred table 23: pair=95.5647, structure=94.4444, content=97.2452, keywords=100.0000, match=97.5583, GT shape={'rows': 11, 'cols': 4}, Pred shape={'rows': 12, 'cols': 4}
- primary GT table 23 -> Pred table 24: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 7, 'cols': 7}, Pred shape={'rows': 7, 'cols': 7}
- primary GT table 24 -> Pred table 25: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 4, 'cols': 3}, Pred shape={'rows': 4, 'cols': 3}
- primary GT table 25 -> Pred table 26: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 4, 'cols': 3}, Pred shape={'rows': 4, 'cols': 3}
- primary GT table 26 -> Pred table 27: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 17, 'cols': 3}, Pred shape={'rows': 17, 'cols': 3}
- primary GT table 27 -> Pred table 28: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 9, 'cols': 3}, Pred shape={'rows': 9, 'cols': 3}
- primary GT table 28 -> Pred table 29: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 8, 'cols': 3}, Pred shape={'rows': 8, 'cols': 3}
- primary GT table 29 -> Pred table 30: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 10, 'cols': 4}, Pred shape={'rows': 10, 'cols': 4}

## Title Layout Evaluation
- GT raw heading levels: `[1, 1, 1, 2, 2, 2, 3, 2, 3, 1, 2, 3, 3, 3, 3, 3, 4, 4, 5, 6, 5, 6, 6, 5, 2, 3, 3, 4, 5, 5, 4, 4, 3, 2, 3, 4, 4, 3, 4, 4, 4, 4, 4, 4, 4, 3, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 4, 3, 4, 4, 4, 4, 4, 4, 4, 4, 3, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 4, 2, 3, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 4, 4, 4, 3, 2, 3, 3, 3, 3, 3, 3, 3, 2, 3, 4, 4, 4, 5, 5, 5, 4, 4, 3, 4, 5, 4, 4, 4] ... (304 total)`
- Pred raw heading levels: `[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] ... (478 total)`
- GT relative heading levels: `[1, 1, 1, 2, 2, 2, 3, 2, 3, 1, 2, 3, 3, 3, 3, 3, 4, 4, 5, 6, 5, 6, 6, 5, 2, 3, 3, 4, 5, 5, 4, 4, 3, 2, 3, 4, 4, 3, 4, 4, 4, 4, 4, 4, 4, 3, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 4, 3, 4, 4, 4, 4, 4, 4, 4, 4, 3, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 4, 2, 3, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 4, 4, 4, 3, 2, 3, 3, 3, 3, 3, 3, 3, 2, 3, 4, 4, 4, 5, 5, 5, 4, 4, 3, 4, 5, 4, 4, 4] ... (304 total)`
- Pred relative heading levels: `[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] ... (478 total)`
- Title layout score: 71.6760
- Heading F1 score: 76.2148
- Level accuracy score: 44.6980
- Order score: 62.3431
- Main penalties:
  - 293 aligned headings have different relative levels.
  - 6 GT headings are missing.
  - 180 predicted headings are extra.

## Text Evaluation
- Text mode: normalized_full_text_preserve_newlines
- Text score: 94.1195
- Body-only text score: 94.1195
- Chart score used by text module: 57.5681
- Average edit distance: 0.0588
- Matched / missing / extra blocks: 1 / 0 / 0
- GT / Pred block counts: 1 / 1

### Worst Match Samples
1. op=match, distance=0.0588, GT blocks 0+1, Pred blocks 0+1
   - GT: ![]\n二零二三年中报\n\n目录\n\n关于我们\n\n1重要提示及释义\n2公司概览\n5董事长致辞\n8财务摘要\n\n经营情况讨论及分析\n\n10综合金融\n14以医疗健康打造价值增长新引擎\n16主要业务经营分析\n16业绩综述\n20寿险及健康险业务\n26...
   - Pred: ![]\n关于我们\n\n1重要提示及释义\n2公司概览\n5董事长致辞\n8财务摘要\n\n经营情况讨论及分析\n\n10综合金融\n14以医疗健康打造价值增长新引擎\n16主要业务经营分析\n16业绩综述\n20寿险及健康险业务\n26财产保险业务\n30保险资金投资组...

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
