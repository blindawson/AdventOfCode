from support import support
import pandas as pd

# List of input commands
cm = support.read_input(r"year_2022/input/07_no_space_on_device.txt", flavor="split")

# Table of Directories
dt = pd.DataFrame(
    columns=["Dir Name", "Files in Dir", "Dirs in Dir", "Immediate Size"], dtype='O'
).set_index("Dir Name")

# Filesize dictionary
fd = {}

def up_dir(dir_name):
    d = dir_name.split('/')
    return "/".join(d[:-1])
    
def down_dir(dir_name, new_dir):
    return dir_name + "/" + new_dir

def find_file_size(dir_name):
    row = dt.loc[dir_name]
    file_size = dt.loc[dir_name, 'Immediate Size']
    for d in row['Dirs in Dir']:
        subdir = down_dir(dir_name, d)
        file_size += find_file_size(subdir)
    return file_size

# Boolean to track when we're reading ls output
listing_dirs = False
dir_name = '.'
# Loop through input commands
for c in cm:
    if listing_dirs:
        if c[0] == 'dir':
            dirs_in_dir.append(c[1])
        elif c[0].isnumeric():
            files_in_dir.append(c[1])
            fd[c[1]] = int(c[0])
            dt.at[dir_name, 'Immediate Size'] += int(c[0])
        else:
            listing_dirs = False
            dt.at[dir_name, 'Files in Dir'] = files_in_dir
            dt.at[dir_name, 'Dirs in Dir'] = dirs_in_dir
    if c[:2] == ['$', 'cd']:
        if c[2] == '..':
            dir_name = up_dir(dir_name)
        else:
            dir_name = down_dir(dir_name, c[2])
            if dir_name not in dt.index:
                dt.loc[dir_name] = ['', '', 0]
    elif c[:2] == ['$', 'ls']:
        listing_dirs = True
        dirs_in_dir = []
        files_in_dir = []

dt['File Size'] = 0
for index, row in dt.iterrows():
    dt.loc[index, 'File Size'] = find_file_size(index)
            
print(dt.loc[dt['File Size'] <= 100000, 'File Size'].sum())

total_disk_space = 70000000
needed_space = 30000000
used_space = dt.loc['./brlw', 'File Size']
perfect_file_size = needed_space - (total_disk_space - used_space)

print(dt.loc[dt['File Size'] > perfect_file_size, 'File Size'].min())