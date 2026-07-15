# EnlightenGAN

Registered model: `EnlightenGAN`

Main model parameters: `generator_channels=32`, `discriminator_channels=32`, `discriminator_layers=3`, `use_attention=True`, `local_patch_ratio=0.5`.

Predict:

```bash
libllie predict EnlightenGAN input.jpg -o results/EnlightenGAN/output.png --device cuda
```
