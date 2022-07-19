file_path = input()

file_name, file_extension = file_path.split("\\")[-1].split(".")
print(f"File name: {file_name}\n"
      f"File extension: {file_extension}")
