

#%%

def print_file_uppercase(filename):
    
    try:
        file = open(filename)
        
        for line in file:
            print(line.upper().strip())
    except Exception:
        print("file doesn't exist")


def parse_csv(filename, separator=","):
    
    try:
        file = open(filename)
        csv = []
        
        for line in file:
            csv.append(line.strip().split(separator))
            
        return csv
    except Exception:
        print("something went wrong")
    
csv = parse_csv("data.csv")





