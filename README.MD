# BitNetDocker Setup (By LuffyAI)

## Folder Structure

- **API (TO-DO)**  
  FastAPI service for locally hosting the LLM and exposing it to other applications.

- **Patch**  
  Fixes applied to the BitNet repository to ensure successful compilation and execution.

- **Pipeline (TO-DO)**  
  Command-line interface that simplifies interacting with BitNet.

## Setup

- To download models other than the default, add your Hugging Face token to and use setup_env:
  ```
  pipeline/.env
  EXAMPLE: python setup_env --hf-repo [SUPPORTED MODEL IN THE setup_env.py file] -q i2_s
  EXAMPLE: python setup_env --hf-repo tiiuae/Falcon3-10B-Base-1.58bit -q i2_s
  ```



- To run inference, use the command python run_inference.py -m <DIR_TO_MODEL's gguff> -p "<SYSTEM_PROMPT>" -cnv

- Example: python run_inference.py -m models/bitnet-b1.58-2B-4T/ggml-model-i2_s.gguf -p "You are a helpful assistant" -cnv

## Running

- To directly access the container shell:
  ```
  docker compose run base bash
  ```
