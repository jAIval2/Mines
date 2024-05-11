from PIL import Image
import numpy as np
import csv
import os

def tile_image(image, tile_size):
    width, height = image.size
    tiles = []
    for y in range(0, height - tile_size + 1, tile_size):
        for x in range(0, width - tile_size + 1, tile_size):
            box = (x, y, x + tile_size, y + tile_size)
            tiles.append(image.crop(box))
    return tiles

def is_mine(tile, mine_references, threshold):
    tile_array = np.array(tile).flatten()
    correlations = []
    for mine_ref in mine_references:
        mine_array = np.array(mine_ref).flatten()
        correlation = np.corrcoef(tile_array, mine_array)[0, 1]
        correlations.append(correlation)
    max_correlation = max(correlations)
    return max_correlation > threshold

def identify_mines(image, references, tile_size=100, threshold=0.9):
    mine_positions = []
    tiles = tile_image(image, tile_size)
    num_tiles_x = image.width // tile_size
    for i, tile in enumerate(tiles):
        if is_mine(tile, references, threshold):
            row = i // num_tiles_x + 1
            col = i % num_tiles_x + 1
            mine_positions.append((col, row))  # Swap col and row for X, Y format
    return mine_positions

def write_to_csv(data, file_path):
    with open(file_path, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

def process_images(image_folder, reference_folder, csv_file):
    references = []
    for ref_filename in os.listdir(reference_folder):
        if ref_filename.endswith(".png") or ref_filename.endswith(".jpg"):
            ref_path = os.path.join(reference_folder, ref_filename)
            ref_image = Image.open(ref_path)
            references.append(ref_image)

    for filename in os.listdir(image_folder):
        if filename.endswith(".png") or filename.endswith(".jpg"):
            image_path = os.path.join(image_folder, filename)
            image = Image.open(image_path)
            mine_tile_positions = identify_mines(image, references)
            mine_data = [(filename,) + pos for pos in mine_tile_positions]
            write_to_csv(mine_data, csv_file)

image_folder = "images"
reference_folder = "references"
csv_file = "mine_posit11ion11s.csv"
process_images(image_folder, reference_folder, csv_file)
print("Mine positions updated in '{}' file.".format(csv_file))
