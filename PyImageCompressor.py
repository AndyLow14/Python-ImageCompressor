import os 

from PIL import Image

TO_COMPRESS_PATH = os.getcwd() + "\ToCompress"
COMPRESSED_PATH = os.getcwd() + "\Compressed"

def compress(quality):
    
    print("")

    # Uncompressed Image Filename List
    img_lst = os.listdir(TO_COMPRESS_PATH)
    tot_size_before = 0
    tot_size_after = 0
    
    for image in img_lst:
        file_path = TO_COMPRESS_PATH + f"\{image}"
        before_size = os.path.getsize(file_path)
        tot_size_before += before_size
    
        picture = Image.open(file_path)
        compressed_filename = "Compressed" + f"\Qual{quality}_" + image
        picture.save(compressed_filename, "JPEG", optimize = True, quality = quality)
        after_size = os.path.getsize(os.getcwd() + f"\{compressed_filename}")
        tot_size_after += after_size
        
        print(f"{int(before_size/1024)}KB -> {int(after_size/1024)}KB  |  " + image)
    
    print("% of Original Size: " + f"{int((tot_size_after/tot_size_before)*100)}%\n")


qual = input("\nEnter Compression Quality [1-Worst | 60-Best]: ")

compress(int(qual))