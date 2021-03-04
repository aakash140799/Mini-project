
import numpy as np
from scripts.grabscreen import grab_screen
import cv2
import time
from scripts.getkeys import key_check
import os
from Variables import w, a, s, d, wa, wd, sa, sd, nk
from Variables import path, log_path, GAME_WIDTH, GAME_HEIGHT, WIDTH, HEIGHT


def save(x):
    _file.write(x+'\n')
    print(x)


def keys_to_output(keys):
    """
    Convert keys to a ...multi-hot... array
     0  1  2  3  4   5   6   7    8
    [W, S, A, D, WA, WD, SA, SD, NOKEY] boolean values.
    """
    if 'W' in keys and 'A' in keys:
        return wa
    elif 'W' in keys and 'D' in keys:
        return wd
    elif 'S' in keys and 'A' in keys:
        return sa
    elif 'S' in keys and 'D' in keys:
        return sd
    elif 'W' in keys:
        return w
    elif 'S' in keys:
        return s
    elif 'A' in keys:
        return a
    elif 'D' in keys:
        return d
    else:
        return nk


def collect(file_name, starting_value):
    training_data = []

    last_time = time.time()
    paused = False
    save('STARTING!!!')
    fps = 0.0

    while True:
        
        if not paused:
            screen = grab_screen(region=(0, 40, GAME_WIDTH, GAME_HEIGHT))
            # resize to something a bit more acceptable for a CNN
            screen = cv2.resize(screen, (WIDTH, HEIGHT))
            # run a color convert;
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)
            
            keys = key_check()
            output = keys_to_output(keys)
            training_data.append([screen, output])

            # Get fps
            diff = round(float(time.time() - last_time), 2)
            fps += round(float(1 / diff), 1)

            last_time = time.time()

            if len(training_data) % 100 == 0:
                save('Avg.fps: ' + str(round(fps/100, 1)))
                fps = 0.0
                
                if len(training_data) == 500:
                    np.save(file_name, training_data)
                    save('SAVED-{}'.format(starting))
                    training_data = []
                    starting_value += 1
                    file_name = path + 'training_data-{}.npy'.format(starting_value)

        keys = key_check()
        if 'T' in keys:
            if paused:
                paused = False
                save('Resumed!')
                time.sleep(1)
            else:
                save('Pausing!')
                paused = True
                time.sleep(1)


if __name__ == '__main__':

    _file = open(log_path + "Collection_log.txt", 'w')

    for i in list(range(4))[::-1]:
        save(str(i+1))
        time.sleep(1)

    starting = 1

    while True:
        file = path + 'training_data-{}.npy'.format(starting)

        if os.path.isfile(file):
            save('File exists, moving along' + str(starting))
            starting += 1
        else:
            save('File does not exist, starting fresh!' + str(starting))
            break

    collect(file_name=file, starting_value=starting)

    _file.close()
