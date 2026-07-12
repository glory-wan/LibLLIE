# Validation

Use this index for writing Python evaluation scripts that validate enhanced low-light images with image-quality metrics. Validation tasks should create or edit a script that calls `llie.evaluate(...)`; do not execute the script unless the user explicitly asks.

Links in this file are documentation links under `$LIBLLIE_ROOT`; open only the linked Markdown docs needed for the task. Do not follow implementation/source paths mentioned by those docs unless the user explicitly approves source inspection.

## Script Workflow

- Import `libllie as llie`.
- Start new scripts from [assets/validation_script.template.py](../assets/validation_script.template.py), copying or adapting it into the user's current workspace rather than editing the asset in place.
- Fill the template's top constants for enhanced-image directory, optional reference-image directory, metrics, optional save path, custom metric modules, and evaluator kwargs.
- Use `llie.evaluate(en=..., ref=..., metrics=..., save_path=..., **kwargs)` for evaluation scripts; include `save_path` only when the user requests saved results or provides a result path.
- Use `llie.eval(...)` only when the user explicitly requests the alias.
- Keep enhanced-image, reference-image, save-result, and custom metric import paths explicit.
- Do not call `libllie evaluate` or `libllie eval` for validation tasks. If the user asks to run the finished script, execute it with `$LIBLLIE_PYTHON path/to/script.py`.
- Preserve filenames during batch prediction so enhanced images can be paired with reference images by filename stem.

## Metric Reference Needs

| Metrics | Reference images | Notes |
| --- | --- | --- |
| `PSNR`, `SSIM`, `MSE`, `MAE`, `LPIPS`, `LOE` | Required | `LPIPS` uses `pyiqa` and may load model weights on first use. |
| `NIQE`, `MUSIQ`, `PI` | Not required | These use `pyiqa` and may load model weights on first use. |

## API Docs Index

### Guide

- [docs/guide/overview.md](../../../docs/guide/overview.md): Python API overview for listing components, prediction, training, evaluation, and image writing.
- [docs/guide/evaluate.md](../../../docs/guide/evaluate.md): Python evaluation workflow, full-reference and no-reference metrics, saving results, and evaluator access.

### Custom Components

- [docs/custom/metric.md](../../../docs/custom/metric.md): Custom evaluation metric extension guide and custom metric import behavior.
