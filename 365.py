import os
def prepare_dir(dir_a='seve_dir'):
    if os.path.exists(dir_a):
        print("ディレクトリ '{}' があります。".format(dir_a))
    else:
        os.mkdir(dir_a)
        print("ディレクトリ '{}' が作成されました。".format(dir_a))

prepare_dir()
