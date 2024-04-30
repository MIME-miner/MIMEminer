import os
import shutil
import config as cfg

try:
    shutil.rmtree(cfg.origin_dir)
    shutil.rmtree(cfg.mutated_dir)
    os.remove(cfg.att_dict_path)
    os.remove(cfg.mutation_log_path)
except Exception as e:
    print(e)

try:
    os.makedirs(cfg.origin_dir)
    os.makedirs(cfg.mutated_dir)
except Exception as e:
    print(e)
