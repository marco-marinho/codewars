import numpy as np


def get_valid(puzzle, row, col):
    valid = set(range(1, 10))
    valid -= set(puzzle[row, :].flatten())
    valid -= set(puzzle[:, col].flatten())
    x_offset = (row // 3) * 3
    y_offset = (col // 3) * 3
    valid -= set(puzzle[x_offset : x_offset + 3, y_offset : y_offset + 3].flatten())
    return valid


def gen_containers(ctype):
    valid_row = [ctype() for _ in range(9)]
    valid_col = [ctype() for _ in range(9)]
    valid_box = [[ctype() for __ in range(3)] for _ in range(3)]
    return valid_row, valid_col, valid_box


def group_valid(puzzle, unfilled_pos):
    valid_row, valid_col, valid_box = gen_containers(list)
    valid_map = {}
    for row, col in unfilled_pos:
        valid = get_valid(puzzle, row, col)
        valid_row[row].append((valid, (row, col)))
        valid_col[col].append((valid, (row, col)))
        valid_box[row // 3][col // 3].append((valid, (row, col)))
        valid_map[(row, col)] = valid
    return valid_row, valid_col, valid_box, valid_map


def remove_hidden_single(ivalid, valid_row, valid_col, valid_box):
    for i in range(1, 10):
        last_entry = None
        for entry, (row, col) in ivalid:
            if i in entry:
                if last_entry is not None:
                    last_entry = None
                    break
                last_entry = (entry, (row, col))
        if last_entry is not None:
            entry, (row, col) = last_entry
            entry.clear()
            entry.add(i)
            for other, _ in valid_row[row]:
                if other != entry:
                    other.discard(i)
            for other, _ in valid_col[col]:
                if other != entry:
                    other.discard(i)
            for other, _ in valid_box[row // 3][col // 3]:
                if other != entry:
                    other.discard(i)


def resolve_hidden_singles(valid_row, valid_col, valid_box):
    for row in valid_row:
        remove_hidden_single(row, valid_row, valid_col, valid_box)
    for col in valid_col:
        remove_hidden_single(col, valid_row, valid_col, valid_box)
    for i in range(3):
        for j in range(3):
            remove_hidden_single(valid_box[i][j], valid_row, valid_col, valid_box)


def remove_nacked_doubles(ivalid):
    doubles = [entry for entry in ivalid if len(entry) == 2]
    for i in range(len(doubles)):
        for j in range(i + 1, len(doubles)):
            if doubles[i] == doubles[j]:
                for entry in ivalid:
                    if entry != doubles[i] and entry != doubles[j]:
                        entry -= doubles[i]
                        entry -= doubles[j]


def resolve_nacked_doubled(valid_row, valid_col, valid_box):
    for row in valid_row:
        remove_nacked_doubles(row)
    for col in valid_col:
        remove_nacked_doubles(col)
    for i in range(3):
        for j in range(3):
            remove_nacked_doubles(valid_box[i][j])


def solver(puzzle, unfilled_pos, idx, valid, invalid):
    if idx >= len(unfilled_pos):
        return True
    x, y = unfilled_pos[idx]
    invalid_row, invalid_col, invalid_box = invalid
    for num in valid[(x, y)]:
        if num in invalid_row[x] | invalid_col[y] | invalid_box[x // 3][y // 3]:
            continue
        puzzle[x, y] = num
        invalid_row[x].add(num)
        invalid_col[y].add(num)
        invalid_box[x // 3][y // 3].add(num)
        if solver(puzzle, unfilled_pos, idx + 1, valid, invalid):
            return True
        puzzle[x, y] = 0
        invalid_row[x].discard(num)
        invalid_col[y].discard(num)
        invalid_box[x // 3][y // 3].discard(num)
    return False


def solve(puzzle):
    puzzle = np.array(puzzle)
    unfilled_pos = list(zip(*np.where(puzzle == 0)))
    valid_row, valid_col, valid_block, valid_map = group_valid(puzzle, unfilled_pos)
    resolve_hidden_singles(valid_row, valid_col, valid_block)
    resolve_nacked_doubled(valid_row, valid_col, valid_block)
    solver(puzzle, unfilled_pos, 0, valid_map, gen_containers(set))
    return puzzle.tolist()
