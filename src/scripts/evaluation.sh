# use HF mirror endpoint so that you can access the datasets properly on DSW notebook.
export HF_ENDPOINT=https://hf-mirror.com

# copy your model config into alpaca folder 
cp -r mini_lima/ alpaca_eval/src/alpaca_eval/models_configs/
# cp -r mini_lima/ /home/zsq259/.conda/envs/alpaca_env/lib/python3.10/site-packages/alpaca_eval/models_configs/
# cp -r mini_lima/ /home/zsq259/.local/lib/python3.11/site-packages/alpaca_eval/models_configs/

alpaca_eval evaluate_from_model \
  --model_configs 'mini_lima' \
  --annotators_config 'chatgpt'