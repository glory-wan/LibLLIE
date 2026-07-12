# CLAHE

Target: `clahe`

```bash
libllie predict clahe input.jpg -o results/clahe/output.jpg --kwargs color_space=lab clip_limit=2.0 "tile_grid_size=(8, 8)"
```

Folder batch processing:

```bash
libllie predict clahe images/ -o results/clahe
```

Parameters passed with `--kwargs`:

| Parameter | Type | Default | Meaning |
| --- | --- | --- | --- |
| `color_space` | `str` | `"yuv"` | Color space where CLAHE is performed |
| `clip_limit` | `float` | `2.0` | Contrast clipping threshold |
| `tile_grid_size` | `tuple` | `(8, 8)` | Local grid size |
