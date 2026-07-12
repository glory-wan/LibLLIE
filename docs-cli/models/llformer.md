# LLFormer

Registered model: `LLFormer` (alias: `LL-Former`)
Default config: `libllie/deepLearning/config/LLFormer.yaml`
Training loss: `llformer`

Set `data.root_dir` before training. The paired patch dataset layout is:

```text
dataset/
  train/
    low/
    high/
  val/
    low/
    high/
```

Patch training uses synchronized `128x128` random crops. Other patch sizes are configured with `data.train_params.crop_size`; patch dimensions should be divisible by 16.

```bash
libllie train libllie/deepLearning/config/LLFormer.yaml
```

Predict with a LibLLIE checkpoint:

```bash
libllie predict outputs/LLFormer/checkpoints/best.pt input.png -o results/LLFormer/output.png --device cuda
```

Memory-efficient UHD inference:

```bash
libllie predict outputs/LLFormer/checkpoints/best.pt uhd_input.png -o results/LLFormer/uhd_output.png --device cuda --kwargs "tile_size=[720, 1280]" "tile_overlap=[360, 640]"
```

Tile dimensions must be divisible by 16. Overlapping predictions are averaged, including boundary tiles.
