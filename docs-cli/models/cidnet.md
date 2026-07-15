# HVI-CIDNet

Registered model: `CIDNet` (alias: `HVI-CIDNet`)

Predict with a LibLLIE checkpoint:

```bash
libllie predict outputs/CIDNet/checkpoints/best.pt input.jpg -o results/CIDNet/output.png --device cuda
```

Documented inference controls: `input_gamma`, `saturation_scale`, and `intensity_scale`; each defaults to `1.0`.
