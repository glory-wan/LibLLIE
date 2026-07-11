# Prediction CLI

Use `predict` for traditional algorithms, model names, and checkpoints:

```bash
libllie predict TARGET SOURCE [-o OUTPUT] [options] [--kwargs KEY=VALUE ...]
```

`TARGET` is an algorithm name, model name, or `.pt`/`.pth` checkpoint path. `SOURCE` is an image path or image folder.

## List Targets

```bash
libllie list
```

## Traditional Algorithm

Single image:

```bash
libllie predict he input.jpg -o results/he_output.jpg
```

Folder batch prediction:

```bash
libllie predict gcp images/ -o results/gcp
```

Batch prediction reads image files from the folder and preserves original file names and suffixes.

## Algorithm Parameters

Pass algorithm parameters through `--kwargs`:

```bash
libllie predict clahe input.jpg -o results/clahe_output.png --kwargs color_space=lab clip_limit=2.0 "tile_grid_size=(8, 8)"
```

```bash
libllie predict gcp input.jpg -o results/gcp_output.png --kwargs gamma_max=5.0 erosion_window=11
```

Quote tuple or list values in your shell.

## Deep-Learning Model

Using only a model name creates the network structure but does not automatically load trained weights:

```bash
libllie predict ZeroDCE input.jpg -o results/zerodce_output.png --device cuda
```

For practical prediction, pass a trained checkpoint:

```bash
libllie predict checkpoints/ZeroDCE_CommonDataset/checkpoints/best.pt input.jpg -o results/zerodce_output.png --device cuda
```

The checkpoint must contain model class and parameter information saved by the training pipeline.

## Folder Prediction

```bash
libllie predict checkpoints/ZeroDCE_CommonDataset/checkpoints/best.pt images/ -o results/zerodce --device cuda
```

Output behavior:

| Input and output | Behavior |
| --- | --- |
| Single image with file output | Save to the specified file |
| Single image with folder output | Save in the folder with the original image name |
| Folder input with folder output | Batch save while preserving original names and relative directories |
| Folder input with no output | Save to `results/{model name or algorithm name}` |

## Do Not Save

For single-image prediction, disable saving with:

```bash
libllie predict gcp input.jpg --no-save
```

## Options

| Option | Meaning |
| --- | --- |
| `-o`, `--output` | Output file path or folder |
| `--backend` | Predictor backend: `auto`, `deep`, or `traditional` |
| `--device` | Device used by deep-learning prediction |
| `--output-dir` | Default predictor output directory |
| `--no-progress` | Disable progress bar for folder prediction |
| `--no-save` | Do not save single-image prediction output |
| `--output-name` | Output file name when saving to a folder |
| `--output-ext` | Output extension override |
| `--kwargs KEY=VALUE ...` | Extra parameters forwarded to prediction |

## Troubleshooting

Run `libllie list` when a model, algorithm, or metric name is not found. If folder prediction produces no output, confirm the folder exists and contains supported image suffixes such as `.jpg`, `.png`, `.bmp`, or `.tif`.
