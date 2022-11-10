"""
Team Three Driver.
"""
from rose.common import obstacles, actions  # NOQA

driver_name = "TEAM THREE"


def drive(world):
    x = world.car.x
    y = world.car.y
    up = rec(True, 0, world, x, y)
    right = rec(False, 0, world, x, y)
    left = rec(False, 0, world, x, y)
    if up >= right and up >= left:
        if world.get((x, y - 1)) == obstacles.PENGUIN:
            return actions.PICKUP
        if world.get((x, y - 1)) == obstacles.WATER:
            return actions.BRAKE
        if world.get((x, y - 1)) == obstacles.CRACK:
            return actions.JUMP
        return actions.NONE
    elif right > up and right > left:
        return actions.RIGHT
    else:
        return actions.LEFT


def rec(flag, num, world, x, y):
    up, left, right, sumSides = 0, 0, 0, 0
    if num == 5:
        if flag:
            if world.get((x, y)) == obstacles.PENGUIN:
                return 10
            if world.get((x, y)) == obstacles.WATER:
                return 5
            if world.get((x, y)) == obstacles.CRACK:
                return 5
            if world.get((x, y)) == obstacles.TRASH or world.get((x, y)) == obstacles.BIKE or world.get((x, y)) == obstacles.BARRIER:
                return 5 * (-1)
            return 0
        else:
            if world.get((x, y)) == obstacles.TRASH or world.get((x, y)) == obstacles.BIKE or world.get((x, y)) == obstacles.BARRIER:
                return 5 * (-1)
            return 0
    if flag:
        if world.get((x, y)) == obstacles.PENGUIN:
            up = 10
        if world.get((x, y)) == obstacles.WATER:
            up = 5
        if world.get((x, y)) == obstacles.CRACK:
            up = 5
        if world.get((x, y)) == obstacles.TRASH or world.get((x, y)) == obstacles.BIKE or world.get(
                (x, y)) == obstacles.BARRIER:
            up = 5 * (-1)
    else:
        if world.get((x, y)) == obstacles.TRASH or world.get((x, y)) == obstacles.BIKE or world.get(
                (x, y)) == obstacles.BARRIER:
            sumSides = 5 * (-1)
    up += rec(True, num+1, world, x, y-1)
    if 0 <= x <= 1 or 4 <= x <= 5:
        right = sumSides + rec(False, num + 1, world, x+1, y-1)
    if 1 <= x <= 2 or 5 <= x <= 6:
        left = sumSides + rec(False, num + 1, world, x-1, y-1)
    return max(up, left, right)
