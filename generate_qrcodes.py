import qrcode
import os

# Base domain
base_url = "https://sample-domain.com"

# Output directory for QR code images
output_dir = "qrcodes"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Number of QR codes to generate (test with 10, full range is 500)
num_codes = 10  # Change to 500 for full generation

# Generate QR codes
for i in range(1, num_codes + 1):
    # Format UID as three digits (e.g., 001, 002, ..., 500)
    uid = f"{i:03d}"
    # Construct URL
    url = f"{base_url}?uid={uid}"
    
    # Create QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    
    # Create image and save
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(f"{output_dir}/qrcode_{uid}.png")
    print(f"Generated QR code for {url}")

print(f"QR codes saved in '{output_dir}' directory")