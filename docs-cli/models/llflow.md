# LLFlow

Registered model: `LLFlow`

Main model parameters: `condition_channels=32`, `condition_blocks=4`, `flow_layers=8`, `flow_hidden_channels=64`, `scale_clamp=2.0`, `sample_temperature=0.0`.

Predict:

```bash
libllie predict LLFlow input.jpg -o results/LLFlow/output.png --device cuda
```

Stochastic inference:

```bash
libllie predict LLFlow input.jpg -o results/LLFlow/sample.png --device cuda --kwargs sample_temperature=0.7
```
