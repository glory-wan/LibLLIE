# Zero-DCE

Registered model: `ZeroDCE`
Default config: `libllie/deepLearning/config/ZeroDCE.yaml`
Training loss: `zerodce`

Predict:

```bash
libllie predict ZeroDCE input.jpg -o results/ZeroDCE/output.png --device cuda
```

Train with the documented arguments:

```bash
libllie train --kwargs model=ZeroDCE dataset=CommonDataset root_dir=datasets/LOL loss=zerodce epochs=10 batch_size=4
```
