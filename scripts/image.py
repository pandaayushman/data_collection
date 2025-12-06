from PIL import Image

def load_image(path="data/images/sample.jpg"):
    img = Image.open(path)
    print("Image size:", img.size)
    return img

if __name__ == "__main__":
    load_image()
