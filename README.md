UnitFlex: Python Package для конвертации единиц измерения (температура, расстояние, валюта)

1. Создайте виртуальное окружение:
   python -m venv .venv

2. Активируйте его:
.venv\Scripts\activate

3. pip install -e .

Гайд по использованию:
1) Через Python
python
from unitflexx.core import convert
print(convert("temperature", "celsius", "fahrenheit", 100))  #example

2) Через CLI 
unitflexx temperature celsius fahrenheit 100 


Поддерживаемые конвертации согласно условию задания
Температура	цельсий в фаренгейт и обратно
Расстояние	км в мили и обратно
Валюта	USD в EUR и обратно

Invalid domains or units raise a ValueError

Тестирование: pytest 

Docker-сборка
docker build -t unitflexx .
docker run --rm unitflexx temperature celsius fahrenheit 0
