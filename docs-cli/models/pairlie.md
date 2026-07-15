# PairLIE

Registered model: `PairLIE` (alias: `Pair-LIE`)

Predict with a LibLLIE checkpoint:

```bash
libllie predict outputs/PairLIE/checkpoints/best.pt input.jpg -o results/PairLIE/output.png --device cuda
```

LOL-style inference:

```bash
libllie predict outputs/PairLIE/checkpoints/best.pt input.jpg -o results/PairLIE/lol.png --device cuda --kwargs enhancement_gamma=0.14
```

Default `enhancement_gamma` is `0.2`.
