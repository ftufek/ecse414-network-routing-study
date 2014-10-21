import time
import os
from multiprocessing import Pool

folder = time.strftime("%Y-%m-%d-%H:%M:%S")
os.system("mkdir "+folder)

def trace(folder, domain):
	os.system("cd " + folder + " && traceroute " + domain + " > " + domain + ".txt")

results = []
pool = Pool(processes=10)
with open("totrace.txt") as f:
	content = f.readlines()
	for host in content:
		t = host.strip()
                results.append(pool.apply_async(trace, [folder, t]))

for res in results:
	res.get(timeout=30)
