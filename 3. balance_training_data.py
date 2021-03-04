

from random import shuffle
import numpy as np
import pandas as pd
from collections import Counter

from Variables import w, a, s, d, wa, wd, sa, sd, nk
from Variables import FILE_I_END, path, log_path, bpath


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

    _file = open(log_path + "/Balance_log.txt", 'w')

    # lefts, rights, forwards, left-forwards, right-forwards,
    # backwards, right-backwards, left-backwards, no inputs
    l = []
    r = []
    f = []
    lf = []
    rf = []
    b = []
    rb = []
    lb = []
    ntg = []

    for index in range(1, FILE_I_END+1):
        temp_data = np.load(path + 'training_data-{}.npy'.format(index),
                            allow_pickle=True)
        if index == 1:
            train_data = temp_data
        else:
            train_data = np.concatenate((train_data, temp_data))

    shuffle(train_data)
    _df = pd.DataFrame(train_data)
    save(str(_df.head()))
    count_moves(_df)
    save("Total (train_data): " + str(len(train_data)))

    for data in train_data:
        img = data[0]
        choice = data[1]

        if choice == w:
            f.append([img, choice])
        elif choice == s:
            b.append([img, choice])
        elif choice == a:
            l.append([img, choice])
        elif choice == d:
            r.append([img, choice])
        elif choice == wa:
            lf.append([img, choice])
        elif choice == wd:
            rf.append([img, choice])
        elif choice == sa:
            lb.append([img, choice])
        elif choice == sd:
            rb.append([img, choice])
        elif choice == nk:
            ntg.append([img, choice])
        else:
            save("No matches!")

    # Balancing to be DONE !!!!
    f = f[:len(rf)]
    lf = lf[:len(rf)]
    ntg = ntg[:len(rf)]
    b = b[:len(lb)]
    rb = rb[:len(lb)]

    final_data = f + lf + b + ntg + rf + lf + rb + lb + l + r

    shuffle(final_data)
    np.save(bpath + 'training_data_v1.npy', final_data)

    try:
        _df = pd.DataFrame(final_data)
        save(str(_df.head()))
        count_moves(_df)
        save("Total (final_data): " + str(len(final_data)))
    except KeyError:
        print("Final data - Empty")

    _file.close()
