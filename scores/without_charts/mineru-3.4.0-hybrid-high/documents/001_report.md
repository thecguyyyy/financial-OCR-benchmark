# Financial Markdown Scoring Report

## Overall
- Final Score: 90.6480
- Table Score: 87.0272
- Title Layout Score: 89.0893
- Text Score: 91.6384

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
- Detected primary GT / Pred chart blocks: 62 / 62
- Representation-neutral chart score: 98.9196
- GT chart token share inside text module: 0.6207
- Removed primary GT / alt GT / Pred chart blocks: 62 / 0 / 62

## Table Evaluation
- Table GT strategy result: primary
- Primary table score: 87.0272
- Matched / missing / extra tables: 2 / 0 / 0
- Table content score: 90.4462
- Table structure score: 84.7479
- Table matrix score: 87.0272
- Table alignment strategy: pred_semantic_best_one_to_one_gt_footprint_weighted
- GT footprint total / extra Pred footprint: 728.2838 / 0.0000
- Chart-table eligible / auxiliary / matched: 0 / 62 / 0

### GT Table Footprint Weights
- GT table 0: weight=72.45%, grid=19x4, characters=3663, footprint=527.6249
- GT table 1: weight=27.55%, grid=8x7, characters=719, footprint=200.6589

### Table Matches
- primary GT table 0 -> Pred table 0: pair=83.1228, structure=78.9474, content=89.3859, keywords=97.9412, match=89.6969, GT shape={'rows': 19, 'cols': 4}, Pred shape={'rows': 13, 'cols': 4}, GT weight=72.45%
- primary GT table 1 -> Pred table 1: pair=97.2936, structure=100.0000, content=93.2341, keywords=100.0000, match=99.1881, GT shape={'rows': 8, 'cols': 7}, Pred shape={'rows': 8, 'cols': 7}, GT weight=27.55%

## Title Layout Evaluation
- GT raw heading levels: `[1, 2, 3, 2, 3, 3, 2, 2, 2, 3, 3, 2, 3, 4, 4, 4, 3, 2, 3, 4, 5, 5, 5, 3, 3, 3, 2, 2, 2, 2]`
- Pred raw heading levels: `[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]`
- GT relative heading levels: `[1, 2, 3, 2, 3, 3, 2, 2, 2, 3, 3, 2, 3, 4, 4, 4, 3, 2, 3, 4, 5, 5, 5, 3, 3, 3, 2, 2, 2, 2]`
- Pred relative heading levels: `[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]`
- Title layout score: 89.0893
- Heading F1 score: 93.3333
- Level accuracy score: 50.8929
- Order score: 93.3333
- Main penalties:
  - 28 aligned headings have different relative levels.
  - 2 GT headings are missing.
  - 2 predicted headings are extra.

## Text Evaluation
- Text mode: normalized_full_text_preserve_newlines
- Text score: 91.6384
- Body-only text score: 91.6384
- Chart score used by text module: 98.9196
- Average edit distance: 0.0836
- Matched / missing / extra blocks: 1 / 0 / 0
- GT / Pred block counts: 1 / 1

### Worst Match Samples
1. op=match, distance=0.0836, GT blocks 0+1, Pred blocks 0+1
   - GT: 食品饮料行业深度报告\n\n平情应物驭势稳进\n\n中低速转型阶段买食品饮料是在买什么?\n\n2024年07月15日\n\n增持(维持)\n\n投资要点\n\nA股高现金流高ROE行业具备稳定估值支撑,15x是参考中枢。在稳态低增长情形下动态⟦FORMULA:PE=DCF...
   - Pred: 平情应物驭势稳进\n\n中低速转型阶段买食品饮料是在买什么?\n\n增持(维持)\n\n投资要点\n\nA股高现金流高ROE行业具备稳定估值支撑,15x是参考中枢。在稳态低增长情形下动态⟦FORMULA:PE=DCF/ESUB(1)=FCFR/(r-g)⟧,能够由此推导得出...

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
