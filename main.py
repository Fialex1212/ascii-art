import PIL.Image

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
    return(grayscale_image)

def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    return characters

def main(new_width=200): #if new_width bigger than 160 it will look more better
    path = input("Enter a valid pathname to an image: ")
    try:
        image = PIL.Image.open(path)
    except:
        print(path, "Is not valid pathname, try find out errro in your path")
    
    new_image = pixels_to_ascii(grayify(resize_image(image)))
    pixel_count = len(new_image)
    ascii_image = "\n".join(new_image[i:(i+new_width)] for i in range(0, pixel_count, new_width))
    
    print(ascii_image)

    with open("ascii_image.txt", "w") as file:
        file.write(ascii_image)

main()