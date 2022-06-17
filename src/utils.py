import time
import sys
import random

DEBUG = True


def typing_effect(text, delay):
    for char in text:
        time.sleep(0)
        sys.stdout.write(char)
        sys.stdout.flush()
    sys.stdout.write("\n")
    sys.stdout.flush()


def debug_print(text):
    if DEBUG:
        print(f"[DEBUG] {text}")
