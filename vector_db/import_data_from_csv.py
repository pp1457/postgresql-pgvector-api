import csv
import ast
import json
from insert_chunk import insert_chunk

def read_csv_to_dict_list(file_path):
    """ read csv to dict list """

    with open(file_path, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        dict_list = [row for row in csv_reader]
    return dict_list

def main():
    """ main """
    file_path = input("File Path: ")
    table = input("Table Name: ")
    chunks = read_csv_to_dict_list(file_path)

    for chunk in chunks:
        chunk["chunk_id"] = int(chunk["chunk_id"])
        chunk["line_range"] = ast.literal_eval(chunk["line_range"])
        chunk["page_range"] = ast.literal_eval(chunk["page_range"])
        chunk["embedding"] = json.loads(chunk["embedding"])
        insert_chunk(chunk, table)

if __name__ == "__main__":
    main()
