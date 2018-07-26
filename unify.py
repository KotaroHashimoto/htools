#!/usr/bin/env python3

import hashlib
import pathlib
import os

#files = glob.glob('*', recursive = True)
files = pathlib.Path().glob('**/*')

hash = hashlib.md5()

h2f = {}

for f in files:

    f = str(f)
    if not os.path.isfile(f) or f.endswith('unify.py'):
        continue    

    with open(f, 'rb') as fp:
        while True:
            chunk = fp.read(2048 * hash.block_size)
            if len(chunk) == 0:
                break

            hash.update(chunk)

    h = hash.hexdigest()    
#    print(f, h)

    if h in h2f:

        if f.split('/')[-1].startswith('.'):
            os.remove(f)
            print(f, 'removed,', h2f[h], 'being remaind')
            continue
        
        elif h2f[h].split('/')[-1].startswith('.'):
            os.remove(h2f[h])
            print(h2f[h], 'removed,', f, 'being remaind')
            h2f[h] = f
            continue

        if len(f) < len(h2f[h]):
            os.remove(h2f[h])
            print(h2f[h], 'removed,', f, 'being remaind')
            h2f[h] = f
            continue

        else:
            os.remove(f)
            print(f, 'removed,', h2f[h], 'being remaind')
            continue
            

    h2f[h] = f
    fp.close()
    
