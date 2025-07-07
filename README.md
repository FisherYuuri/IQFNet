# IQFNet

This repo is an official implementation of the *IQFNet*.
**IQFNet: An Interaction-guided Quality-aware Fusion Network for Visual-Thermal-Depth Salient Object Detection.**

## Prerequisites
- The VDT-2048 dataset is available at:https://pan.baidu.com/s/1JyFBtjlJGf4GE2zeciN1wQ?pwd=bipy
- The pretrained weights for the backbone networks can be downloaded at:
-  [SwinTransformer](https://pan.baidu.com/s/1lRKC_caVWzVuJwvVfsCWYg?pwd=3hj7).
-  [Mobilenetv3](https://pan.baidu.com/s/1PDAgND6AxwZHUFlkx2KOTg?pwd=a4c8).
-  [VGG16](https://pan.baidu.com/s/1QA7IPUp2su2a9QXYiB4GBg?pwd=46ts).

## Usage

### 1. Clone the repository
## Setup
```
conda create -n IQFNet python==3.10
conda activate IQFNet
pip install torch==2.3.1 torchvision==0.18.1 torchaudio==2.3.1 --index-url https://download.pytorch.org/whl/cu118
```
### 2. Training
You can train the model by using 
```
cd Train
python TrainIQFNet.py
python TrainIQFNetVD.py
python TrainIQFNetVT.py
```

### 3. Testing
```
cd Test
python Test.py
python TestVD.py
python TestVT.py
```

### 4. Evaluation
The following table provides links to the pre-trained weights and saliency map results of IQFNet on various datasets:
| Dataset   | Backbone         | Saliency Maps                                             | Model Weights                                             |
|-----------|------------------|------------------------------------------------------------|-----------------------------------------------------------|
| VDT-2048  | Swin Transformer | [Download](https://pan.baidu.com/s/1--DBZLCpAbmVfrUAvJWYlA?pwd=yj3x)| [Download](https://pan.baidu.com/s/1Pgp4E3iRQvH45LkHRkn_Lw?pwd=a4ux)|
| VDT-2048  | Mobilenetv3 | [Download](https://pan.baidu.com/s/1vfkim20_eE0RuSCIEF-M4Q?pwd=52gy)| [Download](https://pan.baidu.com/s/1a9h2zVQ57YgwLUmbiSn-NA?pwd=tntu)|
| VDT-2048  | ResNet50 | [Download](https://pan.baidu.com/s/1xsTBJqFhzBvVuqxdbHXYzQ?pwd=sa3z)| [Download](https://pan.baidu.com/s/1chenHMyO0O7j222lBr6uSQ?pwd=ff5a)|
| VDT-2048  | VGG16 | [Download](https://pan.baidu.com/s/1YTexEdQafTuBkY9i2ZlV6Q?pwd=sdq9)| [Download](https://pan.baidu.com/s/1wbpEsHTMxZGXius10-f8jA?pwd=gqrx)|
| VT-1000   | Swin Transformer | [Download](https://pan.baidu.com/s/1WrnkoOb9tDaE70s8OG1T5A?pwd=7neg)| [Download](https://pan.baidu.com/s/1tcZq--z1XfFR0c9W4x8Zxg?pwd=c26d)|
| STERE     | Swin Transformer | [Download](https://pan.baidu.com/s/1RPSnHfArsmSD7SIUGxYTPw?pwd=yeze)| [Download](https://pan.baidu.com/s/1XffT92MN1RDXWMCovaruEw?pwd=jj6m)|


- We adopt the [evaluation toolbox](https://github.com/DengPingFan/SINet) provided by the SINet repository to compute quantitative metrics. 
- We provide the saliency maps for the challenging sub-datasets at the following link:[Download](https://pan.baidu.com/s/1--DBZLCpAbmVfrUAvJWYlA?pwd=yj3x)
- We provide the saliency maps of competing methods and challenging sub-datasets, which can be accessed via the following link:[Download](https://pan.baidu.com/s/19-waBKdIR0fFYrNQS3J86g?pwd=usqg)


## Acknowledgements
We would like to thank the authors of the following projects for their excellent work and contributions to the community:
- https://github.com/Lx-Bao/IFENet  
- https://github.com/DengPingFan/SINet  
- https://github.com/zyrant/LSNet  
- https://github.com/CSer-Tang-hao/ConTriNet_RGBT-SOD  
