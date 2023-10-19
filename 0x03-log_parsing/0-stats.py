#!/usr/bin/python3
import sys

total_size = 0
status_codes = {str(i): 0 for i in [200, 301, 400, 401, 403, 404, 405, 500]}

try:
    for i, line in enumerate(sys.stdin, 1):
        try:
            parts = line.split()
            status_code = parts[-2]
            file_size = int(parts[-1])
            if status_code in status_codes:
                status_codes[status_code] += 1
            total_size += file_size
        except (IndexError, ValueError):
            pass

        if i % 10 == 0:
            print("File size: {}".format(total_size))
            for code in sorted(status_codes.keys()):
                if status_codes[code] > 0:
                    print("{}: {}".format(code, status_codes[code]))
except KeyboardInterrupt:
    pass
finally:
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))
