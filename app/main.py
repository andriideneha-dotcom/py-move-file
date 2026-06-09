import os
import shutil


def move_file(command: str) -> None:
    parts = command.split()

    src = parts[1]
    dst = parts[2]

    if dst.endswith("/"):
        os.makedirs(dst, exist_ok=True)
        dst = os.path.join(dst, os.path.basename(src))
    else:
        parent_dir = os.path.dirname(dst)
        if parent_dir:
            os.makedirs(parent_dir, exist_ok=True)

    shutil.move(src, dst)
