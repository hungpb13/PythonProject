# Exercise: Alarm Clock
import time
import datetime

import pygame


def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    sound_file = "resources/my_music.mp3"
    is_running = True

    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)

        if current_time == alarm_time:
            print("WAKE UP! ⏰")

            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()
            is_busy = pygame.mixer.music.get_busy()

            while is_busy:
                time.sleep(1)
                stop = input("Press to stop")
                if stop is not None:
                    pygame.mixer.music.stop()
                    break

            is_running = False

        time.sleep(1)

    print("Have a nice day!")


def main():
    alarm_time = input("Enter alarm time (HH:MM:SS): ")
    set_alarm(alarm_time)


if __name__ == "__main__":
    main()
