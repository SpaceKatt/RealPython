'''Add a watermark to a PDF.'''
import os
from pyPdf import PdfFileReader as pfr
from pyPdf import PdfFileWriter as pfw

def critical_info():
    '''Gathers and returns the nessecary information to start the task'''
    path = os.getcwd()
    input_path = os.path.join(path, 'practice_files/The Emperor.pdf')
    in_pdf = pfr(file(input_path, 'rb'))
    out_pdf = pfw()
    return path, in_pdf, out_pdf

def get_watermark(path):
    '''Fetches the watermark, as a PDF.'''
    watermark_path = os.path.join(path, 'practice_files/top secret.pdf')
    watermark = pfr(file(watermark_path, 'rb'))
    return watermark

def add_watermark(in_pdf, out_pdf, watermark):
    '''
    Takes existing PDF and merges it with the watermark,
    which is also a PDF, page by page.
    '''
    for page_num in range(in_pdf.getNumPages()):
        page = in_pdf.getPage(page_num)
        page.mergePage(watermark.getPage(0))
        out_pdf.addPage(page)

def write_new_pdf(out_pdf, path):
    '''Writes the PDF object to a file.'''
    out_path = os.path.join(path, 'output/new_suit.pdf')
    out_pdf.encrypt('good2Bking')
    with open(out_path, 'wb') as out_file:
        out_pdf.write(out_file)

def do_the_task():
    '''Does the things to do the task...'''
    path, in_pdf, out_pdf = critical_info()
    watermark = get_watermark(path)
    add_watermark(in_pdf, out_pdf, watermark)
    write_new_pdf(out_pdf, path)

do_the_task()
