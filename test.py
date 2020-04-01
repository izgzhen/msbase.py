import json
import os

from msbase.utils import log_progress

for i in log_progress(list(range(0, 10))):
    print(i)

for i in log_progress(list(range(0, 10)), desc="desc", print_item=True):
    print(i)

import msbase.argparse_ as argparse

p = argparse.p()
p.add_argument('integers', type=int, help='just some integers')
args = p.parse_args()
print(args.integers)


from msbase.subprocess_ import report_call_std

report = report_call_std(["ls", "."], timeout_s=1)
print(json.dumps(report))

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
print(multiprocess(task, [1, 2, 3], n = 2, debug_mode=True))

from msbase.lab import Step, AbstractLab, to_matrix

config1 = { "A": ["A1", "A2" ], "B": ["B1", "B2"] }
assert len(to_matrix(config1)) == 4

assert len(to_matrix({})) == 1

step1 = Step("mysleep1", ["./mysleep", "1"])
step2 = Step("mysleep2", ["./mysleep", "2"])

class MyLab(AbstractLab):
    def digest_output(self, name: str, output, command):
        return { "STDOUT length": len(output[0]) }

    def digest_column_names(self):
        return [ "STDOUT length"]

lab = MyLab("mylab", [step1, step2],
            configurations={ "A": ["A1", "A2" ], "B": ["B1", "B2"] })
lab.run()

import os
f = [f for f in os.listdir(".") if f.endswith(".log")][0]
from msbase.utils import load_jsonl
assert_eq(len(load_jsonl(f)), 8)
lab.analyze()
os.remove(f)
os.remove('results.tex')

from msbase.logging import logger

logger.warn("bye!")

from msbase.utils import sha256sum

print(sha256sum("test.py"))
