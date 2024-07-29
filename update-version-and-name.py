#!/bin/python3
import yaml
import sys

file_path = 'org.DolphinEmu.dolphin-emu.yml'
commit = sys.argv[1]
with open(file_path) as f:
    y = yaml.safe_load(f)
    y['app-id'] = 'org.DolphinEmu.dolphin-emu-latest'
    for module in y.get('modules', []):
        if module['name'] == 'dolphin-emu':
            module['sources'][0]['commit'] = commit

with open(file_path, 'w') as output:
    yaml.dump(y, output, default_flow_style=False, sort_keys=False)
