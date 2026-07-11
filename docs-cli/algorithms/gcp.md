# GCP

Target: `gcp`

```bash
libllie predict gcp input.jpg -o results/gcp/output.jpg
```

Explicit traditional backend with folder input:

```bash
libllie predict gcp images/ -o results/gcp --backend traditional
```

Custom parameters:

```bash
libllie predict gcp input.jpg -o results/gcp_custom.png --kwargs gamma_max=5.0 erosion_window=11 high_percentile=99.0 low_percentile=1.0
```

Parameters passed with `--kwargs`:

| Parameter | Type | Default | Meaning |
| --- | --- | --- | --- |
| `gamma_max` | `float` | `6.0` | Maximum value of pixel-adaptive gamma |
| `erosion_window` | `int` | `15` | Dark-channel erosion kernel size |
| `atmospheric_bins` | `int` | `200` | Number of histogram bins used during atmospheric light estimation |
| `atmospheric_percentile` | `float` | `0.99` | Dark-channel percentile ratio used to select atmospheric-light candidate regions |
| `t_min` | `float` | `0.1` | Lower bound of the transmission map |
| `blur_ksize` | `int` | `7` | Gaussian smoothing kernel size, must be a positive odd integer |
| `high_percentile` | `float` | `99.5` | High percentile for final dynamic-range stretching |
| `low_percentile` | `float` | `0.5` | Low percentile for final dynamic-range stretching |
| `eps` | `float` | `1e-6` | Small value to avoid division by zero |
