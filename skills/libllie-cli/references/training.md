# Training

Use this index for training low-light enhancement models and managing training configuration. When executing examples from `docs-cli`, use `$LIBLLIE_CLI` in place of `libllie`.

## CLI Functions

- `$LIBLLIE_CLI list`: Lists available models, losses, and datasets before choosing a training setup.
- `$LIBLLIE_CLI train ...`: Trains a low-light enhancement model from a YAML config.
- `--kwargs KEY=VALUE ...`: Overrides training config fields from the CLI.
- `--help`: Shows available training CLI arguments.

## CLI Docs Index

### Guide

- [docs-cli/guide/overview.md](../../../docs-cli/guide/overview.md): CLI overview for listing components, prediction, training, evaluation, and image writing.
- [docs-cli/guide/train.md](../../../docs-cli/guide/train.md): CLI training workflow, config use, overrides, validation, checkpoints, and resume.

### Usage

- [docs-cli/usage/cli.md](../../../docs-cli/usage/cli.md): Compact reference for `train` and shared CLI options.
- [docs-cli/usage/cfg.md](../../../docs-cli/usage/cfg.md): YAML training configuration fields, templates, and CLI override rules.

### Deep-Learning Models

- [docs-cli/models/zero-dce.md](../../../docs-cli/models/zero-dce.md): Zero-DCE CLI prediction and training entry points.
- [docs-cli/models/zero-dce++.md](../../../docs-cli/models/zero-dce++.md): Zero-DCE++ CLI prediction and training entry points.
- [docs-cli/models/sci.md](../../../docs-cli/models/sci.md): SCI CLI prediction and training entry points.
- [docs-cli/models/ruas.md](../../../docs-cli/models/ruas.md): RUAS CLI prediction and training entry points.
- [docs-cli/models/uretinex-net.md](../../../docs-cli/models/uretinex-net.md): URetinex-Net CLI prediction and training entry points.
- [docs-cli/models/retinexformer.md](../../../docs-cli/models/retinexformer.md): RetinexFormer CLI prediction and training entry points.
- [docs-cli/models/lednet.md](../../../docs-cli/models/lednet.md): LEDNet CLI prediction and training entry points.
- [docs-cli/models/zero-ig.md](../../../docs-cli/models/zero-ig.md): Zero-IG CLI prediction and training entry points.
- [docs-cli/models/darkir.md](../../../docs-cli/models/darkir.md): DarkIR CLI prediction and training entry points.
- [docs-cli/models/llnet.md](../../../docs-cli/models/llnet.md): LLNet CLI prediction and training entry points.
- [docs-cli/models/kind.md](../../../docs-cli/models/kind.md): KinD CLI prediction and training entry points.
- [docs-cli/models/kind++.md](../../../docs-cli/models/kind++.md): KinD++ CLI prediction and training entry points.
- [docs-cli/models/enlightengan.md](../../../docs-cli/models/enlightengan.md): EnlightenGAN CLI prediction and training entry points.
- [docs-cli/models/llflow.md](../../../docs-cli/models/llflow.md): LLFlow CLI prediction and training entry points.
- [docs-cli/models/cidnet.md](../../../docs-cli/models/cidnet.md): HVI-CIDNet CLI prediction and training entry points.
- [docs-cli/models/pairlie.md](../../../docs-cli/models/pairlie.md): PairLIE CLI prediction and training entry points.
- [docs-cli/models/llformer.md](../../../docs-cli/models/llformer.md): LLFormer CLI prediction and training entry points.

### Custom Components

- [docs-cli/custom/model.md](../../../docs-cli/custom/model.md): CLI use of registered custom deep-learning models.
- [docs-cli/custom/loss.md](../../../docs-cli/custom/loss.md): CLI use of registered custom training losses.
- [docs-cli/custom/dataset.md](../../../docs-cli/custom/dataset.md): CLI use of registered custom datasets.
