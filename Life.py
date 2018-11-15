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

# seed location's from different sources
seeds = {
    "diehard": [
        [0, 0, 0, 0, 0, 0, 1, 0],
        [1, 1, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 1, 1, 1],
    ],
    "boat": [[1, 1, 0], [1, 0, 1], [0, 1, 0]],
    "r_pentomino": [[0, 1, 1], [1, 1, 0], [0, 1, 0]],
    "pentadecathlon": [
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 1, 1, 1, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
    ],
    "beacon": [[1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 1, 1], [0, 0, 1, 1]],
    "acorn": [[0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0], [1, 1, 0, 0, 1, 1, 1]],
    "spaceship": [[0, 0, 1, 1, 0], [1, 1, 0, 1, 1], [1, 1, 1, 1, 0], [0, 1, 1, 0, 0]],
    "block_switch_engine": [
        [0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 0, 1, 1],
        [0, 0, 0, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 0, 0, 0, 0],
    ],
    "infinite": [
        [1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0],
        [0, 0, 0, 1, 1],
        [0, 1, 1, 0, 1],
        [1, 0, 1, 0, 1],
    ],
}

def randomgrid(n):
 """returns a grid of NxN random values"""
 return np.random.choice([1,0], n*n, p=[0.2, 0.8]).reshape(n, n)


def seed_placer(i, j, grid,seed):
    """ a glider seed to add to the grid universe
    :param i is x position on grid
    :param j is y position on grid
    :param grid is the given universe
    :param seed is type of seed array
    :return grid with seed glider placed
    """
    shape = np.shape(seed)

    grid[i:i + shape[0], j:j + shape[1]] = seed
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


def main(seeds):
    # set parameters
    color = 'Oranges'
    # size of the grid
    n = 30
    strseed = 'pentadecathlon'
    v = seeds.get(strseed)
    if v != None:
        grid = np.zeros((n, n))
        seed_placer(13, 11, grid, v)
    else:
        grid = randomgrid(n)

    # set up animation
    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest', cmap='Purples')
    ani = animation.FuncAnimation(fig, update, fargs=(img, grid, n,),
                                  frames=25,
                                  interval=500,
                                  save_count=50)
    plt.show()


main(seeds)







