import turtle as t
import random as r

def draw_grid(block, grid):
    top = 250
    left = -150
    colors=['black','red','blue','orange','yellow','green','purple','white']
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            sc_x = left + (x*22)
            sc_y = top - (y*22)
            block.goto(sc_x,sc_y)
            block.color(colors[grid[y][x]])
            block.stamp()
    block.goto(left, top)



if __name__ == "__main__":
    sc = t.Screen()
    sc.bgcolor("black")
    sc.setup(width= 600, height= 700)
    grid =[[0]*12 for _ in range(24)]
    for i in range(24):
        grid[i].insert(0,7)
        grid[i].append(7)
    grid.append([7]*14)
    
    block=t.Turtle()
    block.penup()
    block.speed(0)
    block.shape("square")
    block.color("white")
    draw_grid(block, grid)


    for x in grid:
        print(x)

    sc.mainloop()