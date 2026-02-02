import argparse
import asyncio
from pathlib import Path

BITNET_DIR = Path("/app/BitNet")

async def run(*cmd, cwd=BITNET_DIR):
    proc = await asyncio.create_subprocess_exec(
        *cmd,
        cwd=cwd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )

    stdout, stderr = await proc.communicate()

    if proc.returncode != 0:
        raise RuntimeError(stderr.decode())

    return stdout.decode()


async def main(args):
    if args.test:
        """This is a quick test to see if the pipeline can interact with the base BitNet system."""
        print("Running BitNet inference via base system...")
        output = await run(
              "python3",
              "run_inference.py",
              "-m", "/app/BitNet/models/bitnet-b1.58-2B-4T/ggml-model-i2_s.gguf",
              "-p", "What are your favorite books?",
          )
        print(output)
    elif args.chat:
        proc = await asyncio.create_subprocess_exec(
            "streamlit",
            "run",
            "interface.py",
            "--server.port=8501",
            "--server.address=0.0.0.0",
        )
        # Hand off control to Streamlit and wait forever
        await proc.wait()
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--test",
        action="store_true",
        help="Run BitNet inference via base system"
    )
    parser.add_argument(
        "--chat",
        action="store_true",
        help="Launch the BitNet chat interface"
    )
    args = parser.parse_args()
    asyncio.run(main(args))
