batch_dir=data/mistral_generations/
api_key="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"
base_url="https://openrouter.ai/api/v1"

python src/self-instruct/prepare_for_finetuning.py \
    --instance_files ${batch_dir}/machine_generated_instances.jsonl \
    --classification_type_files ${batch_dir}/is_clf_or_not_gpt-3.5-turbo-instruct_template_1.jsonl \
    --output_dir ${batch_dir}/finetuning_data \
    --include_seed_tasks \
    --seed_tasks_path seed_data/seed_tasks.jsonl