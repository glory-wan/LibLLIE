# BIMEF

Target: `bimef`

```bash
libllie predict bimef input.jpg -o results/bimef/output.jpg
```

Manual exposure:

```bash
libllie predict bimef input.jpg -o results/bimef/manual.jpg --kwargs exposure_ratio=3.0
```

Parameters passed with `--kwargs`:

| Parameter | Type | Default | Meaning |
| --- | --- | --- | --- |
| `exposure_ratio` | `Optional[float]` | `None` | Manual exposure ratio; if `None`, it is estimated automatically |
| `target_mean` | `float` | `0.55` | Target luminance mean for automatic exposure |
| `max_ratio` | `float` | `5.0` | Maximum automatic exposure ratio |
| `well_exposed_sigma` | `float` | `0.2` | Sigma for well-exposedness weight |
| `contrast_weight` | `float` | `1.0` | Contrast weight exponent |
| `saturation_weight` | `float` | `1.0` | Saturation weight exponent |
| `well_exposed_weight` | `float` | `1.0` | Well-exposedness weight exponent |
