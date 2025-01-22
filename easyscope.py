import os
import zipfile
import argparse

def archive_and_compress(source_path, destination_path):
    """
    Archives and compresses the specified files or directories.

    Parameters:
    source_path (str): The path to the file or directory to archive.
    destination_path (str): The path where the compressed archive will be stored.
    """
    if not os.path.exists(source_path):
        print(f"Error: The source path '{source_path}' does not exist.")
        return

    with zipfile.ZipFile(destination_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        if os.path.isfile(source_path):
            zipf.write(source_path, os.path.basename(source_path))
        else:
            for foldername, subfolders, filenames in os.walk(source_path):
                for filename in filenames:
                    file_path = os.path.join(foldername, filename)
                    arcname = os.path.relpath(file_path, start=source_path)
                    zipf.write(file_path, arcname)
    
    print(f"Files have been archived and compressed to '{destination_path}'.")

def main():
    parser = argparse.ArgumentParser(description="Archive and compress files on Windows systems.")
    parser.add_argument("source", help="The path to the file or directory to archive.")
    parser.add_argument("destination", help="The path where the compressed archive will be stored.")
    args = parser.parse_args()

    archive_and_compress(args.source, args.destination)

if __name__ == "__main__":
    main()