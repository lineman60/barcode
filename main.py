# import EAN13 from barcode module
from barcode import Code39

# Make sure to pass the number as string
number = "#######"

# Now, let's create a barcode
# class and pass the number
my_code = Code39(number, add_checksum=False)

# Our barcode is ready. Let's save it.
my_code.save("new_code" + number)
