#检查环境
import torch

print("PyTorch version:", torch.__version__)
print("CUDA available:", torch.cuda.is_available())

if torch.cuda.is_available():
    print("GPU:", torch.cuda.get_device_name(torch.cuda.current_device()))

x = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
print("Tensor:", x)
print("Shape:", x.shape)
print("Mean:", x.mean())