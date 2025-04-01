def modify_file(input_filename, output_filename):
  """This function updates the contents on the input file to lowercase"""
  try:
        # Open the input file
        with open(input_filename, 'r') as infile:
            content = infile.read()

        modified_content = content.lower()

        # Open the output file in write mode
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)

        print(f"Content from {input_filename} has been successfully written to {output_filename}")

  except Exception as e:
        print(f"An error occurred: {e}")

# Example
input_filename = '/content/text.txt'  # Filepath
output_filename = '/content/output.txt'
modify_file(input_filename, output_filename)
