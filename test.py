import json
import os

from msbase.utils import *
from msbase.logging import logger
import msbase.argparse_ as argparse
from msbase.subprocess_ import *
from msbase.assert_ import *
from msbase.lab import Step, AbstractLab, to_matrix

write_yaml(load_yaml("test.yaml"), "test.yaml")


def task(i):
    return i + 1

if __name__ == "__main__":
    for i in log_progress(list(range(0, 10))):
        print(i)

    for i in log_progress(list(range(0, 10)), desc="desc", print_item=True):
        print(i)

    p = argparse.p()
    p.add_argument('integers', type=int, help='just some integers')
    args = p.parse_args()
    print(args.integers)

    report = report_call_std(["ls", "."], timeout_s=1)
    print(json.dumps(report))

    assert_eq(1, 1)
    assert_le(1, 2, "1 > 2")

    print(call_std(["ls", "unknown"]))
    ret = try_call_std(["./foo"])
    assert ret == ("standard\n", "error\n", 0), ret

    print(multiprocess(task, [1, 2, 3], n = 2))
    print(multiprocess(task, [1, 2, 3], n = 2, debug_mode=True))

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

    f = [f for f in os.listdir(".") if f.endswith(".log")][0]
    assert_eq(len(load_jsonl(f)), 8)
    lab.analyze()
    os.remove(f)
    os.remove('results.tex')


    logger.warn("bye!")

    print(sha256sum("test.py"))
