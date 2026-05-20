from PIL import Image

image = Image.open("input.png")
pixels = image.load()

# IMAGE SIZE
width, height = image.size

# SECRET KEY
key = 50


#  ENCRYPTION 

for i in range(width):
    for j in range(height):

        # GET RGB VALUES
        r, g, b = pixels[i, j]

        # ENCRYPT PIXELS
        r = (r + key) % 256
        g = (g + key) % 256
        b = (b + key) % 256

        # STORE NEW PIXELS
        pixels[i, j] = (r, g, b)

# SAVE ENCRYPTED IMAGE
image.save("encrypted.png")

print("Image Encrypted Successfully!")


#  DECRYPTION 

# OPEN ENCRYPTED IMAGE
image2 = Image.open("encrypted.png")
pixels2 = image2.load()

# IMAGE SIZE
width, height = image2.size

for i in range(width):
    for j in range(height):

        # GET RGB VALUES
        r, g, b = pixels2[i, j]

        # DECRYPT PIXELS
        r = (r - key) % 256
        g = (g - key) % 256
        b = (b - key) % 256

        # STORE ORIGINAL PIXELS
        pixels2[i, j] = (r, g, b)

# SAVE DECRYPTED IMAGE
image2.save("decrypted.png")

print("Image Decrypted Successfully!")