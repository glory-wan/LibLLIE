# LibLLIE CLI Reference

Both installed commands point to the same CLI:

```bash
libllie ...
llie ...
```

## Commands

| Command | Purpose |
| --- | --- |
| `list` | List available models, algorithms, metrics, losses, and datasets |
| `predict` | Run enhancement |
| `train` | Train a model |
| `evaluate` / `eval` | Evaluate enhanced images |
| `imwrite` | Save or convert an image |

## List

```bash
libllie list
```

## Predict

```bash
libllie predict gcp input.jpg -o results/gcp/output.png
libllie predict checkpoints/ZeroDCE_CommonDataset/checkpoints/best.pt input.jpg -o results/zerodce/output.png --device cuda
libllie predict bimef images/ -o results/bimef
```

Useful options:

| Option | Meaning |
| --- | --- |
| `--backend` | `auto`, `deep`, or `traditional` |
| `--device` | Device for deep-learning prediction |
| `--output-dir` | Default predictor output directory |
| `--no-progress` | Disable folder progress bar |
| `--no-save` | Do not save single-image output |
| `--output-name` | Output file name when saving to a folder |
| `--output-ext` | Output extension override |
| `--kwargs KEY=VALUE ...` | Extra prediction parameters |

Examples with extra parameters:

```bash
libllie predict lime input.jpg -o results/lime.png --kwargs gamma=0.8 guided_radius=15
libllie predict clahe input.jpg -o results/clahe.png --kwargs "tile_grid_size=(8, 8)" clip_limit=2.0
```

## Train

```bash
libllie train libllie/deepLearning/config/ZeroDCE.yaml
libllie train libllie/deepLearning/config/ZeroDCE.yaml --kwargs epochs=5 batch_size=2 device=cpu
```

`--kwargs` entries are forwarded to training.

## Evaluate

```bash
libllie evaluate --en-img-dir results/ZeroDCE --ref-img-dir datasets/LOL/eval15/high --metrics PSNR SSIM --save-path results/eval.json
libllie evaluate --en-img-dir results/ZeroDCE --metrics NIQE --save-path results/eval_no_ref.json
libllie evaluate --en-img-dir results/ZeroDCE --metrics PSNR SSIM --kwargs device=cpu
```

## Imwrite

```bash
libllie imwrite input.jpg -o results/copy.png
libllie imwrite input.jpg -o results --output-name copied.png
libllie imwrite input.jpg -o results/copied --save-format png
```

## KEY=VALUE Parsing

`--kwargs` supports simple Python-like values:

```bash
--kwargs lr=1e-4 epochs=10 amp=false device=cpu
```

| Input | Parsed value |
| --- | --- |
| `true` / `false` | Boolean |
| `none` | `None` |
| `10`, `1e-4`, `(8, 8)` | Python literal value |
| Other strings | Raw string |

## Help

```bash
libllie --help
libllie predict --help
libllie train --help
libllie evaluate --help
libllie imwrite --help
```
