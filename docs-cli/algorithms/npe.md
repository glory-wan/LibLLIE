# NPE

Target: `npe`

```bash
libllie predict npe input.jpg -o results/npe/output.jpg
```

Adjust naturalness:

```bash
libllie predict npe input.jpg -o results/npe/natural.jpg --kwargs naturalness=0.5 enhancement_strength=3.0
```

Parameters passed with `--kwargs`:

| Parameter | Type | Default | Meaning |
| --- | --- | --- | --- |
| `sigma` | `float` | `15.0` | Gaussian scale for bright-pass illumination filtering |
| `illumination_floor` | `float` | `0.05` | Lower bound for illumination |
| `enhancement_strength` | `float` | `4.0` | Strength of the bi-log illumination mapping |
| `naturalness` | `float` | `0.35` | Blend weight for preserving the original naturalness |
| `detail_weight` | `float` | `1.0` | Weight applied to reflectance detail restoration |
