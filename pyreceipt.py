from pyreceipts.receipt import Receipt
import sys

def read_recepipt(file_name):
    receipt = Receipt(file_name)
    text = receipt.read()
    receipt.delete_tmp_file()
    return text

if __name__ == '__main__':
    if not len(sys.argv) > 1:
        print(ValueError('No filename provided'))
    else:
        print(read_recepipt(sys.argv[1]))
