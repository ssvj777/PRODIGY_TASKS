from PIL import Image

def encrypt_image(img):
    width, height = img.size
    for y in range(height):
        for x in range(width):
            pixel = img.getpixel((x, y))
            inverted_pixel = tuple(255 - value for value in pixel)
            img.putpixel((x, y), inverted_pixel)

input_image_path = input("Enter the path of the Image for Encryption: ")

try:
    img = Image.open(input_image_path)
except FileNotFoundError:
    print("File not found. Please provide a valid image file path.")
    exit()

encrypted_img = img.copy()
encrypt_image(encrypted_img)
encrypted_img.save("encrypted_image.jpg")
print("Image encrypted and saved as encrypted_image.jpg")

def decrypt_image(img):
    width, height = img.size
    for y in range(height):
        for x in range(width):
            pixel = img.getpixel((x, y))
            original_pixel = tuple(255 - value for value in pixel)
            img.putpixel((x, y), original_pixel)

input_image_path = input("Enter the path of the Image for Decryption: ")

try:
    img = Image.open(input_image_path)
except FileNotFoundError:
    print("File not found. Please provide a valid image file path.")
    exit()

decrypted_img = img.copy()
decrypt_image(decrypted_img)
decrypted_img.save("decrypted_image.png")
print("Image decrypted and saved as decrypted_image.jpg")
