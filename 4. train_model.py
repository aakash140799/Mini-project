
import numpy as np
from scripts.models import inception_v3 as googlenet
from random import shuffle
from Variables import bpath, log_path, MODEL_NAME, LR, EPOCHS, WIDTH, HEIGHT


def save(x):
    _file.write(x+'\n')
    print(x)


if __name__ == '__main__':

    _file = open(log_path + "Train_log.txt", 'w')

    model = googlenet(WIDTH, HEIGHT, 3, LR, output=9, model_name=MODEL_NAME)

    count = 0
    file_name = bpath + 'training_data_v1.npy'

    train_data = np.load(file_name, allow_pickle=True)
    save(file_name + " " + str(len(train_data)))

    train = train_data[:-50]
    test = train_data[-50:]

    X = np.array([i[0] for i in train]).reshape([-1, WIDTH, HEIGHT, 3])
    Y = [i[1] for i in train]

    test_x = np.array([i[0] for i in test]).reshape([-1, WIDTH, HEIGHT, 3])
    test_y = [i[1] for i in test]

    for _ in range(EPOCHS):
        count += 1
        try:
            model.fit({'input': X}, {'targets': Y}, n_epoch=1,
                      validation_set=({'input': test_x}, {'targets': test_y}),
                      snapshot_step=2500, show_metric=True, run_id=MODEL_NAME)

            if count % 10 == 0:
                save('SAVING MODEL!')
                model.save(MODEL_NAME)

        except Exception as e:
            save(str(e))

    _file.close()

