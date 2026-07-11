# SCI

Registered model: `SCI`
Default config: `libllie/deepLearning/config/SCI.yaml`
Training loss: `sci`

Predict:

```bash
libllie predict SCI input.jpg -o results/SCI/output.png --device cuda
```

Train with the documented arguments:

```bash
libllie train --kwargs model=SCI dataset=CommonDataset root_dir=datasets/LOL loss=sci epochs=10 batch_size=4
```
