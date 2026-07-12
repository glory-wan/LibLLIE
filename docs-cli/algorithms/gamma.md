# Gamma

Target: `Gamma`

```bash
libllie predict Gamma input.jpg -o results/gamma/output.jpg --kwargs gamma=0.6
```

Explicit traditional backend:

```bash
libllie predict Gamma input.jpg -o results/gamma/output.jpg --backend traditional --kwargs gamma=0.6
```

Parameters passed with `--kwargs`:

| Parameter | Type | Default | Meaning |
| --- | --- | --- | --- |
| `gamma` | `float` | `0.6` | Power-law exponent, must be positive |
