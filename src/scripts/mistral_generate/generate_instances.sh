batch_dir=data/mistral_generations/

python src/self-instruct/generate_instances.py \
    --batch_dir ${batch_dir} \
    --api_key "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" \
    --input_file machine_generated_instructions.jsonl \
    --output_file machine_generated_instances.jsonl \
    --max_instances_to_gen 5 \
    --model "mistralai/mistral-7b-instruct:free" \
    --request_batch_size 5