# HE

Target: `he`

```bash
libllie predict he input.jpg -o results/he/output.jpg --kwargs color_space=hsv
```

Folder batch processing:

```bash
libllie predict he images/ -o results/he --kwargs color_space=yuv
```

Parameters passed with `--kwargs`:

| Parameter | Type | Default | Meaning |
| --- | --- | --- | --- |
| `color_space` | `str` | `"rgb"` | Color space where histogram equalization is performed |

Supported `color_space` values: `rgb`, `bgr`, `hsv`, `hls`, `yuv`, `ycbcr`, `lab`.
