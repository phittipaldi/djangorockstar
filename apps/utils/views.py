import barcode
import random
from io import BytesIO as StringIO


class BarcodeGuest:

    def __init__(self):
        self.EAN = barcode.get_barcode_class('code39')

    def generar_barcode_svg(self, guest_token, guest_id):
        ean = self.EAN(guest_token)
        ean.save('image/barcode/barcode_' + guest_id)

    def generar_barcode_buffer(self, guest):
        ean = self.EAN(guest.barcode_value, add_checksum=False)
        fp = StringIO()
        ean.write(fp)
        return fp
