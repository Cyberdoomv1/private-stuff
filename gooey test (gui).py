#IMPORTS-----------------------------------------------------
from guizero import App,Text,TextBox,PushButton

#SUBROUTINES-------------------------------------------------
def add():
    num1 = enter_num1.value
    num2 = enter_num2.value
    answer = int(num1) + int(num2)
    display_answer.value = answer

#MAIN-------------------------------------------------------- 
#Widget code
addition_calc = App(title="Add two numbers")
instructions = Text(addition_calc, text = "Enter a number")
enter_num1 = TextBox(addition_calc)
instructions2 = Text(addition_calc, text = "Enter another number")
enter_num2 = TextBox(addition_calc)
display_answer = Text(addition_calc, text = "answer")
display_number = PushButton(addition_calc, command = add, text = "=")
# display the app
addition_calc.display()