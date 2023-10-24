# Define the source and destination file paths
source_file_path = "textfile.txt"
destination_file_path = "outputfile.txt"

# Open the source file for reading
with open(source_file_path, "r") as source_file:
    # Read the contents of the source file
    source_data = source_file.read()

# Open the destination file for writing
with open(destination_file_path, "w") as destination_file:
    # Write the data from the source file to the destination file
    destination_file.write(source_data)

print(f"Data has been copied from {source_file_path} to {destination_file_path}.")

