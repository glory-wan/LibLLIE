# LibLLIE CLI Overview

After installation, both entry points run the same CLI:

```bash
libllie ...
llie ...
```

## Commands

| Command | Purpose |
| --- | --- |
| `list` | Show available registered components |
| `predict` | Enhance an image or image folder |
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

## Reading Order

1. `docs-cli/guide/image_io.md`
2. `docs-cli/guide/predict.md`
