#!/usr/bin/python3
"""
This function checks if all boxes can be unlocked given the keys in each box.
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.
    Args:
        boxes (list of list): A list of lists where each inner list contains
        keys to other boxes.
    Returns:
        bool: True if all boxes can be opened, else False.
    """
    if not boxes or len(boxes) == 0:
        return False

    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True
    stack = [0]

    while stack:
        current_box = stack.pop()

        for key in boxes[current_box]:
            if 0 <= key < n and not unlocked[key]:
                unlocked[key] = True
                stack.append(key)

    return all(unlocked)
