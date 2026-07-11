# Zero-IG

Registered model: `ZeroIG`
Default config: `libllie/deepLearning/config/ZeroIG.yaml`
Training loss: `zeroig`

Predict:

```bash
libllie predict ZeroIG input.jpg -o results/ZeroIG/output.png --device cuda
```

Train with the documented arguments:

```bash
libllie train --kwargs model=ZeroIG dataset=CommonDataset root_dir=datasets/LOL loss=zeroig epochs=10 batch_size=4
```
