# Custom Loss Functions

After a `BaseLoss` subclass is registered as `my_loss`, select it through CLI training kwargs or YAML.

Train with the documented loss name:

```bash
libllie train --kwargs model=ZeroDCE dataset=LOLv1Dataset root_dir=datasets/LOL loss=my_loss
```

Use documented loss parameters:

```bash
libllie train --kwargs model=MyModel dataset=LOLv1Dataset root_dir=datasets/LOL loss=my_loss "loss_params={'l1_weight': 1.0}"
```

Equivalent YAML fragment consumed by `libllie train path/to/config.yaml`:

```yaml
loss:
  name: my_loss
  params:
    l1_weight: 1.0
```

List CLI-visible registered components:

```bash
libllie list
```
