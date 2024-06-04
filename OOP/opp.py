#object oriented programming
import nashpy as nash

# Define the payoff matrices
P1 = [[(1, 1), (1, 1), (5, 0)],
      [(0, 1), (4, 6), (6, 0)],
      [(2, 1), (3, 5), (2, 8)]]

P2 = [[(10, 4), (5, 3), (3, 2)],
      [(0, 1), (4, 6), (6, 0)],
      [(2, 1), (3, 5), (2, 8)]]

# Create the game
game = nash.Game(P1, P2)

# Find Nash Equilibria
equilibria = list(game.support_enumeration())

# Print the equilibria
for eq in equilibria:
    print("Nash Equilibrium:")
    print("Player 1 strategy:", eq[0])
    print("Player 2 strategy:", eq[1])
