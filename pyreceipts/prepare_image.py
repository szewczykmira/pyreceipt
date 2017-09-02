from PIL import ImageEnhance


def greyscale(img):
    img = img.convert('L')
    return img

def contrast(img):
    contrast = ImageEnhance.Contrast(img)
    img = contrast.enhance(3)
    return img

def remove_noise_by_pixel(img, column, line, pass_factor):
    if img.getpixel((column, line)) < pass_factor:
        return (0)
    return 255

def remove_noise(img, pass_factor=100):
    for column in range(img.size[0]):
        for line in range(img.size[1]):
            value = remove_noise_by_pixel(img, column, line, pass_factor)
            img.putpixel((column, line), value)
    return img


def enlarge_image(img, min_width):
    # File should have at least 900px width to be read properly
    if img.size[0] < min_width:
        width_percent = (min_width/float(img.size[0]))
        height = int(float(img.size[1])*float(width_percent))
        img = img.resize((min_width, height), Image.ANTIALIAS)
    return img
