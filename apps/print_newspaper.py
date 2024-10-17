import subprocess

def print_file(file_path):
    try:
        # Use the 'lp' command to print the file
        subprocess.run(['lp', file_path], check=True)
        print(f"Printing {file_path}...")
    except subprocess.CalledProcessError as e:
        print(f"Failed to print the file: {e}")
    except FileNotFoundError:
        print(f"The file {file_path} was not found.")



file_to_print = input("Enter the filename (with full path) of the article")
print_file(file_to_print)
