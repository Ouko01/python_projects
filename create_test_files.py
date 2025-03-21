import os

folder_path = "C:\\Users\\j\\Desktop\\python_projects\\test_file"

# Create folder if it doesn't exist
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Create sample files inside the folder.
filenames = ["image1.jpg", "document1.txt", "report.pdf", "photo.png"]

for file in filenames:
    with open(os.path.join(folder_path, file), 'w') as f:
        pass  # This ensures the file is created and closed properly.
print("Folder and files created successfully!")
