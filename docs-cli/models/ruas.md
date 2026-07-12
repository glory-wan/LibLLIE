# RUAS

Registered model: `RUAS`
Default config: `libllie/deepLearning/config/RUAS.yaml`
Training loss: `ruas`

Predict:

```bash
libllie predict RUAS input.jpg -o results/RUAS/output.png --device cuda
```

Train with the documented arguments:

```bash
libllie train --kwargs model=RUAS dataset=CommonDataset root_dir=datasets/LOL loss=ruas epochs=10 batch_size=4
```
