import os
import argparse
import cv2
import sys
import shutil
from PIL import Image, ExifTags


abs_dir_path = os.path.dirname(os.path.abspath(__file__))

parser = argparse.ArgumentParser()
parser.add_argument("input_dir", help="input images folder", type=str)
parser.add_argument("gallery_dir", help="output images folder", type=str)
parser.add_argument("output_file", help="output file with list of seelcted images", type=str)
args = parser.parse_args()



output_file = os.path.join(abs_dir_path, args.output_file)
os.makedirs(args.gallery_dir, exist_ok=True)
if os.path.isfile(output_file):
    os.remove(output_file)

def log_output(lines):
    with open(output_file, "a") as out_f:
        for line in lines:
            out_f.write(line + os.linesep)


def image_resize(image, width = None, height = None, inter = cv2.INTER_CUBIC):
    # initialize the dimensions of the image to be resized and
    # grab the image size
    dim = None
    (h, w) = image.shape[:2]

    # if both the width and height are None, then return the
    # original image
    if width is None and height is None:
        return image

    # check to see if the width is None
    if width is None:
        # calculate the ratio of the height and construct the
        # dimensions
        r = height / float(h)
        dim = (int(w * r), height)

    # otherwise, the height is None
    else:
        # calculate the ratio of the width and construct the
        # dimensions
        r = width / float(w)
        dim = (width, int(h * r))

    # resize the image
    resized = cv2.resize(image, dim, interpolation = inter)

    # return the resized image
    return resized

def save_image(img, image_filename_jpg):
    resized_image = image_resize(img, width=1800)
    cv2.imwrite(os.path.join(args.gallery_dir, image_filename_jpg), resized_image)

def print_exif(img_exif):
    print("### EXIF ###")
    if img_exif:
        print(f"{get_exif_field(img_exif,'Model')}")
        print(f"Datetime {get_exif_field(img_exif,'DateTime')}")
    

    print("############")

   
def get_exif_field (exif,field) :
  for (k,v) in exif.items():
     if ExifTags.TAGS.get(k) == field:
        return v
     
if __name__ == "__main__":

    for image_filename in sorted(os.listdir(args.input_dir)):


        print(f"Loading {image_filename}...")

        if image_filename.lower().endswith(".jpg"):

            img = cv2.imread(os.path.join(args.input_dir, image_filename), cv2.IMREAD_COLOR)

            if img is None:
                print(f"ERROR {image_filename}")
                continue

            img_pil = Image.open(os.path.join(args.input_dir, image_filename))
            img_exif = img_pil.getexif()
            print_exif(img_exif)


            if img_exif is None:
                continue

            if get_exif_field(img_exif,'Model') != "Canon EOS 200D II":
                continue

            
            cv2.imshow("image", image_resize(img, width=700))
            cv2.moveWindow("image", 5, 5) 

            available_keys = [ 27, ord('k'), ord('n') ]
            k = 0
            while k not in available_keys:
                k = cv2.waitKey(0)
                print(f"Pressed {chr(k)}")

            if k == 27:    # Esc key to stop
                break
            elif k == ord('k'):  # Save image
                caption = input("IMAGE CAPTION: ")
                image_filename_jpg = ".".join([os.path.splitext(image_filename)[0], "jpg"])

                save_image(img, image_filename_jpg)
                image_name_line = f"- image-name: {image_filename_jpg}"
                image_caption_line = f"  caption: {caption}"
                copyright_line = "  copyright: © Luca Antognetti"
                lines = [image_name_line, image_caption_line, copyright_line]
                log_output(lines)
                os.remove(os.path.join(args.input_dir, image_filename))
            elif k == ord('n'):  # Next image
                os.remove(os.path.join(args.input_dir, image_filename))
                continue

    cv2.destroyAllWindows()
