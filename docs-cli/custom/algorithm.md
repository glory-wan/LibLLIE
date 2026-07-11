# Custom Traditional Enhancement Algorithms

After an `LLIEnhancer` subclass is registered as `my_algorithm`, use it through CLI prediction.

Single image:

```bash
libllie predict my_algorithm input.jpg -o results/my_algorithm/output.png
```

Folder:

```bash
libllie predict my_algorithm images/ -o results/my_algorithm
```

Pass documented runtime parameters with `--kwargs`:

```bash
libllie predict my_algorithm input.jpg -o results/my_algorithm --kwargs gain=1.5
```

List CLI-visible registered components:

```bash
libllie list
```
