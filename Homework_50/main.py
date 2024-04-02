import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True) # Метод який буде скидувати кольорові налаштування.
print(Fore.GREEN + 'This text is green.') # Fore метод який використовується для фарбування тексту, GREEN - колір для тексту(атрибут).
print(Style.BRIGHT, Fore.YELLOW + "I am bright.") # Style метод який використовується для змінення стилю тексту, BRIGHT - стиль(атрибут).
print(Back.YELLOW, Fore.CYAN + 'Hello!') # Back метод який використовується для фарбування заднього фону, YELLOW - колір заднього фону(атрибут).
