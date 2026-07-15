# Training

Use this index for writing Python training scripts for low-light enhancement models and managing training configuration. Training tasks should create or edit a script that calls `llie.train(...)`; do not execute the script unless the user explicitly asks.

Links in this file are documentation links under `$LIBLLIE_ROOT`; open only the linked Markdown docs needed for the task. Do not follow implementation/source paths mentioned by those docs unless the user explicitly approves source inspection.

## Script Workflow

- Import `libllie as llie`.
- Start new scripts from [assets/train_script.template.py](../assets/train_script.template.py), copying or adapting it into the user's current workspace rather than editing the asset in place.
- Fill the template's top constants for `ROOT_DIR` and user config before the helper functions.
- Use `llie.train(config_path, **overrides)` when the user provides a YAML config; include `root_dir` in overrides when the dataset path is supplied outside the config.
- Use `llie.train(**kwargs)` or `llie.train(config_dict)` when the user provides fields directly.
- Keep dataset, checkpoint, output, resume, and pretrained paths explicit.
- Do not call `libllie train` for training tasks. If the user asks to run the finished script, execute it with `$LIBLLIE_PYTHON path/to/script.py`.

## API Docs Index

### Guide

- [docs/guide/overview.md](../../../docs/guide/overview.md): Python API overview for listing components, prediction, training, evaluation, and image writing.
- [docs/guide/train.md](../../../docs/guide/train.md): Python training workflow, config use, overrides, checkpoints, and resume.

### Usage

- [docs/usage/cfg.md](../../../docs/usage/cfg.md): YAML training configuration fields, templates, defaults, and flat override mappings.

### Deep-Learning Models

- [docs/models/zero-dce.md](../../../docs/models/zero-dce.md): Zero-DCE model-specific training notes.
- [docs/models/zero-dce++.md](../../../docs/models/zero-dce++.md): Zero-DCE++ model-specific training notes.
- [docs/models/sci.md](../../../docs/models/sci.md): SCI model-specific training notes.
- [docs/models/ruas.md](../../../docs/models/ruas.md): RUAS model-specific training notes.
- [docs/models/uretinex-net.md](../../../docs/models/uretinex-net.md): URetinex-Net model-specific training notes.
- [docs/models/retinexformer.md](../../../docs/models/retinexformer.md): RetinexFormer model-specific training notes.
- [docs/models/lednet.md](../../../docs/models/lednet.md): LEDNet model-specific training notes.
- [docs/models/zero-ig.md](../../../docs/models/zero-ig.md): Zero-IG model-specific training notes.
- [docs/models/darkir.md](../../../docs/models/darkir.md): DarkIR model-specific training notes.
- [docs/models/llnet.md](../../../docs/models/llnet.md): LLNet model-specific training notes.
- [docs/models/kind.md](../../../docs/models/kind.md): KinD model-specific training notes.
- [docs/models/kind++.md](../../../docs/models/kind++.md): KinD++ model-specific training notes.
- [docs/models/enlightengan.md](../../../docs/models/enlightengan.md): EnlightenGAN model-specific training notes.
- [docs/models/llflow.md](../../../docs/models/llflow.md): LLFlow model-specific training notes.
- [docs/models/cidnet.md](../../../docs/models/cidnet.md): HVI-CIDNet model-specific training notes.
- [docs/models/pairlie.md](../../../docs/models/pairlie.md): PairLIE model-specific training notes.
- [docs/models/llformer.md](../../../docs/models/llformer.md): LLFormer model-specific training notes.

### Custom Components

- [docs/custom/model.md](../../../docs/custom/model.md): Custom deep-learning model extension guide from the README Extension System table.
- [docs/custom/loss.md](../../../docs/custom/loss.md): Custom training loss extension guide from the README Extension System table.
- [docs/custom/dataset.md](../../../docs/custom/dataset.md): Custom dataset extension guide from the README Extension System table.
- [docs/custom/algorithm.md](../../../docs/custom/algorithm.md): Custom traditional algorithm extension guide from the README Extension System table.
- [docs/custom/metric.md](../../../docs/custom/metric.md): Custom evaluation metric extension guide from the README Extension System table.
