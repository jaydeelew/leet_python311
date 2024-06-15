import os

# Path to the directory containing the files
directory = "AllTemplates"

# Iterate over all files in the directory
for filename in os.listdir(directory):
    if ":" in filename:
        # Replace ':' with '_' in the filename
        new_filename = filename.replace(":", "_")
        # Full path for old and new files
        old_file = os.path.join(directory, filename)
        new_file = os.path.join(directory, new_filename)
        # Rename the file
        os.rename(old_file, new_file)
        print(f'Renamed "{filename}" to "{new_filename}"')
