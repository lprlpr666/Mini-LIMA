batch_dir=data/mistral_generations/
api_key="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"
base_url="https://openrouter.ai/api/v1"

python src/self-instruct/identify_clf_or_not.py \
    --batch_dir ${batch_dir} \
    --model "gpt-3.5-turbo-instruct" \
    --request_batch_size 5 \
    # --api_key ${api_key} \
    # --base_url ${base_url}