from itertools import permutations
import subprocess

signals = []
for phase in permutations(range(0,5)):
    input_ = 0
    for n in phase:
        amplifier = subprocess.run('python3 ../5/5b.py input.txt', shell=True, universal_newlines=True, input="{}\n{}".format(n, input_), stdout=subprocess.PIPE)
        input_ = int(amplifier.stdout)

    signals.append(input_)
print(sorted(signals)[-1:])




