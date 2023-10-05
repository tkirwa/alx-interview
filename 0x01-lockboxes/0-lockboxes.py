#!/usr/bin/python3
"""
Solution to lockboxes problem
"""


def canUnlockAll(boxes):
    """
    Determines whether a series of locked boxes can be opened
    based on keys that can be attained.

    Args:
    boxes (list of lists): A list of lists representing locked boxes
                           and their corresponding keys.

    Returns:
    bool: True if all boxes can be opened, False otherwise.
    """

    # Check if boxes is not a list or is empty, return False
    if not isinstance(boxes, list) or not boxes:
        return False

    # Initialize a list to keep track of opened boxes...
    #  the first box is open by default
    opened_boxes = [False] * len(boxes)
    opened_boxes[0] = True

    # Iterate through the boxes to check if we can open all of them
    for box_index, keys in enumerate(boxes):
        if opened_boxes[box_index]:
            # If the current box is already open, check its keys
            for key in keys:
                if 0 <= key < len(boxes) and not opened_boxes[key]:
                    # If the key corresponds to a valid box and...
                    #  that box is closed, open it
                    opened_boxes[key] = True

    # Check if all boxes are open
    return all(opened_boxes)
