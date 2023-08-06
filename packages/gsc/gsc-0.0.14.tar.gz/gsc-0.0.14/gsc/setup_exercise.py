import os
import pathlib
from gsc import cli
from gsc.exercises import (
    push_and_pull,
    sync_error,
    merge_conflict,
    multiple_remotes,
    use_the_force,
)


class SetupError(Exception):
    pass


def setup(gsc_id: str):
    while not os.path.exists(".git"):
        os.chdir("..")
        if os.getcwd() == "/":
            raise SetupError("This is not a git repo.")

    if not gsc_id:
        if not os.path.exists(".gsc_id"):
            raise SetupError(
                "Could not find a Git Scientist exercise ID.\n"
                "Did you mean to give an ID as an argument to gsc?"
            )
        gsc_id = pathlib.Path(".gsc_id").read_text().strip()

    # Just in case someone decides to use dashes.
    gsc_id = gsc_id.replace("-", "_")

    cli.info(f"Setting up {gsc_id}")

    if gsc_id == "push_and_pull":
        push_and_pull.setup()
    elif gsc_id == "sync_error":
        sync_error.setup()
    elif gsc_id == "merge_conflict":
        merge_conflict.setup()
    elif gsc_id == "multiple_remotes":
        multiple_remotes.setup()
    elif gsc_id == "use_the_force":
        use_the_force.setup()
    else:
        raise SetupError("Unknown Git Scientist exercise. Try upgrading gsc.")
