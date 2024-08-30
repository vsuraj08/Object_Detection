import os
import xml.etree.ElementTree as ET

# Define the paths
xml_dir = "data/labels_xml/"  # Folder where the .xml files are located
output_dir = "data/labels/"   # Folder where the .txt files will be saved

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Define your class names
class_names = ['void', 'crack', 'galling', 'keyhole', 'cross section reduction defect', 'flash']

# Convert the .xml files to YOLO format
for xml_file in os.listdir(xml_dir):
    if xml_file.endswith(".xml"):
        tree = ET.parse(os.path.join(xml_dir, xml_file))
        root = tree.getroot()

        # Open the corresponding .txt file
        txt_file = os.path.join(output_dir, os.path.splitext(xml_file)[0] + ".txt")
        with open(txt_file, "w") as f:
            for obj in root.findall("object"):
                class_name = obj.find("name").text
                class_id = class_names.index(class_name)

                # Extract bounding box
                xmlbox = obj.find("bndbox")
                x_min = float(xmlbox.find("xmin").text)
                y_min = float(xmlbox.find("ymin").text)
                x_max = float(xmlbox.find("xmax").text)
                y_max = float(xmlbox.find("ymax").text)

                # Get image dimensions
                width = float(root.find("size").find("width").text)
                height = float(root.find("size").find("height").text)

                # Convert to YOLO format
                x_center = (x_min + x_max) / 2.0 / width
                y_center = (y_min + y_max) / 2.0 / height
                box_width = (x_max - x_min) / width
                box_height = (y_max - y_min) / height

                # Write the YOLO formatted data to the .txt file
                f.write(f"{class_id} {x_center} {y_center} {box_width} {box_height}\n")
