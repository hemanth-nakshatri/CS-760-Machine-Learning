from os import system

alphas = [0.001, 0.01, 0.002, 0.003, 0.004, 0.005]

for alpha in alphas:
    system(f"python run.py -s a2c -t 1000 -d CartPole-v1 -G 200 -e 2000 -a {alpha} -g 0.95 -l [32] --no-plots")