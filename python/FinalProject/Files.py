import os
import shutil
from Version import Version

def clean_add(path):
    for file1 in os.listdir(path):
        new_path = os.path.join(path, file1)
        if os.path.isfile(new_path):
            os.remove(new_path)


def create_wit(path):
    path = os.path.join(path, ".wit")
    if os.path.exists(path):
        raise Exception(".wit folder already exist")
    else:
        os.makedirs(path)
        ph = os.path.join(path, "allFiles")
        os.makedirs(ph)
        ph = os.path.join(path, "add")
        os.makedirs(ph)
        ph = os.path.join(path, "versions")
        os.makedirs(ph)


def add(path, f):
    ph = path + "\\add\\" + f
    if os.path.exists(ph):
        os.remove(ph)
    open(ph, 'w').close()
    shutil.copyfile(os.path.join(path, "allFiles", f), ph)

def create_commit(path, message):
    ph = path + "\\versions\\"
    ver = Version(message)
    ph = os.path.join(ph, str(ver.id))
    if not os.path.exists(ph):
        os.makedirs(ph)
        f = open(os.path.join(ph, "info.txt"), 'w')
        st = "id: %d \n date: %s/%s/%s \n message: %s" % (int(ver.id), ver.date.day, ver.date.month, ver.date.year, str(ver.message))
        f.write(st)
        f.close()
    return ph


def add_to_commit(path, path_commit):
    path_add = os.path.join(path, "add")
    for f in os.listdir(path_add):
        open(os.path.join(path_commit, f), 'w').close()
        shutil.copyfile(os.path.join(path_add, f), os.path.join(path_commit, f))


def commit(path, message):
    add_to_commit(path, create_commit(path, message))
    clean_add(os.path.join(path, "add"))


def return_to_commit(path, path_folder):
    path_add = os.path.join(path, "add")
    path_allfiles = os.path.join(path, "allFiles")
    for f in os.listdir(path_folder):
        ph1 = os.path.join(path_add, f)
        ph2 = os.path.join(path_allfiles, f)
        if os.path.exists(ph1):
            os.remove(ph1)
            if f != "info.txt":
                open(ph1, 'w').close()
                shutil.copyfile(os.path.join(path_folder, f), ph1)
        if os.path.exists(ph2):
            os.remove(ph2)
        if f != "info.txt":
            open(ph2, 'w').close()
            shutil.copyfile(os.path.join(path_folder, f), ph2)
