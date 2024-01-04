import runpod
import json 
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


## VARS FOR MODEL AND GPU
podname = "Slowblood-Notebook"
# model = "codellama/CodeLlama-13b-Instruct-hf"

envs = {"HUGGING_FACE_HUB_TOKEN":HF_ACCESS_TOKEN, 
        #"QUANTIZE":"gptq", 
        "MAX_INPUT_LENGTH": json.dumps(16384),
        "MAX_TOTAL_TOKENS": json.dumps(23040),
        "MAX_BATCH_BATCH_TOKENS": json.dumps(23040),
        "MAX_BATCH_PREFILL_TOKENS": json.dumps(16384),
        "JUPYTER_MODE":"notebook",
        "JUPYTER_PASSWORD":"foocat",
        "WEB_USER":"slowblood",
        "WEB_PASSWORD":"foocat",
        "WORKSPACE":"/workspace",
        }

gpu_type_id = "NVIDIA RTX A6000" # 48GB VRAM $0.79/hr
gpu_count = 1

pod = runpod.create_pod(
    name=podname,
    image_name="runpod/pytorch:3.10-2.0.1-118-runtime",
    gpu_type_id=gpu_type_id,
    cloud_type="SECURE",
    gpu_count=gpu_count,
    volume_in_gb=50,
    container_disk_in_gb=20,
    ports="80/http,8888/http",
    volume_mount_path="/workspace",
    env=envs,
)
    # data_center_id="US-KS-2",
    # docker_args="--model-id " + model,

SERVER_URL = f'https://{pod["id"]}-80.proxy.runpod.net'
print(SERVER_URL)
print(f"Docs (Swagger UI) URL: {SERVER_URL}/docs")

## Updates .env file with new  
env_file = open(".env", "a")  # append mode
env_file.write("\nRP_NB_ENDPOINT_URL=" + SERVER_URL + "\n")
env_file.write("RP_CURRENT_ID=" + {pod["id"]} + "\n")
env_file.close()


## REFERENCES
# https://docs.runpod.io/docs/create-pod