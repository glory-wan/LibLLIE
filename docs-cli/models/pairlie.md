# PairLIE

Registered model: `PairLIE` (alias: `Pair-LIE`)
Default config: `libllie/deepLearning/config/PairLIE.yaml`
Training loss: `pairlie`

Set `data.root_dir` before training. PairLIE needs two different low-light instances of each scene. The official layout is:

```text
PairLIE-training-dataset/
  1/
    exposure_1.png
    exposure_2.png
  2/
    exposure_1.png
    exposure_2.png
```

It also accepts `root/train/scene/...`. Every scene folder must contain at least two supported images.

```bash
libllie train libllie/deepLearning/config/PairLIE.yaml
```

Predict with a LibLLIE checkpoint:

```bash
libllie predict outputs/PairLIE/checkpoints/best.pt input.jpg -o results/PairLIE/output.png --device cuda
```

LOL-style inference:

```bash
libllie predict outputs/PairLIE/checkpoints/best.pt input.jpg -o results/PairLIE/lol.png --device cuda --kwargs enhancement_gamma=0.14
```

Default `enhancement_gamma` is `0.2`.
