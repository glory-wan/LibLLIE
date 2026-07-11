# Evaluation CLI

Use `evaluate` or `eval` to compute quality metrics for enhanced image folders:

```bash
libllie evaluate --en-img-dir EN_DIR [--ref-img-dir REF_DIR] [--metrics METRIC ...] [--save-path PATH]
```

## List Metrics

```bash
libllie list
```

## Full-Reference Evaluation

Use reference images for metrics such as PSNR and SSIM:

```bash
libllie evaluate --en-img-dir results/ZeroDCE --ref-img-dir datasets/LOL/eval15/high --metrics PSNR SSIM --save-path results/eval_full_reference.json
```

Enhanced images and reference images must be matchable by file name or by the evaluator matching rules.

## No-Reference Evaluation

When no reference images are available, omit `--ref-img-dir` and choose no-reference metrics:

```bash
libllie evaluate --en-img-dir results/ZeroDCE --metrics NIQE --save-path results/eval_no_reference.json
```

Available no-reference metrics depend on installed dependencies and registered metrics.

## Multiple Metrics

```bash
libllie evaluate --en-img-dir results/ZeroDCE --ref-img-dir datasets/LOL/eval15/high --metrics PSNR SSIM LOE
```

If `--metrics` is omitted, the evaluator uses its default metric settings.

## Extra Evaluator Parameters

Pass additional evaluator parameters through `--kwargs`:

```bash
libllie evaluate --en-img-dir results/ZeroDCE --metrics PSNR SSIM --kwargs device=cpu
```

## Prediction and Evaluation

```bash
libllie predict checkpoints/ZeroDCE_CommonDataset/checkpoints/best.pt datasets/LOL/eval15/low -o results/ZeroDCE --device cuda
libllie evaluate --en-img-dir results/ZeroDCE --ref-img-dir datasets/LOL/eval15/high --metrics PSNR SSIM --save-path results/ZeroDCE_eval.json
```

## Troubleshooting

Run `libllie list` when a metric is unavailable. If results are empty, check that enhanced and reference image names can be matched and that batch prediction preserved the original names.
