batch_dir=data/mistral_generations/
api_key="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"
base_url="https://openrouter.ai/api/v1"

python src/self-instruct/generate_instances.py \
    --batch_dir ${batch_dir} \
    --input_file machine_generated_instructions.jsonl \
    --output_file machine_generated_instances.jsonl \
    --max_instances_to_gen 5 \
    --model "gpt-3.5-turbo-instruct" \
    --request_batch_size 5