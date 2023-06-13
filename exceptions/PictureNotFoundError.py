class PictureNotFoundError(Exception):

    def __init__(self):
        super().__init__("\nPicture was not found in the book. Program will exit.")
