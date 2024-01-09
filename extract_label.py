import pandas as pd
import os
import re

df = pd.read_csv("project-54-at-2023-12-20-08-28-2f8b7c8d.csv")
saved_columns = df[['img', 'kp-1']]

label_path = 'labels'
pattern = '"'
os.makedirs(label_path, exist_ok=True)

def find_strings_between_chars(full_string, start_char, end_char):
    pattern = re.compile(re.escape(start_char) + "(.*?)" + re.escape(end_char))
    matches = re.findall(pattern, full_string)
    return matches

start_char = "{"
end_char = "}"

def read_extract_labels_from_folder(saved_columns):
    column_values = saved_columns['img'].tolist()

    for i in range(len(column_values)):
        column_values[i] = column_values[i][-28:len(column_values[i])-4]

    for a in range(len(column_values)):
        result = find_strings_between_chars(saved_columns['kp-1'][a], start_char, end_char)
        with open(os.path.join(label_path, column_values[a]+".txt"), 'w') as file:
            for res in result:
                string = ""
                for i in range(len(res)):
                    if res[i] == pattern:
                        if(res[i+1] == 'x'):
                            comma_index = res.find(',', i)
                            substring = res[i+4:comma_index]
                            string = string + " " + substring
                        elif(res[i+1] == 'y'):
                            comma_index = res.find(',', i)
                            substring = res[i+4:comma_index]
                            string = string + " " + substring
                        elif(res[i-1] == '['):
                            if res[i+1] == 'r':
                                string = "0 " + string
                            elif res[i+1] == 'f':
                                string = "1 " + string
                            elif res[i+1] == 'b':
                                string = "2 " + string
                string = string + "\n"
                file.write(string)
read_extract_labels_from_folder(saved_columns)