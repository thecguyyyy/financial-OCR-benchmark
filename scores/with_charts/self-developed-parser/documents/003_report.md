# Financial Markdown Scoring Report

## Overall
- Final Score: 72.4474
- Table Score: 98.7898
- Title Layout Score: 94.8468
- Text Score: 59.4021

## Prediction Cleanup
- Mode: prediction_only_header_footer_cleanup
- Removed pred header/footer lines: 0
- Removed examples:
  - None

## Weights
- Mode: gt_content_information_share
- Table: 15.12%
- Title Layout: 20.00%
- Text: 64.88%
- GT table semantic tokens / grid slots / information units: 4420 / 642 / 5062
- GT body / active chart / text information units: 13500 / 8217 / 21717

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
- Detected primary GT / Pred chart blocks: 44 / 1
- Representation-neutral chart score: 0.7064
- GT chart token share inside text module: 0.3784
- Removed primary GT / alt GT / Pred chart blocks: 0 / 0 / 0

## Table Evaluation
- Table GT strategy result: primary
- Primary table score: 98.7898
- Matched / missing / extra tables: 8 / 0 / 0
- Table content score: 98.4172
- Table structure score: 99.0381
- Table matrix score: 98.7898
- Table alignment strategy: pred_semantic_best_one_to_one_gt_footprint_weighted
- GT footprint total / extra Pred footprint: 1973.3991 / 0.0000
- Chart-table eligible / auxiliary / matched: 1 / 1 / 0

### GT Table Footprint Weights
- GT table 0: weight=6.69%, grid=8x8, characters=272, footprint=131.9394
- GT table 1: weight=31.18%, grid=17x15, characters=1485, footprint=615.3657
- GT table 2: weight=14.43%, grid=9x4, characters=2252, footprint=284.7315
- GT table 3: weight=18.25%, grid=17x8, characters=954, footprint=360.1999
- GT table 4: weight=13.10%, grid=10x6, characters=1114, footprint=258.5343
- GT table 5: weight=6.10%, grid=6x3, characters=804, footprint=120.2996
- GT table 6: weight=6.34%, grid=7x7, characters=319, footprint=125.0240
- GT table 7: weight=3.92%, grid=8x3, characters=249, footprint=77.3046

### Table Matches
- primary GT table 0 -> Pred table 0: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 8, 'cols': 8}, Pred shape={'rows': 8, 'cols': 8}, GT weight=6.69%
- primary GT table 1 -> Pred table 1: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 17, 'cols': 15}, Pred shape={'rows': 17, 'cols': 15}, GT weight=31.18%
- primary GT table 2 -> Pred table 2: pair=95.8178, structure=93.3333, content=99.5444, keywords=98.8710, match=96.8475, GT shape={'rows': 9, 'cols': 4}, Pred shape={'rows': 10, 'cols': 4}, GT weight=14.43%
- primary GT table 3 -> Pred table 3: pair=98.1122, structure=100.0000, content=95.2805, keywords=100.0000, match=99.4337, GT shape={'rows': 17, 'cols': 8}, Pred shape={'rows': 17, 'cols': 8}, GT weight=18.25%
- primary GT table 4 -> Pred table 4: pair=99.5214, structure=100.0000, content=98.8034, keywords=100.0000, match=99.8564, GT shape={'rows': 10, 'cols': 6}, Pred shape={'rows': 10, 'cols': 6}, GT weight=13.10%
- primary GT table 5 -> Pred table 5: pair=98.7113, structure=100.0000, content=96.7782, keywords=100.0000, match=99.6134, GT shape={'rows': 6, 'cols': 3}, Pred shape={'rows': 6, 'cols': 3}, GT weight=6.10%
- primary GT table 6 -> Pred table 6: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 7, 'cols': 7}, Pred shape={'rows': 7, 'cols': 7}, GT weight=6.34%
- primary GT table 7 -> Pred table 7: pair=96.9118, structure=100.0000, content=92.2794, keywords=100.0000, match=99.0735, GT shape={'rows': 8, 'cols': 3}, Pred shape={'rows': 8, 'cols': 3}, GT weight=3.92%

## Title Layout Evaluation
- GT raw heading levels: `[1, 2, 3, 3, 2, 2, 2, 3, 3, 3, 4, 2, 3, 4, 4, 4, 4, 3, 2, 3, 3, 3, 2, 2, 2]`
- Pred raw heading levels: `[1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3]`
- GT relative heading levels: `[1, 2, 3, 3, 2, 2, 2, 3, 3, 3, 4, 2, 3, 4, 4, 4, 4, 3, 2, 3, 3, 3, 2, 2, 2]`
- Pred relative heading levels: `[1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3]`
- Title layout score: 94.8468
- Heading F1 score: 98.0392
- Level accuracy score: 68.0000
- Order score: 96.1538
- Main penalties:
  - 19 aligned headings have different relative levels.
  - 1 predicted headings are extra.

## Text Evaluation
- Text mode: body_edit_distance_plus_representation_neutral_chart_tokens
- Text score: 59.4021
- Body-only text score: 95.1282
- Chart score used by text module: 0.7064
- Average edit distance: 0.0487
- Matched / missing / extra blocks: 1 / 0 / 0
- GT / Pred block counts: 1 / 1

### Worst Match Samples
1. op=match, distance=0.0487, GT blocks 0+1, Pred blocks 0+1
   - GT: 聚焦创新药产业链静待消费医疗改善\n\n2025年01月08日\n\n评级:领先大市\n\n评级变动:维持\n\n投资要点\n\n行业回顾:2024年医药生物(申万)板块涨幅为-4.05%,在申万31个一级行业中排名第31位明显跑输沪深300指数。截至2024年12月27日...
   - Pred: 聚焦创新药产业链静待消费医疗改善\n\n投资要点:\n\n行业回顾:2024年医药生物(申万)板块涨幅为-4.05%,在申万31个一级行业中排名第31位明显跑输沪深300指数。截至2024年12月27日医药生物板块PE(TTM,整体法)均值为26.95倍在申万31个一级行业...

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
