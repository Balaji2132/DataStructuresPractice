from collections import deque
import random

class SnakeAndLadder:
    def __init__(self, snakes, ladders, board_size=100):
        self.snakes = snakes
        self.ladders = ladders
        self.board_size = board_size
        self.queue = deque()

    def play(self, players):
        # Initialize player positions
        player_positions = {player: 0 for player in players}
        self.queue.extend(players)

        while True:
            # Dequeue the current player
            current_player = self.queue.popleft()

            # Roll the dice
            dice_roll = random.randint(1, 6)
            print(f"{current_player} rolled a {dice_roll}")

            # Update the player's position
            new_position = player_positions[current_player] + dice_roll
            if new_position > self.board_size:
                # Skip the turn if the new position exceeds the board size
                print(f"{current_player} stays at {player_positions[current_player]}")
            else:
                # Check for snakes or ladders
                if new_position in self.snakes:
                    print(f"Oops! {current_player} hit a snake at {new_position}. Going down to {self.snakes[new_position]}")
                    new_position = self.snakes[new_position]
                elif new_position in self.ladders:
                    print(f"Yay! {current_player} climbed a ladder at {new_position}. Going up to {self.ladders[new_position]}")
                    new_position = self.ladders[new_position]

                # Update the player's position
                player_positions[current_player] = new_position
                print(f"{current_player} is now at position {new_position}")

            # Check if the player has won
            if new_position == self.board_size:
                print(f"Congratulations! {current_player} wins!")
                break

            # Requeue the player for the next turn
            self.queue.append(current_player)

# Snakes and ladders configuration
snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}

# Initialize the game
game = SnakeAndLadder(snakes, ladders)

# Start the game with players
players = ["Player 1", "Player 2"]
game.play(players)
