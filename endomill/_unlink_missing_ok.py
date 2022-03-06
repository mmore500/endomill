from pathlib import Path


def unlink_missing_ok(path: str) -> None:
    # only python 3.8+ allows convenient missing_ok kwarg for unlink
    try:
        Path(path).unlink()
    except FileNotFoundError:
        pass
