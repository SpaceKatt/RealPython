import argparse
import sys
import os
import csv

curr_dir = os.getcwd()
des = 'Split a CSV file...'
parser = argparse.ArgumentParser(description=des)

parser.add_argument('-i', nargs='?', #type=argparse.FileType('r'),
                    default=sys.stdin, required=True,
                    help='Input file.')
parser.add_argument('-o', nargs='?', #type=argparse.FileType('w'),
                    default=sys.stdout, required=True,
                    help='Output File.')
parser.add_argument('-r', nargs='?', type=int, required=True,
                    help='Split by -r rows.')

args = parser.parse_args()
#args = parser.parse_args(['-i', 'wonka.csv', '-o', 'wonkz',
#                          '-r', '2'])
arg_dict = vars(args)

input_file_path = os.path.join(curr_dir, args.i)
output_file_path = os.path.join(curr_dir, args.o)
row_limit  = args.r

def check_file(input):
    assert os.path.isfile(input)

def check_rows(input, rows):
    with open(input, 'r') as z:
        a = z.readlines()
        if len(a) - 1 < rows:
            raise ValueError('Not enough rows in file. (Excluding header)')
        else:
            pass

#print input_file_path, output_file_path, row_limit

check_file(input_file_path)
check_rows(input_file_path, row_limit)

def fetch_row_list(input):
    with open(input, 'rb') as file:
        file_reader = csv.reader(file)
        header = next(file_reader)
        row_list = []
        for row in file_reader:
            row_list.append(row)
        return header, row_list

header, row_list = fetch_row_list(input_file_path)

def split_files(row_list, row_limit):
    split_list = []
    row_num = 0
    while len(row_list) - row_num >= row_limit:
        chunk = row_list[row_num:row_num + row_limit]
#        print chunk, 'yup'
        split_list.append(chunk)
        row_num += row_limit
    if len(row_list) - row_num > 0:    
        last_chunk = row_list[row_num:]
        split_list.append(last_chunk)
    else:
        pass
#    print last_chunk
    return split_list

split_list = split_files(row_list, row_limit)

def write_split_csvfiles(split_list, output, header):
    chunk_num = 0
#    print split_list
    for list in split_list:
        chunk_name = '{}_{}.csv'.format(output, chunk_num)
        #print list, chunk_name, header
        to_write = [header]
        for item in list:
            to_write.append(item)
#        print to_write, chunk_name
        with open(chunk_name, 'wb') as chunk:
            file_writer = csv.writer(chunk)
            file_writer.writerows(to_write)
        chunk_num += 1
        
write_split_csvfiles(split_list, output_file_path, header)