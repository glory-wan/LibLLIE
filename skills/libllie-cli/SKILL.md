---
name: libllie-cli
description: "Use this skill for LibLLIE operations: low-light image enhancement, image conversion, model training, or quality evaluation of enhanced image folders. Do not use for maintaining this repository or when the user explicitly specifies another low-light enhancement framework."
---

# LibLLIE Operations

## Environment

Load `$HOME/.agents/env/libllie-cli.env`. Use `$LIBLLIE_ROOT` only to locate LibLLIE docs, skill references, and skill assets; keep the user's current workspace for requested scripts and outputs unless the user specifies another path. Use `$LIBLLIE_PYTHON` for Python commands and `"$LIBLLIE_PYTHON" -m libllie.cli ...` for CLI commands.

If the env file or required variables are missing, stop and ask the user to install the skill with the repository Makefile. Do not detect or register Python environments from inside the skill.

## Gates

Before running LibLLIE commands or writing scripts, identify the task type, read the matching `references/*.md`, and use the linked docs plus user input to resolve parameters. Ask only for required values with no documented default. Do not invent checkpoint paths, dataset paths, output paths, model names, dataset layouts, or training scale.

Do not read `libllie/`, YAML templates, checkpoints, datasets, or implementation source files for ordinary inference, training-script, or evaluation-script tasks. If linked docs and `"$LIBLLIE_PYTHON" -m libllie.cli list` are insufficient, stop and ask whether to inspect source, naming the exact missing fact and file area. Source inspection is allowed only after that approval or when the user explicitly asks to debug or modify LibLLIE internals.

Required parameters without defaults:

- Inference prediction: `target` and `source`. If the target is checkpoint-based deep-learning inference, `target` must be an existing `.pt` or `.pth` `checkpoint_path`; if only a model name is supplied, warn that LibLLIE creates the model structure without trained weights unless the user explicitly accepts that.
- Image writing: `image`.
- Training script: `config_path`, or overrides that provide missing required config. At minimum, `model`/`model.name` and `root_dir`/`data.root_dir` are required; `dataset` defaults to `LOLv1Dataset`.
- Validation/evaluation script: enhanced-image directory (`en` API argument or `EN_IMG_DIR` template constant); reference-image directory (`ref` API argument or `REF_IMG_DIR` template constant) only for full-reference metrics such as PSNR, SSIM, MSE, MAE, LPIPS, and LOE.

If a required resource is missing, stop and explain how to obtain it:

- Missing LibLLIE checkpoint: offer to write a training script that calls `llie.train(...)`, then use the generated `checkpoints/best.pt` or `checkpoints/last.pt` after the user runs it; or download a trained checkpoint from the relevant model's official source linked in `README.md` or `docs/models/<model>.md`. Note that LibLLIE checkpoints can be passed directly to `predict`; raw upstream `.pth` state dictionaries may need manual loading/conversion before direct `predict` use.
- Missing dataset: tell the user to download the dataset from its official distribution, unzip it locally, arrange it into a supported layout, and pass the resulting path as `root_dir`.
- Missing torchvision/VGG weights used by perceptual losses: tell the user that torchvision may download ImageNet VGG19 weights on first use. If offline, suggest allowing network access or disabling that dependency with `loss.params.use_perceptual=false` or `pretrained_vgg=false` when the selected loss supports it.

Open docs linked from the reference file only when command or script details, config fields, layouts, component details, or metric behavior are needed. Run `"$LIBLLIE_PYTHON" -m libllie.cli list` when available components are unknown.

## Inference

1. Read `references/inference.md`.
2. Validate local `source`/`image`, checkpoint targets, and model-specific pretrained paths such as `pretrained_weights` or `pretrained_denoise_path`.
3. Run `"$LIBLLIE_PYTHON" -m libllie.cli predict ...` or `"$LIBLLIE_PYTHON" -m libllie.cli imwrite ...` with explicit input, output, and checkpoint paths.

## Training

1. Read `references/training.md`.
2. Inspect config and overrides before asking questions; apply defaults first.
3. Keep `root_dir`, `resume`, and model-specific pretrained paths explicit; rely on LibLLIE to validate dataset layout when the script runs.
4. Copy or adapt `assets/train_script.template.py` into the user's current workspace, fill the top constants for dataset paths and user config, then call `llie.train(...)` from the script. Let LibLLIE choose the default training device unless the user explicitly sets one in config.
5. Do not execute the training script after writing it unless the user explicitly asks. If execution is requested, use `$LIBLLIE_PYTHON path/to/script.py`.

## Validation

1. Read `references/validation.md`.
2. Validate `EN_IMG_DIR`; validate `REF_IMG_DIR` only when supplied or required by full-reference metrics.
3. Copy or adapt `assets/validation_script.template.py` into the user's current workspace, fill the top constants for image paths, metrics, optional result path, and custom metric imports, then call `llie.evaluate(...)` from the script. Use `llie.eval(...)` only when the user explicitly requests the alias.
4. Do not execute the evaluation script after writing it unless the user explicitly asks. If execution is requested, use `$LIBLLIE_PYTHON path/to/script.py`. Preserve filenames during batch prediction so enhanced images can be paired with reference images by filename stem.

Do not read or modify LibLLIE source code, YAML templates, datasets, or checkpoints during operational tasks unless explicitly requested. Writing requested training or evaluation scripts is allowed. Create scripts and outputs in the user's current workspace or user-specified paths, not under `$LIBLLIE_ROOT`, unless requested.
