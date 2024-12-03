![Header](https://github.com/rickert156/rickert156/blob/main/assets/sortemail.png)
# Sort Email
## Скрипт для сортировки email и исключений из базы имейлов по полному совпадению и по целому домену 
Изначально нужно подготовить директорию для хранения списка исключений, директорию для баз
```sh
mkdir Exception && mkdir Base && touch Exception/email.txt && touch Exception/domain.txt 
```
Для обработки базы запускаем main.py
```sh
pyhon3 main.py
```
После этого нужно будет выбрать файл(ввести цифру в терминал). 
Результат будет в директории Result

### Заметка:
Предполагается, что в вашей таблицу есть колонки Name, Email, Company
