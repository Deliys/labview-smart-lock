# 🍪labview smart lock:
 Проект с распознованием лиц использующий клиент написанный на labview и сервер Flask python


# 🍪зависимости: 
    Labview 2018
        - модуль 
        - модуль
    python3.8
        - далее пропишите pin install -r requirements.txt чтобы импоротировать основые зависимости
        - face_recognition


# 🍪работа:
    Сервер - в дериктори с файлом server.py должна быть папка img 
    и файл img/1.jpg (фото лица с которым скрипт будет сравнивать)

    клиет - перед началом работы необходимо изменить ip и порт 
    к которому http.post будет обращаться




# ❗Примечание :
    -если лампока на экране labview загорелась зеленым , то лицо распозналось 
    -красный - человек не находится в базе


