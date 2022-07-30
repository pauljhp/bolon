import PIL
import matplotlib.pyplot as plt
from pathlib import Path
import qrcode
from typing import Optional, Dict, List

def make_qrcode(data: str, save_path: Optional[str]=None):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    if save_path:
        img.save(save_path)
    return str(save_path)