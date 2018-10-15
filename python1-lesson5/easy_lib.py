import os


def make_dir(path):
    try:
        os.mkdir(path)
    except FileExistsError:
        print('Папка уже существует.')
    except Exception:
        print('Непредвиденная ошибка.')
    else:
        print('Папка успешно создана.')


def delete_dir(path):
    try:
        os.rmdir(path)
    except FileNotFoundError:
        print('Папка не существует.')
    except Exception:
        print('Непредвиденная ошибка.')
    else:
        print('Папка успешно удалена.')
