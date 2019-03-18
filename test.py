import msbase.argparse_ as argparse

p = argparse.p()
p.add_argument('integers', type=int, help='just some integers')
args = p.parse_args()
print(args.integers)

from msbase.assert_ import *

assert_eq(1, 1)
assert_le(1, 2, "1 > 2")

from msbase.subprocess_ import *

print(call_std(["ls", "unknown"]))
ret = try_call_std(["./foo"])
assert ret == ("standard\n", "error\n", 0), ret

def task(i):
    return i + 1

print(multiprocess(task, [1, 2, 3], n = 2))

from msbase.lab import Step, AbstractLab, to_matrix

config1 = { "A": ["A1", "A2" ], "B": ["B1", "B2"] }
assert len(to_matrix(config1)) == 4

assert len(to_matrix({})) == 1

step1 = Step("mysleep1", ["./mysleep", "1"],
             configurations={ "A": ["A1", "A2" ], "B": ["B1", "B2"] })
step2 = Step("mysleep2", ["./mysleep", "2"],
             configurations={ "A": ["A3", "A4" ], "B": ["B3", "B4"] })

class MyLab(AbstractLab):
    def digest_output(self, name: str, output):
        return {}

lab = MyLab("mylab", [step1, step2])
lab.run()

import os
f = [f for f in os.listdir(".") if f.endswith(".log")][0]
from msbase.utils import load_jsonl
assert len(load_jsonl(f)) == 8
os.remove(f)
