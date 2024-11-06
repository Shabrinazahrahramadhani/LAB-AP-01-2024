import random
#fungsi untuk menarik kartu
def draw_card():
    return random.randint(1, 11)
#fungsi untuk menampilkan hasil permainan
def check_winner(player_sum, dealer_sum):
    if player_sum > 21:
        return "anda kalah! nilai kartu anda melebihi 21"
    elif dealer_sum > 21:
        return "dealer melebihi 21, anda menang!"
    elif player_sum > dealer_sum:
        return "anda menang!"
    elif player_sum < dealer_sum:
        return "dealer menang!"
    else:
        return "seri!"
#fungsi untuk menjalankan permainan blackjack
def blackjack():
    print("welcome to blackjack!")
#pemain dan dealer mulai dengan dua kartu
