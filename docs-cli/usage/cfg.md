# Training Configuration CLI

Training uses YAML files plus optional CLI overrides:

```bash
libllie train CONFIG.yaml --kwargs KEY=VALUE ...
```

Built-in templates live in `libllie/deepLearning/config/`. Before using a template, update at least `data.root_dir`.

```yaml
data:
  root_dir: path/to/your/dataset/dir
```

Then run:

```bash
libllie train libllie/deepLearning/config/ZeroDCE.yaml
```

## Built-in Templates

| File | Model | Dataset template | Loss |
| --- | --- | --- | --- |
| `DarkIR.yaml` | `DarkIR` | `CommonDataset` | `darkir` |
| `EnlightenGAN.yaml` | `EnlightenGAN` | `CommonDataset` | `enlightengan` |
| `KinD++.yaml` | `KinDPlusPlus` | `CommonDataset` | `kind++` |
| `KinD.yaml` | `KinD` | `CommonDataset` | `kind` |
| `LEDNet.yaml` | `LEDNet` | `CommonDataset` | `lednet` |
| `LLNet.yaml` | `LLNet` | `CommonDataset` | `llnet` |
| `LLFlow.yaml` | `LLFlow` | `CommonDataset` | `llflow` |
| `RetinexFormer.yaml` | `RetinexFormer` | `CommonDataset` | `retinexformer` |
| `RUAS.yaml` | `RUAS` | `LOLv1Dataset` | `ruas_loss` |
| `SCI.yaml` | `SCI` | `LOLv1Dataset` | `sci_loss` |
| `URetinexNet.yaml` | `URetinexNet` | `CommonDataset` | `uretinex` |
| `ZeroDCE++.yaml` | `ZeroDCEPlusPlus` | `LOLv1Dataset` | `zerodce++` |
| `ZeroDCE.yaml` | `ZeroDCEPlusPlus` | `LOLv1Dataset` | `zerodce_loss` |
| `ZeroIG.yaml` | `ZeroIG` | `CommonDataset` | `zeroig` |

## YAML Shape

```yaml
model:
  name: ZeroDCEPlusPlus
  params: {}

data:
  dataset: LOLv1Dataset
  root_dir: path/to/your/dataset/dir
  train_split: train
  val_split: _test
  batch_size: 4
  num_workers: 4
  pin_memory: true
  return_filename: true

loss:
  name: zerodce_loss
  params: {}
  output_index: null
  output_key: null

optimizer:
  name: adam
  lr: 0.0001
  params: {}

scheduler:
  name: cosineannealinglr
  params: {}

train:
  epochs: 100
  device: cuda
  output_dir: null
  save_every: 1
  validate_every: 1
  log_every: 10
  grad_clip: 1.0
  amp: false
  seed: 42
  resume: null
```

## Section Fields

| Section | Common fields |
| --- | --- |
| `model` | `name`, `params` |
| `data` | `dataset`, `root_dir`, `batch_size`, `num_workers`, `pin_memory`, `shuffle`, `drop_last`, `train_split`, `val_split`, `return_filename`, `params`, `train_params`, `val_params` |
| `data` directory overrides | `train_low_dir`, `train_high_dir`, `val_low_dir`, `val_high_dir` |
| `loss` | `name`, `params`, `output_index`, `output_key` |
| `optimizer` | `name`, `lr`, `params` |
| `scheduler` | `name`, `params` |
| `train` | `epochs`, `output_dir`, `save_every`, `validate_every`, `log_every`, `grad_clip`, `amp`, `resume`, `seed`, `device` |

Supported optimizer names are `adam`, `adamw`, `sgd`, and `rmsprop`. Supported scheduler names are `steplr`, `multisteplr`, `cosineannealinglr`, and `reducelronplateau`; `null` disables scheduler construction.

## CLI Overrides

Pass flat overrides with `--kwargs`:

```bash
libllie train libllie/deepLearning/config/ZeroDCE.yaml --kwargs root_dir=datasets/LOL epochs=5 batch_size=2 device=cpu
```

Common mappings:

| Flat key | Config location |
| --- | --- |
| `model`, `model_name` | `model.name` |
| `model_params` | `model.params` |
| `dataset`, `dataset_name` | `data.dataset` |
| `root_dir` | `data.root_dir` |
| `batch_size` | `data.batch_size` |
| `num_workers` | `data.num_workers` |
| `train_split` | `data.train_split` |
| `val_split` | `data.val_split` |
| `loss`, `loss_name` | `loss.name` |
| `loss_params` | `loss.params` |
| `optimizer`, `optimizer_name` | `optimizer.name` |
| `lr` | `optimizer.lr` |
| `optimizer_params` | `optimizer.params` |
| `scheduler`, `scheduler_name` | `scheduler.name` |
| `scheduler_params` | `scheduler.params` |
| `epochs` | `train.epochs` |
| `output_dir` | `train.output_dir` |
| `save_every` | `train.save_every` |
| `validate_every` | `train.validate_every` |
| `log_every` | `train.log_every` |
| `grad_clip` | `train.grad_clip` |
| `amp` | `train.amp` |
| `resume` | `train.resume` |
| `seed` | `train.seed` |
| `device` | `train.device` |

## Minimal Config

```yaml
model:
  name: ZeroDCE

data:
  dataset: CommonDataset
  root_dir: datasets/LOL

loss:
  name: zerodce_loss

train:
  epochs: 10
  device: cuda
```

Run it with:

```bash
libllie train config.yaml
```

## Resume

Set `train.resume` in YAML or pass:

```bash
libllie train libllie/deepLearning/config/ZeroDCE.yaml --kwargs resume=checkpoints/ZeroDCE_CommonDataset/checkpoints/last.pt
```
