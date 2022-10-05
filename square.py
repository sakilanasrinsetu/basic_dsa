def square_number_list(number_list):
    square_value_list = []
    
    for num in number_list:
        square_value_list.append(num*num)
    
    print("Original Value list = " ,number_list, "\nSquare Value list = " ,square_value_list)

# This is a BigO or O(n) Notation

number_list = [2,5,6,10,61]
square_number_list(number_list)

