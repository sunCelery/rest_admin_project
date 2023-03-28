import json
from time import sleep
from pathlib import Path

import psutil


def main():
    while True:
        output_file = open('/tmp/memory_info.json', 'w')
        memory_info = psutil.virtual_memory()
        memory_dict = {
            'total': memory_info.total,
            'available': memory_info.available,
            'used': memory_info.used,
            'free': memory_info.free,
            'percent': memory_info.percent,
            'active': memory_info.active,
            'inactive': memory_info.inactive,
            'buffers': memory_info.buffers,
            'cached': memory_info.cached,
            'shared': memory_info.shared,
            'slab': memory_info.slab,
        }
        json.dump(memory_dict, output_file)
        output_file.close()
        sleep(1)


if __name__ == '__main__':
    main()
