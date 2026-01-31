# BitNetDocker Setup (By LuffyAI)

## Folder Structure

- **API**  
  FastAPI service for locally hosting the LLM and exposing it to other applications.

- **Patch**  
  Fixes applied to the BitNet repository to ensure successful compilation and execution.

- **Pipeline**  
  Command-line interface that simplifies interacting with BitNet.

## Setup

- To download models other than the default, add your Hugging Face token to:
  ```
  pipeline/.env
  ```

## Running

- To directly access the container shell:
  ```
  docker compose run base sh
  ```
