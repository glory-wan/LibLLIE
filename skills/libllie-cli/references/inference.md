# Inference

Use this index for low-light enhancement inference with traditional algorithms, deep-learning model names, trained checkpoints, single images, folders, and image I/O. When executing examples from `docs-cli`, use `$LIBLLIE_CLI` in place of `libllie`.

## CLI Functions

- `$LIBLLIE_CLI list`: Lists available models and traditional algorithms before choosing an inference target.
- `$LIBLLIE_CLI predict ...`: Enhances a single image or image folder with an algorithm, model name, or checkpoint.
- `$LIBLLIE_CLI imwrite ...`: Saves or converts image inputs with LibLLIE image writing utilities.
- `--kwargs KEY=VALUE ...`: Passes algorithm, predictor, or output options to `predict`.
- `--help`: Shows available inference-related CLI arguments.

## CLI Docs Index

### Guide

- [docs-cli/guide/overview.md](../../../docs-cli/guide/overview.md): CLI overview for listing components, prediction, training, evaluation, and image writing.
- [docs-cli/guide/image_io.md](../../../docs-cli/guide/image_io.md): CLI image writing and supported image-source behavior.
- [docs-cli/guide/predict.md](../../../docs-cli/guide/predict.md): CLI prediction for algorithms, model names, checkpoints, folders, and prediction options.

### Usage

- [docs-cli/usage/cli.md](../../../docs-cli/usage/cli.md): Compact reference for `list`, `predict`, `imwrite`, and shared CLI options.

### Traditional Algorithms

- [docs-cli/algorithms/he.md](../../../docs-cli/algorithms/he.md): HE CLI target and parameters.
- [docs-cli/algorithms/ahe.md](../../../docs-cli/algorithms/ahe.md): AHE CLI target and parameters.
- [docs-cli/algorithms/clahe.md](../../../docs-cli/algorithms/clahe.md): CLAHE CLI target and parameters.
- [docs-cli/algorithms/rclahe.md](../../../docs-cli/algorithms/rclahe.md): RCLAHE CLI target and parameters.
- [docs-cli/algorithms/gamma.md](../../../docs-cli/algorithms/gamma.md): Gamma CLI target and parameters.
- [docs-cli/algorithms/gcp.md](../../../docs-cli/algorithms/gcp.md): GCP CLI target and parameters.
- [docs-cli/algorithms/lime.md](../../../docs-cli/algorithms/lime.md): LIME CLI target and parameters.
- [docs-cli/algorithms/bimef.md](../../../docs-cli/algorithms/bimef.md): BIMEF CLI target and parameters.
- [docs-cli/algorithms/npe.md](../../../docs-cli/algorithms/npe.md): NPE CLI target and parameters.
- [docs-cli/algorithms/retinex.md](../../../docs-cli/algorithms/retinex.md): Retinex CLI target and parameters.
- [docs-cli/algorithms/log.md](../../../docs-cli/algorithms/log.md): Log CLI target and parameters.
- [docs-cli/algorithms/dcp.md](../../../docs-cli/algorithms/dcp.md): DCP CLI target and parameters.

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

- [docs-cli/custom/algorithm.md](../../../docs-cli/custom/algorithm.md): CLI use of registered custom traditional algorithms.
- [docs-cli/custom/model.md](../../../docs-cli/custom/model.md): CLI use of registered custom deep-learning models.
