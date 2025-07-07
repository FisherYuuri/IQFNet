from model.IQFNet import IQFNet
from thop import profile
import torch

model1 = IQFNet().cuda()
input = torch.randn(1, 3, 384, 384).cuda()
input2 = torch.randn(1, 3, 384, 384).cuda()
input3 = torch.randn(1, 3, 384, 384).cuda()
flops1, params1 = profile(model1, inputs=(input,input2))
print('params:%.2f(M)'%((params1)/1000000))
print('flops:%.2f(G)'%((flops1)/1000000000))