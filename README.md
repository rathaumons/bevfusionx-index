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
pip install flash-attn --extra-index-url https://rathaumons.github.io/bevfusionx-index/cu130/

# mmcv - cu130d (CUDA 13.0 for Data Center)
pip install mmcv-full --extra-index-url https://rathaumons.github.io/bevfusionx-index/cu130d/
```

## Summary Table

| Package | Vesion | Index Suffix | Release Tag | Built with PyTorch</br>`torch`/`torchvision` |
| - | - | - | - | - |
| [`torchpack`](https://github.com/rathaumons/torchpack) | [`v0.3.2`](https://github.com/rathaumons/torchpack/releases/tag/v0.3.2-bevfusionx) | [`any`](https://rathaumons.github.io/bevfusionx-index/any/) | [`v0.3.2-torchpack-any`](https://github.com/rathaumons/bevfusionx-index/releases/tag/v0.3.2-torchpack-any) | - |
| [`flash-attn`](https://github.com/rathaumons/flash-attention) | [`v1.2.1`](https://github.com/rathaumons/flash-attention/releases/tag/v1.2.1-bevfusionx) | [`cu130`](https://rathaumons.github.io/bevfusionx-index/cu130) | [`v1.2.1-flash-attention-cu130`](https://github.com/rathaumons/bevfusionx-index/releases/tag/v1.2.1-flash-attention-cu130) | `2.11.0+cu130`/`0.26.0+cu130` |
| [`flash-attn`](https://github.com/rathaumons/flash-attention) | [`v1.2.1`](https://github.com/rathaumons/flash-attention/releases/tag/v1.2.1-bevfusionx) | [`cu130d`](https://rathaumons.github.io/bevfusionx-index/cu130d) | [`v1.2.1-flash-attention-cu130d`](https://github.com/rathaumons/bevfusionx-index/releases/tag/v1.2.1-flash-attention-cu130d) | `2.11.0+cu130`/`0.26.0+cu130` |
| [`flash-attn`](https://github.com/rathaumons/flash-attention) | [`v1.2.1`](https://github.com/rathaumons/flash-attention/releases/tag/v1.2.1-bevfusionx) | [`cu128`](https://rathaumons.github.io/bevfusionx-index/cu128) | [`v1.2.1-flash-attention-cu128`](https://github.com/rathaumons/bevfusionx-index/releases/tag/v1.2.1-flash-attention-cu128) | `2.11.0+cu128`/`0.26.0+cu128` |
| [`flash-attn`](https://github.com/rathaumons/flash-attention) | [`v1.2.1`](https://github.com/rathaumons/flash-attention/releases/tag/v1.2.1-bevfusionx) | [`cu126`](https://rathaumons.github.io/bevfusionx-index/cu126) | [`v1.2.1-flash-attention-cu126`](https://github.com/rathaumons/bevfusionx-index/releases/tag/v1.2.1-flash-attention-cu126) | `2.11.0+cu126`/`0.26.0+cu126` |
| [`flash-attn`](https://github.com/rathaumons/flash-attention) | [`v1.2.1`](https://github.com/rathaumons/flash-attention/releases/tag/v1.2.1-bevfusionx) | [`cu121`](https://rathaumons.github.io/bevfusionx-index/cu121) | [`v1.2.1-flash-attention-cu121`](https://github.com/rathaumons/bevfusionx-index/releases/tag/v1.2.1-flash-attention-cu121) | `2.5.1+cu121`/`0.20.1+cu121` |
| [`flash-attn`](https://github.com/rathaumons/flash-attention) | [`v1.2.1`](https://github.com/rathaumons/flash-attention/releases/tag/v1.2.1-bevfusionx) | [`cu113`](https://rathaumons.github.io/bevfusionx-index/cu113) | [`v1.2.1-flash-attention-cu113`](https://github.com/rathaumons/bevfusionx-index/releases/tag/v1.2.1-flash-attention-cu113) | `1.12.1+cu113`/`0.13.1+cu113` |
| [`mmcv-full`](https://github.com/rathaROG/mmcv) | [`v1.7.3`](https://github.com/rathaROG/mmcv/releases/tag/v1.7.3-bevfusionx) | [`cu130`](https://rathaumons.github.io/bevfusionx-index/cu130) | [`v1.7.3-mmcv-cu130`](https://github.com/rathaumons/bevfusionx-index/releases/tag/v1.7.3-mmcv-cu130) | `2.11.0+cu130`/`0.26.0+cu130` |
| [`mmcv-full`](https://github.com/rathaROG/mmcv) | [`v1.7.3`](https://github.com/rathaROG/mmcv/releases/tag/v1.7.3-bevfusionx) | [`cu130d`](https://rathaumons.github.io/bevfusionx-index/cu130d) | [`v1.7.3-mmcv-cu130d`](https://github.com/rathaumons/bevfusionx-index/releases/tag/v1.7.3-mmcv-cu130d) | `2.11.0+cu130`/`0.26.0+cu130` |
| [`mmcv-full`](https://github.com/rathaROG/mmcv) | [`v1.7.3`](https://github.com/rathaROG/mmcv/releases/tag/v1.7.3-bevfusionx) | [`cu128`](https://rathaumons.github.io/bevfusionx-index/cu128) | [`v1.7.3-mmcv-cu128`](https://github.com/rathaumons/bevfusionx-index/releases/tag/v1.7.3-mmcv-cu128) | `2.11.0+cu128`/`0.26.0+cu128` |
| [`mmcv-full`](https://github.com/rathaROG/mmcv) | [`v1.7.3`](https://github.com/rathaROG/mmcv/releases/tag/v1.7.3-bevfusionx) | [`cu126`](https://rathaumons.github.io/bevfusionx-index/cu126) | [`v1.7.3-mmcv-cu126`](https://github.com/rathaumons/bevfusionx-index/releases/tag/v1.7.3-mmcv-cu126) | `2.11.0+cu126`/`0.26.0+cu126` |
| [`mmcv-full`](https://github.com/rathaROG/mmcv) | [`v1.7.3`](https://github.com/rathaROG/mmcv/releases/tag/v1.7.3-bevfusionx) | [`cu121`](https://rathaumons.github.io/bevfusionx-index/cu121) | [`v1.7.3-mmcv-cu121`](https://github.com/rathaumons/bevfusionx-index/releases/tag/v1.7.3-mmcv-cu121) | `2.5.1+cu121`/`0.20.1+cu121` |
| [`mmcv-full`](https://github.com/rathaROG/mmcv) | [`v1.7.3`](https://github.com/rathaROG/mmcv/releases/tag/v1.7.3-bevfusionx) | [`cu113`](https://rathaumons.github.io/bevfusionx-index/cu113) | [`v1.7.3-mmcv-cu113`](https://github.com/rathaumons/bevfusionx-index/releases/tag/v1.7.3-mmcv-cu113) | `1.12.1+cu113`/`0.13.1+cu113` |

THESE WHEELS WERE BUILT SPECIFICALLY FOR [**`BEVFUSION𝕏`**](https://github.com/rathaumons/bevfusionx) AND MAY NOT WORK IN YOUR ENVIROMENT.

## NVIDIA Architecture

The targeted NVIDIA GPU architectures for these builds were determined based on the logic of [`nvidia-arch`](https://github.com/rathaROG/nvidia-arch) using `gpu_type="cons+jets", min_sm=60`, except for:

- The `cu130d` builds, which used `gpu_type="dcen"`.
- The `flash-attn` builds, which used `min_sm=75` since it does not support older architectures.

| Index Suffix |  Included NVIDIA Arches for NVCC |
| - | - |
| `cu130` | `7.5;8.6;8.7;8.9;11.0;12.0;12.1+PTX` |
| `cu130d` | `7.5;8.0;8.6;8.9;9.0;10.0;10.3;12.0+PTX` |
| `cu128` | `6.0;6.1;6.2;7.0;7.2;7.5;8.6;8.7;8.9;12.0+PTX` |
| `cu126` | `6.0;6.1;6.2;7.0;7.2;7.5;8.6;8.7;8.9+PTX` |
| `cu121` | `6.0;6.1;6.2;7.0;7.2;7.5;8.6;8.7;8.9+PTX` |
| `cu113` | `6.0;6.1;6.2;7.0;7.2;7.5;8.6+PTX` |

The base Docker images are sourced from [ratharog/manylinux_2_28_x86_64](https://hub.docker.com/r/ratharog/manylinux_2_28_x86_64).
