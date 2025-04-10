JASPAR to PFM Matrix Converter

<img alt="Python 3.x" src="https://img.shields.io/badge/python-3.x-blue.svg">
<img alt="License" src="https://img.shields.io/badge/license-MIT-green.svg">
This Python script converts JASPAR format matrix files to individual Position Frequency Matrix (PFM) files. It can process a single file or all files in a directory.

🚀 Features

✅ Convert JASPAR matrices to individual PFM files
📁 Process all files in a directory with one command
🗂️ Organize output files in a designated folder
🏷️ Add file prefixes to ensure unique output filenames
⚠️ Handle errors gracefully

📋 Requirements

Python 3.x
Standard Python libraries: os, re, sys, glob (no additional installation needed)

💾 Installation

No installation is needed, just download the script:

curl -O https://raw.githubusercontent.com/yourusername/matrix-converter/main/matrix_converter_all.py

Or clone the repository:

git clone https://github.com/yourusername/matrix-converter.git
cd matrix-converter

🔧 Usage
Basic Usage

python matrix_converter_all.py <input_directory_or_file> [output_directory]

Parameters

| Paramaters | Description | Required |
|----------|----------|----------|
| input_directory_or_file    | Path to a single JASPAR file or a directory containing JASPAR files     | Yes     |
| output_directory    | The directory where PFM files will be saved (default: './output_pfm')     | No     |


Examples

Process a single file:

python matrix_converter_all.py path/to/your_file.jaspar

Process all .jaspar files in a directory:

python matrix_converter_all.py path/to/jaspar_files/

Specify output directory:

📄 Input Format
The script processes JASPAR format files which are commonly used for representing position weight matrices in bioinformatics.

The script expects JASPAR format files with content like:

>MA0001.1 SEP4
A  [ 3 16 12 16... ]
C  [ 4  3  5  3... ]
G  [ 8  0  7  0... ]
T  [ 5  1  0  1... ]

📥 Output Format
The script creates individual PFM files for each matrix found. The output format is:

Each output file is named using the pattern: [input_filename]_[matrix_name].pfm

⚙️ How It Works
<details> <summary>Click to expand the detailed workflow</summary>
The script reads the input file(s)
For each file, it splits the content on > characters
For each matrix section, it extracts the values inside square brackets
It normalizes spaces and formats the output
Each matrix is saved as an individual PFM file in the output directory
</details>
⚠️ Error Handling
The script will continue processing other files if an error occurs in one file. Error messages are displayed in the console but don't stop the execution.

📝 To-Do List
<input checked="" disabled="" type="checkbox"> Basic file conversion functionality
<input checked="" disabled="" type="checkbox"> Directory processing
<input checked="" disabled="" type="checkbox"> Error handling
<input disabled="" type="checkbox"> Support for other matrix formats
<input disabled="" type="checkbox"> Interactive mode
🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

📜 License
MIT License

📬 Contact
For questions or suggestions, please open an issue on GitHub.

Note: This script was developed to simplify the workflow for bioinformaticians working with transcription factor binding site models.

