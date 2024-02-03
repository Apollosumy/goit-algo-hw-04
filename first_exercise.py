import re

def total_salary(path):
    try:    
        with open(path, 'r') as file:
            lines = file.read()
            numbers = re.findall(r'\b\d+\b', lines)
            int_numbers = []
            for i in numbers:
                int_numbers.append(int(i))
            total_amount = sum(int_numbers)
            average_salary = int(sum(int_numbers) / len(int_numbers))
            final_tuple = (total_amount, average_salary)
            
            print(final_tuple)
    except FileNotFoundError:
        print(f"File not found: {path}")
        return None
    except ZeroDivisionError:
        print(f"Error: Non-numeric value found in the file.")
        return None

    

path = "C:\\Users\\sumyu\\Documents\\My repo\\goit-algo-hw-04\\first_exercise.txt"
total_salary(path)   
