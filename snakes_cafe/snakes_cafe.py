print("""
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************

""")

menue=['Wings','Cookies','Spring','Rolls','Salmon','Steak','Meat Tornado','A Literal Garden','Ice Cream','Cake','Pie','Coffee','Tea','Unicorn Tears']
order_list=[]




while True:

    order=input("> ")

    if order=="quite":
        break
    
    elif order.capitalize() in menue:

        if order not in order_list:
            order_list.append(order)
            # print(">",f"{order}")
            print("** 1 order of",order,"have been added to your meal**\n")
            
        elif order in order_list:
            order_list.append(order)
            # print('>',f"{order}")
            print("**",order_list.count(order),"orders of",order,"have been added to your meal**\n")
            


    else:
        print('please choose from the menue\n')
         





