import os
import sys
import random
import subprocess


if __name__ ==' __main__':
    if len(sys.argv) < 2:
        raise Exception('Positional requirement "host" required')
    
    hosts = ['h1', 'h2', 'h3', 'h4', 'h5']
    hosts.remove(sys.argv[1])

    if not os.path.exists('log'):
        os.mkdir('log')

    while True:
        target = random.choice(hosts)
        random_number = random.gauss(0, 1)
        with open('log/mininet.log', 'a') as f:
        if random_number > 21:
            subprocess.Popen(["ping", "-c", "20", "-s", "32768", target], stdout=f)
        else:
            subprocess.Popen(["ping", "-c", "5", target], stdout=f)