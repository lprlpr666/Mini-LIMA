batch_dir=data/mistral_generations/
api_key="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"
base_url="https://openrouter.ai/api/v1"

python src/self-instruct/bootstrap_instructions.py \
    --batch_dir ${batch_dir} \
    --num_instructions_to_generate 2000 \
    --seed_tasks_path seed_data/seed_tasks.jsonl \
    --model "mistralai/mistral-7b-instruct:free" \
    --api_key ${api_key} \
    --base_url ${base_url}

python src/self-instruct/identify_clf_or_not.py \
    --batch_dir ${batch_dir} \
    --model "mistralai/mistral-7b-instruct:free" \
    --request_batch_size 5 \
    --api_key ${api_key} \
    --base_url ${base_url}

python src/self-instruct/generate_instances.py \
    --batch_dir ${batch_dir} \
    --api_key ${api_key} \
    --base_url ${base_url} \
    --input_file machine_generated_instructions.jsonl \
    --output_file machine_generated_instances.jsonl \
    --max_instances_to_gen 5 \
    --model "mistralai/mistral-7b-instruct:free" \
    --request_batch_size 5

python src/self-instruct/prepare_for_finetuning.py \
    --instance_files ${batch_dir}/machine_generated_instances.jsonl \
    --classification_type_files ${batch_dir}/is_clf_or_not_mistral/mistral-7b-instruct:free_template_1.jsonl \
    --output_dir ${batch_dir}/finetuning_data \
    --include_seed_tasks \
    --seed_tasks_path seed_data/seed_tasks.jsonl

python src/data_trans.py