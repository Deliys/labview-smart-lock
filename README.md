# 🍪labview smart lock:
 Проект с распознованием лиц использующий клиент написанный на labview и сервер Flask python


# 🍪зависимости: 
    Labview 2018
        - модуль 
        - модуль
    python3.8
        - далее пропишите pin install -r requirements.txt чтобы импоротировать основые зависимости
            или установите список вручную 
                * Flask==2.1.1
                * Pillow==9.1.0
                * opencv-python==4.5.5.64
                * dlib
        - face_recognition


# 🍪работа:
    Сервер - в дериктори с файлом server.py должна быть папка img 
    и файл img/1.jpg (фото лица с которым скрипт будет сравнивать)

    ![фото сервера](server.PNG)


    клиет - перед началом работы необходимо изменить ip и порт 
    к которому http.post будет обращаться

    ![фото сервера](https://github.com/Deliys/labview-smart-lock/blob/main/server.PNG?raw=true)

    ![alt text](example.com/logo.png)


# ❗Примечание :
    -если лампока на экране labview загорелась зеленым , то лицо распозналось 
    -красный - человек не находится в базе


