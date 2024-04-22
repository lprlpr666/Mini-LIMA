batch_dir=data/gpt3_comp_generations/

python src/self-instruct/bootstrap_instructions.py \
    --batch_dir ${batch_dir} \
    --num_instructions_to_generate 2000 \
    --seed_tasks_path seed_data/seed_tasks.jsonl \
    --model "gpt-3.5-turbo-instruct"

python src/self-instruct/identify_clf_or_not.py \
    --batch_dir ${batch_dir} \
    --model "gpt-3.5-turbo-instruct" \
    --request_batch_size 5

python src/self-instruct/generate_instances.py \
    --batch_dir ${batch_dir} \
    --input_file machine_generated_instructions.jsonl \
    --output_file machine_generated_instances.jsonl \
    --max_instances_to_gen 5 \
    --model "gpt-3.5-turbo-instruct" \
    --request_batch_size 5

python src/self-instruct/prepare_for_finetuning.py \
    --instance_files ${batch_dir}/machine_generated_instances.jsonl \
    --classification_type_files ${batch_dir}/is_clf_or_not_gpt-3.5-turbo-instruct_template_1.jsonl \
    --output_dir ${batch_dir}/finetuning_data \
    --include_seed_tasks \
    --seed_tasks_path seed_data/seed_tasks.jsonl

python src/data_trans.py