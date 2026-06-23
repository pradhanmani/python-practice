
try:
    f = open('corrupt_file.txt')
    # if f.name == 'corrupt_file.txt':
    #     raise Exception
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print('ERROR!')
    
else:           ####else only runs if we dont throw an exception
    print(f.read())
    f.close()
    
finally:     #####finally runs no matter what happens whether the code is succesful or whether we throw  an exception
    print('Executing Finally.....')