---
name: libllie-cli
description: "Use this skill when the user wants to perform low-light image enhancement with traditional algorithms or deep-learning models, train low-light enhancement models, or validate performance metrics for enhanced low-light images."
---

# LibLLIE CLI

## Environment

Load `$HOME/.agents/env/libllie-cli.env`, then operate from `$LIBLLIE_ROOT`. Use `$LIBLLIE_CLI` for CLI commands and `$LIBLLIE_PYTHON` for Python commands.

If the env file or required variables are missing, stop and ask the user to install the skill with the repository Makefile. Do not detect or register Python environments from inside the skill.

## Parameter and Resource Gates

Before running LibLLIE commands, identify the task type and required parameters from the CLI/API docs and code defaults. If a required parameter with no default value is missing or ambiguous, stop and ask for the missing parameter names. Do not invent checkpoint paths, dataset paths, output paths, model names, dataset layouts, or training scale. Do not ask for parameters that have documented/code defaults unless the user explicitly wants to override those defaults.

Required parameters without defaults:

- Inference prediction: `target` and `source`. If the target is checkpoint-based deep-learning inference, `target` must be an existing `.pt` or `.pth` `checkpoint_path`; if only a model name is supplied, warn that LibLLIE creates the model structure without trained weights unless the user explicitly accepts that.
- Image writing: `image`.
- Training: either a `config_path` that already supplies required config, or enough overrides to supply missing required config fields. At minimum, the trainer needs `model`/`model.name` and `root_dir`/`data.root_dir`; `dataset` has a default (`LOLv1Dataset`) and should only be requested when the user needs a non-default dataset. Inspect a provided config before asking for missing fields.
- Validation/evaluation: `en_img_dir`. Require `ref_img_dir` only when the requested metrics need reference images, such as PSNR, SSIM, MSE, MAE, LPIPS, and LOE.

If a required resource is missing, stop and explain how to obtain it:

- Missing LibLLIE checkpoint: tell the user to train with `$LIBLLIE_CLI train ...` and use the generated `checkpoints/best.pt` or `checkpoints/last.pt`, or download a trained checkpoint from the relevant model's official source linked in `README.md` or `docs/models/<model>.md`. Note that LibLLIE checkpoints can be passed directly to `predict`; raw upstream `.pth` state dictionaries may need manual loading/conversion before direct `predict` use.
- Missing dataset: tell the user to download the dataset from its official distribution, unzip it locally, arrange it into a supported layout, and pass the resulting path as `root_dir`. For `LOLv1Dataset`, expect layouts such as `our485/low`, `our485/high`, `eval15/low`, and `eval15/high`. For `CommonDataset`, expect paired folders such as `train/low` with `train/high`, `train/normal`, or `train/target`.
- Missing torchvision/VGG weights used by perceptual losses: tell the user that torchvision may download ImageNet VGG19 weights on first use. If offline, suggest allowing network access or disabling that dependency with `loss.params.use_perceptual=false` or `pretrained_vgg=false` when the selected loss supports it.

## Inference

1. Read `references/inference.md`.
2. Open the CLI docs linked from `inference.md` only when the request needs command details, algorithm/model details, image I/O behavior, or checkpoint guidance.
3. Run `$LIBLLIE_CLI list` when available components are unknown.
4. Before checkpoint-based prediction, validate `checkpoint_path`. Before local image/folder prediction or image writing, validate local `source` or `image` paths. If config overrides include model-specific pretrained paths such as `pretrained_weights` or `pretrained_denoise_path`, validate those paths too.
5. Run `$LIBLLIE_CLI predict ...` for enhancement or `$LIBLLIE_CLI imwrite ...` for image writing tasks.
6. Use explicit input, output, and checkpoint paths. Prefer a trained `.pt` or `.pth` checkpoint for deep-learning inference unless the user explicitly wants an untrained/model-structure run.

## Training

1. Read `references/training.md`.
2. Open the CLI docs linked from `training.md` when the request needs YAML config fields, CLI override syntax, dataset layout, losses, or model-specific details.
3. Inspect the config and overrides before asking questions. Ask only for required fields that are missing after defaults and config values are applied.
4. Before launching a long run, validate `root_dir`, explicit dataset directories such as `train_low_dir`, `train_high_dir`, `val_low_dir`, and `val_high_dir`, `resume_path` when resuming, and model-specific pretrained paths such as `pretrained_weights` or `pretrained_denoise_path`.
5. Run `$LIBLLIE_CLI list` when available models, losses, or datasets are unknown.
6. Run `$LIBLLIE_CLI train ...` with a YAML config and explicit overrides as needed. Use small debug values first when the user has not specified experiment scale.

## Validation

1. Read `references/validation.md`.
2. Open the CLI docs linked from `validation.md` when the request needs metric names, full-reference/no-reference behavior, or evaluator options.
3. Validate `en_img_dir`. Validate `ref_img_dir` only when supplied or required by full-reference metrics.
4. Run `$LIBLLIE_CLI list` when available metrics are unknown.
5. Run `$LIBLLIE_CLI evaluate ...` or `$LIBLLIE_CLI eval ...`. Preserve filenames during batch prediction so enhanced images can be paired with reference images by filename stem.

Do not modify LibLLIE source code, YAML templates, datasets, or checkpoints unless the user asks for code/config changes. When only operating the codebase, create outputs under user-specified paths or a clearly named results/checkpoints directory.
