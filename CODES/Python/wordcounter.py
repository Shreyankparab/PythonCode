def count_file_details(filename):
    try:
        # Open the file in read mode
        with open(filename, 'r') as file:
            # Initialize counters
            line_count = 0
            word_count = 0
            char_count = 0
            
            # Iterate over each line in the file
            for line in file:
                line_count += 1
                words = line.split()
                word_count += len(words)
                char_count += len(line)
        
        # Display the results
        print(f"Number of lines: {line_count}")
        print(f"Number of words: {word_count}")
        print(f"Number of characters: {char_count}")
    
    except FileNotFoundError:
        print(f"The file '{filename}' was not found. Please check the filename and try again.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Get the file name from the user
file_name = input("Enter the file name: ")
count_file_details(file_name)
