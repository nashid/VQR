python run.py \
    --load_pretrained_t5 \
    --model_name=pretrained_mask_model.bin \
    --output_dir=./saved_models \
    --tokenizer_name=Salesforce/codet5-base \
    --model_name_or_path=Salesforce/codet5-base \
    --do_train \
    --train_data_file=../data/vrepair_non_domain_data/processed_non_domain_train.csv \
    --eval_data_file=../data/vrepair_non_domain_data/processed_non_domain_val.csv \
    --epochs 75 \
    --encoder_block_size 512 \
    --vul_repair_block_size 256 \
    --train_batch_size 8 \
    --eval_batch_size 2 \
    --learning_rate 1e-4 \
    --max_grad_norm 1.0 \
    --evaluate_during_training \
    --seed 123456  2>&1 | tee pretrain.log