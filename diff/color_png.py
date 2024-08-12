# from PIL import Image
# import os
#
# file_path = "/home/sergio/Desktop/Bootcamp_Python/diff/Horn_flask_(PSF).png"
# if os.path.exists(file_path):
#     print("Файл існує")
# else:
#     print("Файл не знайдено")
#     exit()
#
# # Open the image
# img = Image.open(file_path)
#
# # Convert the image to RGBA if not already
# img = img.convert("RGBA")
#
# # Define a threshold for "blackness"
# threshold = 30
#
# # Make black areas transparent
# datas = img.getdata()
#
# new_data = []
# for item in datas:
#     # Calculate the brightness of the pixel
#     brightness = sum(item[:3]) // 3  # Average of R, G, and B
#     # Change all nearly black (with any alpha) to transparent
#     if brightness < threshold:
#         # Change to a fully transparent pixel
#         new_data.append((255, 255, 255, 0))
#     else:
#         new_data.append(item)
#
# img.putdata(new_data)
#
# # Create a new image with the desired color (e.g.)
# new_img = Image.new("RGBA", img.size, (105, 236, 122, 255))  # green color
#
# # Composite the images together
# final_img = Image.alpha_composite(new_img, img)
#
# # Save the final image
# final_img.save("Horn flask_colored.png")
#
# print("Обробка завершена. Файл збережено як 'Horn flask_colored.png'.")

from PIL import Image

# Specify the file path
image_path = "/home/sergio/Desktop/Bootcamp_Python/diff/flask-logo.webp"

# Open the original image
img = Image.open(image_path)

# Ensure the image has an alpha channel (RGBA)
img = img.convert("RGBA")

# Create a new image filled with the desired green color (R, G, B, A)
new_img = Image.new("RGBA", img.size, (105, 236, 122, 128))  # Green with 50% transparency

# Composite the new color with the original image
final_img = Image.alpha_composite(new_img, img)

# Save the final image, specifying the path and format
output_path = "/home/sergio/Desktop/SiracencoSerghei/flask-logo_colored.png"
final_img.save(output_path)

print(f"Modified image saved at {output_path}")