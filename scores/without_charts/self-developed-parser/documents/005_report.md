# Financial Markdown Scoring Report

## Overall
- Final Score: 92.6312
- Table Score: 92.7836
- Title Layout Score: 83.8596
- Text Score: 95.8924

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
- Detected primary GT / Pred chart blocks: 21 / 0
- Representation-neutral chart score: 0.0000
- GT chart token share inside text module: 0.0230
- Removed primary GT / alt GT / Pred chart blocks: 21 / 21 / 0

## Table Evaluation
- Table GT strategy result: per_table_max
- Primary table score: 75.0586
- Alt table score: 91.6357
- Per-table rule: each predicted table keeps its higher one-to-one pair score from primary or alt GT.
- Per-table selected primary / alt pairs: 160 / 24
- Per-table reference table count: 178
- Matched / missing / extra tables: 184 / 0 / 3
- Table content score: 88.9274
- Table structure score: 95.3544
- Table matrix score: 92.7836
- Table alignment strategy: per_table_best_of_primary_alt_gt_footprint_weighted
- GT footprint total / extra Pred footprint: 25868.0877 / 85.6627
- Chart-table eligible / auxiliary / matched: 0 / 0 / 0

### Table Matches
- primary GT table 0 -> Pred table 0: pair=99.1185, structure=100.0000, content=97.7961, keywords=90.4324, match=94.9518, GT shape={'rows': 37, 'cols': 3}, Pred shape={'rows': 37, 'cols': 3}
- primary GT table 1 -> Pred table 1: pair=94.7410, structure=100.0000, content=86.8526, keywords=91.0882, match=93.9664, GT shape={'rows': 6, 'cols': 5}, Pred shape={'rows': 6, 'cols': 5}
- primary GT table 2 -> Pred table 2: pair=89.0529, structure=88.8889, content=89.2989, keywords=93.9167, match=91.4520, GT shape={'rows': 6, 'cols': 5}, Pred shape={'rows': 6, 'cols': 6}
- primary GT table 3 -> Pred table 4: pair=74.0531, structure=81.1111, content=63.4660, keywords=75.7131, match=76.2947, GT shape={'rows': 11, 'cols': 5}, Pred shape={'rows': 8, 'cols': 6}
- primary GT table 4 -> Pred table 5: pair=90.0000, structure=83.3333, content=100.0000, keywords=100.0000, match=93.6667, GT shape={'rows': 7, 'cols': 3}, Pred shape={'rows': 7, 'cols': 4}
- primary GT table 5 -> Pred table 6: pair=94.4054, structure=100.0000, content=86.0135, keywords=100.0000, match=98.3216, GT shape={'rows': 37, 'cols': 4}, Pred shape={'rows': 37, 'cols': 4}
- primary GT table 6 -> Pred table 7: pair=89.7479, structure=100.0000, content=74.3697, keywords=100.0000, match=96.9244, GT shape={'rows': 7, 'cols': 4}, Pred shape={'rows': 7, 'cols': 4}
- primary GT table 7 -> Pred table 8: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 5, 'cols': 3}, Pred shape={'rows': 5, 'cols': 3}
- primary GT table 8 -> Pred table 9: pair=99.0244, structure=100.0000, content=97.5610, keywords=92.9688, match=96.1917, GT shape={'rows': 5, 'cols': 3}, Pred shape={'rows': 5, 'cols': 3}
- primary GT table 9 -> Pred table 10: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 6, 'cols': 2}, Pred shape={'rows': 6, 'cols': 2}
- primary GT table 10 -> Pred table 11: pair=86.2242, structure=85.1852, content=87.7828, keywords=100.0000, match=92.9043, GT shape={'rows': 7, 'cols': 4}, Pred shape={'rows': 9, 'cols': 4}
- primary GT table 11 -> Pred table 12: pair=97.6909, structure=100.0000, content=94.2272, keywords=100.0000, match=99.3073, GT shape={'rows': 11, 'cols': 8}, Pred shape={'rows': 11, 'cols': 8}
- primary GT table 12 -> Pred table 13: pair=97.8322, structure=100.0000, content=94.5804, keywords=100.0000, match=99.3497, GT shape={'rows': 11, 'cols': 8}, Pred shape={'rows': 11, 'cols': 8}
- primary GT table 13 -> Pred table 14: pair=99.8198, structure=100.0000, content=99.5495, keywords=100.0000, match=99.9459, GT shape={'rows': 8, 'cols': 4}, Pred shape={'rows': 8, 'cols': 4}
- primary GT table 14 -> Pred table 15: pair=85.2420, structure=86.6667, content=83.1050, keywords=100.0000, match=92.9059, GT shape={'rows': 8, 'cols': 4}, Pred shape={'rows': 8, 'cols': 5}
- primary GT table 64 -> Pred table 16: pair=94.7490, structure=100.0000, content=86.8726, keywords=100.0000, match=98.4247, GT shape={'rows': 8, 'cols': 4}, Pred shape={'rows': 8, 'cols': 4}
- primary GT table 16 -> Pred table 17: pair=98.9427, structure=100.0000, content=97.3568, keywords=100.0000, match=99.6828, GT shape={'rows': 5, 'cols': 5}, Pred shape={'rows': 5, 'cols': 5}
- primary GT table 17 -> Pred table 18: pair=99.5294, structure=100.0000, content=98.8235, keywords=100.0000, match=99.8588, GT shape={'rows': 11, 'cols': 5}, Pred shape={'rows': 11, 'cols': 5}
- primary GT table 18 -> Pred table 19: pair=92.9921, structure=100.0000, content=82.4803, keywords=99.1096, match=97.4524, GT shape={'rows': 14, 'cols': 4}, Pred shape={'rows': 14, 'cols': 4}
- primary GT table 19 -> Pred table 20: pair=87.3173, structure=94.4444, content=76.6265, keywords=100.0000, match=95.0841, GT shape={'rows': 12, 'cols': 4}, Pred shape={'rows': 11, 'cols': 4}
- primary GT table 20 -> Pred table 22: pair=87.2727, structure=100.0000, content=68.1818, keywords=94.1667, match=93.2652, GT shape={'rows': 4, 'cols': 4}, Pred shape={'rows': 4, 'cols': 4}
- primary GT table 21 -> Pred table 23: pair=98.6583, structure=100.0000, content=96.6457, keywords=100.0000, match=99.5975, GT shape={'rows': 16, 'cols': 4}, Pred shape={'rows': 16, 'cols': 4}
- primary GT table 22 -> Pred table 24: pair=93.6314, structure=94.4444, content=92.4119, keywords=100.0000, match=96.9783, GT shape={'rows': 11, 'cols': 4}, Pred shape={'rows': 12, 'cols': 4}
- primary GT table 23 -> Pred table 25: pair=98.9888, structure=100.0000, content=97.4719, keywords=100.0000, match=99.6966, GT shape={'rows': 7, 'cols': 7}, Pred shape={'rows': 7, 'cols': 7}
- primary GT table 24 -> Pred table 26: pair=99.5876, structure=100.0000, content=98.9691, keywords=100.0000, match=99.8763, GT shape={'rows': 4, 'cols': 3}, Pred shape={'rows': 4, 'cols': 3}
- primary GT table 25 -> Pred table 27: pair=99.5745, structure=100.0000, content=98.9362, keywords=100.0000, match=99.8723, GT shape={'rows': 4, 'cols': 3}, Pred shape={'rows': 4, 'cols': 3}
- primary GT table 26 -> Pred table 28: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 17, 'cols': 3}, Pred shape={'rows': 17, 'cols': 3}
- primary GT table 27 -> Pred table 29: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 9, 'cols': 3}, Pred shape={'rows': 9, 'cols': 3}
- primary GT table 28 -> Pred table 30: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 8, 'cols': 3}, Pred shape={'rows': 8, 'cols': 3}
- primary GT table 29 -> Pred table 31: pair=77.0621, structure=77.7778, content=75.9887, keywords=92.0282, match=84.6883, GT shape={'rows': 10, 'cols': 4}, Pred shape={'rows': 15, 'cols': 4}

## Title Layout Evaluation
- GT raw heading levels: `[1, 1, 1, 2, 2, 2, 3, 2, 3, 1, 2, 3, 3, 3, 3, 3, 4, 4, 5, 6, 5, 6, 6, 5, 2, 3, 3, 4, 5, 5, 4, 4, 3, 2, 3, 4, 4, 3, 4, 4, 4, 4, 4, 4, 4, 3, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 4, 3, 4, 4, 4, 4, 4, 4, 4, 4, 3, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 4, 2, 3, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 4, 4, 4, 3, 2, 3, 3, 3, 3, 3, 3, 3, 2, 3, 4, 4, 4, 5, 5, 5, 4, 4, 3, 4, 5, 4, 4, 4] ... (304 total)`
- Pred raw heading levels: `[2, 2, 2, 3, 3, 3, 3, 3, 4, 2, 2, 2, 2, 2, 3, 2, 2, 3, 2, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 1, 2, 3, 2, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 2, 3, 3] ... (374 total)`
- GT relative heading levels: `[1, 1, 1, 2, 2, 2, 3, 2, 3, 1, 2, 3, 3, 3, 3, 3, 4, 4, 5, 6, 5, 6, 6, 5, 2, 3, 3, 4, 5, 5, 4, 4, 3, 2, 3, 4, 4, 3, 4, 4, 4, 4, 4, 4, 4, 3, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, 4, 3, 4, 4, 4, 4, 4, 4, 4, 4, 3, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 4, 2, 3, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 4, 4, 4, 3, 2, 3, 3, 3, 3, 3, 3, 3, 2, 3, 4, 4, 4, 5, 5, 5, 4, 4, 3, 4, 5, 4, 4, 4] ... (304 total)`
- Pred relative heading levels: `[2, 2, 2, 3, 3, 3, 3, 3, 4, 2, 2, 2, 2, 2, 3, 2, 2, 3, 2, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 1, 2, 3, 2, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 2, 3, 3] ... (374 total)`
- Title layout score: 83.8596
- Heading F1 score: 84.9558
- Level accuracy score: 81.9444
- Order score: 77.0053
- Main penalties:
  - 186 aligned headings have different relative levels.
  - 16 GT headings are missing.
  - 86 predicted headings are extra.

## Text Evaluation
- Text mode: normalized_full_text_preserve_newlines
- Text score: 95.8924
- Body-only text score: 95.8924
- Chart score used by text module: 0.0000
- Average edit distance: 0.0411
- Matched / missing / extra blocks: 1 / 0 / 0
- GT / Pred block counts: 1 / 1

### Worst Match Samples
1. op=match, distance=0.0411, GT blocks 0+1, Pred blocks 0+1
   - GT: ![]\n二零二三年中报\n\n目录\n\n关于我们\n\n1重要提示及释义\n2公司概览\n5董事长致辞\n8财务摘要\n\n经营情况讨论及分析\n\n10综合金融\n14以医疗健康打造价值增长新引擎\n16主要业务经营分析\n16业绩综述\n20寿险及健康险业务\n26...
   - Pred: 中国平安PINGAN专业·价值\n\nth351988-2023中国平安成立35周年\n\n专业让生活更简单\n![]\n二零二三年中报\n\n目录\n\n关于我们\n\n重要提示及释义\n公司概览\n董事长致辞\n财务摘要\n\n经营情况讨论及分析\n\n10综合金融\n...

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
