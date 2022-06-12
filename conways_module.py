import numpy as np
import time

class Frame:
    def __init__(self, x_dim, y_dim, num_steps, fill):
        '''Initialized a frame object'''
        self.x_dim = x_dim
        self.y_dim = y_dim
        self.current_step = 0
        self.grid = np.asarray([[0]*self.x_dim]*self.y_dim)
        self.num_steps = num_steps
        self.fill = fill

        for j in range(len(self.grid)):
            for i in range(self.grid.shape[1]):
                if np.random.random() < self.fill:
                    self.grid[j][i] = 1

    def updateFrame(self):
        '''Updates a frame object'''
        new_grid = np.asarray([[0]*self.x_dim]*self.y_dim)
        for j, y in enumerate(self.grid):
            for i, x in enumerate(y):
                count = np.sum(self.grid[j-1:j+2, i-1:i+2]) - self.grid[j][i]
                if (count == 3 or count == 2) and self.grid[j][i] == 1: # rule 1
                    new_grid[j][i] = 1
                elif count == 3 and self.grid[j][i] == 0: # rule 2
                    new_grid[j][i] = 1

        self.grid = new_grid
        self.current_step += 1

    def show(self):
        print('----------------------------------------------------------------')
        for j in self.grid:
            for i in j:
                if i == 1:
                    print('@' + '   ', end = '')
                else:
                    print('.' + '   ', end = '')
            print('\n')
        print('-----------------------------------------------------------------')

    def runSimulation(self):
        frame = Frame(self.x_dim, self.y_dim, self.num_steps, self.fill)
        while frame.current_step < self.num_steps:
            frame.show()
            frame.updateFrame()
            time.sleep(.1)

fs = Frame(35, 19, 10000, .50)
fs.runSimulation()