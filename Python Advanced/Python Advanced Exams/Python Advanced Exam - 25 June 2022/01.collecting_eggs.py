from collections import deque

eggs = deque([int(x) for x in input().split(", ")])
paper = [int(x) for x in input().split(", ")]
box_size = 50
boxes_filled = 0

while eggs and paper:
    egg = eggs.popleft()
    wrapper = paper.pop()

    if egg <= 0:
        paper.append(wrapper)
        continue

    if egg == 13:
        paper.append(wrapper)
        paper[0], paper[-1] = paper[-1], paper[0]
        continue

    if egg + wrapper <= box_size:
        boxes_filled += 1

if boxes_filled > 0:
    print(f"Great! You filled {boxes_filled} boxes.")
else:
    print(f"Sorry! You couldn't fill any boxes!")
if eggs:
    print(f"Eggs left: {', '.join(str(x) for x in eggs)}")
if paper:
    print(f"Pieces of paper left: {', '.join(str(x) for x in paper)}")
