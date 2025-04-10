import os
import re
import sys
import glob

if len(sys.argv) < 2:
    print('Usage: python matrix_converter_all.py <input_directory/file> [output_directory]')
    exit()

input_path = sys.argv[1]

# Set output directory
if len(sys.argv) > 2:
    output_dir = sys.argv[2]  # If output directory is specified
else:
    output_dir = './output_pfm'  # Default output directory

# Create output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# If it's a directory, find all files in it
if os.path.isdir(input_path):
    files = glob.glob(os.path.join(input_path, "*.jaspar"))  # Modify the extension if necessary
else:
    files = [input_path]  # If it's a single file, use that

lineRe = re.compile('.*\[(.*)\]')  # A  [content]
spacesRe = re.compile('\s+')

total_count = 0
for url in files:
    try:
        with open(url, 'r') as f:
            data = f.read()
        
        # Input file name as prefix for output files (for uniqueness)
        file_prefix = os.path.basename(url).split('.')[0] + "_"
        
        count = 0
        for matrix in data.split('>'):
            if not matrix:
                continue
            
            # Create unique name with input file name as prefix
            name = file_prefix + matrix.splitlines()[0].replace('/', '_').replace('\t', ' ') + '.pfm'
            
            lines = []
            for line in matrix.splitlines()[1:]:
                m = lineRe.search(line)
                if m:
                    lines.append(spacesRe.sub(' ', m.group(1)).strip())
            
            # Save the converted file directly to the output directory
            with open(os.path.join(output_dir, name), 'w') as f:
                f.write('\n'.join(lines))
            count += 1
        
        total_count += count
        print(f"Processed: {url} - {count} matrices exported")
    except Exception as e:
        print(f"Error processing file: {url}")
        print(f"Error message: {str(e)}")

print(f"Total of {total_count} matrices exported to directory: {output_dir}")
