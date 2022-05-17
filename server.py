#импорт библиотек
import face_recognition as fr
from PIL import Image, ImageDraw
import pickle
from cv2 import cv2
import json
import base64
from flask import Flask, request, jsonify
import os

def compare_face(img1 , img2):
    #преброзование фотографии в объект класса face_recognition
    img1 = fr.load_image_file(img1)
    #поиск лица на фотографии
    img1_encodings = fr.face_encodings(img1)[0]
    

    #преброзование фотографии в объект класса face_recognition
    img2 = fr.load_image_file(img2)
    #поиск лица на фотографии
    img2_encodings = fr.face_encodings(img2)[0]

    #сравнение лица с первого фото и лица со втрого
    result = fr.compare_faces([img1_encodings], img2_encodings)

    return result


app = Flask(__name__)

@app.route('/', methods=['POST'])
def update_record():
    #получение файла в кодировке base64
    #из атрибутов переданных в запросе от клиента
    record = json.loads(request.data)
    
    #преобразование base64 в фото и сохронение его в файл img/2.jpg
    decodeit = open('img/2.jpg', 'wb')
    decodeit.write(base64.b64decode((record["photo"])))
    decodeit.close()

    #вызов функции compare_face для сранения лиц на фотографиях
    #из базы данных (img/1.jpg) и лица из фото полученного с сервера("img/2.jpg")
    if compare_face("img/1.jpg","img/2.jpg")[0] == True:       
        return "1"
    else:
        return "0"
if __name__ == '__main__':
    #запуск web сервера
    app.run(host='0.0.0.0', port=5000, debug=False)
