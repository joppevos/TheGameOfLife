import c4d
import numpy as np


def execute():
    n = 10
    grid = np.random.choice([1, 0], n * n).reshape(10, 10)
    copygrid = grid.copy()
    y = 0
    for i in range(n):
        for j in range(n):
            if grid[i, j] == 1:
                vec = c4d.Vector(i * 230, j * 230, y)
                obj = c4d.BaseObject(c4d.Ocube)  # Create new cube
                obj.SetRelPos(c4d.Vector(vec))  # Set position of cube
                doc.InsertObject(obj)  # Insert object in document

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
            y = 250
            grid[:] = copygrid[:]


execute()





