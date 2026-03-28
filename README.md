# [bevfusionx-index](https://github.com/rathaumons/bevfusionx-index)

💡This repository provides a [PyPI simple index](https://www.python.org/dev/peps/pep-0503/) of prebuilt wheels for [**`BEVFusionx`**](https://github.com/rathaumons/bevfusionx).

⚡By using this index, you can conveniently install via pip install, saving time on local builds and configuration.

## Package Installation

To install, use the `--extra-index-url` flag with `pip install`:

```bash
pip install {package} --extra-index-url https://rathaumons.github.io/bevfusionx-index/{suffix}/
```

💡See the [Summary Table](#summary-table) below for more details on `{package}` and `{suffix}`.

Examples: 

```bash
# torchpack - any (for both CPU/GPU)
pip install torchpack --extra-index-url https://rathaumons.github.io/bevfusionx-index/any/

# flash-attention - cu130 (CUDA 13.0 for Consumer + Workstation + Jetson)
pip install flash-attention --extra-index-url https://rathaumons.github.io/bevfusionx-index/cu130/

# mmcv - cu130d (CUDA 13.0 for Data Center)
pip install mmcv --extra-index-url https://rathaumons.github.io/bevfusionx-index/cu130d/
```

## Summary Table

See [branch main](https://github.com/rathaumons/bevfusionx-index#summary-table) for up-to-date details.
