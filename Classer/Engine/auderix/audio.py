import os

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

import pygame
from ..VGUI import Lang
from ..VGUI import TextWindow

# Ініціалізація мікшера pygame з оптимальними налаштуваннями буфера
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()

# Глобальний словник для збереження активних аудіоканалів за їхніми назвами
_active_layers = {}


def play_audio(file_path: str, volume: float, loop: bool, layer_name: str):
    """
    Програє аудіофайл на заданому шарі з налаштуванням гучності та зациклення.

    :param file_path: Шлях до файлу (mp3, wav тощо)
    :param volume: Гучність від 0 до 100
    :param loop: True для зациклення, False для одноразового відтворення
    :param layer_name: Унікальне ім'я шару для керування звуком
    """
    if not os.path.exists(file_path):
        TextWindow.cr_window("ЗАГЛУШКА", "ЗАГЛУШКА", 0)
        return

    try:
        sound = pygame.mixer.Sound(file_path)

        # Переводимо гучність з діапазону 0-100 у 0.0-1.0
        normalized_volume = max(0.0, min(1.0, volume / 100.0))
        sound.set_volume(normalized_volume)

        # Знаходимо вільний канал для відтворення
        channel = pygame.mixer.find_channel()
        if channel is None:
            TextWindow.cr_window("ЗАГЛУШКА", "ЗАГЛУШКА", 0)
            return

        loops_count = -1 if loop else 0
        channel.play(sound, loops=loops_count)

        # Зберігаємо канал у реєстр активних шарів
        _active_layers[layer_name] = channel

    except Exception as e:
        TextWindow.cr_window("ЗАГЛУШКА", "ЗАГЛУШКА", 0)


def stop_audio(layer_name: str = "", all_sounds: bool = False):
    """
    Зупиняє аудіо на конкретному шарі або вимикає всі звуки одночасно.

    :param layer_name: Назва аудіошару, який потрібно зупинити (ігнорується, якщо all_sounds=True)
    :param all_sounds: Якщо True — зупиняє взагалі всі звуки та музику, що зараз грають
    """
    global _active_layers

    if all_sounds:
        # Варіант 1: Зупиняємо абсолютно все через глобальний мікшер
        pygame.mixer.stop()
        _active_layers.clear()
    else:
        # Варіант 2: Зупиняємо лише один конкретний шар
        if layer_name in _active_layers:
            channel = _active_layers[layer_name]
            if channel.get_busy():
                channel.stop()
            del _active_layers[layer_name]
        else:
            TextWindow.cr_window("ЗАГЛУШКА", "ЗАГЛУШКА", 0)
