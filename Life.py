import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

"""
rules:
1. If a cell is ON and has fewer than two neighbors that are ON, it .
turns OFF.
2. If a cell is ON and has either two or three neighbors that are ON, .
it remains ON.
3. If a cell is ON and has more than three neighbors that are ON, it .
turns OFF.
4. If a cell is OFF and has exactly three neighbors that are ON, it .
turns ON.
"""
# seeds = {
#     "diehard": [
#         [0, 0, 0, 0, 0, 0, 1, 0],
#         [1, 1, 0, 0, 0, 0, 0, 0],
#         [0, 1, 0, 0, 0, 1, 1, 1],
#     ],
#     "boat": [[1, 1, 0], [1, 0, 1], [0, 1, 0]],
#     "r_pentomino": [[0, 1, 1], [1, 1, 0], [0, 1, 0]],
#     "pentadecathlon": [
#         [1, 1, 1, 1, 1, 1, 1, 1],
#         [1, 0, 1, 1, 1, 1, 0, 1],
#         [1, 1, 1, 1, 1, 1, 1, 1],
#     ],
#     "beacon": [[1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 1, 1], [0, 0, 1, 1]],
#     "acorn": [[0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0], [1, 1, 0, 0, 1, 1, 1]],
#     "spaceship": [[0, 0, 1, 1, 0], [1, 1, 0, 1, 1], [1, 1, 1, 1, 0], [0, 1, 1, 0, 0]],
#     "block_switch_engine": [
#         [0, 0, 0, 0, 0, 0, 1, 0],
#         [0, 0, 0, 0, 1, 0, 1, 1],
#         [0, 0, 0, 0, 1, 0, 1, 0],
#         [0, 0, 0, 0, 1, 0, 0, 0],
#         [0, 0, 1, 0, 0, 0, 0, 0],
#         [1, 0, 1, 0, 0, 0, 0, 0],
#     ],
#     "infinite": [
#         [1, 1, 1, 0, 1],
#         [1, 0, 0, 0, 0],
#         [0, 0, 0, 1, 1],
#         [0, 1, 1, 0, 1],
#         [1, 0, 1, 0, 1],
#     ],
# }

# TODO: ADD SEEDS IN A DIC TO CHOOSE FROM
# TODO: CALL KEY AND PLACE VALUE IN GRID

def randomgrid(n):
 """returns a grid of NxN random values"""
 return np.random.choice([1,0], n*n, p=[0.2, 0.8]).reshape(n, n)


def diehard(i,j,grid):
    diehard = np.array([[0, 0, 0, 0, 0, 0, 1, 0],
                        [1, 1, 0, 0, 0, 0, 0, 0],
                        [0, 1, 0, 0, 0, 1, 1, 1]])

    grid[i:i + 3, j:j + 8] = diehard
    return grid


def glider(i,j, grid):

    """ a glider seed to add to the grid universe
    :param i is x position on grid
    :param j is y position on grid
    :param grid is the given universe
    :return grid with seed glider placed
    """

    glider = np.array([[0, 0, 1],
                       [1, 0, 1],
                       [0, 1, 1]])
    grid[i:i+3, j:j+3] = glider
    return grid


def update(frameNum, img, grid, n):
    """
    check's the number of neighbours from each cell
    and apply's the game's rules to it.
    :param grid is the given universe
    :param n is the size of the grid
    :param return  img frame
    """

    newgrid = grid.copy() # copy the grid for the next generation
    # count neighbours of each cell
    for i in range(n):
        for j in range(n):
            total = int((grid[i, (j - 1) % n] + grid[i, (j + 1) % n] +
                         grid[(i - 1) % n, j] + grid[(i + 1) % n, j] +
                         grid[(i - 1) % n, (j - 1) % n] + grid[(i - 1) % n, (j + 1) % n] +
                         grid[(i + 1) % n, (j - 1) % n] + grid[(i + 1) % n, (j + 1) % n]))


            if grid[i, j] == 1:
                if (total < 2) or (total > 3):
                    newgrid[i, j] = 0
            else:
                if total == 3:
                    newgrid[i, j] = 1
        # update data
    img.set_data(newgrid)
    grid[:] = newgrid[:]
    return img,


def main():
    # set parameters
    color = 'Blues'
    # size of the grid
    n = 50
    seed = 'diehard'
    if seed == 'glider':
        zeros = np.zeros((n, n))
        grid = glider(30, 30, zeros)
    elif seed == 'diehard':
        zeros = np.zeros((n, n))
        grid = diehard(30, 30, zeros)

    else:
        grid = randomgrid(n)

    # set up animation
    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest', cmap=color)
    ani = animation.FuncAnimation(fig, update, fargs=(img, grid, n,),
                                  frames=25,
                                  interval=100,
                                  save_count=50)

    plt.show()


main()







