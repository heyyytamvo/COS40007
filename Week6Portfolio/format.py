import pandas as pd
import os

def convert_to_yolo_format(input_csv, output_dir):
    # Read the CSV file
    df = pd.read_csv(input_csv)

    # Create a mapping for classes to class IDs
    class_map = {name: idx for idx, name in enumerate(df['class'].unique())}

    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    for index, row in df.iterrows():
        filename = row['filename']
        width = row['width']
        height = row['height']
        class_name = row['class']
        xmin = row['xmin']
        ymin = row['ymin']
        xmax = row['xmax']
        ymax = row['ymax']

        # Calculate YOLO format values
        class_id = class_map[class_name]
        x_center = (xmin + xmax) / 2 / width
        y_center = (ymin + ymax) / 2 / height
        bbox_width = (xmax - xmin) / width
        bbox_height = (ymax - ymin) / height

        # Format YOLO output
        yolo_line = f"{class_id} {x_center:.6f} {y_center:.6f} {bbox_width:.6f} {bbox_height:.6f}\n"

        # Write to corresponding .txt file
        output_file = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}.txt")
        with open(output_file, 'a') as f:
            f.write(yolo_line)

if __name__ == "__main__":
    input_csv = "Bounding_boxes/test_labels.csv"  # Replace with your input CSV file
    output_dir = "Bounding_boxes_YOLO/Test"  # Replace with your desired output directory

    convert_to_yolo_format(input_csv, output_dir)
    print("Conversion complete!")