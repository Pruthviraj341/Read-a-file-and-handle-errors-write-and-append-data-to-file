# Read-a-file-and-handle-errors-write-and-append-data-to-file
# File Reader with Error Handling

This is a simple Python program that demonstrates how to **read a text file line by line** while handling errors gracefully.  
It is useful for beginners learning file handling and exception management in Python.

---

## Features
- Opens and reads a file named **`sample.txt`**.
- Prints the file content **line by line**.
- Handles errors if:
  - The file does not exist.
  - Any unexpected issue occurs while reading.

---

## Requirements
- Python 3.x

---

## Usage

1. Create a text file named `sample.txt` in the same directory as the script.  
   Example content:
# Write and Append Data to a File

This Python program demonstrates how to **write, append, and read data from a text file**.  
It allows the user to provide input, saves it into a file, and then appends additional input without overwriting the existing data.

---

## Features
- Takes **user input** and writes it to `output.txt`.
- Appends **additional input** to the same file.
- Reads and displays the **final content** of the file.

---

## Requirements
- Python 3.x

---

## Usage

1. Run the script:
   ```bash
   python file_write_append.py
Enter some text to write to the file: Hello World
Enter additional text to append: This is appended text
Final content of the file:
Hello World
This is appended text
File Modes Used

'w' → Write mode (creates or overwrites the file).

'a' → Append mode (adds new content to the end without erasing existing content).

'r' → Read mode (reads and displays the content).

Error Handling

If any unexpected error occurs while writing, appending, or reading, the program will display a helpful error message.   
