import csv
import ast
import json

def read_csv_to_dict_list(file_path):
    with open(file_path, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        dict_list = [row for row in csv_reader]
    return dict_list

def main():
    file_path = input("File Path: ")
    chunks = read_csv_to_dict_list(file_path)

    for chunk in data:
        chunk["chunk_id"] = int(chunk["chunk_id"])
        chunk["line_range"] = ast.literal_eval(chunk["line_range"])
        chunk["page_range"] = ast.literal_eval(chunk["page_range"])
        chunk["embedding"] = json.loads(chunk["embedding"])
        insert_chunk("10.1.160.76", chunk)

if __name__ == "__main__":
    main()
    
