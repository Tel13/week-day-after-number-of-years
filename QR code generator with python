#QR code generator
import pyqrcode
from pyqrcode import QRCode

def qr_generator(str, name_of_file):
    # generate the QR code
    try:
        file = pyqrcode.create(str)
        file.svg(name_of_file+".svg", scale = 10)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    string = input("Type the string that you want to transform in a QR code:")
    file_name = input("Type the name for save the QR code file:")
    qr_generator(string, file_name)




