"""Canonical user-facing names for benchmark collections."""

PUBLIC_SYSTEMS = [
    (
        "mineru-3.4.0-hybrid-high",
        "MinerU 3.4.0 — Hybrid backend (effort=high; MinerU2.5-Pro-2605-1.2B)",
    ),
    (
        "mineru-3.4.4-vlm",
        "MinerU 3.4.4 — VLM backend (MinerU2.5-Pro-2605-1.2B)",
    ),
    (
        "mineru-3.4.0-pipeline",
        "MinerU 3.4.0 — Pipeline backend (method=auto, lang=ch)",
    ),
    ("self-developed-parser", "自研解析模型（版本未记录）"),
    (
        "paddleocr-vl-1.6-pagewise",
        "PaddleOCR-VL-1.6-0.9B — no cross-page merge",
    ),
    (
        "paddleocr-vl-1.6-cross-page",
        "PaddleOCR-VL-1.6-0.9B — cross-page merge",
    ),
]

COLLECTION_LABELS = {
    "gt_self_check": "GT 自检",
    "pred": "MinerU 3.4.0 — Hybrid backend（effort=high；MinerU2.5-Pro-2605-1.2B）",
    "mineru3_vlm": "MinerU 3.4.4 — VLM backend（MinerU2.5-Pro-2605-1.2B）",
    "pred_mineru3_vlm_4090": "MinerU 3.4.4 — VLM backend（MinerU2.5-Pro-2605-1.2B）",
    "mineru3_pipeline": "MinerU 3.4.0 — Pipeline backend（method=auto，lang=ch）",
    "pred_six_reports_final": "自研解析模型（版本未记录）",
    "paddleocr_vl16": "PaddleOCR-VL-1.6-0.9B — no cross-page merge",
    "pred_paddleocr_vl_1.6": "PaddleOCR-VL-1.6-0.9B — no cross-page merge",
    "paddleocr_vl16_crosspage_merged": "PaddleOCR-VL-1.6-0.9B — cross-page merge",
    "pred_paddleocr_vl_1.6_crosspage_merged": "PaddleOCR-VL-1.6-0.9B — cross-page merge",
    "pred_paddleocr_vl16_gpu": "PaddleOCR-VL-1.6-0.9B — no cross-page merge",
    # Legacy collections retained for reproducibility but excluded from the
    # eight-collection headline benchmark.
    "pred_easyocr_gpu": "EasyOCR (legacy)",
    "pred_paddleocr_gpu": "PaddleOCR PP-StructureV3 (legacy)",
}


def collection_label(collection: str) -> str:
    """Return a stable display label while preserving unknown internal names."""

    return COLLECTION_LABELS.get(collection, collection)
