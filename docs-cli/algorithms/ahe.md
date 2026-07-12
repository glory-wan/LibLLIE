# AHE

Target: `ahe`

```bash
libllie predict ahe input.jpg -o results/ahe/output.jpg --kwargs color_space=yuv "tile_grid_size=(8, 8)"
```

Parameters passed with `--kwargs`:

| Parameter | Type | Default | Meaning |
| --- | --- | --- | --- |
| `color_space` | `str` | `"yuv"` | Color space where equalization is performed |
| `tile_grid_size` | `tuple` | `(8, 8)` | Local grid size |

Supported `color_space` values: `rgb`, `bgr`, `hsv`, `hls`, `yuv`, `ycbcr`, `lab`.
