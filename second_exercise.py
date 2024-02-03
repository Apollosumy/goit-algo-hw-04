
def get_cats_info(path):
    try:    
        list_dicts = []
        with open(path, 'r') as file:
            lines = file.read().split("\n")
        for line in lines:
            parts = line.split(",")
            record = {
                    'id': parts[0],
                    'name': parts[1],
                    'age': int(parts[2])
                }
            list_dicts.append(record)
        print(list_dicts)
    except FileNotFoundError:
        print(f"File not found: {path}")
        return None
    except ValueError:
        print(f"The file contains incorrect data. Check the file: {path}")
        return None
    
  

path = "C:\\Users\\sumyu\\Documents\\My repo\\goit-algo-hw-04\\second_exercise.txt"
get_cats_info(path)
