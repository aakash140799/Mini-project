import os

# Current phase
phase = 2

# Current path to saved models
path = './MODELS/phase' + str(phase) + '/'

# Current path to balanced models
bpath = './MODELS/balanced_phase/'

# Current path to logs
log_path = './Logs/'

# Inputs
w = [1, 0, 0, 0, 0, 0, 0, 0, 0]
s = [0, 1, 0, 0, 0, 0, 0, 0, 0]
a = [0, 0, 1, 0, 0, 0, 0, 0, 0]
d = [0, 0, 0, 1, 0, 0, 0, 0, 0]
wa = [0, 0, 0, 0, 1, 0, 0, 0, 0]
wd = [0, 0, 0, 0, 0, 1, 0, 0, 0]
sd = [0, 0, 0, 0, 0, 0, 0, 1, 0]
sa = [0, 0, 0, 0, 0, 0, 1, 0, 0]
nk = [0, 0, 0, 0, 0, 0, 0, 0, 1]

# No.of training files in current phase
FILE_I_END = len([name for name in os.listdir(path)
                  if os.path.isfile(os.path.join(path, name))])

# Captured dimensions
WIDTH = 160
HEIGHT = 120

MODEL_NAME = 'V1'

LR = 1e-3
EPOCHS = 30

# Collecting/Playing dimensions
GAME_WIDTH = 1600
GAME_HEIGHT = 1200


# Opening cmd at CWD, then-
# tensorboard --logdir="./log"

