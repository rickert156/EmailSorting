![Header](https://github.com/rickert156/rickert156/blob/main/assets/sortemail.png)
# Sort Email
## Скрипт для сортировки email и исключений из базы имейлов по полному совпадению и по целому домену 
Изначально нужно подготовить директорию для хранения списка исключений
```sh
#создать директорию для файлов с исключениями
mkdir Exception 

#создать файл для исключения по имейлу
touch Exception/email.txt 

#создать файл для исключения по домену
touch Exception/domain.txt 
```
Создать директорию с исходной базой
```sh
mkdir Base
```
Для обработки базы запускаем main.py
```sh
pyhon3 main.py
```
После этого нужно будет выбрать файл(ввести цифру в терминал). 
Результат будет в директории Result

### Заметка:
Предполагается, что в вашей таблицу есть колонки Name, Email, Company
