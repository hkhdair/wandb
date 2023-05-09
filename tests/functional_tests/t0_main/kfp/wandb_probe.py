import os
import subprocess


def wandb_probe_package():
    if not os.environ.get("WB_PROBE_PACKAGE"):
        return
    s, o = subprocess.getstatusoutput("git rev-parse HEAD")
    if s:
        return
    return f"git+https://github.com/wandb/wandb.git@{o}#egg=wandb"
