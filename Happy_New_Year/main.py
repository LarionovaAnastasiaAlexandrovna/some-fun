import threading
import time
import random
import pygame

def draw_tree(height):
    spaces = " " * (height - 1)
    stars = "\033[31m*\033[0m"
    print(spaces + stars)

    for i in range(2, height + 1):
        spaces = " " * (height - i)
        colored_stars = generate_colored_stars(2 * i - 1)
        print(spaces + colored_stars)

    print(" " * (height - 1) + "\033[31m|\033[0m")  # Красный ствол

def generate_colored_stars(count):
    colors = ["\033[32m"] * 5 + ["\033[33m"] + ["\033[34m"] + ["\033[31m"]  # 4 зелёных, 1 жёлтый, 1 голубой, 1 красный
    stars = "".join(random.choice(colors) + "*" + "\033[0m" for _ in range(count))
    return stars

def countdown(seconds):
    while seconds > 0:
        print(f"Осталось {seconds} секунд до Нового года!")
        time.sleep(1)
        seconds -= 1
    print("\033[1;31mС Новым годом!\033[0m")  # Красный цвет

def play_new_year_melody():
    pygame.mixer.init()
    pygame.mixer.music.load("Jingle Bells.mp3")  # Путь к вашему аудиофайлу
    pygame.mixer.music.play()

if __name__ == "__main__":
    play_new_year_melody()
    time.sleep(0.5)
    tree_height = int(input("Введите высоту ёлки: "))
    time_wait = int(input("Введите сколько секунд осталось до нового года: "))

    countdown_thread = threading.Thread(target=countdown, args=(time_wait,))
    countdown_thread.start()
    countdown_thread.join()  # Дождаться завершения отсчета перед завершением программы

    draw_tree(tree_height)
    time.sleep(time_wait)  # Подождать еще 5 секунд после отрисовки ёлки
