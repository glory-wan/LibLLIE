# LIME

Target: `lime`

```bash
libllie predict lime input.jpg -o results/lime/output.jpg --kwargs gamma=0.8
```

Folder batch processing:

```bash
libllie predict lime images/ -o results/lime
```

Parameters passed with `--kwargs`:

| Parameter | Type | Default | Meaning |
| --- | --- | --- | --- |
| `gamma` | `float` | `0.8` | Gamma applied to the refined illumination map |
| `guided_radius` | `int` | `15` | Guided filter radius |
| `guided_eps` | `float` | `1e-3` | Guided filter regularization term |
| `illumination_floor` | `float` | `0.05` | Lower bound for illumination |
| `exposure` | `float` | `1.0` | Global exposure multiplier |
