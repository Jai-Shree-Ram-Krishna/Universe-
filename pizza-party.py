try:
    msg="Note:Only enter +ve integer, if you enter -ve value it will be converted into +ve only."
    persons=int(input("({})\nEnter the number of persons in the pizza party :".format(msg)))
    #Calculating for no.of 8 pieces of large pizza.
    num_of_large_pizza = persons // 8
    remaining_people_for_medium_pizza = persons % 8
    #Calculating for no.of 6 pieces of medium pizza.
    num_of_medium_pizza = remaining_people_for_medium_pizza // 6
    remaining_people_for_regular_pizza =  remaining_people_for_medium_pizza % 6
    #Calculating for no.of 4 pieces of regular pizza.
    num_of_regular_pizza = remaining_people_for_regular_pizza // 4
    remaining_people_for_small_pizza = remaining_people_for_regular_pizza % 4
    #Calculating for no.of 1 piece of small pizza.
    num_of_small_pizza = remaining_people_for_small_pizza // 1

    #Desired result.
    result = (num_of_large_pizza * 8) + (num_of_medium_pizza * 6) + (num_of_regular_pizza * 4) + (num_of_small_pizza * 1)
    print("\nIf there are",persons,"individuals.\n")
    print("1) We will have",num_of_large_pizza,"Large pizza.")
    print("2) We will have",num_of_medium_pizza,"Medium pizza.")
    print("3) We will have",num_of_regular_pizza,"Regular pizza.")
    print("4) We will have",num_of_small_pizza,"Small pizza.")
    print("\n({}*8)+({}*6)+({}*4)+({}*1)={}.".format(num_of_large_pizza,num_of_medium_pizza,num_of_regular_pizza,num_of_small_pizza,result))
except BaseException as error:
    print(error)
