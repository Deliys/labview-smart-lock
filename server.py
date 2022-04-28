import face_recognition as fr
from PIL import Image, ImageDraw
import pickle
from cv2 import cv2


import json
import base64
from flask import Flask, request, jsonify
import os



def compare_face(img1 , img2):
    img1 = fr.load_image_file(img1)
    img1_encodings = fr.face_encodings(img1)[0]
    # print(img1_encodings)

    img2 = fr.load_image_file(img2)
    img2_encodings = fr.face_encodings(img2)[0]

    result = fr.compare_faces([img1_encodings], img2_encodings)

    return result

app = Flask(__name__)

@app.route('/', methods=['POST'])
def update_record():
    record = json.loads(request.data)
    
    decodeit = open('img/2.jpg', 'wb')
    decodeit.write(base64.b64decode((record["photo"])))
    decodeit.close()


    if compare_face("img/1.jpg","img/2.jpg")[0] == True:       
        return "1"
    else:
        return "0"
app.run(debug=True,host="0.0.0.0")
