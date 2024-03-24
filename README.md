# Chest-Disease-Classification-from-CT-scan-Image

# create environment
conda create -n chest python=3.8 -y

# activate environment
conda activate chest

# install required packages
pip install -r requirements.txt

# after writing code for dvc 
# intialize dvc
1. dvc init
2. dvc repro
3. dvc dag