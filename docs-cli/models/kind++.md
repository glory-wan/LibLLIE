# KinD++

Registered model: `KinDPlusPlus`

Main model parameters: `decomposition_channels=32`, `restoration_channels=32`, `adjustment_channels=32`, `illumination_ratio=5.0`.

Predict:

```bash
libllie predict KinDPlusPlus input.jpg -o results/KinDPlusPlus/output.png --device cuda
```

Override inference exposure ratio:

```bash
libllie predict KinDPlusPlus input.jpg -o results/KinDPlusPlus/brighter.png --device cuda --kwargs illumination_ratio=6.0
```
