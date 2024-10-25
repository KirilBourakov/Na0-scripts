 # This is a python 3 script used to get text from an image
# requires PIL and keras_ocr

def main():
    try:
        import sys
    except:
        print("ERROR, sys")
    import easyocr
    from PIL import Image


    if (len(sys.argv) != 2):
        print("ERROR, args")
        return
    
    reader = easyocr.Reader(['en'], gpu=False, verbose=False)
    # image = open_and_enhance_image(sys.argv[1])
    # image = Image.open])
    text = reader.readtext(sys.argv[1])
    words = ""

    for t in text:
        words += " " +t[-2]
    print(words)
    

# def open_and_enhance_image(path: str):
#     try:
#         from PIL import Image, ImageOps, ImageEnhance
#     except:
#         print("ERROR, PIL")

#     image = Image.open(path)

#     gray_image = ImageOps.grayscale(image)
#     threshold_image = ImageOps.autocontrast(gray_image, cutoff=0)
#     threshold_image = ImageOps.invert(threshold_image)

#     enhancer = ImageEnhance.Contrast(threshold_image)
#     enhanced_image = enhancer.enhance(1.5)

#     new_size = (enhanced_image.width * 4, enhanced_image.height * 4) 
#     resized_image = enhanced_image.resize(new_size, Image.Resampling.LANCZOS)

#     inverted_image = ImageOps.invert(resized_image)

#     return inverted_image



if __name__ == "__main__":
    main()