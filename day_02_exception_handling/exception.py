

try: 
    # f = open('day_02_exception_handling/test.txt')
    # var = bad_var

    f = open('currupt_file.txt')
    if f.name == 'currupt_file.txt':
        raise Exception
    
except FileNotFoundError as e:
    print(e)
except Exception as e:
    # print(e)
    print('Error!')
else:
    print(f.read())
    f.close()
finally:
    print("Executing Finally....")