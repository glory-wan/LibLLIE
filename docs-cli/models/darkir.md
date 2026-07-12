# DarkIR

Registered model: `DarkIR`
Default config: `libllie/deepLearning/config/DarkIR.yaml`
Training loss: `darkir`

Predict:

```bash
libllie predict DarkIR input.jpg -o results/DarkIR/output.png --device cuda
```

Train with the documented arguments:

```bash
libllie train --kwargs model=DarkIR dataset=CommonDataset root_dir=datasets/LOL loss=darkir epochs=10 batch_size=4
```
