# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt  # для построения графиков
import numpy as np
import math  # математические вычисления


# функция для расчёта координат точки пересечения
def point_intersection(coef_plane: list, coord_point: list, vector_comp: list):
    scalar = 0  # условие и скалярное произведение векторов (нормали и направляющего вектора)
    point_in_plane = 0  # значение, получаемое при подставлении координат точки в уравнение плоскости

    x_desired, y_desired, z_desired = 0, 0, 0  # переменные-координаты точки пересечения

    if coef_plane[:3].count(0) == 3:
        error_plane = "Введены некорректные данные для уравнения плоскости"
        return print(error_plane)

    if vector_comp.count(0) == 3:
        error = "Введены некорректные данные для направляющего вектора"
        return print(error)

    # вычисление скалярного произведения
    for el in range(3):
        scalar += coef_plane[el] * vector_comp[el]
        point_in_plane += coord_point[el] * coef_plane[el]

    point_in_plane += coef_plane[-1]

    # пересекает ли прямая плоскость или не пересекает
    match scalar:
        # если скалярное произведение направляющего вектора и вектора нормали равно нулю
        case 0:
            # если после подставления координат точки в уравнение плоскости тождество сохранилось
            if point_in_plane == 0:
                print("Прямая лежит на плоскости")

            print("Прямая параллельна плоскости")

        case _:

            # получаем параметр t
            t = - point_in_plane / scalar

            # получаем искомые координаты
            x_desired = vector_comp[0] * t + coord_point[0]
            y_desired = vector_comp[1] * t + coord_point[1]
            z_desired = vector_comp[2] * t + coord_point[2]

            # нахождение угла между плоскостью и прямой
            vector_len = 0  # длина направляющего вектора
            normal_len = 0  # длина вектора нормали

            # вычисляем сумму квадратов компонентов направляющего вектора
            for comp in vector_comp:
                vector_len += comp ** 2

            for coeff in range(3):
                normal_len += coef_plane[coeff] ** 2

            vector_len = math.sqrt(vector_len)  # вычисляется длина направляющего вектора
            normal_len = math.sqrt(normal_len)  # вычисляется длина нормали

            sin_angle = math.asin(scalar / (vector_len * normal_len))  # вычисляется синус угла
            angle = math.degrees(sin_angle)  # перевод угла из радиан в градусы

            # нахождения расстояния от точки до плоскости
            distance = math.fabs(point_in_plane) / normal_len

            # вывод текстового сообщения
            answer = f"Уравнение плоскости: ({coef_plane[0]})x + ({coef_plane[1]})y " \
                     f"+ ({coef_plane[2]})z + ({coef_plane[3]}) = 0\n" \
                     f"Заданная точка M1({coord_point[0]}, {coord_point[1]}, {coord_point[2]})\n" \
                     f"Направляющий вектор P=({vector_comp[0]}, {vector_comp[1]}, {vector_comp[2]})\n" \
                     f"Искомые координаты точки пересечения прямой и плоскости:\n" \
                     f"Точка M({round(x_desired, 3)}, {round(y_desired, 3)}, {round(z_desired, 3)})\n" \
                     f"Угол между прямой и плоскостью: {round(math.fabs(angle), 1)}\u00B0\n" \
                     f"Расстояние между точкой и плоскостью: {distance}"

            print(answer)

    # построение графика
    # создаём полотно
    fig = plt.figure()
    axes = fig.add_subplot(projection='3d')
    axes.set_title('График 3D', fontsize=14, fontweight='bold')

    # подписываем оси
    axes.set_xlabel('Ось X')
    axes.set_ylabel('Ось Y')
    axes.set_zlabel('Ось Z')

    if coef_plane[2] != 0 or 0 not in coef_plane:
        # задаём интервал
        x = np.linspace(-100, 100, 100)
        y = np.linspace(-100, 100, 100)

        # Создаем двумерную матрицу-сетку
        xgrid, ygrid = np.meshgrid(x, y)
        z = (- coef_plane[0] * xgrid - coef_plane[1] * ygrid - coef_plane[3]) / coef_plane[2]
        axes.plot_surface(xgrid, ygrid, z, color="aquamarine", alpha=0.25)

    elif coef_plane[0] != 0:
        # задаём интервал
        y = np.linspace(-100, 100, 100)
        z = np.linspace(-100, 100, 100)

        # Создаем двумерную матрицу-сетку
        ygrid, zgrid = np.meshgrid(y, z)
        x = (- coef_plane[1] * ygrid - coef_plane[2] * zgrid - coef_plane[3]) / coef_plane[0]
        axes.plot_surface(x, ygrid, zgrid, color="aquamarine", alpha=0.25)

    elif coef_plane[1] != 0:
        # задаём интервал
        x = np.linspace(-100, 100, 100)
        z = np.linspace(-100, 100, 100)

        # Создаем двумерную матрицу-сетку
        xgrid, zgrid = np.meshgrid(x, z)
        y = (- coef_plane[0] * xgrid - coef_plane[2] * zgrid - coef_plane[3]) / coef_plane[1]
        axes.plot_surface(xgrid, y, zgrid, color="aquamarine", alpha=0.25)

    # построение прямой
    t = np.linspace(-100, 100, 200)

    x_line = coord_point[0] + vector_comp[0] * t
    y_line = coord_point[1] + vector_comp[1] * t
    z_line = coord_point[2] + vector_comp[2] * t

    # отрисовка прямой на графике
    axes.plot3D(x_line, y_line, z_line, color="mediumseagreen", alpha=0.8)

    # отрисовка заданной точки на графике
    axes.scatter3D(coord_point[0], coord_point[1], coord_point[2], color="orange")
    axes.text(coord_point[0], coord_point[1], coord_point[2], 'M1({}, {}, {})'.format(round(coord_point[0], 2),
                                                                                      round(coord_point[1], 2),
                                                                                      round(coord_point[2], 2)))

    if scalar != 0:
        # отрисовка точки пересечения на графике
        axes.scatter3D(x_desired, y_desired, z_desired, color="red")
        axes.text(x_desired, y_desired, z_desired, 'M({}, {}, {})'.format(round(x_desired, 2),
                                                                          round(y_desired, 2),
                                                                          round(z_desired, 2)))
    elif scalar == 0 and point_in_plane == 0:
        axes.text2D(0, 0.95, "Прямая лежит на плоскости", transform=axes.transAxes,
                    bbox=dict(facecolor='red', alpha=0.4))

    else:
        axes.text2D(0, 0.95, "Прямая параллельна плоскости", transform=axes.transAxes,
                    bbox=dict(facecolor='red', alpha=0.4))

    # количество делений на каждой из осей
    axes.locator_params(axis='x', nbins=20)
    axes.locator_params(axis='y', nbins=20)
    axes.locator_params(axis='z', nbins=20)
    plt.show()


point_intersection([-1, 2, -3, -6], [20, 40, 13], [2, 2, 2])
