import os 

from PIL import Image

TO_COMPRESS_PATH = os.getcwd() + "\ToCompress"
COMPRESSED_PATH = os.getcwd() + "\Compressed"

def compress(quality):

    # Uncompressed Image Filename List
    img_lst = os.listdir(TO_COMPRESS_PATH)
    
    for image in img_lst:
        file_path = TO_COMPRESS_PATH + f"\{image}"
        before_size = os.path.getsize(file_path)
    
        picture = Image.open(file_path)
        compressed_filename = "Compressed" + f"\Qual{quality}_" + image
        picture.save(compressed_filename, "JPEG", optimize = True, quality = quality)
        after_size = os.path.getsize(os.getcwd() + f"\{compressed_filename}")
        
        print(f" {int(before_size/1024)}KB -> {int(after_size/1024)}KB  |   " + image)

qual = input("Enter Compression Quality [1-Worst | 60-Best]: ")

compress(int(qual))