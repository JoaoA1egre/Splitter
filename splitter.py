import csv
import os

csv_file_path = "original file path"
output_folder = "output file path"

max_lines = 2500

with open(csv_file_path, 'r', encoding='utf-8') as file:

    csv_reader = csv.reader(file, delimiter=';')
    header = next(csv_reader)
    line_count = 0
    file_count = 1
    
    output_file = os.path.join(output_folder, f"output_{file_count}.csv")
    with open(output_file, 'w', encoding='utf-8', newline='') as out_file:
        
        writer = csv.writer(out_file, delimiter=';')
        writer.writerow(header)
        for row in csv_reader:
        
            row = [value.replace('"', '') for value in row]
            writer.writerow(row)
            line_count += 1
            if line_count >= max_lines:

                out_file.close()
                file_count += 1
                output_file = os.path.join(output_folder, f"output_{file_count}.csv")
                out_file = open(output_file, 'w', encoding='utf-8', newline='')
                writer = csv.writer(out_file, delimiter=';')
                writer.writerow(header)
                line_count = 0
        
        out_file.close()
