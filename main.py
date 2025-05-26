# Multithreading = run multiple threads (tasks) at the same time in a single process

import threading
import time


def walk_dog(dog_name):
    time.sleep(4)
    print(f"You walk {dog_name}")


def take_out_trash():
    time.sleep(2)
    print("You take out the trash")


def get_mail():
    time.sleep(3)
    print("You get the mail")


def main():
    # Single thread --> main thread: walk_dog > tak_out_trask > get_mail
    # Run all tasks one by one
    # walk_dog("Scooby")
    # take_out_trash()
    # get_mail()

    # Multithreading
    task_one = threading.Thread(target=walk_dog, args=("Scooby",))
    task_one.start()

    task_two = threading.Thread(target=take_out_trash)
    task_two.start()

    task_three = threading.Thread(target=get_mail)
    task_three.start()

    # Wait for all tasks to finish
    task_one.join()
    task_two.join()
    task_three.join()

    print("All tasks completed")


if __name__ == "__main__":
    main()
