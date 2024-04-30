import os
import shutil
import config as cfg

try:
    shutil.rmtree(cfg.extract_dest_path)
    # os.remove(cfg.diff_record_path)
except Exception as e:
    print(e)

