# Pitch Detector using Python and Aubio

The Pitch Detector is a Python program that uses the Aubio and prrat libraries to detect and visualize the fundamental frequency of an audio signal in real-time. This program provides a graphical interface to display the detected pitch, frequency, and cents deviation from the closest note. You can choose between using the Aubio library, the prrat library, or a combined graphical interface for pitch detection.

## Features

- Real-time fundamental frequency detection and visualization using Aubio and prrat libraries.
- Display of the detected note name, frequency (Hz), and cents deviation.
- Visualization of the detected pitch using a moving circle.
- User-friendly graphical interface using the Pygame library.
- Option to run the Aubio library, prrat library, or both libraries simultaneously.

## Installation

1. Make sure you have Python installed on your system.
2. Install the required libraries using the following command:
   ```
   pip install pygame aubio parselmouth numpy pyaudio music21
   ```
3. Download the `prratAlgo.py` and `aubioAlgo.py` files, which contain the pitch detection algorithms using the prrat and Aubio libraries.
4. Run the `game.py` script to use the graphical interface, or run the `prratAlgo.py` and `aubioAlgo.py` scripts separately to use each library individually.
5. Follow the instructions in the graphical interface or console to sing or play a musical note into your microphone.

## Usage

1. Run the `game.py` script to use the graphical interface for pitch detection.
2. Alternatively, run the `prratAlgo.py` script for pitch detection using the prrat library.
3. Run the `aubioAlgo.py` script for pitch detection using the Aubio library.
4. Sing or play a musical note into your microphone.
5. The graphical interface or console will display the detected note, frequency, and cents deviation in real-time.
6. The moving circle on the screen (if using the graphical interface) represents the pitch height.
7. Close the graphical window or stop the console process to exit the pitch detection.

## Compatibility

This program requires the Pygame, Aubio, parselmouth, numpy, pyaudio, and music21 libraries to be installed on your system.

## Screenshots

![Screenshot](screenshot.png)
*Fig. 1: The Pitch Detector in action, displaying the detected pitch, frequency, and cents deviation.*

## Contact

For any questions or feedback regarding the Pitch Detector program, please feel free to reach out to the developer:

Name: Morteza Hatami
Email: m.hatami@live.com
