import matplotlib.pyplot as plt  # для построения графиков
from mpl_toolkits.mplot3d.art3d import Poly3DCollection  # для построения плоскости по 4 точкам
import math  # математические вычисления

import noise  # для генерации шума Перлина
import numpy as np

import time

# функция для создания поверхности
def maps():
    shape = (200, 200)  # размеры сетки
    scale = 200.0  # масштаб
    octaves = 5  # октавы
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
                                        base=31) * 100

    return world


# функция для расчёта коэффициентов уравнения плоскости
def plane_coefficients(dot_1: list, dot_2: list, dot_3: list):
    A = (dot_2[1] - dot_1[1]) * (dot_3[2] - dot_1[2]) - (dot_2[2] - dot_1[2]) * (dot_3[1] - dot_1[1])
    B = (dot_2[2] - dot_1[2]) * (dot_3[0] - dot_1[0]) - (dot_2[0] - dot_1[0]) * (dot_3[2] - dot_1[2])
    C = (dot_2[0] - dot_1[0]) * (dot_3[1] - dot_1[1]) - (dot_2[1] - dot_1[1]) * (dot_3[0] - dot_1[0])
    D = dot_1[0] * (-A) + dot_1[1] * (-B) + dot_1[2] * (-C)

    return [A, B, C, D]


# фукция для нахождения наиближайшей точки
def highest(coord_points: list, set_point: list):
    lengths = []  # список длин векторов

    for i in range(len(coord_points)):
        # расчёт компонентов векторов
        difference = [coord_points[i][x] - set_point[x] for x in range(3)]
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


# функция нахождения точки пересечения прямой и плоскости
def intersection(flat: list, given_point: list, direction_vector: list):
    # вычисление произведения вручную
    scalar_vector = 0  # скалярное произведение векторов
    on_surface = 0  # подставление координат точки в уравнение окружности

    for el in range(3):
        scalar_vector += flat[el] * direction_vector[el]
        on_surface += flat[el] * given_point[el]

    on_surface += flat[3]

    if scalar_vector == 0:
        return False

    # вычисление координат точки пересечения
    t = - on_surface / scalar_vector

    x_int = direction_vector[0] * t + given_point[0]
    y_int = direction_vector[1] * t + given_point[1]
    z_int = direction_vector[2] * t + given_point[2]

    return [x_int, y_int, z_int]


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
            plane_1 = plane_coefficients(component_3, component_1, component_4)
            # вычисление коэффицентов первой плоскости
            plane_2 = plane_coefficients(component_3, component_2, component_4)

            # если есть персечение
            if answer := intersection(plane_1, point, vector):
                # если точка между точками
                if comparison(component_3, component_1, component_4, answer, plane_1):
                    print(component_3, component_1, component_4)
                    points.append(answer)

            if answer := intersection(plane_2, point, vector):
                if comparison(component_3, component_2, component_4, answer, plane_2):
                    print(component_3, component_2, component_4)
                    points.append(answer)

    return points


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
def distance_between(ground: list, view: list):
    # вычисление вручную
    multiplication = 0

    for i in range(3):
        multiplication += ground[i] * view[i]
    multiplication += ground[3]

    normal_sqr = [x ** 2 for x in ground[:3]]
    len_normal = math.sqrt(sum(normal_sqr))

    # расстояние между точкой и плоскостью
    distance = math.fabs(multiplication / len_normal)

    return distance


# функция, осуществляющая проверку на поиск точки пересечения,
def is_point(p_1, p_2, p_3, spot, vec):
    plane = plane_coefficients(p_1, p_2, p_3)

    # если существует пересечение
    if p_inter := intersection(plane, spot, vec):

        # если точка между точками
        if comparison(p_1, p_2, p_3, p_inter, plane):
            return p_inter

    return False


# функция оптимального поиска точки пересечения
def search_optimum(card, point_coord: list, direction: list):
    list_places = []  # список найденных точек пересечения

    # длины по координате x и y
    size_x = len(card[0])
    size_y = len(card)

    # если проекция прямой перпендикулярна OX
    if (direction[0] == 0) and (direction[1] != 0):

        x_m = math.floor(point_coord[0])

        if x_m < 0:
            return []

        for y in range(1, size_y):

            object_1 = [x_m, y, card[x_m][y]]
            object_2 = [x_m, y - 1, card[x_m][y - 1]]

            if x_m < size_x - 1:

                object_3 = [x_m + 1, y - 1, card[x_m + 1][y - 1]]
                object_4 = [x_m + 1, y, card[x_m + 1][y]]

                # если найдена точка пересечения внутри первого треугольника
                if dot := is_point(object_2, object_1, object_4, point_coord, direction):
                    list_places.append(dot)

                # если найдена точка пересечения внутри второго треугольника
                if dot := is_point(object_2, object_3, object_4, point_coord, direction):
                    list_places.append(dot)

            else:
                object_5 = [x_m - 1, y - 1, card[x_m - 1][y - 1]]
                object_6 = [x_m - 1, y, card[x_m - 1][y]]

                # если найдена точка пересечения внутри первого треугольника
                if dot := is_point(object_5, object_6, object_1, point_coord, direction):
                    list_places.append(dot)

                # если найдена точка пересечения внутри второго треугольника
                if dot := is_point(object_5, object_2, object_1, point_coord, direction):
                    list_places.append(dot)

    # если проекция прямой перпендикулярна OY
    elif (direction[1] == 0) and (direction[0] != 0):

        y_m = math.floor(point_coord[1])

        if y_m < 0:
            return []

        for x in range(1, size_x):

            item_1 = [x, y_m, card[x][y_m]]
            item_4 = [x - 1, y_m, card[x - 1][y_m]]

            if y_m < size_y - 1:
                item_2 = [x, y_m + 1, card[x][y_m + 1]]
                item_3 = [x - 1, y_m + 1, card[x - 1][y_m + 1]]

                # если найдена точка пересечения внутри первого треугольника
                if dot := is_point(item_2, item_3, item_4, point_coord, direction):
                    list_places.append(dot)

                # если найдена точка пересечения внутри второго треугольника
                if dot := is_point(item_2, item_1, item_4, point_coord, direction):
                    list_places.append(dot)

            else:

                item_5 = [x, y_m - 1, card[x][y_m - 1]]
                item_6 = [x - 1, y_m - 1, card[x - 1][y_m - 1]]

                # если найдена точка пересечения внутри первого треугольника
                if dot := is_point(item_6, item_4, item_1, point_coord, direction):
                    list_places.append(dot)

                # если найдена точка пересечения внутри второго треугольника
                if dot := is_point(item_6, item_5, item_1, point_coord, direction):
                    list_places.append(dot)

    # если проекция прямой выраждается в точку
    elif (direction[0] == 0) and (direction[1] == 0):

        x = math.floor(point_coord[0])
        y = math.floor(point_coord[1])

        if (x < 0) or (x >= size_x):
            return []

        if (y < 0) or (y >= size_y):
            return []

        height_1 = [x, y, card[x][y]]
        height_2 = [x + 1, y, card[x + 1][y]]
        height_3 = [x + 1, y - 1, card[x + 1][y - 1]]
        height_4 = [x, y - 1, card[x][y - 1]]

        # если найдена точка пересечения внутри первого треугольника
        if dot := is_point(height_4, height_1, height_2, point_coord, direction):
            list_places.append(dot)

        # если найдена точка пересечения внутри второго треугольника
        if dot := is_point(height_4, height_3, height_2, point_coord, direction):
            list_places.append(dot)

    # сравниваем значения компонент по модулю направляющего вектора
    elif math.fabs(direction[0]) >= math.fabs(direction[1]):

        for x in range(1, size_x):

            # вычисляем предыдущую координату по y
            y_last = ((x - 1) - point_coord[0]) * (direction[1] / direction[0]) + point_coord[1]
            # вычисляем текущую координату по y
            y_current = (x - point_coord[0]) * (direction[1] / direction[0]) + point_coord[1]

            # если текущая координата отрцательная, то переходим к следующему шагу
            if (y_current < 0) or (y_current >= size_y):
                continue

            # округляем значения
            y_0 = math.floor(y_last)
            y_1 = math.floor(y_current)

            # вычислим координаты квадратов
            peak_1 = [x, y_1, card[x][y_1]]
            peak_3 = [x - 1, y_1, card[x - 1][y_1]]

            if y_1 + 1 != size_y:

                peak_2 = [x, y_1 + 1, card[x][y_1 + 1]]
                peak_4 = [x - 1, y_1 + 1, card[x - 1][y_1 + 1]]

                # если найдена точка пересечения внутри первого треугольника
                if dot := is_point(peak_3, peak_1, peak_2, point_coord, direction):
                    list_places.append(dot)
                # если найдена точка пересечения внутри второго треугольника
                if dot := is_point(peak_3, peak_4, peak_2, point_coord, direction):
                    list_places.append(dot)

            # если прямая пересекает более 1 квадрата
            if y_1 - y_0 == 1:

                peak_5 = [x, y_1 - 2, card[x][y_1 - 2]]
                peak_6 = [x - 1, y_1 - 2, card[x - 1][y_1 - 2]]

                # если найдена точка пересечения внутри первого треугольника
                if dot := is_point(peak_6, peak_3, peak_1, point_coord, direction):
                    list_places.append(dot)
                # если найдена точка пересечения внутри второго треугольника
                if dot := is_point(peak_6, peak_5, peak_1, point_coord, direction):
                    list_places.append(dot)

            elif (y_1 - y_0 == -1) and (y_1 + 2 < size_y):

                peak_7 = [x, y_1 + 1, card[x][y_1 + 1]]
                peak_8 = [x - 1, y_1 + 1, card[x - 1][y_1 + 1]]
                peak_9 = [x, y_1 + 2, card[x][y_1 + 2]]
                peak_10 = [x - 1, y_1 + 2, card[x - 1][y_1 + 2]]

                # если найдена точка пересечения внутри первого треугольника
                if dot := is_point(peak_8, peak_10, peak_9, point_coord, direction):
                    list_places.append(dot)
                # если найдена точка пересечения внутри второго треугольника
                if dot := is_point(peak_8, peak_7, peak_9, point_coord, direction):
                    list_places.append(dot)

    elif math.fabs(direction[0]) < math.fabs(direction[1]):

        for y in range(1, size_y):

            # вычисляем предыдущую координату по x
            x_last = ((y - 1) - point_coord[1]) * (direction[0] / direction[1]) + point_coord[0]
            # вычисляем текущую координату по x
            x_current = (y - point_coord[1]) * (direction[0] / direction[1]) + point_coord[0]

            # если текущая координата отрцательная, то переходим к следующему шагу
            if x_current < 0:
                continue

            # округляем значения
            x_0 = math.floor(x_last)
            x_1 = math.floor(x_current)

            # print(x_1)
            # вычисляем координаты точек
            place_1 = [x_1, y, card[x_1][y]]
            place_2 = [x_1 + 1, y, card[x_1 + 1][y]]
            place_3 = [x_1, y - 1, card[x_1][y - 1]]
            place_4 = [x_1 + 1, y - 1, card[x_1 + 1][y - 1]]

            # print(place_1, place_2, place_3, place_4)

            # если найдена точка пересечения внутри первого треугольника
            if dot := is_point(place_3, place_1, place_2, point_coord, direction):
                list_places.append(dot)
            # если найдена точка пересечения внутри второго треугольника
            if dot := is_point(place_3, place_4, place_2, point_coord, direction):
                list_places.append(dot)

            if (x_1 - x_0 == 1) and (x_1 + 2 != size_x):

                place_5 = [x_1 + 2, y, card[x_1 + 2][y]]
                place_6 = [x_1 + 2, y - 1, card[x_1 + 2][y - 1]]

                # если найдена точка пересечения внутри первого треугольника
                if dot := is_point(place_4, place_6, place_5, point_coord, direction):
                    list_places.append(dot)

                # если найдена точка пересечения внутри второго треугольника
                if dot := is_point(place_4, place_2, place_5, point_coord, direction):
                    list_places.append(dot)

            elif x_1 - x_0 == -1:

                place_7 = [x_1 - 1, y, card[x_1 - 1][y]]
                place_8 = [x_1 - 1, y - 1, card[x_1 - 1][y - 1]]

                # если найдена точка пересечения внутри первого треугольника
                if dot := is_point(place_8, place_3, place_1, point_coord, direction):
                    list_places.append(dot)

                # если найдена точка пересечения внутри второго треугольника
                if dot := is_point(place_8, place_7, place_1, point_coord, direction):
                    list_places.append(dot)

    return list_places


# функция для построения плоскости
def coordinates(arguments: list, pixel: list) -> tuple:
    indent = 40  # разброс
    axis_3 = []

    # координаты точек по двум осям
    axis_1 = [pixel[0] + indent, pixel[0] + indent, pixel[0] - indent, pixel[0] - indent]
    axis_2 = [pixel[1] - indent, pixel[1] + indent, pixel[1] + indent, pixel[1] - indent]

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
def construction(matrix, locations: list, place: list):
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
    inter = highest(locations, place)

    # отрисовка точки пересечения
    ax.scatter3D(inter[0], inter[1], inter[2], color="red", linewidth=1, zorder=2)
    ax.text(inter[0], inter[1], inter[2], 'M({}, {}, {})'.format(round(inter[0], 2),
                                                                 round(inter[1], 2),
                                                                 round(inter[2], 2), ))
    # отрисовка заданной точки
    ax.scatter3D(place[0], place[1], place[2], color="orange", linewidth=1, zorder=2)
    ax.text(place[0], place[1], place[2], 'M1({}, {}, {})'.format(round(place[0], 2),
                                                                  round(place[1], 2),
                                                                  round(place[2], 2)))

    # координаты начала вектора
    x_p = place[0]
    y_p = place[1]
    z_p = place[2]

    # кооридинаты вектора
    u_x = inter[0] - place[0]
    u_y = inter[1] - place[1]
    u_z = inter[2] - place[2]

    # построение вектора
    ax.quiver(x_p, y_p, z_p, u_x, u_y, u_z, color='green', linewidth=1, zorder=2)

    plt.show()


def main():
    p = [1, 0, 17]  # направляющий вектор
    M_1 = [150, 140, 28]  # заданная точка

    world = maps()

    start_time = time.time()
    data = search_optimum(world, M_1, p)
    end_time = time.time()

    print(data)

    print((end_time - start_time) * (10 ** 3), "ms")

    start_time = time.time()
    new_data = search(world, M_1, p)
    end_time = time.time()
    print((end_time - start_time) * (10 ** 3), "ms")
    # construction(world, data, M_1)


if __name__ == "__main__":
    main()
