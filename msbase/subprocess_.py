import subprocess
import os
import sys
import glob
from os.path import join

def call_std(args, cwd=None, env=None, output=True):
    if output:
        p = subprocess.Popen(args, stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE, cwd=cwd, env=env)
        stdout, stderr = p.communicate()
        return_code = p.wait()
        return (return_code, str(stdout, "utf-8"), str(stderr, "utf-8"))
    else:
        code = subprocess.call(args, cwd=cwd, env=env)
        return (code, None, None)

def try_call_std(args, cwd=None, env=None, verbose=True, output=True):
    if verbose:
        cprint("+ " + " ".join(args), "blue")
    code, stdout, stderr = call_std(args, cwd, env, output)
    if code != 0:
        if verbose:
            print("STDOUT: ")
            print(stdout)
            print("STDERR: ")
            cprint(stderr, "red")
        raise Exception("calling " + " ".join(args) + " failed")
    else:
        return stdout, stderr

from multiprocessing import Pool, Value
import time

def multiprocess(task, inputs, n: int, verbose=True, return_dict=True):
    counter = Value('i', 0)
    total = float(len(inputs))
    start_time = time.time()

    global run
    def run(input):
        with counter.get_lock():
            if verbose:
                print("%fs - progress: %f" % (time.time() - start_time, counter.value / total))
            counter.value += 1
        try:
            return (True, task(input))
        except Exception as e:
            return (False, e)

    with Pool(n) as p:
        results = p.map(run, inputs)
        if verbose:
            print("total spent time: %f" % (time.time() - start_time))
        if return_dict:
            return dict(zip(inputs, results))
        else:
            return results
