# Financial Markdown Scoring Report

## Overall
- Final Score: 93.3348
- Table Score: 87.5689
- Title Layout Score: 92.0599
- Text Score: 98.0747

## Prediction Cleanup
- Mode: prediction_only_header_footer_cleanup
- Removed pred header/footer lines: 0
- Removed examples:
  - None

## Weights
- Mode: gt_content_information_share
- Table: 33.67%
- Title Layout: 20.00%
- Text: 46.33%
- GT table semantic tokens / grid slots / information units: 31531 / 10479 / 42010
- GT body / active chart / text information units: 57817 / 0 / 57817

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
- Primary table score: 76.7653
- Alt table score: 86.5988
- Per-table rule: each predicted table keeps its higher one-to-one pair score from primary or alt GT.
- Per-table selected primary / alt pairs: 192 / 28
- Per-table reference table count: 210
- Matched / missing / extra tables: 220 / 0 / 16
- Table content score: 85.4220
- Table structure score: 89.0001
- Table matrix score: 87.5689
- Table alignment strategy: per_table_best_of_primary_alt_gt_footprint_weighted
- GT footprint total / extra Pred footprint: 26576.0262 / 1478.1415
- Chart-table eligible / auxiliary / matched: 0 / 0 / 0

### Table Matches
- primary GT table 0 -> Pred table 1: pair=98.9793, structure=100.0000, content=97.4482, keywords=100.0000, match=99.6938, GT shape={'rows': 21, 'cols': 3}, Pred shape={'rows': 21, 'cols': 3}
- primary GT table 1 -> Pred table 2: pair=99.6291, structure=100.0000, content=99.0726, keywords=100.0000, match=99.8887, GT shape={'rows': 13, 'cols': 4}, Pred shape={'rows': 13, 'cols': 4}
- primary GT table 2 -> Pred table 3: pair=99.0643, structure=100.0000, content=97.6608, keywords=100.0000, match=99.7193, GT shape={'rows': 6, 'cols': 3}, Pred shape={'rows': 6, 'cols': 3}
- primary GT table 3 -> Pred table 4: pair=99.4872, structure=100.0000, content=98.7179, keywords=100.0000, match=99.8462, GT shape={'rows': 3, 'cols': 2}, Pred shape={'rows': 3, 'cols': 2}
- primary GT table 4 -> Pred table 5: pair=79.7248, structure=83.3333, content=74.3119, keywords=81.4386, match=81.3034, GT shape={'rows': 3, 'cols': 2}, Pred shape={'rows': 4, 'cols': 2}
- primary GT table 5 -> Pred table 6: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 11, 'cols': 5}, Pred shape={'rows': 11, 'cols': 5}
- primary GT table 6 -> Pred table 7: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 5, 'cols': 4}, Pred shape={'rows': 5, 'cols': 4}
- primary GT table 7 -> Pred table 8: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 5, 'cols': 5}, Pred shape={'rows': 5, 'cols': 5}
- primary GT table 8 -> Pred table 9: pair=99.8427, structure=100.0000, content=99.6068, keywords=100.0000, match=99.9528, GT shape={'rows': 12, 'cols': 5}, Pred shape={'rows': 12, 'cols': 5}
- primary GT table 9 -> Pred table 10: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 5, 'cols': 3}, Pred shape={'rows': 5, 'cols': 3}
- primary GT table 10 -> Pred table 11: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 16, 'cols': 6}, Pred shape={'rows': 16, 'cols': 6}
- primary GT table 11 -> Pred table 12: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 14, 'cols': 7}, Pred shape={'rows': 14, 'cols': 7}
- primary GT table 12 -> Pred table 13: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 4, 'cols': 6}, Pred shape={'rows': 4, 'cols': 6}
- primary GT table 13 -> Pred table 14: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 4, 'cols': 7}, Pred shape={'rows': 4, 'cols': 7}
- primary GT table 14 -> Pred table 15: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 3, 'cols': 2}, Pred shape={'rows': 3, 'cols': 2}
- primary GT table 15 -> Pred table 16: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 7, 'cols': 4}, Pred shape={'rows': 7, 'cols': 4}
- primary GT table 16 -> Pred table 17: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 3, 'cols': 2}, Pred shape={'rows': 3, 'cols': 2}
- primary GT table 17 -> Pred table 18: pair=94.4286, structure=91.6667, content=98.5714, keywords=88.3333, match=90.8286, GT shape={'rows': 7, 'cols': 4}, Pred shape={'rows': 8, 'cols': 4}
- primary GT table 18 -> Pred table 19: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 5, 'cols': 5}, Pred shape={'rows': 5, 'cols': 5}
- primary GT table 19 -> Pred table 20: pair=92.2662, structure=92.5926, content=91.7767, keywords=95.3243, match=93.8605, GT shape={'rows': 8, 'cols': 5}, Pred shape={'rows': 9, 'cols': 5}
- primary GT table 20 -> Pred table 22: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 11, 'cols': 4}, Pred shape={'rows': 11, 'cols': 4}
- primary GT table 21 -> Pred table 23: pair=99.7990, structure=100.0000, content=99.4975, keywords=100.0000, match=99.9397, GT shape={'rows': 6, 'cols': 4}, Pred shape={'rows': 6, 'cols': 4}
- primary GT table 22 -> Pred table 24: pair=99.8135, structure=100.0000, content=99.5338, keywords=100.0000, match=99.9441, GT shape={'rows': 11, 'cols': 4}, Pred shape={'rows': 11, 'cols': 4}
- primary GT table 23 -> Pred table 25: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 8, 'cols': 5}, Pred shape={'rows': 8, 'cols': 5}
- primary GT table 24 -> Pred table 26: pair=99.8740, structure=100.0000, content=99.6850, keywords=100.0000, match=99.9622, GT shape={'rows': 20, 'cols': 7}, Pred shape={'rows': 20, 'cols': 7}
- primary GT table 25 -> Pred table 27: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 8, 'cols': 9}, Pred shape={'rows': 8, 'cols': 9}
- primary GT table 26 -> Pred table 28: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 3, 'cols': 3}, Pred shape={'rows': 3, 'cols': 3}
- primary GT table 27 -> Pred table 29: pair=98.3448, structure=100.0000, content=95.8621, keywords=98.1438, match=98.5753, GT shape={'rows': 2, 'cols': 15}, Pred shape={'rows': 2, 'cols': 15}
- primary GT table 28 -> Pred table 30: pair=97.8947, structure=100.0000, content=94.7368, keywords=96.7620, match=97.7494, GT shape={'rows': 2, 'cols': 14}, Pred shape={'rows': 2, 'cols': 14}
- primary GT table 29 -> Pred table 31: pair=93.2822, structure=92.5926, content=94.3166, keywords=80.8117, match=86.9090, GT shape={'rows': 8, 'cols': 9}, Pred shape={'rows': 9, 'cols': 9}

## Title Layout Evaluation
- GT raw heading levels: `[1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 3, 2, 3, 4, 4, 4, 3, 3, 4, 4, 4, 4, 3, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 3, 3, 4, 4, 4, 3, 4, 4, 4, 4, 5, 5, 3, 4, 4, 3, 3, 3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 4, 5, 5, 5, 5, 5, 5, 3, 3, 3, 2, 3, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 4, 4, 5, 5, 4, 3, 4, 4, 4, 3, 3, 3, 4, 4, 4, 4, 3, 3, 3, 4, 4, 3, 3, 4] ... (498 total)`
- Pred raw heading levels: `[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2] ... (466 total)`
- GT relative heading levels: `[1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 3, 2, 3, 4, 4, 4, 3, 3, 4, 4, 4, 4, 3, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 3, 3, 4, 4, 4, 3, 4, 4, 4, 4, 5, 5, 3, 4, 4, 3, 3, 3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 4, 5, 5, 5, 5, 5, 5, 3, 3, 3, 2, 3, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 4, 4, 5, 5, 4, 3, 4, 4, 4, 3, 3, 3, 4, 4, 4, 4, 3, 3, 3, 4, 4, 3, 3, 4] ... (498 total)`
- Pred relative heading levels: `[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2] ... (466 total)`
- Title layout score: 92.0599
- Heading F1 score: 96.4730
- Level accuracy score: 55.4409
- Order score: 93.3735
- Main penalties:
  - 457 aligned headings have different relative levels.
  - 33 GT headings are missing.
  - 1 predicted headings are extra.

## Text Evaluation
- Text mode: normalized_full_text_preserve_newlines
- Text score: 98.0747
- Body-only text score: 98.0747
- Chart score used by text module: 100.0000
- Average edit distance: 0.0193
- Matched / missing / extra blocks: 1 / 0 / 0
- GT / Pred block counts: 1 / 1

### Worst Match Samples
1. op=match, distance=0.0193, GT blocks 0+1, Pred blocks 0+1
   - GT: 宁波先锋新材料股份有限公司\n\n2025年年度报告\n\n2026年4月\n\n2025年年度报告\n\n第一节重要提示目录和释义\n\n公司董事会及董事高级管理人员保证年度报告内容的真实准确完整不存在虚假记载误导性陈述或者重大遗漏并承担个别和连带的法律责任。\n\n公司...
   - Pred: 宁波先锋新材料股份有限公司\n\n2025年年度报告\n\n2026年4月\n\n第一节重要提示目录和释义\n\n公司董事会及董事高级管理人员保证年度报告内容的真实准确完整不存在虚假记载误导性陈述或者重大遗漏并承担个别和连带的法律责任。\n\n公司负责人熊军主管会计工作负责...

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
