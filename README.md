# Mini-LIMA
Mini-LIMA

### Introduction

- instruction dataset construction
- model alignment via supervised fine-tuning(sft)
- model evaluation

### Run our project

#### Setup

run [`src/scripts/setup.sh`](./src/scripts/setup.sh).

#### Instruction Dataset Construction

refer to this article [https://arxiv.org/pdf/2212.10560.pdf](https://arxiv.org/pdf/2212.10560.pdf).

run [`src/scripts/self_instruct.sh`](./src/scripts/self_instruct.sh).

see instruction dataset generated with seed data in `data/gpt3_generations/finetuning_data/all_generated_instances.jsonl`.

#### Supervised Fine-tuning

using [https://github.com/hiyouga/LLaMA-Factory/tree/main](https://github.com/hiyouga/LLaMA-Factory/tree/main).

run [`finetune/run.sh`](./finetune/run.sh).

#### Model Evaluation

using [https://github.com/tatsu-lab/alpaca_eval](https://github.com/tatsu-lab/alpaca_eval).

need to set a new conda eviroment other than base.

run [`src/scripts/evaluation.sh`](./src/scripts/evaluation.sh).

### Results

#### parameters setting

We tried different parameters for the whole pipeline, here is some of the parameters we tried:

- Instruction Dataset Construction
    - openai gpt3 model: `gpt3-turbo`, `gpt3-turbo-instruct`, `mistral`.    

- Supervised Fine-tuning
    - model: `qwen-1.5-0.5B`
    - finetuning_type: `full`, `lora`
    - template: `qwen`, `default`
    - sum of dataset

- Model Evaluation
    - prompt: [`prompt.txt`](./mini_lima/prompt.txt), [`prompt1.txt`](./mini_lima/prompt1.txt), [`prompt2.txt`](./mini_lima/prompt2.txt)
    - temperature: `0.7`

#### Results

We use the final win rate in alpaca evaluation to determine the quality of the model.

These are some results we got:

| dataset construction | dataset sum(with seeds) | template | prompt  | model outputs                                                | win rate                                                     |
| -------------------- | ----------------------- | -------- | ------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| none                 | 0(unfinetuned model)    | none     | prompt  | [see](./finalresults/unftn_results/results/mini_lima/model_outputs.json) | [6.42](./finalresults/unftn_results/results/mini_lima/chatgpt/leaderboard.csv) |
| gpt3-turbo-instruct  | 338                     | default  | prompt  | [see](./finalresults/338-default-prompt-results1/mini_lima/model_outputs.json) | [29.31](./finalresults/338-default-prompt-results1/mini_lima/chatgpt/leaderboard.csv) |
| gpt3-turbo-instruct  | 338                     | default  | prompt  | [see](./finalresults/338-default-prompt-results2/mini_lima/model_outputs.json) | [13.74](./finalresults/338-default-prompt-results2/mini_lima/chatgpt/leaderboard.csv) |
| gpt3-turbo-instruct  | 338                     | default  | prompt1 | [see](./finalresults/338-default-prompt1-results/mini_lima/model_outputs.json) | [9.16](./finalresults/338-default-prompt1-results/mini_lima/chatgpt/leaderboard.csv) |
| gpt3-turbo-instruct  | 338                     | qwen     | prompt1 | [see](./finalresults/338-qwen-prompt1-results/mini_lima/model_outputs.json) | [9.28](./finalresults/338-qwen-prompt1-results/mini_lima/chatgpt/leaderboard.csv) |
| gpt3-turbo-instruct  | 1735                    | default  | prompt  | [see](./finalresults/1735-default-prompt-results1/mini_lima/model_outputs.json) | [10.86](./finalresults/1735-default-prompt-results1/mini_lima/chatgpt/leaderboard.csv) |
| gpt3-turbo-instruct  | 1735                    | default  | prompt  | [see](./finalresults/1735-default-prompt-results2/mini_lima/model_outputs.json) | [11.22](./finalresults/1735-default-prompt-results2/mini_lima/chatgpt/leaderboard.csv) |
| gpt3-turbo-instruct  | 1735                    | default  | prompt1 | [see]()                                                      |                                                              |
| gpt3-turbo-instruct  | 1735                    | qwen     | prompt  | [see](./finalresults/1735-qwen-prompt-results/mini_lima/model_outputs.json) | [11.42](./finalresults/1735-qwen-prompt-results/mini_lima/chatgpt/leaderboard.csv) |
| gpt3-turbo-instruct  | 1735                    | qwen     | prompt2 | [see](./finalresults/1735-qwen-prompt2-results/mini_lima/model_outputs.json) | [8.75](./finalresults/1735-qwen-prompt2-results/mini_lima/chatgpt/leaderboard.csv) |
| gpt3-turbo-instruct  | 1735                    |          |         | [see]()                                                      |                                                              |
| gpt3-turbo           | 500                     | qwen     | prompt  | [see]()                                                      |                                                              |
| mistral              | 944                     | qwen     | prompt  |                                                              |                                                              |

