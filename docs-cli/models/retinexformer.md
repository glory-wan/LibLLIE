# RetinexFormer

Registered model: `RetinexFormer`
Default config: `libllie/deepLearning/config/RetinexFormer.yaml`
Training loss: `retinexformer`

Predict:

```bash
libllie predict RetinexFormer input.jpg -o results/RetinexFormer/output.png --device cuda
```

Train with the documented arguments:

```bash
libllie train --kwargs model=RetinexFormer dataset=CommonDataset root_dir=datasets/LOL loss=retinexformer epochs=10 batch_size=4
```

Train from YAML:

```bash
libllie train libllie/deepLearning/config/RetinexFormer.yaml
```
