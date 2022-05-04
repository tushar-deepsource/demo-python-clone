from my_utils import get_file_names

# bruh
files = get_file_names()
python_file_found = any(file.endswith(".py") for file in files)
