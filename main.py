import pygame
import random

# setup display
pygame.init()
width, height = 800, 500
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Rock, scissors, paper, lizard, Spock!")

# colors
white = (255, 255, 255)
black = (0, 0, 0)

# fonts
basic_font = pygame.font.SysFont("Helvetica", 25)

# choices
choices = ["rock", "paper", "scissors", "lizard", "Spock"]

# images
logo = pygame.image.load("logo.png")
logo_rect = logo.get_rect()
logo_rect.center = (width - 170, 150)

rock = pygame.image.load("rock.png")
rock_rect = rock.get_rect()
rock_rect.bottomleft = (150, 460)

scissors = pygame.image.load("scissors.png")
scissors_rect = scissors.get_rect()
scissors_rect.bottomleft = (250, 458)

paper = pygame.image.load("paper.png")
paper_rect = paper.get_rect()
paper_rect.bottomleft = (350, 460)

lizard = pygame.image.load("lizard.png")
lizard_rect = lizard.get_rect()
lizard_rect.bottomleft = (450, 460)

spock = pygame.image.load("spock.png")
spock_rect = spock.get_rect()
spock_rect.bottomleft = (550, 460)

# game variable
user_score = 0
computer_score = 0


# game
def game(user_choice):
    global user_score
    global computer_score

    computer_choice = random.choice(choices)
    if computer_choice == user_choice:
        result(computer_choice, "Draw!", "")
    elif user_choice == "paper":
        if computer_choice == "rock":
            user_score += 1
            result(computer_choice, "You won!", "Paper covers rock.")
        elif computer_choice == "scissors":
            computer_score += 1
            result(computer_choice, "You lost!", "Scissors cuts paper.")
        elif computer_choice == "lizard":
            computer_score += 1
            result(computer_choice, "You lost!", "Lizard eats paper.")
        elif computer_choice == "Spock":
            user_score += 1
            result(computer_choice, "You won!", "Paper disproves Spock.")
    elif user_choice == "rock":
        if computer_choice == "paper":
            computer_score += 1
            result(computer_choice, "You lost!", "Paper covers rock.")
        elif computer_choice == "scissors":
            user_score += 1
            result(computer_choice, "You won!", "Rock crushes scissors.")
        elif computer_choice == "lizard":
            user_score += 1
            result(computer_choice, "You won!", "Rock crushes lizard.")
        elif computer_choice == "Spock":
            computer_score += 1
            result(computer_choice, "You lost!", "Spock vaporizes rock.")
    elif user_choice == "scissors":
        if computer_choice == "paper":
            user_score += 1
            result(computer_choice, "You won!", "Scissors cuts paper.")
        elif computer_choice == "rock":
            computer_score += 1
            result(computer_choice, "You lost!", "Rock crushes scissors.")
        elif computer_choice == "lizard":
            user_score += 1
            result(computer_choice, "You won!", "Scissors decapitates lizard.")
        elif computer_choice == "Spock":
            computer_score += 1
            result(computer_choice, "You lost!", "Spock smashes scissors.")
    elif user_choice == "lizard":
        if computer_choice == "paper":
            user_score += 1
            result(computer_choice, "You won!", "Lizard eats paper.")
        elif computer_choice == "rock":
            computer_score += 1
            result(computer_choice, "You lost!", "Rock crushes lizard.")
        elif computer_choice == "scissors":
            computer_score += 1
            result(computer_choice, "You lost!", "Scissors decapitates lizard.")
        elif computer_choice == "Spock":
            user_score += 1
            result(computer_choice, "You won!", "Lizard poisons Spock.")
    elif user_choice == "Spock":
        if computer_choice == "paper":
            computer_score += 1
            result(computer_choice, "You lost!", "Paper disproves Spock.")
        elif computer_choice == "rock":
            user_score += 1
            result(computer_choice, "You won!", "Spock vaporizes rock.")
        elif computer_choice == "scissors":
            user_score += 1
            result(computer_choice, "You won!", "Spock smashes scissors.")
        elif computer_choice == "lizard":
            computer_score += 1
            result(computer_choice, "You lost!", "Lizard poisons Spock.")


def result(computer_choice, result_text, explain):
    window.fill(white)

    computer_choice_text = basic_font.render(f"Computer choice: {computer_choice}", True, black)
    computer_choice_text_rect = computer_choice_text.get_rect(center=(width / 2, 150))
    window.blit(computer_choice_text, computer_choice_text_rect)

    explain_text = basic_font.render(explain, True, black)
    explain_text_rect = explain_text.get_rect(center=(width/2, 250))
    window.blit(explain_text, explain_text_rect)

    result_text = basic_font.render(result_text, True, black)
    result_text_rect = result_text.get_rect(center=(width/2, 350))
    window.blit(result_text, result_text_rect)

    pygame.display.update()
    pygame.time.delay(3000)


# setup game loop
FPS = 60
clock = pygame.time.Clock()

# mainloop
run = True
while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if rock_rect.collidepoint(x, y):
                game("rock")
            if paper_rect.collidepoint(x, y):
                game("paper")
            if scissors_rect.collidepoint(x, y):
                game("scissors")
            if lizard_rect.collidepoint(x, y):
                game("lizard")
            if spock_rect.collidepoint(x, y):
                game("Spock")

    window.fill(white)

    text_user_score = basic_font.render(f"Player score: {user_score}", True, black)
    window.blit(text_user_score, (100, 70))

    text_computer_score = basic_font.render(f"Computer score: {computer_score}", True, black)
    window.blit(text_computer_score, (100, 130))

    window.blit(logo, logo_rect)

    text_your_choice = basic_font.render("Your choice: ", True, black)
    window.blit(text_your_choice, (100, 300))

    window.blit(rock, rock_rect)
    window.blit(paper, paper_rect)
    window.blit(scissors, scissors_rect)
    window.blit(lizard, lizard_rect)
    window.blit(spock, spock_rect)

    pygame.display.update()

pygame.quit()
