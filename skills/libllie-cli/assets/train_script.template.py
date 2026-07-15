"""LibLLIE training script template.

Copy this file into the user's workspace, fill the constants near the top,
then run it with the skill's configured Python:

    $LIBLLIE_PYTHON path/to/train_script.py
"""

from pathlib import Path
from typing import Any, Dict, Optional

import libllie as llie


# ---------------------------------------------------------------------------
# 1. USER DATASET PATH
# ---------------------------------------------------------------------------
# Replace this path with the user's dataset root.
ROOT_DIR = Path("path/to/dataset/root")


# ---------------------------------------------------------------------------
# 2. USER CONFIG
# ---------------------------------------------------------------------------
# Option A: set CONFIG_PATH to a user-provided YAML config.
# Option B: leave CONFIG_PATH as None and edit the inline config values below.
CONFIG_PATH: Optional[Path] = None

OUTPUT_DIR: Optional[Path] = Path("path/to/output")
RESUME_PATH: Optional[Path] = None

CONFIG: Dict[str, Any] = {
    "model": {
        "name": "ZeroDCE",
        "params": {},
    },
    "data": {
        "dataset": "LOLv1Dataset",
        "root_dir": str(ROOT_DIR),
        "train_split": "train",
        "val_split": "val",
        "batch_size": 4,
        "num_workers": 0,
        "pin_memory": False,
        "return_filename": True,
    },
    "loss": {
        "name": "zerodce_loss",
        "params": {},
    },
    "train": {
        "amp": False,
        "epochs": 100,
        "output_dir": None,
        "resume": None,
        "save_every": 1,
        "validate_every": 1,
        "log_every": 10,
    },
}


# ---------------------------------------------------------------------------
# 3. START TRAINING
# ---------------------------------------------------------------------------
def main() -> None:
    if CONFIG_PATH is not None:
        overrides = {
            "root_dir": str(ROOT_DIR),
        }
        if OUTPUT_DIR is not None:
            overrides["output_dir"] = str(OUTPUT_DIR)
        if RESUME_PATH is not None:
            overrides["resume"] = str(RESUME_PATH)
        result = llie.train(str(CONFIG_PATH), **overrides)
    else:
        CONFIG["train"]["output_dir"] = None if OUTPUT_DIR is None else str(OUTPUT_DIR)
        CONFIG["train"]["resume"] = None if RESUME_PATH is None else str(RESUME_PATH)
        result = llie.train(CONFIG)

    print(result)


if __name__ == "__main__":
    main()
