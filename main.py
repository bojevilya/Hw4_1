def total_salary(path):
    of_the_whole = 0
    count = 0

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                surname, salary = line.strip().split(',')
                of_the_whole += int(salary)
                count += 1

        if count != 0:
            average = of_the_whole / count
        else:
            average = 0

        return of_the_whole, average

    except FileNotFoundError:
        print("File not find")
        return None, None
    except Exception as e:
        print(f"Error: {e}")
        return None, None

of_the_whole, average = total_salary("salary.txt")
if of_the_whole is not None and average is not None:
    print(f"The total amount of salary: {of_the_whole}, Average salary: {average}")
