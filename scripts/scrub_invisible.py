#!/usr/bin/env python3
from pathlib import Path

BANNED = {'tmp','temp','\u200b'}


def scrub_invisible(path: str) -> int:
    p = Path(path)
    found = 0
    for f in p.rglob('*'):
        name = f.name.replace('\u200b','')
        if name != f.name:
            f.rename(f.with_name(name))
            found += 1
    return found

if __name__ == '__main__':
    import sys
    target = sys.argv[1] if len(sys.argv)>1 else '.'
    print(scrub_invisible(target))
