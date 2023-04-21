import os

def get_directory_files(directory):
    file_list = []
    for root, directories, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            file_list.append(file_path)
    return file_list

if __name__ == '__main__':
    directory = input('Enter directory path: ')
    files = get_directory_files(directory)
    print(f'Found {len(files)} files in {directory}')
