#НЕ справился сам, нашел решение в интернете!!! Нужен разбор дз
import re

def remove_html_tags(text):
    # Удаление парных HTML-тегов
    text = re.sub(r'<.*?>', '', text)
    # Удаление одиночных HTML-тегов
    text = re.sub(r'<.*?/>', '', text)
    return text

# Пример использования
html_text = '<div id="rcnt" style="clear:both;position:relative;zoom:1"><p>Hello, world!</p></div>'
clean_text = remove_html_tags(html_text)
print(clean_text)  # Выведет: Hello, world!