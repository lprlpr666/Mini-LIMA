batch_dir=data/gpt3_generations/

python src/self-instruct/generate_instances.py \
    --batch_dir ${batch_dir} \
    --input_file machine_generated_instructions.jsonl \
    --output_file machine_generated_instances.jsonl \
    --max_instances_to_gen 5 \
    --model "gpt-3.5-turbo" \
    --request_batch_size 5 \
    --chat_api True