# Image I/O CLI

LibLLIE exposes image writing through `imwrite`. Image reading and return-format conversion to PIL, NumPy, Tensor, bytes, base64, or file path are Python API features, not standalone CLI commands.

## Save or Convert

```bash
libllie imwrite input.jpg -o results/output.png
```

If `-o/--output` is a file path, the file name and suffix come from that path.

## Save to a Folder

```bash
libllie imwrite input.jpg -o results --output-name enhanced.png
```

When the output is a folder, pass `--output-name` to choose the saved file name.

## Default Output

If no output is passed, `imwrite` uses the default save location.

```bash
libllie imwrite input.jpg
```

## Save Format

```bash
libllie imwrite input.jpg -o results/enhanced --save-format png
```

When the output path has a suffix, the suffix usually determines the save format. Use `--save-format` when a forced format is needed.

## String Image Sources

The CLI image argument is a string source accepted by image writing, such as a local path, URL, or base64 string.

## Prediction Input

`predict` uses LibLLIE image I/O internally and accepts image paths or image folders:

```bash
libllie predict gcp input.jpg -o results/gcp_output.png
```
