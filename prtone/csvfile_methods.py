import csv
import os

my_path = '/home/spacekatt/realpython/prtone'

with open(os.path.join(my_path, 'wonka.csv'), 'rb') as wonk:
    read_wonk = csv.reader(wonk)
    next(read_wonk)
    for first, last, reward in read_wonk:
        print '{} {} got: {}.'.format(first, last, reward)
        
with open(os.path.join(my_path, "movies.csv"), "wb") as my_file:
    my_file_writer = csv.writer(my_file)
    my_file_writer.writerows(my_ratings)