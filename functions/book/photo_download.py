import urllib
from bs4 import BeautifulSoup
from PIL import Image, ImageDraw, ImageFont


from exceptions.PictureNotFoundError import PictureNotFoundError

def get_picture_source(soup, book_id):

    images = soup.select("img")

    if images:
        try:
            source = images[0]["src"]
        except TypeError:
            raise PictureNotFoundError()
        source_url = f"https://www.gutenberg.org/cache/epub/{book_id}/{source}"
    else:
        # Original picture not found, return None
        return None

    return source_url


def download_picture(url, image_path):
    if url is None:
        # Original picture not found, create a white image
        black_image = Image.new("RGB", (1000, 1000), color="white")
        black_image.save(image_path)
    else:
        urllib.request.urlretrieve(url, image_path)

def edit_image(input_filename, output_filename):
    # Open the image file
    img = Image.open(input_filename)

    # Define the area for cropping (left, upper, right, lower)
    crop_area = (50, 50, 300, 300)  # Replace these values as needed

    # Crop the image
    cropped_img = img.crop(crop_area)

    # Define the size for resizing
    resize_size = (500, 500)  # Replace these values as needed

    # Resize the image
    resized_img = cropped_img.resize(resize_size)

    # Load a font (provide the full path to the .ttf file)
    font = ImageFont.truetype('arial.ttf', 15)

    # Get an image drawing interface
    d = ImageDraw.Draw(resized_img)

    # Define the position for the watermark (x, y from the bottom left corner)
    watermark_position = (10, resized_img.height - 20)  # The second value might need adjustment based on the font size

    # Add the watermark
    d.text(watermark_position, "Downloaded from Project Gutenberg", fill=(0, 0, 0), font=font)

    # Save the image
    resized_img.save(output_filename)