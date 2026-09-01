# Financial Markdown Scoring Report

## Overall
- Final Score: 94.1864
- Table Score: 93.7991
- Title Layout Score: 96.2279
- Text Score: 93.6614

## Prediction Cleanup
- Mode: prediction_only_header_footer_cleanup
- Removed pred header/footer lines: 0
- Removed examples:
  - None

## Weights
- Mode: gt_content_information_share
- Table: 8.47%
- Title Layout: 20.00%
- Text: 71.53%
- GT table semantic tokens / grid slots / information units: 940 / 220 / 1160
- GT body / active chart / text information units: 9790 / 0 / 9790

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
- Detected primary GT / Pred chart blocks: 17 / 0
- Representation-neutral chart score: 0.0000
- GT chart token share inside text module: 0.1844
- Removed primary GT / alt GT / Pred chart blocks: 17 / 0 / 0

## Table Evaluation
- Table GT strategy result: primary
- Primary table score: 93.7991
- Matched / missing / extra tables: 6 / 0 / 0
- Table content score: 92.3160
- Table structure score: 94.7879
- Table matrix score: 93.7991
- Table alignment strategy: pred_semantic_best_one_to_one_gt_footprint_weighted
- GT footprint total / extra Pred footprint: 543.5627 / 0.0000
- Chart-table eligible / auxiliary / matched: 6 / 0 / 0

### GT Table Footprint Weights
- GT table 0: weight=30.91%, grid=12x7, characters=336, footprint=168.0000
- GT table 1: weight=26.60%, grid=11x5, characters=380, footprint=144.5683
- GT table 2: weight=15.39%, grid=11x4, characters=159, footprint=83.6421
- GT table 3: weight=8.38%, grid=6x2, characters=173, footprint=45.5631
- GT table 4: weight=9.64%, grid=5x3, characters=183, footprint=52.3927
- GT table 5: weight=9.09%, grid=5x2, characters=244, footprint=49.3964

### Table Matches
- primary GT table 0 -> Pred table 0: pair=99.8086, structure=100.0000, content=99.5215, keywords=100.0000, match=99.9426, GT shape={'rows': 12, 'cols': 7}, Pred shape={'rows': 12, 'cols': 7}, GT weight=30.91%
- primary GT table 1 -> Pred table 1: pair=96.9756, structure=100.0000, content=92.4390, keywords=100.0000, match=99.0927, GT shape={'rows': 11, 'cols': 5}, Pred shape={'rows': 11, 'cols': 5}, GT weight=26.60%
- primary GT table 2 -> Pred table 2: pair=99.2079, structure=100.0000, content=98.0198, keywords=100.0000, match=99.7624, GT shape={'rows': 11, 'cols': 4}, Pred shape={'rows': 11, 'cols': 4}, GT weight=15.39%
- primary GT table 3 -> Pred table 3: pair=91.6338, structure=90.4762, content=93.3702, keywords=87.7365, match=89.4536, GT shape={'rows': 6, 'cols': 2}, Pred shape={'rows': 7, 'cols': 2}, GT weight=8.38%
- primary GT table 4 -> Pred table 4: pair=73.7436, structure=77.7778, content=67.6923, keywords=73.0645, match=74.2109, GT shape={'rows': 5, 'cols': 3}, Pred shape={'rows': 5, 'cols': 2}, GT weight=9.64%
- primary GT table 5 -> Pred table 5: pair=78.1746, structure=75.0000, content=82.9365, keywords=92.3611, match=84.6329, GT shape={'rows': 5, 'cols': 2}, Pred shape={'rows': 8, 'cols': 2}, GT weight=9.09%

## Title Layout Evaluation
- GT raw heading levels: `[1, 2, 2, 2, 3, 3, 2, 2, 3, 3, 2, 3, 3, 3, 2, 3, 3, 3, 4, 4, 4, 2, 2, 2, 2, 2, 2, 2]`
- Pred raw heading levels: `[1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]`
- GT relative heading levels: `[1, 2, 2, 2, 3, 3, 2, 2, 3, 3, 2, 3, 3, 3, 2, 3, 3, 3, 4, 4, 4, 2, 2, 2, 2, 2, 2, 2]`
- Pred relative heading levels: `[1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]`
- Title layout score: 96.2279
- Heading F1 score: 98.2456
- Level accuracy score: 79.7619
- Order score: 96.5517
- Main penalties:
  - 14 aligned headings have different relative levels.
  - 1 predicted headings are extra.

## Text Evaluation
- Text mode: normalized_full_text_preserve_newlines
- Text score: 93.6614
- Body-only text score: 93.6614
- Chart score used by text module: 0.0000
- Average edit distance: 0.0634
- Matched / missing / extra blocks: 1 / 0 / 0
- GT / Pred block counts: 1 / 1

### Worst Match Samples
1. op=match, distance=0.0634, GT blocks 0+1, Pred blocks 0+1
   - GT: 银幕春秋:线下光影与线上风云\n\n传媒行业深度报告\n\n行业概述\n\n电影产业是指以电影制作为核心通过电影的生产发行和放映以及电影音像产品电影衍生品电影院和放映场所的建设等相关产业经济形态的统称。\n\n投资要点\n\n产业特点:1.独特盈利模式:电影产业的盈利模式独...
   - Pred: 数据来源:聚源,\n\n银幕春秋:线下光影与线上风云\n\n传媒行业深度报告\n\n[行业概述:Table\Sum\n\n电影产业是指以电影制作为核心通过电影的生产发行和放映以及电影音像产品电影衍生品电影院和放映场所的建设等相关产业经济形态的统称。\n\n投资要点:\n\n...

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
