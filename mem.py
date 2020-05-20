#!/usr/bin/env python3

import matplotlib.pyplot as plt
import subprocess

COUNT = 10

cmd = subprocess.run(['ps', '-caxm', '-orss,comm'], capture_output=True)
procs = cmd.stdout.decode('utf-8').split("\n")[1:-1]

mems = []
labels = []
explodes = []
for proc in procs:
    (mem, label) = proc.strip().split(' ', maxsplit=1)
    if len(mems) < COUNT:
        mems.append(mem)
        labels.append(label)
        explodes.append(0)
explodes[0] = 0.1

plt.pie(mems, explode=explodes, labels=labels, autopct='%1.1f%%')
plt.axis('equal')
plt.show()