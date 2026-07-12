# Custom Datasets

After a `BaseDataset` subclass is registered as `MyDataset`, select it through CLI training kwargs.

Basic training:

```bash
libllie train --kwargs model=ZeroDCE dataset=MyDataset root_dir=datasets/MyDataset
```

With documented split and loader parameters:

```bash
libllie train --kwargs model=ZeroDCE dataset=MyDataset root_dir=datasets/MyDataset train_split=train val_split=val batch_size=4
```

If the directory does not match the dataset parser, pass explicit directories:

```bash
libllie train --kwargs model=ZeroDCE dataset=MyDataset root_dir=datasets/MyDataset train_low_dir=datasets/MyDataset/train/input train_high_dir=datasets/MyDataset/train/target
```

The documented YAML `data` section can also be used from any full training config passed to:

```bash
libllie train path/to/config.yaml
```

List CLI-visible registered components:

```bash
libllie list
```
