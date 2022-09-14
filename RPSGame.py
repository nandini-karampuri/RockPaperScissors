import random


def play(user):
    computer = random.choice(['R', 'P', 'S'])
    if user == computer:
        print(f'It\'s a tie ! you:{user} and computer:{computer}')
        return
    if (user == 'R' and computer == 'S') or (user == 'P' and computer == 'R') or (user == 'S' and computer == 'P'):
        print(f'You Won! you:{user} and computer:{computer}')
        return
    print(f'You Lost! computer:{computer} and you:{user}')
    return


if __name__ == '__main__':
    while True:
        user = input(
            "What's your choice? 'R' for Rock, 'S' for Scissors and 'P' for Paper: ").upper()
        if user in ['R', 'P', 'S']:
            play(user)
            break
        else:
            print('Please select from the choice')
