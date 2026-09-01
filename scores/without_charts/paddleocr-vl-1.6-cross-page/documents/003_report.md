# Financial Markdown Scoring Report

## Overall
- Final Score: 97.1186
- Table Score: 97.9682
- Title Layout Score: 91.2586
- Text Score: 98.8144

## Prediction Cleanup
- Mode: prediction_only_header_footer_cleanup
- Removed pred header/footer lines: 0
- Removed examples:
  - None

## Weights
- Mode: gt_content_information_share
- Table: 21.82%
- Title Layout: 20.00%
- Text: 58.18%
- GT table semantic tokens / grid slots / information units: 4420 / 642 / 5062
- GT body / active chart / text information units: 13500 / 0 / 13500

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
- Detected primary GT / Pred chart blocks: 44 / 0
- Representation-neutral chart score: 0.0000
- GT chart token share inside text module: 0.3784
- Removed primary GT / alt GT / Pred chart blocks: 44 / 0 / 0

## Table Evaluation
- Table GT strategy result: primary
- Primary table score: 97.9682
- Matched / missing / extra tables: 8 / 0 / 1
- Table content score: 97.5205
- Table structure score: 98.2667
- Table matrix score: 97.9682
- Table alignment strategy: pred_semantic_best_one_to_one_gt_footprint_weighted
- GT footprint total / extra Pred footprint: 1973.3991 / 15.4919
- Chart-table eligible / auxiliary / matched: 1 / 0 / 0

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
- primary GT table 0 -> Pred table 1: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 8, 'cols': 8}, Pred shape={'rows': 8, 'cols': 8}, GT weight=6.69%
- primary GT table 1 -> Pred table 2: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 17, 'cols': 15}, Pred shape={'rows': 17, 'cols': 15}, GT weight=31.18%
- primary GT table 2 -> Pred table 3: pair=95.9453, structure=93.3333, content=99.8633, keywords=100.0000, match=97.4503, GT shape={'rows': 9, 'cols': 4}, Pred shape={'rows': 10, 'cols': 4}, GT weight=14.43%
- primary GT table 3 -> Pred table 4: pair=96.6638, structure=100.0000, content=91.6595, keywords=97.9412, match=97.9697, GT shape={'rows': 17, 'cols': 8}, Pred shape={'rows': 17, 'cols': 8}, GT weight=18.25%
- primary GT table 4 -> Pred table 5: pair=99.5214, structure=100.0000, content=98.8034, keywords=100.0000, match=99.8564, GT shape={'rows': 10, 'cols': 6}, Pred shape={'rows': 10, 'cols': 6}, GT weight=13.10%
- primary GT table 5 -> Pred table 6: pair=99.9010, structure=100.0000, content=99.7525, keywords=100.0000, match=99.9703, GT shape={'rows': 6, 'cols': 3}, Pred shape={'rows': 6, 'cols': 3}, GT weight=6.10%
- primary GT table 6 -> Pred table 7: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 7, 'cols': 7}, Pred shape={'rows': 7, 'cols': 7}, GT weight=6.34%
- primary GT table 7 -> Pred table 8: pair=100.0000, structure=100.0000, content=100.0000, keywords=100.0000, match=100.0000, GT shape={'rows': 8, 'cols': 3}, Pred shape={'rows': 8, 'cols': 3}, GT weight=3.92%

## Title Layout Evaluation
- GT raw heading levels: `[1, 2, 3, 3, 2, 2, 2, 3, 3, 3, 4, 2, 3, 4, 4, 4, 4, 3, 2, 3, 3, 3, 2, 2, 2]`
- Pred raw heading levels: `[5, 5, 5, 2, 2, 2, 3, 3, 3, 5, 2, 3, 4, 4, 4, 4, 3, 2, 3, 3, 3, 2, 2, 3]`
- GT relative heading levels: `[1, 2, 3, 3, 2, 2, 2, 3, 3, 3, 4, 2, 3, 4, 4, 4, 4, 3, 2, 3, 3, 3, 2, 2, 2]`
- Pred relative heading levels: `[4, 4, 4, 1, 1, 1, 2, 2, 2, 4, 1, 2, 3, 3, 3, 3, 2, 1, 2, 2, 2, 1, 1, 2]`
- Title layout score: 91.2586
- Heading F1 score: 93.8776
- Level accuracy score: 69.5652
- Order score: 92.0000
- Main penalties:
  - 21 aligned headings have different relative levels.
  - 2 GT headings are missing.
  - 1 predicted headings are extra.

## Text Evaluation
- Text mode: normalized_full_text_preserve_newlines
- Text score: 98.8144
- Body-only text score: 98.8144
- Chart score used by text module: 0.0000
- Average edit distance: 0.0119
- Matched / missing / extra blocks: 1 / 0 / 0
- GT / Pred block counts: 1 / 1

### Worst Match Samples
1. op=match, distance=0.0119, GT blocks 0+1, Pred blocks 0+1
   - GT: 聚焦创新药产业链静待消费医疗改善\n\n2025年01月08日\n\n评级:领先大市\n\n评级变动:维持\n\n投资要点\n\n行业回顾:2024年医药生物(申万)板块涨幅为-4.05%,在申万31个一级行业中排名第31位明显跑输沪深300指数。截至2024年12月27日...
   - Pred: 2025年01月08日\n\n评级\n\n领先大市\n\n评级变动:维持\n\n行业涨跌幅比较\n![]\n相关报告\n\n1医药生物行业2024年11月月报:业绩增长承压重点关注创新药产业链消费医疗2024-11-05\n\n聚焦创新药产业链静待消费医疗改善\n\n投资要...

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
