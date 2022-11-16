import os

from PIL import Image

TO_COMPRESS_PATH = os.getcwd() + "\ToCompress"
COMPRESSED_PATH = os.getcwd() + "\Compressed"

def compress(quality):

    # Uncompressed Image Filename List
    img_lst = os.listdir(TO_COMPRESS_PATH)
    
    for image in img_lst:
        file_path = TO_COMPRESS_PATH + f"\{image}"
    
        picture = Image.open(file_path)
        picture.save("Compressed" + f"\Qual{quality}_" + image, "JPEG", optimize = True, quality = quality)

qual = input("Enter Compression Quality [1-Worst | 60-Best]: ")

compress(int(qual))