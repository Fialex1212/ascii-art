import os
from PIL import Image

#Symbols for out conver
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]


def resize_image(image, new_width=200): # If new_width bigger than 160 it will look more better
    width, height = image.size
    ratio = height / width
    new_height = int(new_width*ratio*0.45) # Mul by 0.45 to better size
    resized_image = image.resize((new_width, new_height))
    return(resized_image)

def grayify(image):
    grayscale_image = image.convert("L")
    return grayscale_image

def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    return characters

def main(new_width=200):
    try:
        path = input("Enter a valid pathname to an image: ")
        image = Image.open(path)
    except Exception as e:
        print(f"Error: {e}")
        print("Please ensure the path is correct and points to a valid image file.")
        return

    new_image = pixels_to_ascii(grayify(resize_image(image)))
    pixel_count = len(new_image)
    ascii_image = "\n".join(new_image[i:(i+new_width)] for i in range(0, pixel_count, new_width))

    base_filename = os.path.splitext(os.path.basename(path))[0]
    output_filename = f"{base_filename}.txt"

    print(ascii_image)

    with open(output_filename, "w") as file:
        file.write(ascii_image)
    
    print(f"ASCII art saved to {output_filename}")

if __name__ == "__main__":
    main()