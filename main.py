from barcode import EAN13 # EAN13 is one of python barcode standard. 

from barcode.writer import ImageWriter  # The ImageWriter is used to generate our barcode as .png format. 

num_of_barcodes = int(input("How many Barcodes you Need? "))

numbers = range(num_of_barcodes)

for i in numbers:
    id = input(" Give 12-Digit numbers for your barcode id: ")

    my_code = EAN13(id, writer=ImageWriter())   # Creating an instance of the barcode class

    name = input(" Give the name to save barcodes: ")

    my_code.save(name) # Saving  the barcode 




