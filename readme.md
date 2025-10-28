# 🧠Describr: AI Visual Helper

Describr is a desktop application designed to assist visually impaired users by providing audible descriptions of images. It leverages the power of Google's Gemini AI to analyze an uploaded image and generate a concise description, which is then read aloud using a text-to-speech engine. Users can also ask follow-up questions about the image content.

## Features

-   **Image-to-Text Description:** Upload an image (`.jpg`, `.png`, `.jpeg`) and receive a detailed description.
-   **Text-to-Speech (TTS):** The generated description is automatically read aloud.
-   **Audio Replay:** Replay the audio description at any time.
-   **Interactive Q&A:** Ask specific questions about the uploaded image and receive audible answers.
-   **Simple GUI:** An intuitive and easy-to-use interface built with Tkinter.

## How It Works

The application follows a simple workflow:

1.  **Image Upload:** The user uploads an image through the application's interface.
2.  **Image Processing:** The image is read and encoded using OpenCV.
3.  **AI Analysis:** The encoded image is sent to the Google Gemini API, which generates a descriptive caption.
4.  **Audible Output:** The `pyttsx3` library converts the text caption into speech and plays it for the user.
5.  **Display:** The caption is also displayed in the GUI for reference.

## Setup and Installation

### Prerequisites

-   Python 3.x

### Steps

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/whoisibk/Describr-AI.git
    cd Describr-AI
    ```

2.  **Install the required packages:**
    ```sh
    pip install -r requirements.txt
    ```

3.  **Set up your API Key:**
    -   This project requires a Google Gemini API key.
    -   Create a file named `.env` in the root directory of the project.
    -   Add your API key to the `.env` file in the following format:
        ```
        GEMINI_API_KEY="YOUR_API_KEY_HERE"
        ```

## Usage

1.  **Run the application:**
    ```sh
    python app.py
    ```

2.  **Upload an Image:**
    -   Click the **`UPLOAD IMAGE 📁`** button.
    -   Select an image file from your computer.

3.  **Get Description:**
    -   The application will display a "Loading..." window while it processes the image and contacts the API.
    -   Once complete, the description will appear in the text box and be read aloud.

4.  **Replay and Ask Questions:**
    -   Click **`REPLAY AUDIO 📢`** to hear the description again.
    -   Click **`GOT QUESTIONS❓`** to open a new window where you can type a question about the image and submit it to get an audible response.

## Technologies Used

-   **Python**
-   **Google Gemini API:** For image understanding and content generation.
-   **Tkinter:** For the graphical user interface.
-   **pyttsx3:** For text-to-speech conversion.
-   **OpenCV:** For image reading and processing.
-   **Pillow (PIL):** For handling and displaying images within the Tkinter GUI.