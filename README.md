

## 🍪labview smart lock:
 Проект с распознованием лиц использующий клиент написанный на labview и сервер Flask python


## 🍪зависимости: 
    Labview 2018
        - NI-IMAQ это камера 
        - base64_fast_encode.vi импортировать как функцию
        - httpClient
    python3.8
        - далее пропишите pin install -r requirements.txt чтобы импортировать основые зависимости
            или установите список вручную 
                * Flask==2.1.1
                * click==7.1.2
                * dlib==19.22.99
                * face-recognition==1.3.0
                * face-recognition-models==0.3.0
                * imutils==0.5.4
                * numpy==1.20.2
                * opencv-python==4.5.1.48
                * Pillow==8.2.0




## 🍪работа:
<img src="server.PNG" alt="poc" style="max-width:300px" />
    Сервер - в дериктории с файлом server.py должна быть папка img 
    и файл img/1.jpg (фото лица с которым скрипт будет сравнивать)
<img src="client1.jpg" alt="poc" style="max-width:300px" />
<img src="client2.jpg" alt="poc" style="max-width:300px" />
    клиент - перед началом работы необходимо изменить ip и порт 
    к которому http.post будет обращаться



# ❗Примечание :
    -если лампока на экране labview загорелась зеленым , то лицо распозналось 
    -красный - человек не находится в базе


