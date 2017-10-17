#Created on: October 2017
#Created by: Nicholas Brean
#this program asks what kind of pizza you want then ask how many toppings and calculates the cost then puts the cost into a real dollar format


import ui

#global variables
Large_pizza = 6.00
Extra_Large = 10.00
Topping1 = 1.00
Topping2 = 1.25
Topping3 = 2.50
Topping4 = 3.75
HST = 1.13



def pizza_order(sender):
	#the first half of the pizza's are large the second half being extra large
	#getting the input for a pizza size
    if int(view['large_extra_large_textfield'].text) == 1:
    	#getting input for amount of toppings
        if int(view['choose_amount_toppings'].text) == 1:
           SubTotal = Large_pizza + Topping1
           HST_printed_out = SubTotal * HST - SubTotal
           FinalPrice = (SubTotal * HST) 
           view['sub_total_label'].text = 'The Sub Total is: ${:,.2F}'.format(SubTotal)
           view['final_total_label'].text = 'The Final Price is: ${:,.2F}'.format(FinalPrice)
           view['HST_label'].text = 'The HST  is: ${:,.2F}'.format(HST_printed_out)

    if int(view['large_extra_large_textfield'].text) == 1:
        if int(view['choose_amount_toppings'].text) == 2:
           SubTotal = Large_pizza + Topping2
           HST_printed_out = SubTotal * HST - SubTotal
           FinalPrice = (SubTotal * HST) 
           view['sub_total_label'].text = 'The Sub Total is: ${:,.2F}'.format(SubTotal)
           view['final_total_label'].text = 'The Final Price is: ${:,.2F}'.format(FinalPrice)
           view['HST_label'].text = 'The HST  is: ${:,.2F}'.format(HST_printed_out)

    if int(view['large_extra_large_textfield'].text) == 1:
        if int(view['choose_amount_toppings'].text) == 3:
           SubTotal = Large_pizza + Topping3
           HST_printed_out = SubTotal * HST - SubTotal
           FinalPrice = (SubTotal * HST) 
           view['sub_total_label'].text = 'The Sub Total is: ${:,.2F}'.format(SubTotal)
           view['final_total_label'].text = 'The Final Price is: ${:,.2F}'.format(FinalPrice)
           view['HST_label'].text = 'The HST  is: ${:,.2F}'.format(HST_printed_out)

    if int(view['large_extra_large_textfield'].text) == 1:
        if int(view['choose_amount_toppings'].text) == 4:
           SubTotal = Large_pizza + Topping4
           HST_printed_out = SubTotal * HST - SubTotal
           FinalPrice = (SubTotal * HST) 
           view['sub_total_label'].text = 'The Sub Total is: ${:,.2F}'.format(SubTotal)
           view['final_total_label'].text = 'The Final Price is: ${:,.2F}'.format(FinalPrice)
           view['HST_label'].text = 'The HST  is: ${:,.2F}'.format(HST_printed_out)

# this is for a extra large pizza amd either 1 2 3 or 4 toppings
    if int(view['large_extra_large_textfield'].text) == 2:
        if int(view['choose_amount_toppings'].text) == 1:
           SubTotal = Extra_Large + Topping1
           HST_printed_out = SubTotal * HST - SubTotal
           FinalPrice = (SubTotal * HST) 
           view['sub_total_label'].text = 'The Sub Total is: ${:,.2F}'.format(SubTotal)
           view['final_total_label'].text = 'The Final Price is: ${:,.2F}'.format(FinalPrice)
           view['HST_label'].text = 'The HST  is: ${:,.2F}'.format(HST_printed_out)

    if int(view['large_extra_large_textfield'].text) == 2:
        if int(view['choose_amount_toppings'].text) == 2:
           SubTotal = Extra_Large + Topping2
           HST_printed_out = SubTotal * HST - SubTotal
           FinalPrice = (SubTotal * HST) 
           view['sub_total_label'].text = 'The Sub Total is: ${:,.2F}'.format(SubTotal)
           view['final_total_label'].text = 'The Final Price is: ${:,.2F}'.format(FinalPrice)
           view['HST_label'].text = 'The HST  is: ${:,.2F}'.format(HST_printed_out)

    if int(view['large_extra_large_textfield'].text) == 2:
        if int(view['choose_amount_toppings'].text) == 3:
           SubTotal = Extra_Large + Topping3
           HST_printed_out = SubTotal * HST - SubTotal
           FinalPrice = (SubTotal * HST) 
           view['sub_total_label'].text = 'The Sub Total is: ${:,.2F}'.format(SubTotal)
           view['final_total_label'].text = 'The Final Price is: ${:,.2F}'.format(FinalPrice)
           view['HST_label'].text = 'The HST  is: ${:,.2F}'.format(HST_printed_out)

    if int(view['large_extra_large_textfield'].text) == 2:
        if int(view['choose_amount_toppings'].text) == 4:
           SubTotal = Extra_Large + Topping4
           HST_printed_out = SubTotal * HST - SubTotal
           FinalPrice = (SubTotal * HST) 
           view['sub_total_label'].text = 'The Sub Total is: ${:,.2F}'.format(SubTotal)
           view['final_total_label'].text = 'The Final Price is: ${:,.2F}'.format(FinalPrice)
           view['HST_label'].text = 'The HST  is: ${:,.2F}'.format(HST_printed_out)




view = ui.load_view()
view.present('sheet')
