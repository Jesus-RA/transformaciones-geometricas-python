import math

def traslation(point, traslation_factor):
    [x, y] = point
    [tx, ty] = traslation_factor
    return [x + tx, y + ty]

def rotation(point, angle):
    [x, y] = point

    x_rotated = ( x * math.cos(angle) ) - ( y * math.sin(angle) )
    y_rotated = ( x * math.sin(angle) ) + ( y * math.cos(angle) )

    return [x_rotated, y_rotated]

def scaling(point, scaling_factor):
    [x, y] = point
    [sx, sy] = scaling_factor

    return [x * sx, y * sy]

def rotation_with_arbitrary_pivot(point, rotation_factor):
    [x, y] = point
    [xr, yr] = rotation_factor

    x_rotated = xr + (x - xr) * math.cos(angulo) - (y - yr) * math.sin(angulo)
    y_rotated = yr + (x - xr) * math.sin(angulo) + (y - yr) * math.cos(angulo)

    return [x_rotated, y_rotated]

def fixed_point_scaling(point, scaling_factor):
    [x, y] = point
    [xf, yf] = scaling_factor

    x_scaled = x * sx + xf * (1 - sx)
    y_scaled = y * sy + yf * (1 - sy)

    return [x_scaled, y_scaled]