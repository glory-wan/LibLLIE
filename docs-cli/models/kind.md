# KinD

Registered model: `KinD`

Main model parameters: `decomposition_channels=64`, `decomposition_layers=5`, `restoration_channels=32`, `adjustment_channels=32`, `adjustment_layers=3`, `illumination_ratio=5.0`.

Predict:

```bash
libllie predict KinD input.jpg -o results/KinD/output.png --device cuda
```

Override inference exposure ratio:

```bash
libllie predict KinD input.jpg -o results/KinD/brighter.png --device cuda --kwargs illumination_ratio=6.0
```
