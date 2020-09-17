import hashlib, os


def get_file_info(pathname):
    get_file_info = []
    get_file_info_data = []
    for dirpath, dirnames, filenames in os.walk(pathname):
        for filename in filenames:
            hash_object = hashlib.sha1(filename.encode()).hexdigest()
            dir_file_name = os.path.join(dirpath, filename)
            file_state = os.stat(dir_file_name).st_mtime
            get_file_info.append([{filename: dirpath}, {filename: hash_object}, {filename: file_state}])
            get_file_info_data.append([dirpath, filename, hash_object, file_state])
    return get_file_info_data


ROOT_DIR = os.path.dirname(os.path.abspath(path='.'))
data_dict = get_file_info(ROOT_DIR)
