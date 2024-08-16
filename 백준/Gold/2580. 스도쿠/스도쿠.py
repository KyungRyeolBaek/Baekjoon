import sys

def find_empty(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return (i, j)
    return None

def is_valid(grid, num, pos):
    row, col = pos
    
    # Check the row
    for j in range(9):
        if grid[row][j] == num:
            return False

    # Check the column
    for i in range(9):
        if grid[i][col] == num:
            return False

    # Check the box
    box_x = col // 3
    box_y = row // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if grid[i][j] == num:
                return False

    return True

def solve_sudoku(grid):
    find = find_empty(grid)
    if not find:
        return True  # 모든 빈칸을 채운 경우

    row, col = find

    for num in range(1, 10):
        if is_valid(grid, num, (row, col)):
            grid[row][col] = num

            if solve_sudoku(grid):
                return True

            grid[row][col] = 0

    return False

def main():
    grid = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
    
    solve_sudoku(grid)
    
    for row in grid:
        print(" ".join(map(str, row)))

if __name__ == "__main__":
    main()
