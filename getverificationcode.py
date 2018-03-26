import pytesseract

number_1_site = (5, 1, 16, 15)
number_2_site = (29, 1, 40, 15)
operator_site = (17, 1, 25, 13)


def get_verification_code(image):
    image = image.convert('L')
    threshold = 144
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    image = image.point(table, '1')
    number_1_image = image.crop(number_1_site).resize((44, 56))
    number_2_image = image.crop(number_2_site).resize((44, 56))
    operator_image = image.crop(operator_site).resize((32, 48))
    number_1 = pytesseract.image_to_string(number_1_image, config="-psm 10 -c tessedit_char_whitelist=1234567890")
    number_2 = pytesseract.image_to_string(number_2_image, config="-psm 10 -c tessedit_char_whitelist=1234567890")
    operator = pytesseract.image_to_string(operator_image, config="-psm 10 -c tessedit_char_whitelist=*+")
    return number_1+operator+number_2

