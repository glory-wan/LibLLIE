# LibLLIE CLI Overview

After installation, both entry points run the same CLI:

```bash
libllie ...
llie ...
```

## Commands

| Command | Purpose |
| --- | --- |
| `list` | Show available models, algorithms, metrics, losses, and datasets |
| `predict` | Enhance an image or image folder |
| `train` | Start training from YAML or CLI overrides |
| `evaluate` / `eval` | Compute quality metrics for enhanced images |
| `imwrite` | Save or convert an image |

Image reading is not exposed as a standalone CLI command.

## List Components

```bash
libllie list
```

## Basic Workflow

Save or convert an image:

```bash
libllie imwrite input.jpg -o results/copy.png
```

Enhance with a traditional algorithm:

```bash
libllie predict gcp input.jpg -o results/gcp_output.png
```

Enhance with a trained deep-learning checkpoint:

```bash
libllie predict checkpoints/ZeroDCE_CommonDataset/checkpoints/best.pt input.jpg -o results/zerodce_output.png --device cuda
```

Passing only a model name such as `ZeroDCE` creates the model structure but does not automatically load trained weights. For useful prediction, pass a trained `.pt` or `.pth` checkpoint.

Train from a YAML configuration:

```bash
libllie train libllie/deepLearning/config/ZeroDCE.yaml
```

Evaluate enhanced images:

```bash
libllie evaluate --en-img-dir results/ZeroDCE --ref-img-dir datasets/LOL/eval15/high --metrics PSNR SSIM --save-path results/eval.json
```

## Reading Order

1. `docs-cli/guide/image_io.md`
2. `docs-cli/guide/predict.md`
3. `docs-cli/guide/train.md`
4. `docs-cli/guide/evaluate.md`
