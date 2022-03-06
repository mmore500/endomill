import atexit
import shutil
import warnings


def add_instance_outpath(outpath: str) -> None:
    if not outpath.endswith('.endomill.ipynb'):
        warnings.warn(f'outpath {outpath} missing .endomill.ipynb extension')

    @atexit.register
    def add_instance_outpath_callback():
        shutil.copy('executing.endomill.ipynb', outpath)
