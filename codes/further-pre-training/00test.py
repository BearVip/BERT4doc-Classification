import tensorflow as tf
import numpy as np
import pandas as pd
import fastNLP as fn
import sys
import torch



print(torch.__version__) # 1.7.0+cpu
print(torch.distributed.is_available()) # True

print(pd.__version__) #　1.0.0
print(np.__version__) # 1.16.0
print(tf.__version__) # 1.15.0
print(fn.__version__) # 1.0.1

print(sys.version) # 3.7.9