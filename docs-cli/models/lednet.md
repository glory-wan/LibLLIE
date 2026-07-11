# LEDNet

Registered model: `LEDNet`
Default config: `libllie/deepLearning/config/LEDNet.yaml`
Training loss: `lednet`

Predict:

```bash
libllie predict LEDNet input.jpg -o results/LEDNet/output.png --device cuda
```

Train with the documented arguments:

```bash
libllie train --kwargs model=LEDNet dataset=CommonDataset root_dir=datasets/LOL loss=lednet epochs=10 batch_size=4
```
