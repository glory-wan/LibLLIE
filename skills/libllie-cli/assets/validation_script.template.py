"""LibLLIE validation script template.

Copy this file into the user's workspace, fill the constants near the top,
then run it with the skill's configured Python:

    $LIBLLIE_PYTHON path/to/validation_script.py
"""

import importlib
from pathlib import Path
from typing import Any, Dict, List, Optional

import libllie as llie


# ---------------------------------------------------------------------------
# 1. USER IMAGE PATHS
# ---------------------------------------------------------------------------
# Use REF_IMG_DIR=None for no-reference metrics such as NIQE, MUSIQ, or PI.
EN_IMG_DIR = Path("path/to/enhanced/images")
REF_IMG_DIR: Optional[Path] = Path("path/to/reference/images")
SAVE_PATH: Optional[Path] = Path("path/to/evaluation.json")


# ---------------------------------------------------------------------------
# 2. USER METRICS
# ---------------------------------------------------------------------------
# Full-reference metrics need REF_IMG_DIR. No-reference metrics do not.
METRICS: List[str] = ["PSNR", "SSIM"]
FULL_REFERENCE_METRICS = {"PSNR", "SSIM", "MSE", "MAE", "LPIPS", "LOE"}


# ---------------------------------------------------------------------------
# 3. USER EVALUATOR OPTIONS
# ---------------------------------------------------------------------------
# Import custom metric modules before llie.evaluate() so they are registered.
CUSTOM_METRIC_MODULES: List[str] = []
RETURN_EVALUATOR = False
EVALUATOR_KWARGS: Dict[str, Any] = {}


def validate_paths() -> None:
    if not EN_IMG_DIR.is_dir():
        raise FileNotFoundError(f"Enhanced image directory not found: {EN_IMG_DIR}")

    if REF_IMG_DIR is not None and not REF_IMG_DIR.is_dir():
        raise FileNotFoundError(f"Reference image directory not found: {REF_IMG_DIR}")

    if REF_IMG_DIR is None and any(metric.upper() in FULL_REFERENCE_METRICS for metric in METRICS):
        raise ValueError("Full-reference metrics require REF_IMG_DIR.")

    if SAVE_PATH is not None:
        SAVE_PATH.parent.mkdir(parents=True, exist_ok=True)


def main() -> None:
    validate_paths()

    for module_name in CUSTOM_METRIC_MODULES:
        importlib.import_module(module_name)

    results = llie.evaluate(
        en=str(EN_IMG_DIR),
        ref=None if REF_IMG_DIR is None else str(REF_IMG_DIR),
        metrics=METRICS,
        save_path=None if SAVE_PATH is None else str(SAVE_PATH),
        return_evaluator=RETURN_EVALUATOR,
        **EVALUATOR_KWARGS,
    )
    print(results)


if __name__ == "__main__":
    main()
