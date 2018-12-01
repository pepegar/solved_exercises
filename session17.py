

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


def copy_file(origin, destination):
    
    try:
        origin_file = open(origin)
        destination_file = open(destination, "w")
        
        for line in origin_file:
            destination_file.write(line)
            
        destination_file.close()
        
    except Exception:
        print("something went wrong")    
    
    
    
    
    
    
    
    
    
    
    
    

