import matplotlib.pyplot as plt  # для построения графиков
import numpy as np
import math  # математические вычисления


# функция нахождения точки пересечения прямой и плоскости
def intersection(surface: list, point: list, vector: list):
    scalar_vector = np.dot(surface[:3], vector)
    on_surface = np.dot(surface[0:3], point) + surface[-1]

    t = - on_surface / scalar_vector

    x_int = vector[0] * t + point[0]
    y_int = vector[1] * t + point[1]
    z_int = vector[2] * t + point[2]

    return [x_int, y_int, z_int]


# функция, вычисляющая угол между прямой и плоскостью
def angle(surface_eq: list, guide_vector: list):
    sqr_vector = [x ** 2 for x in guide_vector]
    sqr_normal = [x ** 2 for x in surface_eq]

    len_vector = math.sqrt(sum(sqr_vector))
    len_normal = math.sqrt(sum(sqr_normal))

    mult_vectors = np.dot(surface_eq[:3], guide_vector)

    sin_angle = math.sin(mult_vectors / (len_vector * len_normal))
    angle_between = math.degrees(sin_angle)

    return angle_between


# функция вычисления расстояния между точкой и плоскостью
def distance_between(surface: list, point: list):
    multiplication = np.dot(surface[0:3], point) + surface[-1]
    normal_sqr = [x ** 2 for x in surface]
    len_normal = math.sqrt(sum(normal_sqr))

    distance = math.fabs(multiplication / len_normal)

    return distance


# функция для построения плоскости
def coordinates(arguments: list):
    first_coordinate = np.linspace(-100, 100, 100)
    second_coordinate = np.linspace(-100, 100, 100)

    axis_1, axis_2 = np.meshgrid(first_coordinate, second_coordinate)

    axis_3 = (- arguments[0] * axis_1 - arguments[1] * axis_2 - arguments[3]) / arguments[2]

    return axis_1, axis_2, axis_3


# функция построения графика
def graphics(surface: list, point: list, vector: list, point_inter: list):
    fig = plt.figure()
    axes = fig.add_subplot(projection='3d')
    axes.set_title('График 3D', fontsize=14, fontweight='bold')

    # подписываем оси
    axes.set_xlabel('Ось X')
    axes.set_ylabel('Ось Y')
    axes.set_zlabel('Ось Z')

    # количество делений на каждой из осей
    axes.locator_params(axis='x', nbins=20)
    axes.locator_params(axis='y', nbins=20)
    axes.locator_params(axis='z', nbins=20)

    # построение прямой
    t = np.linspace(-100, 100, 200)

    x_line = point[0] + vector[0] * t
    y_line = point[1] + vector[1] * t
    z_line = point[2] + vector[2] * t

    # отрисовка прямой на графике
    axes.plot3D(x_line, y_line, z_line, color="mediumseagreen", alpha=0.8)

    # отрисовка заданной точки на графике
    axes.scatter3D(point[0], point[1], point[2], color="orange")
    axes.text(point[0], point[1], point[2], 'M1({}, {}, {})'.format(round(point[0], 2),
                                                                    round(point[1], 2),
                                                                    round(point[2], 2)))

    # отрисовка точки пересечения на графике
    axes.scatter3D(point_inter[0], point_inter[1], point_inter[2], color="red")
    axes.text(point_inter[0], point_inter[1], point_inter[2], 'M({}, {}, {})'.format(round(point_inter[0], 2),
                                                                                     round(point_inter[1], 2),
                                                                                     round(point_inter[2], 2)))
    x, y, z = 0, 0, 0

    if (surface[2] != 0) or (0 not in surface):
        x, y, z = coordinates(surface)

    elif surface[0] != 0:
        y, z, x = coordinates([surface[1], surface[2], surface[0], surface[3]])

    elif surface[1] != 0:
        x, z, y = coordinates([surface[0], surface[2], surface[1], surface[3]])

    axes.plot_surface(x, y, z, color="aquamarine", alpha=0.25)

    plt.show()


def main():
    A, B, C, D = -1, 2, -3, -6
    surf = [A, B, C, D]
    p = [2, 2, 2]
    M_1 = [20, 40, 13]

    point_intersection = intersection(surf, M_1, p)
    print_angle = angle(surf, p)
    distance_answer = distance_between(surf, M_1)
    graphics(surf, M_1, p, point_intersection)


if __name__ == "__main__":
    main()
