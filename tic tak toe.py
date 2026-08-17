board = """
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

for turn in range(9):
    player = "X" if turn % 2 == 0 else "O"
    symbol = "❌" if player == "X" else "⭕"

    choice = input(
        board + f"\n{player} o'yinchi raqam tanlang: "
    )

    # Noto'g'ri raqam yoki band katakni tekshirish
    while choice not in "123456789" or choice in x_inputs + o_inputs:
        choice = input(
            f"Noto'g'ri tanlov! {player} o'yinchi boshqa raqam tanlang: "
        )

    # Jadvalga belgi qo'yish
    board = board.replace(choice, symbol)

    # Tanlangan raqamni saqlash
    if player == "X":
        x_inputs += choice
        current_inputs = x_inputs
    else:
        o_inputs += choice
        current_inputs = o_inputs

    # G'olibni tekshirish
    if any(all(number in current_inputs for number in win) for win in wins):
        print("\n" + board)
        print(f"\n🎉 {player} o'yinchi g'alaba qozondi!")
        break

else:
    print("\n" + board)
    print("\nDurrang!")