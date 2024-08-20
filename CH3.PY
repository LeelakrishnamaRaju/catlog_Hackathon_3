import qrcode
from PIL import Image
import hashlib

# Generate a unique hash for each drug batch
def generate_batch_hash(drug_name, batch_number):
    return hashlib.sha256(f'{drug_name}{batch_number}'.encode()).hexdigest()

# Generate a QR code for the batch and display it
def generate_qr_code(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Display the image
    img.show()

    # Optionally, save the image
    img.save(f"{data}.png")
    print(f"QR Code generated and saved as {data}.png")

# Get user input
drug_name = input("Enter the drug name: ")
batch_number = input("Enter the batch number: ")

# Generate the batch hash and QR code
batch_hash = generate_batch_hash(drug_name, batch_number)
generate_qr_code(batch_hash)
