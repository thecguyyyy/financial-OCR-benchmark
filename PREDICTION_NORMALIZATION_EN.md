# Unified Prediction Normalization Protocol (001–010)

The benchmark now has one Prediction-normalization implementation. Industry reports 001–004 and financial filings 005–010 no longer maintain separate copies of the common engine or file traversal logic.

## 1. Unified architecture

- Single shared engine: `normalizers/common.py`
- Single batch entry point: `python normalize_all_predictions.py`
- Parser profiles: `normalizers/normalize_*.py`; each profile only selects stable protocol transformations for that parser
- Document discovery: every `NNN.md` file in the input directory is discovered and sorted automatically, so the same implementation handles 001–010 and also supports systems that cover only a subset
- Each system writes an independent `normalization_manifest.json` with document IDs, input/output SHA-256 values, transformation counts, and validation results

## 2. Fairness boundary

Adapters remove parser protocol artifacts; they do not repair answers:

- They never read GT, PDFs, score reports, or another parser's output.
- They do not branch on document ID, company, report title, or known scores.
- They do not rewrite entities, numbers, body meaning, or table cells.
- They do not merge, split, delete, or reorder business tables.
- They do not repair genuine OCR errors, omissions, flattened heading depth, or missing tables.
- A transformation is allowed only when the parser's own output syntax identifies a container, path, coordinate record, page marker, internal label, or repeated running header/footer.

## 3. Shared operations

All profiles use the same implementation, but a rule runs only when the profile explicitly calls it:

1. Normalize CRLF/CR to LF and remove a UTF-8 BOM.
2. Normalize Markdown, reference-style, and HTML images to `![]`.
3. Remove HTML comments while retaining visible content.
4. Unwrap presentation-only `sup/sub` tags and retain their text.
5. Remove isolated page numbers; repeated running headers/footers and page-level headings repeated at page boundaries are detected from the Prediction alone, with the first occurrence retained.
6. Normalize trailing whitespace, excess blank lines, and adjacent image markers.
7. Validate table matrices, genuine heading order, and idempotence before writing output.

### Exhaustive removal list and examples

Every item must be proven from stable Prediction syntax or a repetition pattern within that Prediction. The table lists every class handled by formal normalization; it is not permission to delete text merely because it looks untidy.

| Class | Condition for removal/normalization | Example: input → output |
|---|---|---|
| Encoding and whitespace | UTF-8 BOM, CRLF/CR, trailing whitespace, repeated blank lines | `BOM + a\r\n\r\n\r\n b` → `a\n\nb` |
| Image implementation details | Local/remote image paths, alt text, HTML image attributes, coordinate-image records | `![](C:\\tmp\\p3.png)`, `<img x="12" ...>` → `![]` |
| Parser containers | HTML comments and presentation-only alignment `div`, `sup/sub`, or known `details/summary` wrappers that add no text | `<div align="center">Text</div>` → `Text` |
| Pagination noise | `<pagebreak>`, isolated `12`, `- 12 -`, `Page 12 of 90` | `Text\n<pagebreak>\n13` → `Text` |
| Repeated running text | The exact text occurs within the first five visible lines of at least three page segments in the Prediction; later occurrences only are removed | Three pages begin `Example Securities Research` → retain the first only |
| Internal labels and display escapes | Line-boundary `Table_*`/`Tale_*` leakage and known presentation escapes outside tables | `Table_17\nRevenue` → `Revenue`; `\\*key\\*` → `*key*` |
| Peripheral-only visual figure content | A numbered title is followed only by `![]`, source, and contiguous note, with no table or chart-data transcription | `Figure 1: Trend\n![]\nSource: ...` → retain `Figure 1: Trend` |
| Explicit directory layouts | A table inside an explicit contents/list-of-figures section where at least 80% of rows are figure/table-number entries; it becomes equivalent directory text | `<table><tr><td>Figure 1 ...</td>` → `Figure 1 ...` |

The following are never removable, regardless of score, repetition, or apparent formatting quality: entities such as companies/products/people, body sentences, years and monetary values, percentages and units, formula tokens, figure titles, chart-data transcriptions, any cell of a formal business table, and genuine headings or their levels. For example, `Revenue: RMB 1.25bn`, `| Year | Revenue |`, and `# 1. Operations` must remain unchanged.

## 4. Parser-specific profiles

| Parser | Transformations | Explicitly excluded |
|---|---|---|
| MinerU 3.4.0 Hybrid high | Unwrap `details/summary`; preserve informative chart boundaries from MinerU's own summary type; convert natural images, flowcharts, and Mermaid to `![]`; remove entries inside explicit contents/list-of-figures sections while retaining their headings; undo display escapes such as `\\~`, `\\*`, `\\+`, `\\_`, and `\\$` outside tables; remove leaked line-boundary `Table_*`/`Tale_*` labels; attach the adjacent raster marker, source, and contiguous notes to a structured chart boundary; remove generated English descriptions of decorative images; remove repeated running noise | No formula repair, table-cell rewriting, or table-type guessing from captions |
| MinerU 3.4.4 VLM | Uses the same MinerU protocol rules as Hybrid; only transformations actually present in VLM output are counted in its own manifest | No answer sharing with Hybrid and no score-based selection |
| MinerU 3.4.0 Pipeline | Normalize image paths; for an image-only numbered figure, remove only the adjacent marker/source/note while retaining the title; unwrap `sup/sub`; remove comments and repeated page noise | No invented chart data and no cross-page table merge |
| Self-developed parser | When a commented coordinate image is immediately followed by a 2D table, mark both as one chart object while retaining both representations; unwrap remaining commented coordinate images, remove `<pagebreak>`, and normalize `page/x/y/w/h` records to `![]`; restore serialized literal `\\n` inside HTML table cells as line breaks; convert a layout table inside an explicit figure directory back to text when at least 80% of its rows start with a figure/table number; remove page-level headings repeated at page boundaries on at least 3 pages while retaining the first occurrence; unwrap presentation braces around CJK emphasis outside formulas and tables; convert visual square bullets to Markdown lists only for the industry-report output variant; clean the local image-only numbered-figure pattern; then remove comments and repeated page noise | No content rewrite guided by GT, PDF, document ID, or score; no split or merge of business tables and no change to non-whitespace cell content; selected/unselected boxes in annual reports remain distinct |
| PaddleOCR-VL-1.6 pagewise | Unwrap alignment `div` containers while retaining text; normalize images; clean the local numbered-title-plus-image-marker pattern while retaining the title; unwrap `sup/sub`; remove comments and repeated page noise | No cross-page merge |
| PaddleOCR-VL-1.6 cross-page | Uses the same presentation cleanup as pagewise and preserves cross-page table boundaries already present in the input | Does not rerun merging and does not reclassify HTML tables merely because a title starts with “Figure/Table N” |

## 5. Chart boundaries

MinerU Hybrid/VLM expose a stable chart type through `details/summary`, so the adapter may emit a `<chart data-type="...">` boundary. The title stays in body text; the adjacent raster marker, data source, and contiguous notes move into the same chart block.

Pipeline, PaddleOCR, and the self-developed parser do not expose an equivalent structured chart container. Their adapters therefore recognize only the local numbered-title-followed-by-image-marker pattern. Formal HTML/Markdown tables are always retained and are never reclassified solely from a “Figure/Table N” title.

## 6. Automatic validation

Every output must pass all checks:

1. Business-table count and 2D cell matrices remain unchanged. A layout table proven to be inside an explicit figure directory is excluded from the business-table inventory, but every directory-row character is retained as text. Validation otherwise ignores only whitespace around canonical image markers and whitespace introduced by restoring literal `\\n` as table-cell line breaks; every non-whitespace business-cell character must remain identical.
2. Genuine non-directory heading text, levels, and order remain unchanged. Directory entries mis-promoted to headings inside an explicit directory section may be removed as protocol noise. A page-level heading may also be removed only when the Prediction itself places the exact heading within the first 5 visible lines of at least 3 page segments, and the first occurrence must be retained.
3. A second normalization pass produces byte-identical output.
4. Manifest flags `uses_ground_truth`, `uses_pdf`, `uses_document_id_rules`, `merges_or_splits_tables`, and `reorders_content` are all `false`.

Normalization stops immediately when any check fails.

## 7. Usage

Normalize every available official Prediction:

```bash
python normalize_all_predictions.py
```

Run one profile directly:

```bash
python normalizers/normalize_mineru_hybrid.py \
  --input-dir predictions/mineru-3.4.0-hybrid-high \
  --output-dir normalized_predictions/mineru-3.4.0-hybrid-high
```

For a new parser, copy `normalizers/normalize_parser_template.py` and add only rules justified by that parser's own output protocol. Do not copy the shared engine.
