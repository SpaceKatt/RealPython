import os
import glob

my_path = '/home/spacekatt/realpython/prtone'

input_file_form = os.path.join(my_path, '*.py')

print 'Printing all python files:'
for file in sorted(glob.glob(input_file_form)):
    if os.path.isfile(file) == True:
        print file.replace('%s/' % my_path, '')[:-3]