# Task 1: Read a File and Handle Errors

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            # Read and print line by line
            for line in file:
                print(line.strip())  # strip() removes extra newline characters
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function
read_file("sample.txt")

# Task 2: Write and Append Data to a File

def write_and_append_file(filename):
    try:
        # Step 1: Take user input and write it to a file
        user_input = input("Enter some text to write to the file: ")
        with open(filename, 'w') as file:   # 'w' = write mode (creates/overwrites file)
            file.write(user_input + "\n")
        print(f"Data written to {filename} successfully.")

        # Step 2: Append additional data to the same file
        extra_input = input("Enter additional text to append: ")
        with open(filename, 'a') as file:   # 'a' = append mode
            file.write(extra_input + "\n")
        print(f"Additional data appended to {filename} successfully.")

        # Step 3: Read and display final content
        print("\nFinal content of the file:")
        with open(filename, 'r') as file:
            for line in file:
                print(line.strip())

    except Exception as e:
        print(f"An error occurred: {e}")

# Run the function
write_and_append_file("output.txt")
