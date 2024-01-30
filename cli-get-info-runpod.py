import runpod
import os
from dotenv import load_dotenv, find_dotenv

## LOAD/CHECK ENV TOKENS 
_ = load_dotenv(find_dotenv())
HF_ACCESS_TOKEN = os.getenv("HF_ACCESS_TOKEN", "hf-some-token")
RUNPOD_API_KEY = os.getenv("RUNPOD_API_KEY", "add-here-if-not-set-in-env-file")
assert HF_ACCESS_TOKEN.startswith("hf_"), "This doesn't look like a valid Hugging Face Token"
assert not RUNPOD_API_KEY.startswith("add-here"), "This doesn't look like a valid Runpod API Key"

runpod.api_key = RUNPOD_API_KEY 
print("HF_ACCESS_TOKEN: " + HF_ACCESS_TOKEN[0:6])
print("RUNPOD_API_KEY: " + runpod.api_key[0:6])
print()

print("GPUs: ")
for gpu in runpod.get_gpus():
    # print(gpu)
    detail = runpod.get_gpu(gpu["id"])
    print(detail)

# OR in slowblood module:
# with RUNPOD_API_KEY in .env or ENVIRONMENT
# slowblood.runpod_get_available_gpus()

# OR from shell:
# python -c "import slowblood;slowblood.runpod_get_available_gpus()"