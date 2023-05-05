# An example of how to define a function that prints 2D Lists
# First we create our 2D Lists

student_scores1 = [[12, 15, 19, 75, 100],
                  [50, 69, 80, 79, 99],
                  [25, 25, 25, 50, 75],
                  [100, 100, 100, 99, 0]]

student_scores2 = [[1, 4, 2, 1, 1],
                   [50, 50, 100, 29, 30],
                   [12, 10, 47, 84, 92],
                   [99, 90, 99, 98, 100]]

# Next we need to define our function

def print2d(x):  # We are creating a function called print2d()
    counter = 0  # We will add to this counter each time we loop

    for rows in x:  
        print(f'\nStudent {counter + 1}: ') # Each time we iterate through a row/inner list, we will print this. Student 1, Student 2 etc
        counter += 1  # Increases the counter by 1 each time the loop runs
        for col in rows:  # Iterates through each item within the inner lists
            print(col, end = '% ')  # Prints each grade. End is used to add the % and a blank space to the end of each grade
                                    # End also keeps the grades of each individual list on the same line
            
# Now we have defined our function, we can pass whichever 2D List we like through it
            
print2d(student_scores1)
print()
print2d(student_scores2)


        




    