import random
from Assets import blackjack

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    if len(cards) == 2 and sum(cards) == 21:
        return 0
    elif sum(cards) > 21 and len(cards) == 2:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(u_scores,c_scores):
    if u_scores == c_scores:
        return "It's a draw!"
    elif c_scores == 0:
        return "User loses! Computer has a black jack!"
    elif u_scores == 0:
        return "You win using a black jack!"
    elif u_scores > 21:
        return "You went over! Computer wins!"
    elif c_scores > 21:
        return "You win! Computer went over!"
    elif u_scores > c_scores:
        return "You win!"
    else:
        return "Computer wins!"

def game():
    print(blackjack.logo)
    user_cards = [deal_card() for _ in range(2)]
    computer_cards = [deal_card() for _ in range(2)]
    is_game_over = False
    computer_score = -1
    user_score = -1

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards are: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0:
            is_game_over = True
        elif computer_score == 0:
            is_game_over = True
        else:
            draw_another = input("Type 'y' to draw another card or 'n' to pass: ").lower().strip()
            if draw_another == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score,computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n':").lower().strip() == "y":
    print("\n" * 30)
    game()