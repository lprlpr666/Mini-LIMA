conda activate base

## clone llama-factory as sft codebase
git clone https://github.com/hiyouga/LLaMA-Factory.git
cd LLaMA-Factory/
pip install -r requirements.txt
cd ..

## directly install alpaca eval as evaluation codebase
git clone https://github.com/tatsu-lab/alpaca_eval.git
cd alpaca_eval/
pip install -e .
cd ..

# install specific sklearn version
pip install scikit-learn==1.4.0

import os
os.environ['MODELSCOPE_CACHE'] = './modelscope_hub'

# download the model
from modelscope.models import Model
model = Model.from_pretrained('qwen/Qwen1.5-0.5B')