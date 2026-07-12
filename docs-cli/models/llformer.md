# LLFormer

Registered model: `LLFormer` (alias: `LL-Former`)

Predict with a LibLLIE checkpoint:

```bash
libllie predict outputs/LLFormer/checkpoints/best.pt input.png -o results/LLFormer/output.png --device cuda
```

Memory-efficient UHD inference:

```bash
libllie predict outputs/LLFormer/checkpoints/best.pt uhd_input.png -o results/LLFormer/uhd_output.png --device cuda --kwargs "tile_size=[720, 1280]" "tile_overlap=[360, 640]"
```

Tile dimensions must be divisible by 16. Overlapping predictions are averaged, including boundary tiles.
