from pdf2image import convert_from_bytes , convert_from_path 
import io
import os
from PIL import Image
import base64
from dotenv import load_dotenv

load_dotenv()

def convert_to_img(upload_pdf):
    try:
        if upload_pdf is None:
            raise ValueError("Uploaded file is not there...")
        img_list = convert_from_bytes(upload_pdf.read() , poppler_path=os.getenv("POPPER_DIRECTORY_PATH"))
        front_page =  img_list[0]
        # front_page.save("resume/page1.png")
        
        img_byte_arr = io.BytesIO()
        front_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode()  # encode to base64
            }
        ]
        return pdf_parts
        
        
        # return front_page
    
    except Exception as e:
        raise e
        
        