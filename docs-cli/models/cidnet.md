# HVI-CIDNet

Registered model: `CIDNet` (alias: `HVI-CIDNet`)
Default config: `libllie/deepLearning/config/CIDNet.yaml`
Training loss: `cidnet`

Before training, set `data.root_dir` in the YAML file. The config expects a LOLv1-compatible paired layout.

```bash
libllie train libllie/deepLearning/config/CIDNet.yaml
```

For an offline or lightweight smoke test, set `loss.params.use_perceptual: false` in the YAML.

Predict with a LibLLIE checkpoint:

```bash
libllie predict outputs/CIDNet/checkpoints/best.pt input.jpg -o results/CIDNet/output.png --device cuda
```

Documented inference controls: `input_gamma`, `saturation_scale`, and `intensity_scale`; each defaults to `1.0`.
