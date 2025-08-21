import serial
import pygame
import time

pygame.mixer.init()

pygame.mixer.music.load('src\SoundTrack\hello.mp3')

ser = serial.Serial('COM3', 115200, timeout=1)

is_playing = False

while True:
    try:
        if ser.in_waiting > 0:
            analog_value = ser.readline().decode('utf-8').strip()
            if analog_value.isdigit():
                analog_value = int(analog_value)

                print(f"Analog Value: {analog_value}")

                if analog_value < 1500 and not pygame.mixer.music.get_busy():
                    pygame.mixer.music.play()
                    is_playing = True

        if is_playing and not pygame.mixer.music.get_busy():
            is_playing = False
        
        time.sleep(0.1)
    except KeyboardInterrupt:
        break

pygame.mixer.music.stop()
ser.close()