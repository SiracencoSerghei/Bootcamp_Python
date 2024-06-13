""" look on https://pypi.org/project/colorgram.py/ for pip install colorgram.py"""
import colorgram

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    rgb_colors.append(color.rgb)
print(rgb_colors)
#
# from PIL import Image
#
# def extract_all_distinct_colors(image_path):
#     """
#     Extracts all distinct colors from an image by iterating over each pixel.
#
#     Args:
#     image_path (str): The path to the image file.
#
#     Returns:
#     set: A set of RGB tuples representing all distinct colors.
#     """
#     # Open the image file.
#     with Image.open(image_path) as img:
#         # Convert the image to RGB if it's not already.
#         if img.mode != 'RGB':
#             img = img.convert('RGB')
#
#         # Create a set to store unique colors.
#         unique_colors = set()
#
#         # Iterate over each pixel in the image.
#         for pixel in img.getdata():
#             unique_colors.add(pixel)
#
#     return unique_colors
#
# # Example usage:
# image_path = 'image.jpg'
# all_distinct_colors = extract_all_distinct_colors(image_path)
#
# # Print the extracted colors.
# for color in all_distinct_colors:
#     print(color)