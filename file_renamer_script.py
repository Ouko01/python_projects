import os

# Specify the folder containing the files.
folder_path = input("Enter the folder path: ")

# Check if the directory exists.
if not os.path.isdir(folder_path):
    print("Invalid directory. Please check the path and try again.")
else:
    files = os.listdir(folder_path) # Get all the files in the folder.

    # Loop through each file and rename it.
    for index, filename in enumerate(files):
        old_path = os.path.join(folder_path, filename) # Full path of the old.

        #Define new filename(Example: file_1.txt, file_2.txt)
        file_extension = os.path.splitext(filename)[1] # Get the extension.
        new_filename = f"file_{index+1}{file_extension}"
        new_path = os.path.join(folder_path, new_filename) # Full path of the new file.

        os.rename(old_path, new_path) # Rename the file.
        print(f"Renamed: {filename} > {new_filename}")

    print("✅fIle renaming completed!")