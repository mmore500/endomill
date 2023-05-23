import atexit
import shutil
import warnings


def add_instance_outpath(outpath: str) -> None:
    if not outpath.endswith('.endomill.ipynb'):
        warnings.warn(f'outpath {outpath} missing .endomill.ipynb extension')

    @atexit.register
    def add_instance_outpath_callback():
        # manual outpath only compatible with worker_id
        worker_id = 0
        shutil.copy(f'executing{worker_id}.endomill.ipynb', outpath)
