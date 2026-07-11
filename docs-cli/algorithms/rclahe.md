# RCLAHE

Target: `rclahe`

```bash
libllie predict rclahe input.jpg -o results/rclahe/output.jpg --kwargs color_space=hsv clip_limit=2.0 "tile_grid_size=(8, 8)" iterations=3
```

Parameters passed with `--kwargs`:

| Parameter | Type | Default | Meaning |
| --- | --- | --- | --- |
| `color_space` | `str` | `"yuv"` | Color space where CLAHE is performed |
| `clip_limit` | `float` | `2.0` | Contrast clipping threshold |
| `tile_grid_size` | `tuple` | `(8, 8)` | Local grid size |
| `iterations` | `int` | `2` | Number of recursive CLAHE applications |
