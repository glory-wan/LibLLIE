# Custom Evaluation Metrics

After a `BaseMetric` subclass is registered as `MyMetric` or `MyNoReferenceMetric`, select it with `--metrics`.

Full-reference evaluation:

```bash
libllie evaluate --en results/MyModel --ref datasets/LOL/eval15/high --metrics MyMetric --save-path results/eval_my_metric.json
```

No-reference evaluation:

```bash
libllie evaluate --en results/MyModel --metrics MyNoReferenceMetric
```

Class names ending in `Metric` can be selected with or without that suffix.

List CLI-visible registered components:

```bash
libllie list
```
