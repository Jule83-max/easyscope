# EasyScope

## Overview
EasyScope is a simple yet efficient command-line tool designed for Windows systems to archive and compress files and directories. It helps users save disk space and improve file load times by creating compressed archives of specified files or directories.

## Features
- Archive individual files or entire directories.
- Compress files into a ZIP format, reducing space usage.
- Simple command-line interface for ease of use.

## Requirements
- Python 3.x
- Windows operating system

## Installation
1. Ensure you have Python 3.x installed on your Windows system.
2. Download the `easyscope.py` file from this repository.

## Usage
Open a command prompt and navigate to the directory containing `easyscope.py`. Use the following command format to archive and compress files or directories:

```bash
python easyscope.py <source_path> <destination_path>
```

- `<source_path>`: The path to the file or directory you want to archive.
- `<destination_path>`: The path where you want to store the compressed archive.

### Example
To compress a directory named `Documents` and save the archive as `archive.zip` on your desktop, run:

```bash
python easyscope.py "C:\Users\YourName\Documents" "C:\Users\YourName\Desktop\archive.zip"
```

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contributing
Contributions are welcome! Please fork the repository and use a feature branch. Pull requests are accepted.

## Support
If you encounter any issues or have questions, please open an issue in this repository.