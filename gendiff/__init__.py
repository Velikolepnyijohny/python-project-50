import json
from collections import OrderedDict

def generate_diff(file_path1, file_path2):
    with open(file_path1, 'r') as f1, open(file_path2, 'r') as f2:
        data1 = json.load(f1)
        data2 = json.load(f2)
    
    all_keys = sorted(set(data1.keys()) | set(data2.keys()))
    
    diff_lines = []
    
    for key in all_keys:
        if key not in data2:
            diff_lines.append(f"  - {key}: {format_value(data1[key])}")
        elif key not in data1:
            diff_lines.append(f"  + {key}: {format_value(data2[key])}")
        elif data1[key] == data2[key]:
            diff_lines.append(f"    {key}: {format_value(data1[key])}")
        else:
            diff_lines.append(f"  - {key}: {format_value(data1[key])}")
            diff_lines.append(f"  + {key}: {format_value(data2[key])}")
    
    result = "{\n" + "\n".join(diff_lines) + "\n}"
    return result

def format_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    else:
        return str(value)
