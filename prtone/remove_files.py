import os
import glob

my_path = '/home/spacekatt/realpython/prtone/subfolder'
empty_file_names = 'fileone.txt', 'filetwo.txt', 'filethree.txt'
copy = 'yup.'

if os.path.exists(my_path) == True:
    pass
else:
    os.makedirs(my_path)
    
for file in empty_file_names:
    path = os.path.join(my_path, file)
    with open(path, 'w') as foo:
        foo.write(copy)
        
extention = '.txt'
input_file_form = os.path.join(my_path, '*{}'.format(extention))

def print_files():
    print 'Printing all "{}" files:'.format(extention)
    for file in sorted(glob.glob(input_file_form)):
        if os.path.isfile(file) == True:
            print file.replace('%s/' % my_path, '')[:-len(extention)]

print_files()
for current_folder, subfolders, file_names in os.walk(my_path):
#    print current_folder, subfolders, file_names
    for file in file_names:
        file_path = os.path.join(my_path, file)
        if os.path.getsize(file_path) <= 4:
            print 'Deleting empty file... {}'.format(file)
            os.remove(file_path)
            print_files()