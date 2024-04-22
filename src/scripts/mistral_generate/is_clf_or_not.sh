batch_dir=data/mistral_generations/

python src/self-instruct/identify_clf_or_not.py \
    --batch_dir ${batch_dir} \
    --model "mistralai/mistral-7b-instruct:free" \
    --request_batch_size 5