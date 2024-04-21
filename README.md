# Mini-LIMA
Mini-LIMA

### Introduction

- instruction dataset construction
- model alignment via supervised fine-tuning(sft)
- model evaluation

### Setup

run [`src/scripts/setup.sh`](./src/scripts/setup.sh).

### Instruction Dataset Construction

refer to this article [https://arxiv.org/pdf/2212.10560.pdf](https://arxiv.org/pdf/2212.10560.pdf).

run [`src/scripts/self_instruct.sh`](./src/scripts/self_instruct.sh).

see instruction dataset generated with seed data in `data/gpt3_generations/finetuning_data/all_generated_instances.jsonl`.

### Supervised Fine-tuning

run [`finetune/run.sh`](./finetune/run.sh).