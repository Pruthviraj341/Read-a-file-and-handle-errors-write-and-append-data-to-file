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

