import time
import sys
import random


def typing_effect(text, delay):
    for char in text:
        time.sleep(delay)
        sys.stdout.write(char)
        sys.stdout.flush()
    sys.stdout.write("\n")
    sys.stdout.flush()


def debug_print(text):
    print(f"[DEBUG] {text}")
