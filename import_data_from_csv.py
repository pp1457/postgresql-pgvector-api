import csv

def read_csv_to_dict_list(file_path):
    with open(file_path, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        dict_list = [row for row in csv_reader]
    return dict_list

def main():
    file_path = input("File Path: ")
    chunks = read_csv_to_dict_list(file_path)

    for chunk in data:
        insert_chunk(chunk)

if __name__ == "__main__":
    main()
    
