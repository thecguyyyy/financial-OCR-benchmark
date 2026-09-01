# Financial Markdown Scoring Report

## Overall
- Final Score: 81.6851
- Table Score: 49.5502
- Title Layout Score: 89.1491
- Text Score: 84.3530

## Prediction Cleanup
- Mode: prediction_only_header_footer_cleanup
- Removed pred header/footer lines: 0
- Removed examples:
  - None

## Weights
- Mode: gt_content_information_share
- Table: 10.42%
- Title Layout: 20.00%
- Text: 69.58%
- GT table semantic tokens / grid slots / information units: 1928 / 132 / 2060
- GT body / active chart / text information units: 13753 / 0 / 13753

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
- Detected primary GT / Pred chart blocks: 62 / 0
- Representation-neutral chart score: 0.0000
- GT chart token share inside text module: 0.6207
- Removed primary GT / alt GT / Pred chart blocks: 62 / 0 / 0

## Table Evaluation
- Table GT strategy result: primary
- Primary table score: 49.5502
- Matched / missing / extra tables: 2 / 0 / 1
- Table content score: 37.7205
- Table structure score: 57.4367
- Table matrix score: 49.5502
- Table alignment strategy: pred_semantic_best_one_to_one_gt_footprint_weighted
- GT footprint total / extra Pred footprint: 728.2838 / 119.8666
- Chart-table eligible / auxiliary / matched: 0 / 0 / 0

### GT Table Footprint Weights
- GT table 0: weight=72.45%, grid=19x4, characters=3663, footprint=527.6249
- GT table 1: weight=27.55%, grid=8x7, characters=719, footprint=200.6589

### Table Matches
- primary GT table 0 -> Pred table 0: pair=42.6706, structure=54.2982, content=25.2292, keywords=82.2059, match=64.7638, GT shape={'rows': 19, 'cols': 4}, Pred shape={'rows': 7, 'cols': 5}, GT weight=72.45%
- primary GT table 1 -> Pred table 2: pair=97.2395, structure=100.0000, content=93.0988, keywords=89.3388, match=93.8413, GT shape={'rows': 8, 'cols': 7}, Pred shape={'rows': 8, 'cols': 7}, GT weight=27.55%

## Title Layout Evaluation
- GT raw heading levels: `[1, 2, 3, 2, 3, 3, 2, 2, 2, 3, 3, 2, 3, 4, 4, 4, 3, 2, 3, 4, 5, 5, 5, 3, 3, 3, 2, 2, 2, 2]`
- Pred raw heading levels: `[2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]`
- GT relative heading levels: `[1, 2, 3, 2, 3, 3, 2, 2, 2, 3, 3, 2, 3, 4, 4, 4, 3, 2, 3, 4, 5, 5, 5, 3, 3, 3, 2, 2, 2, 2]`
- Pred relative heading levels: `[2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]`
- Title layout score: 89.1491
- Heading F1 score: 91.2281
- Level accuracy score: 75.0000
- Order score: 86.6667
- Main penalties:
  - 17 aligned headings have different relative levels.
  - 4 GT headings are missing.
  - 1 predicted headings are extra.

## Text Evaluation
- Text mode: normalized_full_text_preserve_newlines
- Text score: 84.3530
- Body-only text score: 84.3530
- Chart score used by text module: 0.0000
- Average edit distance: 0.1565
- Matched / missing / extra blocks: 1 / 0 / 0
- GT / Pred block counts: 1 / 1

### Worst Match Samples
1. op=match, distance=0.1565, GT blocks 0+1, Pred blocks 0+1
   - GT: 食品饮料行业深度报告\n\n平情应物驭势稳进\n\n中低速转型阶段买食品饮料是在买什么?\n\n2024年07月15日\n\n增持(维持)\n\n投资要点\n\nA股高现金流高ROE行业具备稳定估值支撑,15x是参考中枢。在稳态低增长情形下动态⟦FORMULA:PE=DCF...
   - Pred: 平情应物驭势稳进\n中低速转型阶段买食品饮料是在买什么?\n\n增持(维持)\n\n投资要点\n\nA股高现金流高ROE行业具备稳定估值支撑,15x是参考中枢。在稳态低增长情形下动态PE=DCF/E1=FCFR/(r-g),能够由此推导得出,1215倍动态PE是多数稳态低增...

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
