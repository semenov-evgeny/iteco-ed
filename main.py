import hashlib, os


def get_file_info(pathname):
    get_file_info = []
    get_file_info_data = []
    for dirpath, dirnames, filenames in os.walk(pathname):
        for filename in filenames:
            hash_object = hashlib.sha1(filename.encode())
            hex_dig = hash_object.hexdigest()
            #file_state = os.stat(filename)
            #print(file_state)
            #print(file_state.st_atime)
            #print(os.stat(filename).st_mtime)
            get_file_info.append([{filename: dirpath}, {filename: hex_dig}, {filename}])
            get_file_info_data.append([dirpath, filename, hex_dig])
    print(get_file_info)


    return get_file_info_data


ROOT_DIR = os.path.dirname(os.path.abspath(path='.'))
data_dict = get_file_info(ROOT_DIR)
