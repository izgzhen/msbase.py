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
print(try_call_std(["ls", "."], cwd="/tmp"))

def task(i):
    return i + 1

print(multiprocess(task, [1, 2, 3], n = 2))
