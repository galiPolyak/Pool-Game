import os

def delete_svg_files(start_index, end_index):
    for i in range(start_index, end_index + 1):
        file_name = f"table-{i}.svg"
        if os.path.exists(file_name):
            os.remove(file_name)
            print(f"Deleted {file_name}")

if __name__ == "__main__":
    delete_svg_files(0, 600)