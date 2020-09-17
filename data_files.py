import pandas as pd
from main import get_file_info, ROOT_DIR
my_data = get_file_info(ROOT_DIR)


df = pd.DataFrame(data = my_data)
df.to_csv('data.csv', header = ['dirpath','filename','sha1', 'st_mtime'])