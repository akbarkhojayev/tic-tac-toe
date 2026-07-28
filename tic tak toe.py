jadval = """
 -------------
|  1 |  2 |  3 |
 -------------
|  4 |  5 |  6 |
 -------------
|  7 |  8 |  9 |
 -------------
"""

wins = [
    "123", "456", "789",
    "147", "258", "369",
    "159", "357"
]

x_inputs = ""
o_inputs = ""
numbers = "123456789"
winner = False

for turn in range(1, 10):
    player = "X" if turn % 2 else "O"
    symbol = "❌" if player == "X" else "⭕"
    inputs = x_inputs if player == "X" else o_inputs

    choice = input(jadval + f"{player} o'yinchi raqam tanlasin: ")

    while (
        choice not in numbers
        or choice in x_inputs
        or choice in o_inputs
    ):
        choice = input(f"{player} o'yinchi qayta raqam tanlasin: ")

    jadval = jadval.replace(choice, symbol)

    if player == "X":
        x_inputs += choice
        inputs = x_inputs
    else:
        o_inputs += choice
        inputs = o_inputs

    for win in wins:
        if all(i in inputs for i in win):
            print(jadval)
            print(f"{player} o'yinchi g'alaba qozondi!")
            winner = True
            break

    if winner:
        break

if not winner:
    print(jadval)
    print("Durrang !!!")
