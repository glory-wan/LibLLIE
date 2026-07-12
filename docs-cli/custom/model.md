# Custom Deep-Learning Models

After an `LLIEModel` subclass is registered as `MyModel`, use it through CLI prediction and training.

Predict:

```bash
libllie predict MyModel input.jpg -o results/MyModel --device cuda
```

Train with documented keyword arguments:

```bash
libllie train --kwargs model=MyModel dataset=LOLv1Dataset root_dir=datasets/LOL loss=charbonnier epochs=10 batch_size=4 device=cuda
```

Or train from the documented YAML file:

```bash
libllie train path/to/MyModel.yaml
```

The YAML must set documented fields such as `model.name: MyModel`, `data.dataset: LOLv1Dataset`, `data.root_dir: datasets/LOL`, `loss.name: charbonnier`, and `train.device: cuda`.

List CLI-visible registered components:

```bash
libllie list
```
