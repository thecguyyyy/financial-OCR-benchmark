# Financial Markdown Scoring Report

## Overall
- Final Score: 97.3334
- Table Score: 98.8339
- Title Layout Score: 95.3671
- Text Score: 97.0317

## Prediction Cleanup
- Mode: prediction_only_header_footer_cleanup
- Removed pred header/footer lines: 0
- Removed examples:
  - None

## Weights
- Mode: gt_content_information_share
- Table: 35.22%
- Title Layout: 20.00%
- Text: 44.78%
- GT table semantic tokens / grid slots / information units: 6616 / 1076 / 7692
- GT body / active chart / text information units: 9782 / 0 / 9782

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
- Detected primary GT / Pred chart blocks: 12 / 0
- Representation-neutral chart score: 0.0000
- GT chart token share inside text module: 0.2296
- Removed primary GT / alt GT / Pred chart blocks: 12 / 0 / 0

## Table Evaluation
- Table GT strategy result: primary
- Primary table score: 98.8339
- Matched / missing / extra tables: 8 / 0 / 0
- Table content score: 97.0847
- Table structure score: 100.0000
- Table matrix score: 98.8339
- Table alignment strategy: pred_semantic_best_one_to_one_gt_footprint_weighted
- GT footprint total / extra Pred footprint: 3473.3817 / 0.0000
- Chart-table eligible / auxiliary / matched: 8 / 0 / 0

### GT Table Footprint Weights
- GT table 0: weight=9.72%, grid=18x8, characters=791, footprint=337.4967
- GT table 1: weight=2.39%, grid=11x4, characters=156, footprint=82.8493
- GT table 2: weight=2.79%, grid=6x8, characters=196, footprint=96.9948
- GT table 3: weight=3.34%, grid=6x4, characters=561, footprint=116.0345
- GT table 4: weight=38.02%, grid=53x7, characters=4701, footprint=1320.6328
- GT table 5: weight=37.58%, grid=56x7, characters=4347, footprint=1305.3827
- GT table 6: weight=3.00%, grid=11x3, characters=330, footprint=104.3552
- GT table 7: weight=3.16%, grid=4x5, characters=601, footprint=109.6358

### Table Matches
- primary GT table 0 -> Pred table 0: pair=99.4030, structure=100.0000, content=98.5075, keywords=100.0000, match=99.8209, GT shape={'rows': 18, 'cols': 8}, Pred shape={'rows': 18, 'cols': 8}, GT weight=9.72%
- primary GT table 1 -> Pred table 1: pair=98.8119, structure=100.0000, content=97.0297, keywords=100.0000, match=99.6436, GT shape={'rows': 11, 'cols': 4}, Pred shape={'rows': 11, 'cols': 4}, GT weight=2.39%
- primary GT table 2 -> Pred table 2: pair=97.7600, structure=100.0000, content=94.4000, keywords=100.0000, match=99.3280, GT shape={'rows': 6, 'cols': 8}, Pred shape={'rows': 6, 'cols': 8}, GT weight=2.79%
- primary GT table 3 -> Pred table 3: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 6, 'cols': 4}, Pred shape={'rows': 6, 'cols': 4}, GT weight=3.34%
- primary GT table 4 -> Pred table 4: pair=98.6675, structure=100.0000, content=96.6687, keywords=93.9421, match=96.5713, GT shape={'rows': 53, 'cols': 7}, Pred shape={'rows': 53, 'cols': 7}, GT weight=38.02%
- primary GT table 5 -> Pred table 5: pair=98.6746, structure=100.0000, content=96.6866, keywords=97.8125, match=98.5086, GT shape={'rows': 56, 'cols': 7}, Pred shape={'rows': 56, 'cols': 7}, GT weight=37.58%
- primary GT table 6 -> Pred table 6: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 11, 'cols': 3}, Pred shape={'rows': 11, 'cols': 3}, GT weight=3.00%
- primary GT table 7 -> Pred table 7: pair=99.6046, structure=100.0000, content=99.0115, keywords=98.8042, match=99.2835, GT shape={'rows': 4, 'cols': 5}, Pred shape={'rows': 4, 'cols': 5}, GT weight=3.16%

## Title Layout Evaluation
- GT raw heading levels: `[1, 2, 2, 2, 2, 2, 2, 3, 4, 4, 3, 4, 4, 5, 5, 2, 2, 2, 2]`
- Pred raw heading levels: `[1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]`
- GT relative heading levels: `[1, 2, 2, 2, 2, 2, 2, 3, 4, 4, 3, 4, 4, 5, 5, 2, 2, 2, 2]`
- Pred relative heading levels: `[1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]`
- Title layout score: 95.3671
- Heading F1 score: 97.2973
- Level accuracy score: 80.5556
- Order score: 94.7368
- Main penalties:
  - 8 aligned headings have different relative levels.
  - 1 GT headings are missing.

## Text Evaluation
- Text mode: normalized_full_text_preserve_newlines
- Text score: 97.0317
- Body-only text score: 97.0317
- Chart score used by text module: 0.0000
- Average edit distance: 0.0297
- Matched / missing / extra blocks: 1 / 0 / 0
- GT / Pred block counts: 1 / 1

### Worst Match Samples
1. op=match, distance=0.0297, GT blocks 0+1, Pred blocks 0+1
   - GT: 以BD出海关税风险小看好创新药国际化进程\n\n投资逻辑\n\n美国潜在关税威胁对我国创新药影响小。原本全球药品贸易近乎零关税据WTO官网显示,1994年《药品贸易协定》取消大量药品及其用于生产这些商品的物质的关税和其他关税和费用将它们永久地约束在免税水平加拿大欧盟日本澳门...
   - Pred: 以BD出海关税风险小看好创新药国际化进程\n\n投资逻辑\n\n美国潜在关税威胁对我国创新药影响小。原本全球药品贸易近乎零关税据WTO官网显示,1994年《药品贸易协定》取消大量药品及其用于生产这些商品的物质的关税和其他关税和费用将它们永久地约束在免税水平加拿大欧盟日本澳门...

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
