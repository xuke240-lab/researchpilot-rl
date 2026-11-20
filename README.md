项目用途：ResearchPilot-RL 84 天学习工程，D01 完成线性回归训练。
使用环境：Conda 的 research-rl，Python 3.11。

## D01 运行方法

在项目根目录运行，使用已有 Conda 环境：

```powershell
conda activate research-rl
python -m src.check_env
python -m src.train_linear
python -m pytest -q
```

环境检查应显示 Tensor shape 为 `[2, 2]`，mean 为 `2.5`。

## D01 实验与验收记录

- 数据：`x = [[1], [2], [3], [4]]`，`y = 3*x + 2`。
- 参数初值：`w = 0`，`b = 0`；优化器：SGD；损失：均方误差。
- 当前学习率：`0.01`，训练步数：`1000`。
- 最终参数：`w = 3.014892578125`，`b = 1.9562135934829712`。
- 最后一次参数更新后重新计算的 MSE：`0.0003202091611456126`。
- `pytest`：`1 passed`。当前测试验证自动求导，不覆盖训练收敛。
- 原学习率 `1e-4` 在1000步后：`loss=3.7151`、`w=2.6698`、`b=0.9369`；调整后误差明显下降。

## 环境记录

`env_report.md` 保存 Python、PyTorch、CUDA 和 Tensor 检查结果；
`requirements.lock` 保存本次已安装的依赖版本，使用 UTF-8 编码。

当前使用 Python 3.11.18、PyTorch 2.15.0+cu132、RTX 3060 Laptop GPU。
训练示例的张量运行在 CPU 上，CUDA 可用性检查与训练设备是两件事。

新电脑配置时，先创建 Python 3.11 的 Conda 环境，并按
[PyTorch 官方安装页面](https://pytorch.org/get-started/locally/)选择适配系统和显卡的安装方式。
当前依赖清单中的 `+cu132` 表示 GPU 专用构建，可能需要匹配的官方安装源；
本次尚未在全新环境执行完整重建，依赖清单不代表已验证跨电脑安装。
