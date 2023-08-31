#!/usr/bin/env python3

import os.path
from PIL import Image

def is_image(filename):
  """Check if a filename is an image."""
  extensions = [".jpg", ".jpeg", ".png"]
  return os.path.splitext(filename)[1].lower() in extensions

images = []
i=1

print(" === IMGs to PDF Program === ")
print(" === Type \"stop\" to stop === ")
while True:
	filename = input("Enter name of image {}:  ".format(i))
	if os.path.isfile(filename):
		if not is_image(filename):
			print("Wrong image format!")
		else:
			image_i = Image.open(filename)
			im_i = image_i.convert('RGB')
			images.append(im_i)
			i+=1
	elif filename.lower() == "stop":
		break
	else:
		print("File {} not found!".format(filename))

pdf_path = ""
pdf_name = input("Save as [.pdf]: ")
if not pdf_name.endswith(".pdf"):
	pdf_name += ".pdf"

images[0].save(os.path.join(pdf_path, pdf_name), save_all=True, append_images=images[1:])
