
import cv2
import numpy as np
import pandas as pd
from collections import Counter
from Variables import w, a, s, d, wa, wd, sa, sd, nk
from Variables import FILE_I_END, path, log_path


def save(x):
    _file.write(x+'\n')
    print(x)


def count_moves(df):
    count = Counter(df[1].apply(str))
    for i, j in count.items():
        if i == str(w):
            save('w: {}'.format(j))
        elif i == str(s):
            save('s: {}'.format(j))
        elif i == str(a):
            save('a: {}'.format(j))
        elif i == str(d):
            save('d: {}'.format(j))
        elif i == str(wa):
            save('wa: {}'.format(j))
        elif i == str(wd):
            save('wd: {}'.format(j))
        elif i == str(sa):
            save('sa: {}'.format(j))
        elif i == str(sd):
            save('sd: {}'.format(j))
        elif i == str(nk):
            save('ntg: {}'.format(j))


if __name__ == '__main__':

    _file = open(log_path + "/View_log.txt", 'w')

    for index in range(1, FILE_I_END+1):
        temp_data = np.load(path + 'training_data-{}.npy'.format(index),
                            allow_pickle=True)
        if index == 1:
            train_data = temp_data
        else:
            train_data = np.concatenate((train_data, temp_data))

    _df = pd.DataFrame(train_data)
    save(str(_df.head()))

    count_moves(_df)
    save("Total : {}".format(len(train_data)))

    for data in train_data:
        img = data[0]
        choice = data[1]

        cv2.imshow('test', img)
        # save(str(choice))
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

    _file.close()
