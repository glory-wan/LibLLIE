# LLFlow

Registered model: `LLFlow`
Default config: `libllie/deepLearning/config/LLFlow.yaml`

Main model parameters: `condition_channels=32`, `condition_blocks=4`, `flow_layers=8`, `flow_hidden_channels=64`, `scale_clamp=2.0`, `sample_temperature=0.0`.

Predict:

```bash
libllie predict LLFlow input.jpg -o results/LLFlow/output.png --device cuda
```

Train from the documented config:

```bash
libllie train libllie/deepLearning/config/LLFlow.yaml --kwargs root_dir=datasets/LOL epochs=10 batch_size=2
```

Stochastic inference:

```bash
libllie predict LLFlow input.jpg -o results/LLFlow/sample.png --device cuda --kwargs sample_temperature=0.7
```
