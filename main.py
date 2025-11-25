# Импорт load_dotenv.
from dotenv import load_dotenv 

# Импорт библиотеки для работы с окружением.
import os  

def print_author():
    load_dotenv() # Загрузка переменных из .env
    author = os.getenv('AUTHOR')   # Теперь переменные доступны через os.environ
    print(f"Автор проекта: {author}") 

print_author()

