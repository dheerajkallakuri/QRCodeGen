import qrcode
import re
from random import randrange,choice 

def generate_qr_code(data):
    try:
        # Create a QR code instance
        qr = qrcode.QRCode(
            version=1,
            error_correction=choice([
                qrcode.constants.ERROR_CORRECT_L,
                qrcode.constants.ERROR_CORRECT_M,
                qrcode.constants.ERROR_CORRECT_Q,
                qrcode.constants.ERROR_CORRECT_H
            ]),
            box_size=10,
            border=choice([2, 4, 6]),  # Randomize border size
        )

        # Add data to the QR code
        qr.add_data(data)
        qr.make(fit=True)

        # Create an image from the QR code
        img = qr.make_image(fill_color=(randrange(1,255),randrange(1,255),randrange(1,255)), back_color="white")
        
        return img
    except Exception as e:
        print(f"Error generating QR code: {e}")
        return False

def validate_url(url):
    # Simple URL validation using regex
    pattern = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|'  # ...or ipv4
        r'\[?[A-F0-9]*:[A-F0-9:]+\]?)'  # ...or ipv6
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    return pattern.match(url) is not None
