# Custom Deep-Learning Models

After an `LLIEModel` subclass is registered as `MyModel`, use it through CLI prediction.

Predict:

```bash
libllie predict MyModel input.jpg -o results/MyModel --device cuda
```

List CLI-visible registered components:

```bash
libllie list
```
