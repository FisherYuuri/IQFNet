# IQFNet

This repo is an official implementation of the *IQFNet*.
**IQFNet: An Interaction-guided Quality-aware Fusion Network for Visual-Thermal-Depth Salient Object Detection.**

## Prerequisites
- The VDT-2048 dataset is available at:https://pan.baidu.com/s/1JyFBtjlJGf4GE2zeciN1wQ?pwd=bipy
- 


## Usage

### 1. Clone the repository
## Setup
```
conda create -n IQFNet python==3.10
conda activate IQFNet
pip install torch==2.3.1 torchvision==0.18.1 torchaudio==2.3.1 --index-url https://download.pytorch.org/whl/cu118
```
### 2. Training
Download the pretrained model **swin_base_patch4_window12_384_22k.pth**. <br>

You can train the model by using 
```
python Train.py
```

### 3. Testing
```
python Test.py
```

### 4. Evaluation
The following table provides links to the pre-trained weights and saliency map results of IQFNet on various datasets:
| Dataset   | Model Weights                                              | Saliency Maps                                             |
|-----------|------------------------------------------------------------|-----------------------------------------------------------|
| VDT-2048  | [Download](https://pan.baidu.com/s/1Girb29F6WxQzUjNU6jFn7w?pwd=k3qe) k3qe | [Download](https://pan.baidu.com/s/1Girb29F6WxQzUjNU6jFn7w?pwd=k3qe) k3qe |
| VT-1000   | [Download](https://pan.baidu.com/s/1Girb29F6WxQzUjNU6jFn7w?pwd=k3qe) k3qe | [Download](https://pan.baidu.com/s/1Girb29F6WxQzUjNU6jFn7w?pwd=k3qe) k3qe |
| STERE     | [Download](https://pan.baidu.com/s/1Girb29F6WxQzUjNU6jFn7w?pwd=k3qe) k3qe | [Download](https://pan.baidu.com/s/1Girb29F6WxQzUjNU6jFn7w?pwd=k3qe) k3qe |
We adopt the [evaluation toolbox](https://github.com/DengPingFan/SINet) provided by the SINet repository to compute quantitative metrics.

