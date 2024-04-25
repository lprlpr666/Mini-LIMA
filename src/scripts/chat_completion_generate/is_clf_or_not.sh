batch_dir=data/gpt3_generations/


python src/self-instruct/identify_clf_or_not.py \
    --batch_dir ${batch_dir} \
    --model "gpt-3.5-turbo" \
    --request_batch_size 5 \
    --chat_api True 