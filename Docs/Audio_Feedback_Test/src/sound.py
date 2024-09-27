import serial
import pygame
import time

# Initialize the Pygame mixer
pygame.mixer.init()

# Load audio tracks
audio1 = 'src\SoundTrack\One_Sound.mp3'
audio2 = 'src\SoundTrack\Two_Sound.mp3'
audio3 = 'src\SoundTrack\Three_Sound.mp3'

# Open the serial port
ser = serial.Serial('COM3', 115200, timeout=1)

is_playing = False

def play_audio(file):
    """Play the specified audio file."""
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()

while True:
    try:
        if ser.in_waiting > 0:
            # Read and decode sensor inputs
            sensor_data = ser.readline().decode('utf-8').strip()
            sensor_values = sensor_data.split(",")  # Expecting data in 'sensor1,sensor2' format

            if len(sensor_values) == 2 and all(val.isdigit() for val in sensor_values):
                sensor1_value = int(sensor_values[0])
                sensor2_value = int(sensor_values[1])

                print(f"Sensor1: {sensor1_value}, Sensor2: {sensor2_value}")

                # Determine which audio to play based on the sensor values
                if sensor1_value < 1000 and sensor2_value > 1000 and not pygame.mixer.music.get_busy():
                    play_audio(audio1)
                    is_playing = True
                    print(1);
                elif sensor1_value > 1000 and sensor2_value < 1000 and not pygame.mixer.music.get_busy():
                    play_audio(audio2)
                    is_playing = True
                    print(2);
                elif sensor1_value < 1000 and sensor2_value < 1000 and not pygame.mixer.music.get_busy():
                    play_audio(audio3)
                    is_playing = True
                    print(3);

        # Reset is_playing flag when music stops
        if is_playing and not pygame.mixer.music.get_busy():
            is_playing = False

        time.sleep(0.1)

    except KeyboardInterrupt:
        break

# Stop the music and close the serial port on exit
pygame.mixer.music.stop()
ser.close()
