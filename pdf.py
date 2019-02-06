import os  # os module imported here
import wand
from PyPDF2 import PdfFileWriter, PdfFileReader
from PIL import Image
from wand.image import Image


# FIND PDF FILE
def fileOpen():
    pdffiles = []

    for file in os.listdir('/home/nilufer/Downloads/problem2/pdf'):
        try:
            if file.endswith(".pdf"):
                print "pdf file found:\t", file
                pdffiles.append(str(file))

        except Exception as e:
            raise e
            print "No files found here!"
    return pdffiles


# SPLIT PDF PAGES
def PageOpen(pdffile):
    path = '/home/nilufer/Downloads/problem2/pdf'
    pdfPage = []
    for a in range(len(pdffile)):
        path2 = os.path.join(path, pdffile[a])
        fname = os.path.splitext(os.path.basename(path2))
        pdf = PdfFileReader(path2)
        for page in range(pdf.getNumPages()):
            pdf_writer = PdfFileWriter()
            pdf_writer.addPage(pdf.getPage(page))

            output_filename = '{}_page_{}.pdf'.format(
                fname, page + 1)

            with open('/home/nilufer/Desktop/pdfPages/%s' % output_filename, 'wb') as out:
                pdf_writer.write(out)

    return pdfPage


def run():
    pdffile = []
    pdfPage = []
    pdffile = fileOpen()

    pdfPage = PageOpen(pdffile)


run()

