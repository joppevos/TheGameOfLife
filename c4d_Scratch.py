import c4d
import numpy as np
from c4d.modules.thinkingparticles import TP_MasterSystem


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
# TODO: ADD RANDOM EFFECTS, COLOR, SIZE?
# TODO: MAKE EASY TO ACCES PARAMETERS
# TODO: MAKE A THIRD DIMENTION WITH DIFFERENT RULES


class Particle:
    def __init__(self):
        self.tp = doc.GetParticleSystem()

    def creatept(self):
        self.p = self.tp.AllocParticle()
        return self.p
    def move(self, vec):
        self.tp.SetPosition(self.p, vec)


def generate(particle, grid, n, y):
    """
    Calculates 1 generation
    :param particle: particle instance from class Particle
    :param grid: the grid from the generation before
    :param n: size of the grid in n
    :return: new generation grid
    """
    copygrid = grid.copy()
    for i in range(n):
        for j in range(n):
            p = particle.creatept()
            basetime = c4d.BaseTime(z=3, n=False)
            particle.tp.SetLife(p, basetime)
            total = int((grid[i, (j - 1) % n] + grid[i, (j + 1) % n] +
                         grid[(i - 1) % n, j] + grid[(i + 1) % n, j] +
                         grid[(i - 1) % n, (j - 1) % n] + grid[(i - 1) % n, (j + 1) % n] +
                         grid[(i + 1) % n, (j - 1) % n] + grid[(i + 1) % n, (j + 1) % n]))

            if grid[i, j] == 1:
                if (total < 2) or (total > 3):
                    copygrid[i, j] = 0

            else:
                if total == 3:
                    copygrid[i, j] = 1

            if grid[i, j] == 1:

                vec = c4d.Vector(i * 230, j * 230, y)
                particle.move(vec)

    grid[:] = copygrid[:]

    return grid


class Render:
    n = 50
    firstgen = True
    y = 200

    def __init__(self):
        self.grid = randomgrid(self.n)
        self.seed = np.zeros((self.n, self.n))
        self.tp = doc.GetParticleSystem()

    def remove(self):
        self.tp.FreeAllParticles()

    def move(self, vec):
        self.tp.SetPosition(self.p, vec)

    def update(self, seedsdict):
        self.tp.FreeAllParticles()
        p = Particle()
        if self.firstgen:
            strseed = 'block_switch_engine'
            v = seedsdict.get(strseed)
            newgrid = generate(p, seed_placer(20, 20, self.seed, v), self.n, self.y)
            print(newgrid)
        else:
            newgrid = generate(p, self.grid, self.n, self.y)
        self.grid = newgrid
        self.y += 0
        if self.firstgen: # removes the first generation
            self.tp.FreeAllParticles()
            self.firstgen = False


def randomgrid(n):
    """returns a grid of NxN random values"""
    return np.random.choice([1, 0], n * n, p=[0.2, 0.8]).reshape(n, n)


def seed_placer(i, j, grid, seed):
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


instance = Render()


def main():

    if frame % 2 == 0:
        instance.update(seeds)