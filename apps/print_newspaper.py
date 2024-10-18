import subprocess

# Usage: Printer operator should run this program and provide the
# name of each section to print by 2am for punctual delivery.

def print_file(file_path):
    try:
        # Use the 'lp' command to print the file
        subprocess.run(['lp', "readyForPressing/{}".format(file_path)], check=True)
        print(f"Printing {file_path}...")
    except subprocess.CalledProcessError as e:
        print(f"Failed to print the file: {e}")
    except FileNotFoundError:
        print(f"The file {file_path} was not found.")



file_to_print = input("Enter the filename of the section")
print_file(file_to_print)
