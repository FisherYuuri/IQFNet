import os
from torch.utils.data import DataLoader
from lib.dataset import Data
import torch.nn.functional as F
import torch
import cv2
import numpy as np
# from model.IQFNet import IQFNet
from model.IQFNetmobilenet import IQFNet
# from model.IQFNetVGG import IQFNet
# from model.IQFNetResNet import IQFNet


if __name__ == '__main__':
    model_path = './model_weight/VDT2048/IQFNetMobilenetv3.pth'

    out_path = './Result/VDT2048/MobileNetv3'


    data = Data(root='./dataset/VDT2048/Test/', mode='test')
    loader = DataLoader(data, batch_size=1, shuffle=False)
    net = IQFNet().cuda()
    print('loading model from %s...' % model_path)
    net.load_state_dict(torch.load(model_path))
    if not os.path.exists(out_path): os.mkdir(out_path)

    img_num = len(loader)
    net.eval()
    with torch.no_grad():
        for rgb, t, d, eg, mask, (H, W), name in loader:
            x1e_pred, x1e_pred_t, x1e_pred_d, x_pred, x_refine = net(rgb.cuda().float(), t.cuda().float(), d.cuda().float())
            score1 = F.interpolate(x_refine, size=(H, W), mode='bilinear', align_corners=True)
            pred = np.squeeze(torch.sigmoid(score1).cpu().data.numpy())
            pred = (pred - pred.min()) / (pred.max() - pred.min() + 1e-8)
            cv2.imwrite(os.path.join(out_path, name[0][:-4] + '.png'), 255 * pred)




