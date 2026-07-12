# Validation

Use this index for validating enhanced low-light images with image-quality metrics. When executing examples from `docs-cli`, use `$LIBLLIE_CLI` in place of `libllie`.

## CLI Functions

- `$LIBLLIE_CLI list`: Lists available metrics before evaluation.
- `$LIBLLIE_CLI evaluate ...` / `$LIBLLIE_CLI eval ...`: Evaluates enhanced image folders with full-reference or no-reference metrics.
- `--kwargs KEY=VALUE ...`: Passes evaluator options to the evaluation command.
- `--help`: Shows available evaluation CLI arguments.

## CLI Docs Index

### Guide

- [docs-cli/guide/overview.md](../../../docs-cli/guide/overview.md): CLI overview for listing components, prediction, training, evaluation, and image writing.
- [docs-cli/guide/evaluate.md](../../../docs-cli/guide/evaluate.md): CLI evaluation for full-reference and no-reference metrics.

### Usage

- [docs-cli/usage/cli.md](../../../docs-cli/usage/cli.md): Compact reference for `evaluate`, `eval`, and shared CLI options.

### Custom Components

- [docs-cli/custom/metric.md](../../../docs-cli/custom/metric.md): CLI use of registered custom evaluation metrics.
