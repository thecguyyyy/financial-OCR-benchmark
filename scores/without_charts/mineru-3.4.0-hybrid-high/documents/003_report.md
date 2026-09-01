# Financial Markdown Scoring Report

## Overall
- Final Score: 95.9440
- Table Score: 98.1856
- Title Layout Score: 87.7845
- Text Score: 97.9083

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
- Detected primary GT / Pred chart blocks: 44 / 44
- Representation-neutral chart score: 94.7324
- GT chart token share inside text module: 0.3784
- Removed primary GT / alt GT / Pred chart blocks: 44 / 0 / 44

## Table Evaluation
- Table GT strategy result: primary
- Primary table score: 98.1856
- Matched / missing / extra tables: 8 / 0 / 1
- Table content score: 96.6324
- Table structure score: 99.2211
- Table matrix score: 98.1856
- Table alignment strategy: pred_semantic_best_one_to_one_gt_footprint_weighted
- GT footprint total / extra Pred footprint: 1973.3991 / 15.4919
- Chart-table eligible / auxiliary / matched: 1 / 44 / 0

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
- primary GT table 2 -> Pred table 3: pair=99.2164, structure=100.0000, content=98.0410, keywords=100.0000, match=99.7649, GT shape={'rows': 9, 'cols': 4}, Pred shape={'rows': 9, 'cols': 4}, GT weight=14.43%
- primary GT table 3 -> Pred table 4: pair=97.6087, structure=100.0000, content=94.0217, keywords=100.0000, match=99.2826, GT shape={'rows': 17, 'cols': 8}, Pred shape={'rows': 17, 'cols': 8}, GT weight=18.25%
- primary GT table 4 -> Pred table 5: pair=98.6183, structure=100.0000, content=96.5458, keywords=100.0000, match=99.5855, GT shape={'rows': 10, 'cols': 6}, Pred shape={'rows': 10, 'cols': 6}, GT weight=13.10%
- primary GT table 5 -> Pred table 6: pair=98.6617, structure=100.0000, content=96.6543, keywords=100.0000, match=99.5985, GT shape={'rows': 6, 'cols': 3}, Pred shape={'rows': 6, 'cols': 3}, GT weight=6.10%
- primary GT table 6 -> Pred table 7: pair=98.2561, structure=100.0000, content=95.6403, keywords=100.0000, match=99.4768, GT shape={'rows': 7, 'cols': 7}, Pred shape={'rows': 7, 'cols': 7}, GT weight=6.34%
- primary GT table 7 -> Pred table 8: pair=96.9118, structure=100.0000, content=92.2794, keywords=100.0000, match=99.0735, GT shape={'rows': 8, 'cols': 3}, Pred shape={'rows': 8, 'cols': 3}, GT weight=3.92%

## Title Layout Evaluation
- GT raw heading levels: `[1, 2, 3, 3, 2, 2, 2, 3, 3, 3, 4, 2, 3, 4, 4, 4, 4, 3, 2, 3, 3, 3, 2, 2, 2]`
- Pred raw heading levels: `[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]`
- GT relative heading levels: `[1, 2, 3, 3, 2, 2, 2, 3, 3, 3, 4, 2, 3, 4, 4, 4, 4, 3, 2, 3, 3, 3, 2, 2, 2]`
- Pred relative heading levels: `[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]`
- Title layout score: 87.7845
- Heading F1 score: 93.6170
- Level accuracy score: 40.9091
- Order score: 88.0000
- Main penalties:
  - 21 aligned headings have different relative levels.
  - 3 GT headings are missing.

## Text Evaluation
- Text mode: normalized_full_text_preserve_newlines
- Text score: 97.9083
- Body-only text score: 97.9083
- Chart score used by text module: 94.7324
- Average edit distance: 0.0209
- Matched / missing / extra blocks: 1 / 0 / 0
- GT / Pred block counts: 1 / 1

### Worst Match Samples
1. op=match, distance=0.0209, GT blocks 0+1, Pred blocks 0+1
   - GT: 聚焦创新药产业链静待消费医疗改善\n\n2025年01月08日\n\n评级:领先大市\n\n评级变动:维持\n\n投资要点\n\n行业回顾:2024年医药生物(申万)板块涨幅为-4.05%,在申万31个一级行业中排名第31位明显跑输沪深300指数。截至2024年12月27日...
   - Pred: 2025年01月08日\n\n评级\n\n领先大市\n\n评级变动:维持\n\n行业涨跌幅比较\n\n相关报告\n\n1医药生物行业2024年11月月报:业绩增长承压重点关注创新药产业链消费医疗2024-11-05\n\n聚焦创新药产业链静待消费医疗改善\n\n投资要点:\...

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
