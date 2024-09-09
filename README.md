# SmartGlove Project

The **SmartGlove** is an innovative wearable device designed to recognize hand gestures and convert them into audio commands, as well as control home automation systems. Utilizing advanced flex sensors and a microcontroller, the SmartGlove captures the precise movements of the user's fingers and translates these gestures into specific audio outputs. This cutting-edge technology enables seamless communication for individuals with speech impairments and offers intuitive control over smart home devices.......

# Weekly Updates

## Week 1: Microcontroller and Machine Learning Model Research

In the first week, I focused on researching the appropriate microcontroller and machine learning (ML) model for the SmartGlove project. After evaluating several options, I decided to use the **ESP32** microcontroller due to its powerful processing capabilities and suitability for running machine learning models.

In parallel, I explored various ML models and ultimately chose **TensorFlow Lite** for training and deploying the gesture recognition model. TensorFlow Lite is a lightweight version of TensorFlow, designed to run on resource-constrained devices like microcontrollers. It provides the necessary tools to optimize ML models for low-latency and efficient inference on edge devices, making it an ideal choice for the SmartGlove.

![Esp32](https://github.com/user-attachments/assets/5f861c8b-3c01-4997-b798-b858e388d406)

## Week 2: Flex Sensor and Microcontroller Simulation

During the second week, I created a simulation using Tinkercad to explore how a flex sensor interacts with a microcontroller, specifically an Arduino board, and how the flex sensor's varying resistance can control the lighting of LEDs.

![Screenshot 2024-09-09 165151](https://github.com/user-attachments/assets/9f956720-9e3a-4f3e-9526-d6c91a29007a)

#### Simulation Overview:
The simulation demonstrates how a flex sensor, connected to an Arduino Uno, can be used to control multiple LEDs based on the sensor's bending degree. Below is a breakdown of what the simulation represents:

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
