'''
Cropping and copying PDF files.
'''
import os
import copy
from pyPdf import PdfFileReader as pdr
from pyPdf import PdfFileWriter as pdw

def get_paths():
    '''Locates files and creates PDF objects.'''
    path = os.getcwd()
    file_path = os.path.join(path, 'practice_files/half and half.pdf')
    pdf_in = pdr(file(file_path, 'rb'))
    pdf_out = pdw()
    return path, pdf_in, pdf_out

def copy_crop_add(pdf_in, pdf_out):
    '''
    Loads a page from the PDF, copies it.
    First, crops off the right side of the page, adds the
        left-hand side to the new pdf.
    Second, from the copy, crops off the left side,
        adds the right-hand side to the new pdf.
    Loop.
    '''
    for page_num in range(pdf_in.getNumPages()):
        page_left = pdf_in.getPage(page_num)
        page_right = copy.copy(page_left)
        upper_right = page_left.mediaBox.upperRight
        # crop and add left-hand side of page
        page_left.mediaBox.upperRight = (upper_right[0]/2,
            upper_right[1])
        pdf_out.addPage(page_left)
        # crop and add right-hand side of page
        page_right.mediaBox.upperLeft = (upper_right[0]/2,
            upper_right[1])
        pdf_out.addPage(page_right)

def write_pdf(pdf_out, path):
    '''From the PDF object, write to file.'''
    out_path = os.path.join(path, 'output/The_Little_Mermaid.pdf')
    with open(out_path, 'wb') as out_file:
        pdf_out.write(out_file)

def trio():
    '''Get relevant information, do task, write outcome.'''
    path, pdf_in, pdf_out = get_paths()
    copy_crop_add(pdf_in, pdf_out)
    write_pdf(pdf_out, path)

trio()
