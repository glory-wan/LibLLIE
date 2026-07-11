# URetinex-Net

Registered model: `URetinexNet`
Default config: `libllie/deepLearning/config/URetinexNet.yaml`
Training loss: `uretinex`

Predict:

```bash
libllie predict URetinexNet input.jpg -o results/URetinexNet/output.png --device cuda
```

Train with the documented arguments:

```bash
libllie train --kwargs model=URetinexNet dataset=CommonDataset root_dir=datasets/LOL loss=uretinex epochs=10 batch_size=4
```
