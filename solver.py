# You may need this if you really want to use a recursive solution!
# It raises the cap on how many recursions can happen. Use this at your own risk!

# sys.setrecursionlimit(100000)
from game import Game
import sys


filename = sys.argv[1]
mode = sys.argv[2]


def solve(mode):
    start = Game(filename)
    start.start()
    # Parent game state (where player is at X)
    queue = [start]

    solution = []

    # We want to limit the 'e' move count
    e_count = 0

    while True:
        if len(queue) == 0:
            break

        # If it it BFS or DFS
        if mode == 'BFS':
            node = queue[0]
            # Remove the first element from the queue after taking it
            queue = queue[1:]
        else:
            node = queue[-1]
            # Remove the last element from the queue after taking it
            queue.pop()

        # If node is at finished state and won, then print solution
        if node.finished and not(node.lost):
            solution = node.moves_made
            break

        moves = ['e','w','a','s','d']
        # Loop through the moves and create children objects
        for m in moves:
            new_child = Game(filename)

            # Bring this child game state to the same as parent
            for i in node.moves_made:
                new_child.game_move(i)

            # Now make the next moves
            new_child.game_move(m)

            # If new child picked water bucket, then make this attribute True
            if new_child.player.num_water_buckets > node.player.num_water_buckets:
                new_child.picked_bucket = True

            # Only allow e to be a move if the player is on tp pad
            if node.on_tp_pad and m == 'e':
                if e_count < 3:
                    queue.append(new_child)
                    e_count += 1
                    continue
                else:
                    continue

            # If a canceling move was made without achieving anything
            # Eg w, s without getting water bucket then continue to next iteration
            complimentary_moves = [['w','s'],['s','w'],['a','d'],['d','a']]
            if len(new_child.moves_made) >= 2:
                # If the child backtracked from the move before
                if [new_child.moves_made[-1],new_child.moves_made[-2]] in complimentary_moves:
                    # Now the parent node (previous child node) picked up a picked_bucket
                    # So it is fine to back track, else we just go to next iteration
                    if not(node.picked_bucket) or not(node.on_tp_pad):
                        continue

            # If this new move did not achieve anything (eg hitting a wall),
            # Then we do not need to append it to the queue
            if (new_child.player.col != node.player.col or
            new_child.player.row != node.player.row):
                if not(new_child.lost):
                    queue.append(new_child)


    return solution


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print('Usage: python3 solver.py <filename> <mode>')
        exit()

    if mode == 'BFS' or mode == 'DFS':
        solution_found = solve(mode)
        if solution_found:
            print('Path has {} moves.'.format(len(solution_found)))
            print('Path: ' + ', '.join(solution_found))
        else:
            print("There is no possible path.")
    else:
        print('Usage: python3 solver.py <filename> <mode>')
        exit()
