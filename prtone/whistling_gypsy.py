'''
Opens 'The Whistling Gypsy.pdf'. Display title, author, number of pages.
Extract the full contents into a .txt file, encode to UTF-8.
Save a new pdf version, don't include cover page, into 'output'.
'''
import os
from pyPdf import PdfFileReader as pdr
from pyPdf import PdfFileWriter as pdw

def get_file_path():
    '''Returns the path of the file in question.'''
    filename = 'practice_files/The Whistling Gypsy.pdf'
    path = os.path.join(os.getcwd(), filename)
    return path

def display_single_page():
    '''Display a single page for planning purposes.'''
    path = get_file_path()
    input_file = pdr(file(path, 'rb'))
    print input_file.getPage(1).extractText().encode('utf-8')

def get_info(pdf_file):
    '''From file, return nessecary information.'''
    page_num = pdf_file.getNumPages()
    title = pdf_file.getDocumentInfo().title
    author = pdf_file.getDocumentInfo().author
    return title, author, page_num

def display_info(title, author, page_num):
    '''Displays relevant information.'''
    print 'Title:', title
    print 'Author:', author
    print 'Number of pages:', page_num

def get_out_paths():
    '''Returns paths for output to pdf and txt.'''
    filename = 'The_Whistling_Gypsy'
    path = os.path.join(os.getcwd(), 'output')
    pdf_path = os.path.join(path, filename + '.pdf')
    txt_path = os.path.join(path, filename + '.txt')
    return pdf_path, txt_path

def write_txt_file(in_pdf, out_path, page_num):
    '''Writes contents of a pdf file to a *.txt file.'''
    with open(out_path, 'w') as w_file:
        for page in range(page_num):
            text = in_pdf.getPage(page).extractText()
            text = text.encode('utf-8')
            w_file.write(text)
            w_file.write('\n\n')

def write_pdf_coverless(input_pdf, pdf_out, page_num):
    '''
    Writes contents of pdf file to a *.pdf file,
    without a cover page.
    '''
    pdfw = pdw()
    with open(pdf_out, 'wb') as w_file:
        for page in range(1, page_num):
            pdfw.addPage(input_pdf.getPage(page))
        pdfw.write(w_file)

def summary():
    '''Does all the things to do the stuff.'''
    path = get_file_path()
    input_pdf = pdr(file(path, 'rb'))
    title, author, page_num = get_info(input_pdf)
    display_info(title, author, page_num)
    pdf_out, txt_out = get_out_paths()
    write_txt_file(input_pdf, txt_out, page_num)
    write_pdf_coverless(input_pdf, pdf_out, page_num)
    print 'Done.'

#display_single_page()
summary()
