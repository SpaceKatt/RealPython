"""
Basic PDF manipulation operations.
"""
import os
from pyPdf import PdfFileReader as pdr
from pyPdf import PdfFileWriter as pdw

def get_path():
    '''Returns the file path and some pdf objects.'''
    path = os.getcwd()
    file_path = os.path.join(path, 'practice_files/ugly.pdf')
    input_file = pdr(file(file_path, 'rb'))
    output_pdf = pdw()
    return path, input_file, output_pdf

def rotate_pages(input_file, output_pdf):
    '''Rotates pages if needed and updates output_pdf object.'''
    for page_num in range(input_file.getNumPages()):
        page = input_file.getPage(page_num)
        if page_num % 2 == 0:
            page.rotateClockwise(90)
        output_pdf.addPage(page)

def write_output_pdf(output_pdf, path):
    '''Writes from the output_pdf object to the file path.'''
    out_path = os.path.join(path, 'output/conforming_duck.pdf')
    with open(out_path, 'wb') as out_file:
        output_pdf.write(out_file)

def do_stuff():
    '''All the stuff at once!'''
    path, input_file, output_pdf = get_path()
    rotate_pages(input_file, output_pdf)
    write_output_pdf(output_pdf, path)

do_stuff()
