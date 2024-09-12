import serial
import pygame
import time

# Initialize pygame mixer for MP3 playback
pygame.mixer.init()

# Load the MP3 file
pygame.mixer.music.load('src\SoundTrack\hello.mp3')

# Open serial connection with ESP32 (Adjust 'COM3' to your serial port)
ser = serial.Serial('COM3', 115200, timeout=1)

# Variable to track whether the sound is playing
is_playing = False

while True:
    try:
        # Read serial data from ESP32
        if ser.in_waiting > 0:
            analog_value = ser.readline().decode('utf-8').strip()
            if analog_value.isdigit():
                analog_value = int(analog_value)

                print(f"Analog Value: {analog_value}")

                # Check if the analog value is smaller than 1500 and the track is not already playing
                if analog_value < 1500 and not pygame.mixer.music.get_busy():
                    # Play the sound if it's not already playing
                    pygame.mixer.music.play()
                    is_playing = True  # Mark as playing

        # Check if the music finished playing
        if is_playing and not pygame.mixer.music.get_busy():
            # Sound finished, mark it as stopped
            is_playing = False

        time.sleep(0.1)  # Add a short delay for stability
    except KeyboardInterrupt:
        break

# Stop the music and close the serial connection
pygame.mixer.music.stop()
ser.close()
