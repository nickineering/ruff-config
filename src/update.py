import shutil
from pathlib import Path


def update_ruff_base() -> None:
    """Copy the ruff.toml file to the new package so it can be extended from."""
    src_file = Path(__file__) / "nickineering-ruff-base.toml"
    dest_file = Path.cwd() / "ruff.toml"
    shutil.copy(src_file, dest_file)
