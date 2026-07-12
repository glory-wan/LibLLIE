# Training CLI

Use `train` with an optional YAML config and optional flat overrides:

```bash
libllie train [CONFIG] [--kwargs KEY=VALUE ...]
```

## Train from YAML

```bash
libllie train libllie/deepLearning/config/ZeroDCE.yaml
```

Before training with a built-in template, update at least `data.root_dir` in the YAML file.

## Train with CLI Parameters

```bash
libllie train --kwargs model=ZeroDCE dataset=CommonDataset root_dir=datasets/LOL loss=zerodce optimizer=adam lr=1e-4 epochs=10 batch_size=4 device=cuda
```

## Override YAML Values

```bash
libllie train libllie/deepLearning/config/ZeroDCE.yaml --kwargs epochs=5 batch_size=2 device=cuda
```

CLI overrides are merged into the training configuration.

## List Training Components

```bash
libllie list
```

## Common Overrides

| Key | Meaning |
| --- | --- |
| `model` / `model_name` | Model name |
| `dataset` / `dataset_name` | Dataset name |
| `root_dir` | Dataset root directory |
| `loss` / `loss_name` | Loss function name |
| `optimizer` / `optimizer_name` | Optimizer name |
| `lr` | Learning rate |
| `epochs` | Number of epochs |
| `batch_size` | Batch size |
| `device` | Training device, for example `cuda` or `cpu` |
| `output_dir` | Training output directory |
| `resume` | Checkpoint path for resuming training |

The exact supported parameters depend on the current trainer, model, dataset, and loss configuration.

## Outputs

Training usually writes:

| Output | Meaning |
| --- | --- |
| `checkpoints/last.pt` | Most recently saved checkpoint |
| `checkpoints/best.pt` | Best validation checkpoint |
| Training logs | Losses, metrics, or status information |

Use the saved checkpoint for prediction:

```bash
libllie predict checkpoints/ZeroDCE_CommonDataset/checkpoints/best.pt input.jpg -o results/zerodce_output.png --device cuda
```

## Resume

```bash
libllie train libllie/deepLearning/config/ZeroDCE.yaml --kwargs resume=checkpoints/ZeroDCE_CommonDataset/checkpoints/last.pt
```

## Practical Settings

Use smaller `epochs` and `batch_size` values while debugging. Use YAML files for reproducible experiments. Set `device=cpu` if CUDA is unavailable.
