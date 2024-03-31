# File Creation
try:
    with open("my_file.txt", "w") as file:
        file.write("This is line 1\n")
        file.write("12345\n")
        file.write("Another line with text and numbers: 67890\n")
        print("File created and initial content written successfully.")
except Exception as e:
    print("Error occurred while creating the file:", e)
finally:
    print("File creation process completed.\n")

# File Reading and Display
try:
    with open("my_file.txt", "r") as file:
        print("Content of my_file.txt:")
        for line in file:
            print(line.strip())
except Exception as e:
    print("Error occurred while reading the file:", e)
finally:
    print("\nFile reading process completed.\n")

# File Appending
try:
    with open("my_file.txt", "a") as file:
        file.write("This is an appended line\n")
        file.write("54321\n")
        file.write("Yet another line appended: 09876\n")
        print("Content appended to my_file.txt successfully.")
except Exception as e:
    print("Error occurred while appending to the file:", e)
finally:
    print("File appending process completed.\n")
