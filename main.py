import openai
import os
import win32clipboard
import pyautogui
import keyboard
import time
import pyperclip


def send(text_for_CGPT):
    # Retrieve the OpenAI API key from environment variables
    openai.api_key = os.getenv('OPENAI_KEY')

    # Check if the API key is set, exit if not
    if not openai.api_key:
        print("OPENAI_KEY is not set. Please set your environment variable.")
        exit()

    try:
        # Indicate the start of the process by typing "S"
        pyautogui.write("S")

        # Read guidelines from a file to set as the system message
        with open('Richtlinien_chatgpt.txt', 'r', encoding='utf-8') as file:
            richtlinien = file.read()

        # Send a chat completion request to OpenAI
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": richtlinien},
                {"role": "user", "content": text_for_CGPT}
            ]
        )

        # Retrieve and print the response text
        print(response['choices'][0]['message']['content'])
        text = response['choices'][0]['message']['content']

        # Indicate that the response has arrived by typing "R"
        pyautogui.write("R")
        return text
    except Exception as e:
        # Print the error message and indicate error by typing "E"
        print(f"An error occurred: {e}")
        pyautogui.write("E")


def write_char(char):
    # Handle special cases for certain German characters
    if char == '*':
        return
    elif char in "öäüÖÄÜ":
        pyperclip.copy(char)
        pyautogui.hotkey('ctrl', 'v')
    else:
        pyautogui.write(char, interval=0.001)


def find_text():
    # Open the clipboard and retrieve the text
    win32clipboard.OpenClipboard()
    text_for_CGPT = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    print(text_for_CGPT)
    return text_for_CGPT


def writing(text, current_position):
    while True:
        if keyboard.is_pressed('page down'):
            # Type the text starting from the current position
            for i in range(current_position, len(text)):
                if not keyboard.is_pressed('page down'):
                    return i
                write_char(text[i])
            else:
                return 0
        elif keyboard.is_pressed('page up'):
            return 0

        # Sleep briefly to prevent high CPU usage
        time.sleep(0.0001)


if __name__ == "__main__":
    while True:
        if keyboard.is_pressed("f5"):
            # Retrieve text from clipboard and send it to OpenAI
            text_for_CGPT = find_text()
            text = send(text_for_CGPT)
            current_position = 0
            try:
                while True:
                    # Continuously write the text based on keyboard input
                    current_position = writing(text, current_position)
            except Exception as e:
                # Print any error that occurs during writing
                print(f"An error occurred: {e}")
            print("Press 'Page Down' to continue writing, 'Page Up' to restart.")
        else:
            # Sleep briefly to prevent high CPU usage when waiting for key press
            time.sleep(0.1)
