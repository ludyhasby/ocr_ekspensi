import numpy as np
from paddleocr import PaddleOCR, draw_ocr # main OCR dependencies
from matplotlib import pyplot as plt # plot images
import cv2 #opencv
import os # folder directory navigation
os.environ['KMP_DUPLICATE_LIB_OK']='True'
import re
from PIL import Image


## list to string
def listToString(list):
  str = ""
  for i in list:
    str += i
    str += " "
  return str
def tidak_ada_angka_titik_koma(s):
    return not re.search(r'[\d.,]', s)
def AdaHuruf(s):
   return re.match(r'[a-zA-Z]', s) is not None

## fungsi ekstraksi teks 
def summary(list):
  print("Process Generate Kirim dimulai.....")
  store_summary = listToString(result_text[:3])
  indeks_total = [index for index, word in enumerate(result_text) if re.search(r'tota\w*', word)][-1]
  # digit_list = re.findall(r"\d+", result_text[indeks_total+1])
  digit_list = result_text[indeks_total+1]
  digit_list = re.findall(r"[\d]+", digit_list)
  if digit_list[-1] == '00' :
     digit_list = digit_list[:-1]

  # total_value= int(''.join(digit_list))
  total_value= int(''.join(digit_list))
  detail_transaksi = listToString(asli)
  print("---- Summary Transaksi ---- ")
  print(f"Headline   : {store_summary}")
  print(f"Total      : {total_value}")
  print(f"Detail     : {detail_transaksi}")
  print("Sukses !")
  
  kirim = [word for word in result_text[:indeks_total] if (tidak_ada_angka_titik_koma(word) or AdaHuruf(word))]
  kirim = kirim[:8]
  kirim.append(f"Dengan Total {total_value}")
  kirim = listToString(kirim)
  print("Teks yang dikirim ke NLP...")
  print("Berupa Teks selain angka + digit total")
  print(kirim)

  return kirim 

## Streamlit Packing ##

file = 'geprek.jpeg'

if file:
    img = Image.open(file)
    ocr = PaddleOCR(lang='en')
    img_path = "temp_image.png"
    img.save(img_path)
    result = ocr.ocr(img_path)

    result_text = []
    asli = []
    for res in result[0]:
        asli.append(res[1][0])
        result_text.append(res[1][0].lower())
        # print(res[1][0])

    ### [o1] ini untuk menampilkan gambar dalam visualisasi ekstraksi (box coordinates, text, score)
    ## hapus teks code dibawah jika tidak diperlukan
    # extract
    boxes = [res[0] for res in result[0]]
    text = [res[1][0] for res in result[0]]
    scores = [res[1][1] for res in result[0]]

    # spesfikasi font path for draw_ocr method
    font_path = os.path.join('PaddleOCR', 'doc', 'fonts', 'latin.ttf')
    # import our image
    img = cv2.imread(img_path) # import image
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # reorders the color channels
    # visualize our image and detection
    plt.figure(figsize=(15, 15)) # resizing display area
    annotated = draw_ocr(img, boxes, text, scores, font_path=font_path) # draw annotation
    plt.imshow(annotated)# show image using matplotlib
    plt.show() ## HAPUS atau COMMENT ini agar proses bisa ke selanjutnya

    ### [o1] visulasasi berakhir

    # Next Processing (NLP)
    kirim = summary(result_text)


    # Tempatkan pemodelan NLP anda disini 
    ### START CODE ###
    # model_nlp = .....
    # label_predict = model_nlp.predict(kirim)

    ### END CODE ###

    # append to cloud -> Matching Keywords
    ### START CODE ###

    ### END CODE ###

    os.remove("temp_image.png")