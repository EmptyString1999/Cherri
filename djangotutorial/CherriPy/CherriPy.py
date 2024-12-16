import codecs
def read_txt():
    out = []
    try:
        with codecs.open("CherriPy/CherriPy.html", "r", "utf-8") as f:
            lines = f.readlines()
            print(lines)
        out = lines
    except FileNotFoundError:
        out = "File not found"
    out_string = ""
    for index, line in enumerate(out):
        if "{{ cherry_block }}" in line:
            load_cherries = [
                """┌──────┐
│ col1 │
└──────┘"""
            ]
            for cherry in load_cherries:
                out_string += cherry
        else:
            out_string += line
    return out_string

def run():
    output_string = read_txt()
    print(output_string)
    return output_string