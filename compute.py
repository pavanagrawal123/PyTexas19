import requests
from multiprocessing import Pool, TimeoutError
from string import printable
import random
import hashlib 
import argparse
count = 1000
done = 0

parser = argparse.ArgumentParser(description='Config the script.')


parser.add_argument('--address', type=str, help='address to query')
parser.add_argument('--count', type=int, help='how many hashes to break')
parser.add_argument('--concurrency', type=int, help='how concurrently the API should be called')
args = parser.parse_args()


def invoke(val):
    global done
    done+=1
    string = ''.join(random.choices(printable, k=3))
    hsh = hashlib.md5(string.encode()).hexdigest()
    print("sent" + args.address  + "/?hash=" + hsh + "?&start=" + str(0) + "&end=" + str(1000000))
    val = requests.get(args.address + "/?hash=" + hsh + "&start=" + str(0) + "&end=" + str(1000000))
    print("processed" + args.address  + "/?hash=" + hsh + "?&start=" + str(0) + "&end=" + str(1000000))
    return val.text


with Pool(processes=args.concurrency) as pool:
    results = pool.map(invoke, range(args.count))
    print(results)
