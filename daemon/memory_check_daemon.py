import json
from time import sleep
from pathlib import Path

import psutil


def main():
    while True:
        output_file = open(Path('/tmp/memory_info.txt'), 'w')
        output_file.write(
            json.dumps(str(psutil.virtual_memory())[6:-1])
            )
        output_file.close()
        sleep(1)


if __name__ == '__main__':
    main()
