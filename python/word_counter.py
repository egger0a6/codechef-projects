def read_input_file(filename):

    try:
        # Open the file in read mode ('r')
        with open(filename, "r") as file:
        # Read the file content and strip any leading or trailing whitespaces
            content = file.read().strip()
        return content
    except FileNotFoundError:
        # Handle the case where the file does not exist
        print(f"Error: The file '{filename}' was not found.")
        # Return an empty string if the file is not found
        return ""
    

if __name__ == "__main__":
    
    filename = 'input.txt'
    text = read_input_file(filename)
    print(text)