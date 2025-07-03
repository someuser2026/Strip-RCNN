conda env create -n openmmlab python=3.8 -y
pip install torch==1.10.0+cu111 torchvision==0.11.0+cu111 torchaudio==0.10.0 -f https://download.pytorch.org/whl/torch_stable.html
pip install mmcv-full==1.7.2 -f https://download.openmmlab.com/mmcv/dist/cu111/torch1.10.0/index.html
pip install -U openmim
mim install mmdet
git clone https://github.com/YXB-NKU/Strip-R-CNN.git
cd Strip-R-CNN
pip install -v -e .
pip install timm