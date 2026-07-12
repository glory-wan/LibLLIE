---
name: libllie-cli
description: "Use this skill when the user wants to perform low-light image enhancement with traditional algorithms or deep-learning models, train low-light enhancement models, or validate performance metrics for enhanced low-light images."
---

# LibLLIE CLI

## Environment

Load `$HOME/.agents/env/libllie-cli.env`, then operate from `$LIBLLIE_ROOT`. Use `$LIBLLIE_CLI` for CLI commands and `$LIBLLIE_PYTHON` for Python commands.

If the env file or required variables are missing, stop and ask the user to install the skill with the repository Makefile. Do not detect or register Python environments from inside the skill.

## Inference

1. Read `references/inference.md`.
2. Open the CLI docs linked from `inference.md` only when the request needs command details, algorithm/model details, image I/O behavior, or checkpoint guidance.
3. Run `$LIBLLIE_CLI list` when available components are unknown.
4. Run `$LIBLLIE_CLI predict ...` for enhancement or `$LIBLLIE_CLI imwrite ...` for image writing tasks.
5. Use explicit input, output, and checkpoint paths. Prefer a trained `.pt` or `.pth` checkpoint for deep-learning inference unless the user explicitly wants an untrained/model-structure run.

## Training

1. Read `references/training.md`.
2. Open the CLI docs linked from `training.md` when the request needs YAML config fields, CLI override syntax, dataset layout, losses, or model-specific details.
3. Confirm dataset layout, device, epochs, batch size, config file, and output directory before launching a long run.
4. Run `$LIBLLIE_CLI list` when available models, losses, or datasets are unknown.
5. Run `$LIBLLIE_CLI train ...` with a YAML config and explicit overrides as needed. Use small debug values first when the user has not specified experiment scale.

## Validation

1. Read `references/validation.md`.
2. Open the CLI docs linked from `validation.md` when the request needs metric names, full-reference/no-reference behavior, or evaluator options.
3. Confirm enhanced image directory, reference image directory when required, metrics, and output location.
4. Run `$LIBLLIE_CLI list` when available metrics are unknown.
5. Run `$LIBLLIE_CLI evaluate ...` or `$LIBLLIE_CLI eval ...`. Preserve filenames during batch prediction so enhanced images can be paired with reference images by filename stem.

Do not modify LibLLIE source code, YAML templates, datasets, or checkpoints unless the user asks for code/config changes. When only operating the codebase, create outputs under user-specified paths or a clearly named results/checkpoints directory.
