batch_dir=data/gpt3_generations/

python src/self-instruct/bootstrap_instructions.py \
    --batch_dir ${batch_dir} \
<<<<<<< HEAD:src/scripts/generate_instructions_for_chat_completion.sh
    --num_instructions_to_generate 10000 \
=======
    --num_instructions_to_generate 2000 \
>>>>>>> 06cc15f6a42445eae78612cbcd4c619d91e967e4:src/scripts/chat_completion_generate/generate_instructions.sh
    --seed_tasks_path seed_data/seed_tasks.jsonl \
    --model "gpt-3.5-turbo"