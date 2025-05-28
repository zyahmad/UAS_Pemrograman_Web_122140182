import os
from uuid import uuid4

UPLOAD_DIR = os.path.join(os.path.dirname(__file__), '../../uploads')
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

def save_uploaded_file(file_field):
    filename = file_field.filename
    unique_filename = f"{uuid4().hex}_{filename}"
    destination = os.path.join(UPLOAD_DIR, unique_filename)
    with open(destination, 'wb') as output_file:
        output_file.write(file_field.file.read())
    return unique_filename
