# KinD++

Registered model: `KinDPlusPlus`
Default config: `libllie/deepLearning/config/KinD++.yaml`

Main model parameters: `decomposition_channels=32`, `restoration_channels=32`, `adjustment_channels=32`, `illumination_ratio=5.0`.

Predict:

```bash
libllie predict KinDPlusPlus input.jpg -o results/KinDPlusPlus/output.png --device cuda
```

Train from the documented config:

```bash
libllie train libllie/deepLearning/config/KinD++.yaml --kwargs root_dir=datasets/LOL epochs=10 batch_size=2
```

Override inference exposure ratio:

```bash
libllie predict KinDPlusPlus input.jpg -o results/KinDPlusPlus/brighter.png --device cuda --kwargs illumination_ratio=6.0
```
