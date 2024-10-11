
import os
import sys
import pyautogui as pytg


from PIL import Image, ImageFilter

img_path = os.path.join(r"C:\Users\Usuario\Downloads","brain.png")
borderSize = 20
color = (255, 0, 0)


# Open original image and extract the alpha channel
im = Image.open(img_path)
alpha = im.getchannel('A')

# Create red image the same size and copy alpha channel across
background = Image.new('RGBA', im.size, color=color)
background.putalpha(alpha) 

# Make the background bigger
background=background.resize((background.size[0]+borderSize, background.size[1]+borderSize))

# Merge the targeted image (foreground) with the background
foreground = Image.open(img_path)
background.paste(foreground, (int(borderSize/2), int(borderSize/2)), foreground.convert("RGBA"))
imageWithBorder = background
imageWithBorder.save("teste.png")