# Retinex

Targets: `ssr`, `msr`, `msrcr`

SSR:

```bash
libllie predict ssr input.jpg -o results/ssr/output.jpg --kwargs sigma=80.0
```

MSR:

```bash
libllie predict msr input.jpg -o results/msr/output.jpg --kwargs "scales=(15.0, 80.0, 250.0)"
```

MSRCR:

```bash
libllie predict msrcr input.jpg -o results/msrcr/output.jpg --kwargs alpha=125.0 beta=46.0
```

Folder batch processing:

```bash
libllie predict msrcr images/ -o results/msrcr
```

Common parameters passed with `--kwargs`:

| Parameter | Type | Default | Meaning |
| --- | --- | --- | --- |
| `low_clip` | `float` | `1.0` | Lower percentile used for display normalization |
| `high_clip` | `float` | `99.0` | Upper percentile used for display normalization |
| `eps` | `float` | `1e-6` | Small value used to avoid log and division instability |

SSR parameters:

| Parameter | Type | Default | Meaning |
| --- | --- | --- | --- |
| `sigma` | `float` | `80.0` | Gaussian surround scale |

MSR parameters:

| Parameter | Type | Default | Meaning |
| --- | --- | --- | --- |
| `scales` | `Sequence[float]` | `(15.0, 80.0, 250.0)` | Gaussian surround scales |

MSRCR parameters:

| Parameter | Type | Default | Meaning |
| --- | --- | --- | --- |
| `scales` | `Sequence[float]` | `(15.0, 80.0, 250.0)` | Gaussian surround scales |
| `alpha` | `float` | `125.0` | Color-restoration intensity gain |
| `beta` | `float` | `46.0` | Color-restoration log gain |
| `gain` | `float` | `1.0` | Global gain applied to the restored Retinex response |
| `offset` | `float` | `0.0` | Global offset applied before display normalization |
