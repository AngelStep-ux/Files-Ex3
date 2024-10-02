import os

file_names = ['1.txt', '2.txt', '3.txt']  

def merge_files(file_names, output_file):
    files_content = {}

    for file_name in file_names:
        with open(file_name, 'r', encoding='utf-8') as f:
            content = f.readlines()
            files_content[file_name] = content

    sorted_files = sorted(files_content.items(), key=lambda item: len(item[1]))

    with open(output_file, 'w', encoding='utf-8') as out_file:
        for file_name, content in sorted_files:
            out_file.write(f"{file_name}\n")
            out_file.write(f"{len(content)}\n")
            out_file.writelines(content)

output_file_name = 'merged_output.txt'
merge_files(file_names, output_file_name)

print(f'Файлы успешно объединены в {output_file_name}.')