import os

def delete_dir(dir_a='save_dir'):
    if os.path.exists(dir_a):
        print("ディレクトリ '{}' が存在してます。".format(dir_a))
        os.rmdir(dir_a)
        print("ディレクトリ '{}' を消去しました。".format(dir_a))
    else:
        print("ディレクトリ '{}' 存在しないです。".format(dir_a))
delete_dir()
