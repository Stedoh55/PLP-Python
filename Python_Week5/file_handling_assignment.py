file = open('my_file.txt', 'w')

# Writing multiple lines at a time
file.writelines(['\nMy Python Assignment', '\nFor the week 5', '\nIs Cool and Awesome', '\nI rate this Topic', '\n9\n'])

# closing the file
file.close()

# Appending the file
with open('my_file.txt', 'a') as f:
    f.write('Hello,PLP Learners\n')
    f.write('Python is very enjoyable\n')
    f.write('I have liked if already!')

# Error handling
try:
    unknown = open('fix.txt', 'r')
except FileNotFoundError:
    print('The file could not be found!')

