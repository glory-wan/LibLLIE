# LLNet

Registered model: `LLNet`
Default config: `libllie/deepLearning/config/LLNet.yaml`

Main model parameters: `patch_size=17`, `patch_stride=3`, `hidden_dims=[2000, 1600, 1200]`, `activation="sigmoid"`, `output_activation="sigmoid"`.

Predict:

```bash
libllie predict LLNet input.jpg -o results/LLNet/output.png --device cuda
```

Train from the documented config:

```bash
libllie train libllie/deepLearning/config/LLNet.yaml --kwargs root_dir=datasets/LOL epochs=10 batch_size=1
```

Quick debug training with smaller hidden dimensions:

```bash
libllie train --kwargs model=LLNet dataset=CommonDataset root_dir=datasets/LOL loss=llnet "model_params={'hidden_dims': [256, 128, 64], 'patch_stride': 8}" epochs=2 batch_size=1
```
