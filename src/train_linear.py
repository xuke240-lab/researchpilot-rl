#练习
import torch

torch.manual_seed(42)

#1.构造数据器

x = torch.tensor([[1.0], [2.0], [3.0], [4.0]])
y = 3*x + 2

#2. 创建可训练参数
w = torch.nn.Parameter(torch.tensor(0.0))
b = torch.nn.Parameter(torch.tensor(0.0))

#3 优化器

optimizer = torch.optim.SGD([w,b],lr=1e-4)

#4.xunlian

for step in range(1000):

    pred = w*x+b

    loss = torch.mean((pred-y)**2)

    #清空梯度

    optimizer.zero_grad()

    loss.backward()

    optimizer.step()

    if(step+1)%100 == 0:
        print(
            f"Step {step+1},"
            f"Loss={loss.item():.4f},"
            f"Weight={w.item():.4f},"
            f"Bias={b.item():.4f}"
        )