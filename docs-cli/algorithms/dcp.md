# DCP / Dark Channel

Target: `dcp`

```bash
libllie predict dcp input.jpg -o results/dcp/output.jpg --kwargs size=15 omega=0.95 t_min=0.1
```

Folder batch processing:

```bash
libllie predict dcp images/ -o results/dcp
```

Parameters passed with `--kwargs`:

| Parameter | Type | Default | Meaning |
| --- | --- | --- | --- |
| `size` | `int` | `15` | Dark-channel erosion kernel size |
| `omega` | `float` | `0.95` | Transmission estimation weight |
| `t_min` | `float` | `0.1` | Minimum transmission |
| `guided_radius` | `int` | `60` | Guided filter radius |
| `guided_eps` | `float` | `1e-4` | Guided filter regularization term |
