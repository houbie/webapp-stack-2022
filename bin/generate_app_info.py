#!/usr/bin/env python3

import datetime
import json
import os
import platform
import subprocess
from pathlib import Path


def read_git_commit():
    r = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True, check=True, text=True)
    return r.stdout.rstrip()


def read_git_branch():
    if "BRANCH_NAME" in os.environ:
        return os.environ["BRANCH_NAME"]
    r = subprocess.run(["git", "rev-parse", "--abbrev-ref", "HEAD"], capture_output=True, check=True, text=True)
    return r.stdout.rstrip()


def generate_app_info():
    commit = read_git_commit()
    branch = read_git_branch()
    # TODO: read version from tag
    return {
        "Built-Date": datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc, microsecond=0).isoformat(),
        "Git-Commit": commit,
        "Git-Branch": branch,
        "Created-By": f"Python {platform.python_version()}",
    }


def write_app_info():
    data = generate_app_info()
    # make sure generated folder exists
    generated = Path("generated")
    generated.mkdir(exist_ok=True)
    with generated.joinpath("app-info.json").open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4, sort_keys=True)


if __name__ == "__main__":
    write_app_info()
