import random

numboxes = 100
trials = 100
success = 0

for t in range(trials):
    # Setup
    boxes = []
    slips = []
    for b in range(numboxes):
        boxes.append(b)
        slips.append(b)
    random.shuffle(slips)
    # Experiment
    for p in range(numboxes):
        curbox = p
        tries = 0
        while slips[curbox] != p and tries < numboxes/2:
            curbox = slips[curbox]
            tries += 1
        if tries >= numboxes/2:
            break
        elif p == numboxes - 1:
            success += 1

print(success/trials)