# Zero-DCE++

Registered model: `ZeroDCEPlusPlus`
Default config: `libllie/deepLearning/config/ZeroDCE++.yaml`
Training loss: `zerodce_extension`

Predict:

```bash
libllie predict ZeroDCEPlusPlus input.jpg -o results/ZeroDCEPlusPlus/output.png --device cuda
```

Train with the documented arguments:

```bash
libllie train --kwargs model=ZeroDCEPlusPlus dataset=CommonDataset root_dir=datasets/LOL loss=zerodce_extension epochs=10 batch_size=4
```
