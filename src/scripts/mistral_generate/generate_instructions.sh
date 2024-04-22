batch_dir=data/mistral_generations/

python src/self-instruct/bootstrap_instructions.py \
    --batch_dir ${batch_dir} \
    --num_instructions_to_generate 2000 \
    --seed_tasks_path seed_data/seed_tasks.jsonl \
    --model "mistralai/mistral-7b-instruct:free" \
    --api_key "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" \
    --base_url "https://openrouter.ai/api/v1"