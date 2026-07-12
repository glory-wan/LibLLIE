# LLNet

Registered model: `LLNet`

Main model parameters: `patch_size=17`, `patch_stride=3`, `hidden_dims=[2000, 1600, 1200]`, `activation="sigmoid"`, `output_activation="sigmoid"`.

Predict:

```bash
libllie predict LLNet input.jpg -o results/LLNet/output.png --device cuda
```
