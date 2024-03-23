import sys
import exifread

def print_metadata(image_path):
  """
  Prints the metadata of an image file.

  Args:
      image_path: The path to the image file.
  """
  try:
    with open(image_path, 'rb') as image_file:
      tags = exifread.process_file(image_file)

      if tags:
        print("Image Metadata:")
        for tag, value in tags.items():
          if isinstance(value, bytes):
            value = value.decode('utf-8')
          print(f"{tag}: {value}")
      else:
        print("Image does not contain any metadata.")
  except FileNotFoundError:
    print(f"Error: File '{image_path}' not found.")

# Get the image path from command line arguments
if len(sys.argv) > 1:
  image_path = sys.argv[1]
  print_metadata(image_path)
else:
  print("Usage: python image_metadata.py <image_path>")
