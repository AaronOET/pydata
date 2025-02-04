# chk.py
import tensorflow as tf
import os

os.environ["CUDA_VISIBLE_DIVICES"] = "0"

print(tf.__version__)