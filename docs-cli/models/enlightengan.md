# EnlightenGAN

Registered model: `EnlightenGAN`
Default config: `libllie/deepLearning/config/EnlightenGAN.yaml`

Main model parameters: `generator_channels=32`, `discriminator_channels=32`, `discriminator_layers=3`, `use_attention=True`, `local_patch_ratio=0.5`.

Predict:

```bash
libllie predict EnlightenGAN input.jpg -o results/EnlightenGAN/output.png --device cuda
```

Train from the documented config:

```bash
libllie train libllie/deepLearning/config/EnlightenGAN.yaml --kwargs root_dir=datasets/LOL epochs=10 batch_size=2
```

Quick debug training:

```bash
libllie train --kwargs model=EnlightenGAN dataset=CommonDataset root_dir=datasets/LOL loss=enlightengan "model_params={'generator_channels': 16, 'discriminator_channels': 16}" epochs=2 batch_size=1
```
