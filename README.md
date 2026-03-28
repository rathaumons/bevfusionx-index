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

| Package | Index Suffix | Current Vesion | Release Tag |
| - | - | - | - |
| [`torchpack`](https://github.com/rathaumons/torchpack) | [`any`](https://rathaumons.github.io/bevfusionx-index/any/) | [`v0.3.2`](https://github.com/rathaumons/torchpack/releases/tag/v0.3.2-bevfusionx) | [`v0.3.2-torchpack-any`](https://github.com/rathaumons/bevfusionx-index/releases/tag/v0.3.2-torchpack-any) |
| [`flash-attention`](https://github.com/rathaumons/flash-attention) | [`cu130`](https://rathaumons.github.io/bevfusionx-index/cu130) | [`v1.2.1`](https://github.com/rathaumons/flash-attention/releases/tag/v1.2.1-bevfusionx) | [`v1.2.1-flash-attention-cu130`](https://github.com/rathaumons/bevfusionx-index/releases/tag/v1.2.1-flash-attention-cu130) |
| [`flash-attention`](https://github.com/rathaumons/flash-attention) | [`cu130d`](https://rathaumons.github.io/bevfusionx-index/cu130d) | [`v1.2.1`](https://github.com/rathaumons/flash-attention/releases/tag/v1.2.1-bevfusionx) | [`v1.2.1-flash-attention-cu130d`](https://github.com/rathaumons/bevfusionx-index/releases/tag/v1.2.1-flash-attention-cu130d) |
| [`flash-attention`](https://github.com/rathaumons/flash-attention) | [`cu128`](https://rathaumons.github.io/bevfusionx-index/cu128) | [`v1.2.1`](https://github.com/rathaumons/flash-attention/releases/tag/v1.2.1-bevfusionx) | [`v1.2.1-flash-attention-cu128`](https://github.com/rathaumons/bevfusionx-index/releases/tag/v1.2.1-flash-attention-cu128) |
| [`flash-attention`](https://github.com/rathaumons/flash-attention) | [`cu126`](https://rathaumons.github.io/bevfusionx-index/cu126) | [`v1.2.1`](https://github.com/rathaumons/flash-attention/releases/tag/v1.2.1-bevfusionx) | [`v1.2.1-flash-attention-cu126`](https://github.com/rathaumons/bevfusionx-index/releases/tag/v1.2.1-flash-attention-cu126) |
| [`flash-attention`](https://github.com/rathaumons/flash-attention) | [`cu121`](https://rathaumons.github.io/bevfusionx-index/cu121) | [`v1.2.1`](https://github.com/rathaumons/flash-attention/releases/tag/v1.2.1-bevfusionx) | [`v1.2.1-flash-attention-cu121`](https://github.com/rathaumons/bevfusionx-index/releases/tag/v1.2.1-flash-attention-cu121) |
| [`flash-attention`](https://github.com/rathaumons/flash-attention) | [`cu113`](https://rathaumons.github.io/bevfusionx-index/cu113) | [`v1.2.1`](https://github.com/rathaumons/flash-attention/releases/tag/v1.2.1-bevfusionx) | [`v1.2.1-flash-attention-cu113`](https://github.com/rathaumons/bevfusionx-index/releases/tag/v1.2.1-flash-attention-cu113) |
| [`mmcv`](https://github.com/rathaROG/mmcv) | [`cu130`](https://rathaumons.github.io/bevfusionx-index/cu130) | [`v1.7.3`](https://github.com/rathaROG/mmcv/releases/tag/v1.7.3-bevfusionx) | [`v1.7.3-mmcv-cu130`](https://github.com/rathaumons/bevfusionx-index/releases/tag/v1.7.3-mmcv-cu130) |
| [`mmcv`](https://github.com/rathaROG/mmcv) | [`cu130d`](https://rathaumons.github.io/bevfusionx-index/cu130d) | [`v1.7.3`](https://github.com/rathaROG/mmcv/releases/tag/v1.7.3-bevfusionx) | [`v1.7.3-mmcv-cu130d`](https://github.com/rathaumons/bevfusionx-index/releases/tag/v1.7.3-mmcv-cu130d) |
| [`mmcv`](https://github.com/rathaROG/mmcv) | [`cu128`](https://rathaumons.github.io/bevfusionx-index/cu128) | [`v1.7.3`](https://github.com/rathaROG/mmcv/releases/tag/v1.7.3-bevfusionx) | [`v1.7.3-mmcv-cu128`](https://github.com/rathaumons/bevfusionx-index/releases/tag/v1.7.3-mmcv-cu128) |
| [`mmcv`](https://github.com/rathaROG/mmcv) | [`cu126`](https://rathaumons.github.io/bevfusionx-index/cu126) | [`v1.7.3`](https://github.com/rathaROG/mmcv/releases/tag/v1.7.3-bevfusionx) | [`v1.7.3-mmcv-cu126`](https://github.com/rathaumons/bevfusionx-index/releases/tag/v1.7.3-mmcv-cu126) |
| [`mmcv`](https://github.com/rathaROG/mmcv) | [`cu121`](https://rathaumons.github.io/bevfusionx-index/cu121) | [`v1.7.3`](https://github.com/rathaROG/mmcv/releases/tag/v1.7.3-bevfusionx) | [`v1.7.3-mmcv-cu121`](https://github.com/rathaumons/bevfusionx-index/releases/tag/v1.7.3-mmcv-cu121) |
| [`mmcv`](https://github.com/rathaROG/mmcv) | [`cu113`](https://rathaumons.github.io/bevfusionx-index/cu113) | [`v1.7.3`](https://github.com/rathaROG/mmcv/releases/tag/v1.7.3-bevfusionx) | [`v1.7.3-mmcv-cu113`](https://github.com/rathaumons/bevfusionx-index/releases/tag/v1.7.3-mmcv-cu113) |

THESE WHEELS ARE BUILT SPECIFICALLY FOR [**`BEVFUSION𝕏`**](https://github.com/rathaumons/bevfusionx) AND MAY NOT WORK IN YOUR ENVIROMENT.
