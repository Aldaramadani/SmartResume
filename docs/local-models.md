# Local Model Deployment

SmartResume can run without external APIs in two different ways.

## Option 1: OpenAI-compatible vLLM server

1. Install vLLM and download the resume model:
   ```bash
   pip install vllm
   python scripts/download_models.py
   ```
2. Launch the server (port 8001 is used by default in the config):
   ```bash
   python -m vllm.entrypoints.openai.api_server \
     --model ./models/Qwen3-0.6B \
     --port 8001 \
     --host 0.0.0.0 \
     --tensor-parallel-size 1
   ```
3. Update `configs/config.yaml` so that the extraction channels point to the local endpoint:
   ```yaml
   channels:
     local_qwen:
       name: "models/Qwen3-0.6B"
       api_url: "http://localhost:8001/v1"
       api_key: "local"

   extract_channels:
     basic_info: "local_qwen"
     work_experience: "local_qwen"
     education: "local_qwen"
   ```
4. Run the parser as usual:
   ```bash
   python scripts/start.py --file resume.pdf
   ```

## Option 2: Direct model loading (offline)

If you prefer to load the Transformers model directly, enable the direct mode in the same config:

```yaml
use_direct_models: true
direct_model_name: "models/Qwen3-0.6B"
```

When `use_direct_models` is true, SmartResume first attempts to load the model from disk and falls back to the configured channels or remote API if necessary.

## Python API example

```python
from smartresume import ResumeAnalyzer

analyzer = ResumeAnalyzer(init_ocr=True, init_llm=True, config_path="configs/config.yaml")
result = analyzer.pipeline(
    cv_path="resume.pdf",
    resume_id="resume_001",
    extract_types=["basic_info", "work_experience", "education"],
)
```

No extra arguments are required—the behavior is entirely driven by the YAML configuration.