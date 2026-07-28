jadval = """ ____ ____ ____
| 1 | 2 | 3 |
 ---- ---- ----
| 4 | 5 | 6 | 
 ---- ---- ----
| 7 | 8 | 9 |
 ---- ---- ----
"""

win = ["123","456","789","159","147","357","369","258"]
x_inputs = ""
o_inputs = ""

qoida = "123456789"

winner = False

for i in range(1,10):
    if winner:
        break

    if i % 2 != 0:
        x_input = input(jadval + "X o'yinchi raqam tanlasin: ")
        while x_input not in qoida or x_input in o_inputs or x_input in x_inputs:
            x_input = input("X o'yinchi qayta raqam tanlasin: ")

        jadval = jadval.replace(x_input, "❌")
        x_inputs += x_input
        for x in win:
            if x[0] in x_inputs and x[1] in x_inputs and x[2] in x_inputs:
                print(jadval + "X o'yinchi galaba qozondi !!!")
                winner = True
    else:
        o_input = input(jadval + "0 o'yinchi raqam tanlasin: ")
        while o_input not in qoida or o_input in x_inputs or o_input in o_inputs:
            o_input = input("0 o'yinchi qayta raqam tanlasin: ")

        jadval = jadval.replace(o_input, "⭕")
        o_inputs += o_input
        for o in win:
            if o[0] in o_inputs and o[1] in o_inputs and o[2] in o_inputs:
                print(jadval + "0 o'yinchi galaba qozondi !!!")
                winner = True
if not winner:
    print(jadval + "Durrang")
