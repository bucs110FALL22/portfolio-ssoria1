import json

def main():

    fptr = open("assets/ideas.json")
    data = fptr.read()
    fptr.close()
    print(data, type(data))
    
    jsondata = json.loads(data)
    print(jsondata, type(jsondata))
    print(jsondata["TimeStopper"])

    jsondata["TimeStopper"].append("flux capacitor")

    fptr = open("assets/ideas.json", "w")
    data = json.dumps(jsondata)
    fptr.write(data)
    fptr.close()

def print_file():
    fileref = open("assets/ideas.txt")
    for i, line in enumerate(fileref):
        print(f"line {i}: {line}")
    fileref.close()


def fileexamples():
    fileref = open("assets/ideas.txt")

    print_file()
    
    fileref = open("assets/ideas.txt", "w")
    
    fileref.write("\nThis is some additional data")
    fileref.close()
    print_file()
    fileref = open("assets/ideas.txt", "a")
    fileref.write("\nThis is some more additional data")
    fileref.close()
    print_file()

    
    
main()