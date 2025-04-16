import random
from Assets import game_data, project_logos
score = 0

def get_person():
    return random.choice(game_data.data)

def compare(a,b):
    print(f"Compare A: {a["name"]}, a {a["description"]}, from {a["country"]}")
    print(project_logos.vs)
    print(f"Against B: {b["name"]}, a {b["description"]}, from {b["country"]}")
    if a["follower_count"] > b["follower_count"]:
        return a
    elif b["follower_count"] > a["follower_count"]:
        return b
    else:
        print("They have the same number of followers!")
        return a

def check_answer(has_more_followers, guess):
    return has_more_followers == guess

def select_option(guess,people):
    if guess == 'a':
        return people[0]
    else:
        return people[1]

is_game_over = False
person_a = get_person()

while not is_game_over:
    print(project_logos.higherlower)

    person_b = get_person()

    while person_a == person_b:
        person_b = get_person()

    people_to_compare = [person_a,person_b]

    has_more_followers = compare(person_a, person_b)

    guess = input("Who has more followers? Type 'a' or 'b': ").lower().strip()

    if check_answer(has_more_followers,select_option(guess,people_to_compare)):

        person_a = person_b
        score += 1
        print(f"You got it right! Current score:{score}")

    else:
        is_game_over = True
        print("Game over")

