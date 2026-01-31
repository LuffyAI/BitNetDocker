import argparse
import asyncio  


async def main(args):
    if args.test:
       pass

    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--test", action='store_true', help='Runs a test of the BitNet pipeline')
    args = parser.parse_args()
    asyncio.run(main(args))
