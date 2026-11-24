import os
import shutil
import sys


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "./output"
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    if not os.path.isfile(src):
        print("error: entry.png not found next to main.py", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    copied = os.path.getsize(dst)
    if copied != os.path.getsize(src) or copied == 0:
        print("error: copied entry.png is empty or incomplete", file=sys.stderr)
        return 1
    print(f"wrote {dst} ({copied} bytes)")
    return 0


raise SystemExit(main())
