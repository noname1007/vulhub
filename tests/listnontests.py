#!/usr/bin/env python
import yaml
import os
import tempfile


with open(r'../.github/workflows/docker-image.yml', 'r') as f:
    data = yaml.load(f, Loader=yaml.SafeLoader)


ylist = []
for _, job in data['jobs'].items():
    if not isinstance(job, dict):
        continue

    for step in job['steps']:
        if 'name' not in step:
            continue
        
        name = step['name']
        if name == 'cleanup':
            continue
        
        ylist.append(name)


nlist = []
for name in os.listdir('../base'):
    nlist.append(name)


ylist = sorted(ylist)
nlist = sorted(nlist)

with open('/tmp/1', 'w') as f:
    f.write('\n'.join(ylist))

with open('/tmp/2', 'w') as f:
    f.write('\n'.join(nlist))
