#!/usr/bin/python3

def canUnlockAll(boxes):
    if not boxes:
        return False

    num_boxes = len(boxes)
    unlocked = [False] * num_boxes
    unlocked[0] = True  # The first box is always unlocked
    stack = [0]  # Start with the first box

    while stack:
        current_box = stack.pop()  # Pop the last box from the stack

        # Iterate through the keys in the current box
        for key in boxes[current_box]:
            # Check if the key is valid (within bounds) and...
            #  the corresponding box is not yet unlocked
            if 0 <= key < num_boxes and not unlocked[key]:
                # Mark the box as unlocked
                unlocked[key] = True
                # Add the box to the stack for further exploration
                stack.append(key)

    # Return True if all boxes are unlocked, else return False
    return all(unlocked)


# Example usage:
# if __name__ == "__main__":
#     boxes = [[1], [2], [3], [4], []]
#     print(canUnlockAll(boxes))  # True

#     boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
#     print(canUnlockAll(boxes))  # True

#     boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
#     print(canUnlockAll(boxes))  # False
