

## 🍪labview smart lock:
 Проект с распознованием лиц использующий клиент написанный на labview и сервер Flask python


## 🍪зависимости: 
    Labview 2018
        - NI-IMAQ это камера 
        - base64_fast_encode.vi импортировать как функцию
        - httpClient
    python3.8
        - далее пропишите pin install -r requirements.txt чтобы импоротировать основые зависимости
            или установите список вручную 
                * Flask==2.1.1
                * Pillow==9.1.0
                * opencv-python==4.5.5.64
                * dlib
        - face_recognition


## 🍪работа:
<img src="server.PNG" alt="poc" style="max-width:300px" />
    Сервер - в дериктории с файлом server.py должна быть папка img 
    и файл img/1.jpg (фото лица с которым скрипт будет сравнивать)

    

    клиет - перед началом работы необходимо изменить ip и порт 
    к которому http.post будет обращаться


<img src="client1.jpg" alt="poc" style="max-width:300px" />
<img src="client2.jpg" alt="poc" style="max-width:300px" />



# ❗Примечание :
    -если лампока на экране labview загорелась зеленым , то лицо распозналось 
    -красный - человек не находится в базе


