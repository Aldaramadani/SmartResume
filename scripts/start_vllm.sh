#!/bin/bash

export TORCH_COMPILE_DISABLED=1
export TORCHDYNAMO_DISABLE=1
export VLLM_USE_MODELSCOPE=False
export TRITON_CACHE_DIR=/tmp/triton_cache
export VLLM_ATTENTION_BACKEND=XFORMERS

CUDA_VISIBLE_DEVICES=1 python -m vllm.entrypoints.openai.api_server \
    --model ./models/Alibaba-EI/SmartResume/Qwen3-0.6B \
    --host localhost \
    --port 8001 \
    --tensor-parallel-size 1 \
    --gpu-memory-utilization 0.8 \
    --max-model-len 8192 \
    --trust-remote-code \
    --enforce-eager \
    --disable-custom-all-reduce
