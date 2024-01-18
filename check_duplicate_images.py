from PIL import Image

def images_are_same(img_path1, img_path2):
    """
    Compares two images and returns True if they are exactly the same, False otherwise.
    """
    try:
        with Image.open(img_path1) as img1, Image.open(img_path2) as img2:
            # Compare image sizes first
            if img1.size != img2.size:
                return False

            # Compare pixel data
            pixels1 = list(img1.getdata())
            pixels2 = list(img2.getdata())

            return pixels1 == pixels2

    except IOError as e:
        print(f"An error occurred: {e}")
        return False

# Example usage
image_path1 = 'path/to/your/first/image.jpg'
image_path2 = 'path/to/your/second/image.jpg'

if images_are_same(image_path1, image_path2):
    print("Images are the same.")
else:
    print("Images are different.")
