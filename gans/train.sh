rm -rf outputs 
python3 -m pip install -r StyleGAN.pytorch/requirements.txt
python3 StyleGAN.pytorch/train.py --config ./sample.yaml

