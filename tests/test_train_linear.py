import torch

def test_autograd():
    x = torch.tensor(2.0, requires_grad=True)

    y = x**2 + 3*x 
    y.backward()

    assert x.grad.item() == 7.0