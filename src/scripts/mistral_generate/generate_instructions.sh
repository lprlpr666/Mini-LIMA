batch_dir=data/test/
api_key="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"
base_url="https://openrouter.ai/api/v1"

python src/self-instruct/bootstrap_instructions.py \
    --batch_dir ${batch_dir} \
    --num_instructions_to_generate 2000 \
    --seed_tasks_path seed_data/seed_tasks.jsonl \
    --model "mistralai/mistral-7b-instruct:free" \
    --api_key "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" \
    --base_url "https://openrouter.ai/api/v1"