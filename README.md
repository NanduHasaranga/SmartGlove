# SmartGlove Project

## Project Overview
The **SmartGlove** is an innovative wearable device designed to recognize hand gestures and convert them into audio commands, as well as control smart home automation systems. This project aims to develop a responsive, user-friendly solution that empowers individuals with speech impairments to communicate through hand gestures while also providing intuitive gesture-based control over connected smart devices. Using advanced flex sensors and a powerful microcontroller, the SmartGlove captures precise finger movements and translates them into specific audio outputs and control signals for home automation. The development process will be documented, from initial design and prototyping to final implementation, providing a detailed overview of each stage.

![SmartGloveHome](https://github.com/user-attachments/assets/39d6b4cc-ab44-46ae-8fd2-bf972ecedf96)

## Proposed Features
- **Gesture Recognition**: Detect and interpret hand gestures using advanced flex sensors.
- **Audio Output**: Convert gestures into real-time audio feedback to assist with communication for speech-impaired individuals.
- **Smart Home Integration**: Control smart home devices such as lights, fans, or media systems using recognized hand gestures.
- **Machine Learning**: Incorporate a TensorFlow Lite machine learning model to enhance gesture recognition accuracy.
- **User-Friendly Interface**: Enable easy customization of gestures and commands, making the SmartGlove adaptable to different user needs.

## Proposed Technologies and Tools
- **Programming Languages**: Python, C/C++
- **Libraries**: TensorFlow Lite, OpenCV (for potential future expansions)
- **Hardware**:
  - **Flex Sensors**: To detect the bending of fingers.
  - **ESP32**: As the main microcontroller for handling sensor input and wireless communication.
  - **Audio Output Module**: For converting gestures into audio commands.
- **Development Environment**: VSCode, Arduino IDE, PlatformIO
- **Machine Learning Framework**: TensorFlow Lite for gesture recognition.

## Weekly Progress
- **Week 1**: Define project requirements and research gesture recognition technologies. Select microcontroller and flex sensors for the SmartGlove.
- **Week 2**: Interface flex sensors with ESP32 and set up a basic gesture recognition system. Configure serial communication for testing sensor outputs.

- **Arduino Uno**: The microcontroller used in this simulation. It reads the analog values from the flex sensor and controls the LEDs based on the sensor's output.
- **Flex Sensor**: Positioned on the right side of the breadboard, the flex sensor changes its resistance when bent. This change in resistance alters the voltage output, which is read by the Arduino's analog pin (A0).
- **LEDs**: A series of LEDs are connected to the digital pins of the Arduino (D2 to D6). These LEDs light up sequentially or in varying patterns depending on the flex sensor's readings.
- **Voltage Measurement**: The simulation includes a virtual multimeter displaying the voltage across the flex sensor, which changes as the sensor bends, illustrating how the sensor’s resistance varies with the angle of the bend.
- **Resistors**: Each LED is connected in series with a resistor to limit the current and protect the LEDs from burning out.

#### How it Works:
- When the flex sensor is straight, it has a certain baseline resistance. As it bends, the resistance increases or decreases, depending on the sensor's orientation.
- The Arduino reads the analog input from the flex sensor and converts it into a corresponding value. This value is then used to determine how many LEDs should light up or in what pattern.
- As the flex sensor bends more, the analog value changes, and more LEDs are turned on to indicate the level of flex.

This simulation is a fundamental step in understanding how the SmartGlove can interpret hand gestures and translate them into meaningful outputs like controlling devices or generating audio commands. By using the Tinkercad platform, I was able to visualize and test the basic concept of using flex sensors to create variable input signals for the microcontroller.
