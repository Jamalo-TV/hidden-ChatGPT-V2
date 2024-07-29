# README

## Overview

This script interacts with OpenAI's GPT-4 model to automate text processing based on user inputs. It utilizes various libraries for clipboard access, keyboard interaction, and automation to facilitate seamless integration with ChatGPT. 

## Prerequisites

Ensure you have the following Python libraries installed:

- `openai`
- `pyautogui`
- `pyperclip`
- `keyboard`
- `pywin32`
- `os`

You can install them using pip:
```pip install openai pyautogui pyperclip keyboard pywin32```

## Environment Setup

You need to set the `OPENAI_KEY` environment variable with your OpenAI API key. To set it, run the following command in your terminal or add it to your environment variables:
```bash
export OPENAI_KEY='your_openai_api_key'
```

## Files

- `Richtlinien_chatgpt.txt`: This file should contain the guidelines or instructions for ChatGPT. Place it in the same directory as the script.

## Usage

1. **Run the Script**: Start the script by running:
   ```bash
   python main.py
   ```

2. **Activate the Process**: Press the `F5` key to initiate the process. The script will:
   - Retrieve text from the clipboard.
   - Send the text to OpenAI's GPT-4 model with predefined guidelines.
   - Print the response from the model.

3. **Automated Writing**:
   - The script will wait for further instructions:
     - Press `Page Down` to continue writing the response.
     - Press `Page Up` to restart the process.
   - The script handles typing of text, including special cases for certain German characters.

## Functions

### `send(text_for_CGPT)`
- Sends the provided text to OpenAI's GPT-4 model.
- Reads guidelines from `Richtlinien_chatgpt.txt`.
- Handles responses and errors.

### `write_char(char)`
- Writes a character.
- Handles special German characters.

### `find_text()`
- Retrieves text from the clipboard.

### `writing(text, current_position)`
- Writes the text starting from the specified position.
- Listens for `Page Down` and `Page Up` key presses to control the writing process.

## Main Loop
- Listens for the `F5` key press to start the process.
- Continues writing based on keyboard inputs.

## Error Handling
- The script prints any errors encountered during the sending or writing process and indicates errors using predefined keystrokes.

## Notes
- Ensure your clipboard contains the text you want to process before pressing `F5`.
- Adjust the sleep intervals if needed to optimize CPU usage.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
