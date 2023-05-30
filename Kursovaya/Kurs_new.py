import matplotlib.pyplot as plt  # для построения графиков
from mpl_toolkits.mplot3d.art3d import Poly3DCollection  # для построения плоскости по 4 точкам
import math  # математические вычисления

import noise  # для генерации шума Перлина
import numpy as np


# функция для создания поверхности
def maps():
    shape = (50, 50)  # размеры сетки
    scale = 100.0  # масштаб
    octaves = 6  # октавы
    persistence = 0.5
    lacunarity = 2.0

    world = np.zeros(shape)  # создаём матрицу

    # заполнение матрицы значениями высот
    for i in range(shape[0]):
        for j in range(shape[1]):
            world[i][j] = noise.pnoise2(i / scale,
                                        j / scale,
                                        octaves=octaves,
                                        persistence=persistence,
                                        lacunarity=lacunarity,
                                        repeatx=2048,
                                        repeaty=2048,
                                        base=42) * 100

    return world


# функция для расчёта коэффициентов уравнения плоскости
def plane_coefficients(point_1: list, point_2: list, point_3: list):
    A = (point_2[1] - point_1[1]) * (point_3[2] - point_1[2]) - (point_2[2] - point_1[2]) * (point_3[1] - point_1[1])
    B = (point_2[2] - point_1[2]) * (point_3[0] - point_1[0]) - (point_2[0] - point_1[0]) * (point_3[2] - point_1[2])
    C = (point_2[0] - point_1[0]) * (point_3[1] - point_1[1]) - (point_2[1] - point_1[1]) * (point_3[0] - point_1[0])
    D = point_1[0] * (-A) + point_1[1] * (-B) + point_1[2] * (-C)

    return [A, B, C, D]


# фукция для нахождения наиближайшей точки
def highest(coord_points: list, point: list):
    lengths = []  # список длин векторов

    for i in range(len(coord_points)):
        # расчёт компонентов векторов
        difference = [coord_points[i][x] - point[x] for x in range(3)]
        # расчёт длин векторов
        length = math.sqrt(sum([el ** 2 for el in difference]))
        lengths.append(length)

    index = lengths.index(min(lengths))  # индекс координат точки, которая ближе всех к заданной

    return coord_points[index]


# функция сравнения координат точки пересечения с координатами точек плоскости
def comparison(tri_a, tri_b, tri_c, m, normal):
    # расчёт компонент векторов, соединяющих найденную точку пересечения
    # с точками треугольника
    ma = [m[i] - tri_a[i] for i in range(3)]
    mb = [m[i] - tri_b[i] for i in range(3)]
    mc = [m[i] - tri_c[i] for i in range(3)]

    # вычисление векторного произведения между найденными векторами
    ma_mb = [ma[1] * mb[2] - ma[2] * mb[1], -(ma[0] * mb[2] - ma[2] * mb[0]), ma[0] * mb[1] - ma[1] * mb[0]]
    mb_mc = [mb[1] * mc[2] - mb[2] * mc[1], -(mb[0] * mc[2] - mb[2] * mc[0]), mb[0] * mc[1] - mb[1] * mc[0]]
    mc_ma = [mc[1] * ma[2] - mc[2] * ma[1], -(mc[0] * ma[2] - mc[2] * ma[0]), mc[0] * ma[1] - mc[1] * ma[0]]

    # вычисление скалярного произведения
    scalar_1 = sum([normal[i] * ma_mb[i] for i in range(3)])
    scalar_2 = sum([normal[i] * mb_mc[i] for i in range(3)])
    scalar_3 = sum([normal[i] * mc_ma[i] for i in range(3)])

    # если все скалярные произведения не отрицательные
    if (scalar_1 >= 0) and (scalar_2 >= 0) and (scalar_3 >= 0):
        return True

    # если все скалярные произведения отрицательные
    elif (scalar_1 < 0) and (scalar_2 < 0) and (scalar_3 < 0):
        return True

    # иначе все произведения разных знаков
    else:
        return False


# функция поиска точки пересечения
def search(matrix, point: list, vector: list):
    points = []  # вектор, содержащий точки пересечения с разными плоскостями
    # идём по строкам
    for line in range(1, len(matrix)):
        # идём по столбцам
        for column in range(1, len(matrix)):
            # вычисление точек плоскости
            component_1 = [line, column - 1, matrix[line][column - 1]]
            component_2 = [line - 1, column, matrix[line - 1][column]]
            component_3 = [line - 1, column - 1, matrix[line - 1][column - 1]]
            component_4 = [line, column, matrix[line][column]]

            # вычисление коэффицентов первой плоскости
            plane_1 = plane_coefficients(component_3,
                                         component_1,
                                         component_4)
            # вычисление коэффицентов первой плоскости
            plane_2 = plane_coefficients(component_3,
                                         component_2,
                                         component_4)
            # если есть персечение
            if answer := intersection(plane_1, point, vector):
                # если точка между точками
                if comparison(component_3, component_1, component_4, answer, plane_1):
                    points.append(answer)

            if answer := intersection(plane_2, point, vector):
                if comparison(component_3, component_2, component_4, answer, plane_2):
                    points.append(answer)

    return points


# функция нахождения точки пересечения прямой и плоскости
def intersection(surface: list, point: list, vector: list):
    # вычисление произведения вручную
    scalar_vector = 0  # скалярное произведение векторов
    on_surface = 0  # подставление координат точки в уравнение окружности

    for el in range(3):
        scalar_vector += surface[el] * vector[el]
        on_surface += surface[el] * point[el]

    on_surface += surface[3]

    if scalar_vector == 0:
        return False

    # вычисление координат точки пересечения
    t = - on_surface / scalar_vector

    x_int = vector[0] * t + point[0]
    y_int = vector[1] * t + point[1]
    z_int = vector[2] * t + point[2]

    return [x_int, y_int, z_int]


# функция, вычисляющая угол между прямой и плоскостью
def angle(surface_eq: list, guide_vector: list) -> float:
    sqr_vector = [x ** 2 for x in guide_vector]  # список компонент вектора в квадрате
    sqr_normal = [x ** 2 for x in surface_eq]  # список компонент нормали в квадрате

    # вычисление длин векторов
    len_vector = math.sqrt(sum(sqr_vector))
    len_normal = math.sqrt(sum(sqr_normal))

    # вычисление произведения вручную
    mult_vectors = 0

    for el in range(3):
        mult_vectors += surface_eq[el] * guide_vector[el]

    sin_angle = math.fabs(math.asin(mult_vectors / (len_vector * len_normal)))
    angle_between = math.degrees(sin_angle)  # угол между прямой и плоскостью

    return angle_between


# функция вычисления расстояния между точкой и плоскостью
def distance_between(surface: list, point: list):
    # вычисление вручную
    multiplication = 0

    for i in range(3):
        multiplication += surface[i] * point[i]
    multiplication += surface[3]

    normal_sqr = [x ** 2 for x in surface[:3]]
    len_normal = math.sqrt(sum(normal_sqr))

    # расстояние между точкой и плоскостью
    distance = math.fabs(multiplication / len_normal)

    return distance


# функция для построения плоскости
def coordinates(arguments: list, point: list) -> tuple:
    indent = 40  # разброс
    axis_3 = []

    # координаты точек по двум осям
    axis_1 = [point[0] + indent, point[0] + indent, point[0] - indent, point[0] - indent]
    axis_2 = [point[1] - indent, point[1] + indent, point[1] + indent, point[1] - indent]

    # вычисление координат точек по третьей оси
    for el in range(4):
        axis_3.append((- arguments[0] * axis_1[el] - arguments[1] * axis_2[el] - arguments[3]) / arguments[2])

    return axis_1, axis_2, axis_3


# функция построения графика
def graphics(surface: list, point: list, point_inter: list) -> None:
    fig = plt.figure()  # создание фигуры
    axes = fig.add_subplot(projection='3d')  # создание 3d-полотна в фигуре
    axes.set_title('График 3D', fontsize=14, fontweight='bold')  # заголовок в полотне

    # подписываем оси
    axes.set_xlabel('Ось X')
    axes.set_ylabel('Ось Y')
    axes.set_zlabel('Ось Z')

    # координаты "хвоста"(начала) вектора
    x_p = point[0]
    y_p = point[1]
    z_p = point[2]

    # кооридинаты вектора
    u_x = point_inter[0] - point[0]
    u_y = point_inter[1] - point[1]
    u_z = point_inter[2] - point[2]

    # построение вектора
    axes.quiver(x_p, y_p, z_p, u_x, u_y, u_z, color='green', linewidth=2)

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
    # координаты для построения плоскости
    x, y, z = [], [], []

    # вычисление координат в зависимости от коэффициентов
    if (surface[2] != 0) or (0 not in surface):
        x, y, z = coordinates(surface, point_inter[:2])

    elif surface[0] != 0:
        y, z, x = coordinates([surface[1], surface[2], surface[0], surface[3]],
                              [point_inter[1], point_inter[2]])

    elif surface[1] != 0:
        x, z, y = coordinates([surface[0], surface[2], surface[1], surface[3]],
                              [point_inter[0], point_inter[2]])

    # создание 2D-списка
    points = [[[x[i], y[i], z[i]] for i in range(4)]]

    # построение плоскости по 4 точкам
    axes.add_collection3d(Poly3DCollection(points, alpha=0.5))

    # задание границ по каждой из осей
    axes.set_xlim(min(point[0], min(x)) - 10, max(point[0], max(x)) + 10)
    axes.set_ylim(min(point[1], min(y)) - 10, max(point[1], max(y)) + 10)
    axes.set_zlim(min(point[2], min(z)) - 10, max(point[2], max(z)) + 10)

    # построение графика
    plt.show()


# функция для построения поверхности и точек с вектором
def construction(matrix, points, point):
    fig = plt.figure()
    ax = fig.add_subplot(projection="3d", computed_zorder=False)

    ax.set_title('График 3D', fontsize=14, fontweight='bold')  # заголовок в полотне

    # подписываем оси
    ax.set_xlabel('Ось X')
    ax.set_ylabel('Ось Y')
    ax.set_zlabel('Ось Z')

    lin_x = np.linspace(0, len(matrix), len(matrix), endpoint=False)
    lin_y = np.linspace(0, len(matrix), len(matrix), endpoint=False)
    x, y = np.meshgrid(lin_x, lin_y)

    # построение поверхности
    ax.plot_surface(x, y, matrix.transpose(), cmap='terrain', zorder=1)

    # нахождение наивысшей точки
    inter = highest(points, point)

    # отрисовка точки пересечения
    ax.scatter3D(inter[0], inter[1], inter[2], color="red", linewidth=1, zorder=2)
    ax.text(inter[0], inter[1], inter[2], 'M({}, {}, {})'.format(round(inter[0], 2),
                                                                 round(inter[1], 2),
                                                                 round(inter[2], 2), ))
    # отрисовка заданной точки
    ax.scatter3D(point[0], point[1], point[2], color="orange", linewidth=1, zorder=2)
    ax.text(point[0], point[1], point[2], 'M1({}, {}, {})'.format(round(point[0], 2),
                                                                  round(point[1], 2),
                                                                  round(point[2], 2)))

    # координаты начала вектора
    x_p = point[0]
    y_p = point[1]
    z_p = point[2]

    # кооридинаты вектора
    u_x = inter[0] - point[0]
    u_y = inter[1] - point[1]
    u_z = inter[2] - point[2]

    # построение вектора
    ax.quiver(x_p, y_p, z_p, u_x, u_y, u_z, color='green', linewidth=1, zorder=2)

    plt.show()


def main():
    p = [5, 7, -20]  # направляющий вектор
    M_1 = [15, 30, 18]  # заданная точка
    # surf = [-2, 12, -41, 2]
    # inter = intersection(surf, M_1, p)
    # angle_between = angle(surf[:3], p)
    # dist = distance_between(surf, M_1)
    # graphics(surf, M_1, inter)

    world = maps()

    data = search(world, M_1, p)
    construction(world, data, M_1)


if __name__ == "__main__":
    main()
