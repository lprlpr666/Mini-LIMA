batch_dir=data/gpt3_comp_generations/

python src/self-instruct/bootstrap_instructions.py \
    --batch_dir ${batch_dir} \
    --num_instructions_to_generate 2000 \
    --seed_tasks_path seed_data/seed_tasks.jsonl \
    --model "gpt-3.5-turbo-instruct"