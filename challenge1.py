def solution(A):
    total_bricks = sum(A)
    if total_bricks % 10 != 0:
        return -1

    boxes_needed = total_bricks // 10
    moves = 0
    current_box = 1
    for bricks in A:
        if current_box <= bricks:
            moves += bricks - current_box + 1
            current_box = 1
        else:
            current_box = bricks + 1

    return moves




# Instance attribute are only called when an object has been created.
# class attribute can only be called by the class itself but not an instance or an object.