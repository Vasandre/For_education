import matplotlib.pyplot as plt  # для построения графиков
from mpl_toolkits.mplot3d.art3d import Poly3DCollection  # для построения плоскости по 4 точкам
import math  # математические вычисления


# функция нахождения точки пересечения прямой и плоскости
def intersection(surface: list, point: list, vector: list) -> list:
    # вычисление произведения вручную
    scalar_vector = 0  # скалярное произведение векторов
    on_surface = 0  # подставление координат точки в уравнение окружности

    for el in range(3):
        scalar_vector += surface[el] * vector[el]
        on_surface += surface[el] * point[el]

    on_surface += surface[3]

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

    sin_angle = math.sin(mult_vectors / (len_vector * len_normal))
    angle_between = math.degrees(sin_angle)  # угол между прямой и плоскостью

    return angle_between


# функция вычисления расстояния между точкой и плоскостью
def distance_between(surface: list, point: list):
    # вычисление вручную
    multiplication = 0

    for i in range(3):
        multiplication += surface[i] * point[i]
    multiplication += surface[3]

    normal_sqr = [x ** 2 for x in surface]
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

    # координаты "хвоста" вектора
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


def main():
    # задание коэффициентов для уравнения плоскости
    A, B, C, D = 20, 4, 9, 0
    surf = [A, B, C, D]
    p = [20, 1, 20]  # направляющий вектор
    M_1 = [50, 20, 10]  # заданная точка

    point_intersection = intersection(surf, M_1, p)
    print_angle = angle(surf, p)
    distance_answer = distance_between(surf, M_1)
    graphics(surf, M_1, point_intersection)


if __name__ == "__main__":
    main()
