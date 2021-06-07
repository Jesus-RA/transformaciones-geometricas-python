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

def rotation_with_arbitrary_pivot(point, angle, pivot):
    [x, y] = point
    [xr, yr] = pivot

    x_rotated = xr + (x - xr) * math.cos(angle) - (y - yr) * math.sin(angle)
    y_rotated = yr + (x - xr) * math.sin(angle) + (y - yr) * math.cos(angle)

    return [x_rotated, y_rotated]

def fixed_point_scaling(point, scaling_factor, pivot):
    [x, y] = point
    [sx, sy] = scaling_factor
    [xf, yf] = pivot


    x_scaled = x * sx + xf * (1 - sx)
    y_scaled = y * sy + yf * (1 - sy)

    return [x_scaled, y_scaled]