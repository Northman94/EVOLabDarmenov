
DEGREE_BY_DIRECTION = {"N": 0, "NE": 45, "E": 90, "SE": 135, "S": 180, "SW": 225, "W": 270, "NW": 315}

DIRECTION_BY_DEGREE = {0: "N", 45: "NE", 90: "E", 135: "SE", 180: "S", 225: "SW", 270: "W", 315: "NW"}

FULL_CIRCLE = 360


def direction(facing, turn):
    if facing not in DEGREE_BY_DIRECTION:
        raise KeyError("Wrong Direction")

    if turn not in DIRECTION_BY_DEGREE:
        raise KeyError("Wrong Turn")

    degrees = DEGREE_BY_DIRECTION[facing]

    result = (degrees + turn) % FULL_CIRCLE

    new_direction = DIRECTION_BY_DEGREE[result]

    return new_direction
