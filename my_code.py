# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 20:40:25 2024

This .py file is a copy of "For_Paper_1.py" file by Mavrin S.V.

@author: Simakin
"""

import numpy as np
import math

import Input_Data
import Func_1
import Plots_1


P = np.zeros([4, 2])  ## массив с координатами контр. точек для 1 Безье кривой.
P[0,:] = [2.5,  0]
P[1,:] = [3.33, 2.5]
P[2,:] = [5.7,  3.7]
P[3,:] = [6.6,  3.7]
HP = np.array([1, 1, 1, 1])

Q = np.zeros([4, 2])  ## массив с координатами контр. точек для 2 Безье кривой.
Q[0,:] = [6.6,  3.7 + 1]
Q[1,:] = [11,   4.5]
Q[2,:] = [14,   3.3]
Q[3,:] = [19,   1]
HQ = np.array([1, 1, 1, 1])

R = np.zeros([4, 2])
HR = np.array([1, 1, 1, 1])

n_vert = np.shape(P)[0] - 1  ## степень Безье кривой.
print("n_vert = ", n_vert)


# Input_Data.
# Расчёт кубического сплайна

p = 3  ## Что-то с производными.
m_not = n_vert + 1 + p    
print(f"p = {p}", f"n_vert = {n_vert}", f"m_not = {m_not}\n", sep="\n")

U = np.zeros([m_not+1])
Input_Data.Calculation_U_Open_Uniform(p, n_vert, m_not, U)
u_start1 = U[p]
u_stop1 = U[n_vert+1]
print(f"U = {U}", f"u_start1 = {u_start1},  (index_start = {p})", f"u_stop1  = {u_stop1},  (index_stop  = {n_vert+1})\n", sep="\n")

V = np.zeros([m_not+1])
Input_Data.Calculation_U_Open_Uniform(p, n_vert, m_not, V)
v_start1 = V[p]
v_stop1 = V[n_vert+1]
print(f"V = {V}", f"v_start1 = {v_start1},  (index_start = {p})", f"v_stop1  = {v_stop1},  (index_stop = {n_vert+1})\n", sep="\n")

T = np.zeros([m_not+1])
Input_Data.Calculation_U_Open_Uniform(p, n_vert, m_not, T)
t_start1 = T[p]
t_stop1 = T[n_vert+1]
print(f"T = {T}", f"t_start1 = {t_start1},  (index_start = {p})", f"t_stop1  = {t_stop1},  (index_stop = {n_vert+1})\n", sep="\n")

# ------------------------------------------------------------------------------
# Расчет Первой Безье-крив. ( Р - кривая )
# ders_p1 - для заданного "u" массив BASIS функций и все их (до р) производные
ders_p1 = np.zeros([p+1, p+1])

# C2 - массив, в нем для заданного "u" возвращаются C2[0,:]- x,y - сплайна
#                               для заданного "u"  C2[1,:]- x,y - 1-вой ПРОИЗВОДНОЙ сплайна
#                               для заданного "u"  C2[2,:]- x,y - 2-ой ПРОИЗВОДНОЙ сплайна
#                               для заданного "u"  C2[p,:]- x,y -"p"-ой ПРОИЗВОДНОЙ сплайна
C2_NURBS_p1 = np.zeros([p+1, 2])  # индекс "2" для 2D задачи, "3" - для 3D

n_u1 = 60
data_CurvePoin_and_Deriv_NURBS_p1 = np.zeros([(n_u1+1), (p+1), 2])

for iu in range(n_u1 + 1):
    u_i = (iu / n_u1) * (u_stop1 - u_start1) + u_start1

    Func_1.CurvePoin_and_Deriv_NURBS(n_vert, p, U, P, HP, u_i, C2_NURBS_p1, ders_p1)

    data_CurvePoin_and_Deriv_NURBS_p1[iu, :, :] = C2_NURBS_p1  # хранится Кубический Сплайн

# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Расчет Второрй Безье-кривой ( Q - кривая )
# ders - для заданного "u" массив BASIS функций и  все их (до р) производныЕ
ders_p2 = np.zeros([p+1, p+1])

# C2 - массив, в нем для заданного "u" возвращаются C2[0,:]- x,y - сплайна
#                               для заданного "u"  C2[1,:]- x,y - 1-вой ПРОИЗВОДНОЙ сплайна
#                               для заданного "u"  C2[0,:]- x,y - 2-ой ПРОИЗВОДНОЙ сплайна
#                               для заданного "u"  C2[p,:]- x,y -"p"-ой ПРОИЗВОДНОЙ сплайна
C2_NURBS_p2 = np.zeros([p+1, 2])  # идекс "2" для 2D задачи, "3" - для 3D

n_u2 = 60
data_CurvePoin_and_Deriv_NURBS_p2 = np.zeros([(n_u2+1), (p+1), 2])

for iv in range(n_u2 + 1):
    v_i = (iv / n_u2) * (v_stop1 - v_start1) + v_start1

    Func_1.CurvePoin_and_Deriv_NURBS(n_vert, p, V, Q, HQ, v_i, C2_NURBS_p2, ders_p2)

    data_CurvePoin_and_Deriv_NURBS_p2[iv, :, :] = C2_NURBS_p2  # хранится Кубический Сплайн

# ------------------------------------------------------------------------------


Title = "Исходные данные Для СОПРЯЖЕНИЯ двух Безье-кривых 3-й Степени"
#Title = ' '

labels_legend1 = "P Многоугольник"
labels_legend2 = "P Безье Кривая"
labels_legend3 = "Q Многоугольник"
labels_legend4 = "Q Безье Кривая"

y_min = -1
y_max = 7.0
x_min = 0
x_max = 20

Plots_1.plot_Trace_Lines_2_for_Mergin_a(P[:, 0], P[:, 1],
                                        Q[:, 0], Q[:, 1],

                                        data_CurvePoin_and_Deriv_NURBS_p1[:, 0, 0],
                                        data_CurvePoin_and_Deriv_NURBS_p1[:, 0, 1],
                                        data_CurvePoin_and_Deriv_NURBS_p2[:, 0, 0],
                                        data_CurvePoin_and_Deriv_NURBS_p2[:, 0, 1],

                                        y_min, y_max, x_min, x_max,
                                        Title, labels_legend1, labels_legend2,
                                        labels_legend3, labels_legend4)


# ------------------------------------------------------------------------------
# Блок ДИСКРЕТ. НОРМА  без Ограничений

Eps1 = np.zeros([4, 2])
Del1 = np.zeros([4, 2])
Lam1 = np.zeros([4, 2])
X1 = np.zeros([12, 2])
X1_1 = np.zeros([12, 2])
Matrix_A1 = np.zeros([12, 12])
Matrix_B1 = np.zeros([12, 2])

# p = 3  ## повторение
ders = np.zeros([p+1, p+1])  # массив, в котором - в 1-ой строке - Базисные Функции
                             #                   - в 2-ой строке - первые производные Базисных Функций
                             #                   - в 3-ой строке - вторые производные Базисных Функций и т.д. ........

u0 = 1.0  # Конечная Точка на Р-кривой, для неё расчитываем 1. Базис. функции и 2. Три произв. Базис. Функций == ТОЧКА СОПРЯЖЕНИЯ
span = Func_1.FindSpan(n_vert, p, u0, U)
Func_1.DersBasisFuns(span, u0, p, p, U, ders)
print("*u0=", u0, "  ders=\n", ders)

#  Производные БАЗИСНЫх ФУНКЦИИ в конечной точке  Р-кривой
N_001 = ders[0, 0];  N_101 = ders[0, 1];  N_201 = ders[0, 2];  N_301 = ders[0, 3]  # НУЛЕВЫЕ ПРОИЗВОДНЫЕ = сама функция
N_011 = ders[1, 0];  N_111 = ders[1, 1];  N_211 = ders[1, 2];  N_311 = ders[1, 3]  # ПЕРВЫЕ ПРОИЗВОДНЫЕ
N_021 = ders[2, 0];  N_121 = ders[2, 1];  N_221 = ders[2, 2];  N_321 = ders[2, 3]  # ВТОРЫЕ ПРОИЗВОДНЫЕ
N_031 = ders[3, 0];  N_131 = ders[3, 1];  N_231 = ders[3, 2];  N_331 = ders[3, 3]  # ТРЕТЬИ ПРОИЗВОДНЫЕ

u0 = 0.0 # # Начальная  ТОЧКА НА Q-кривой, для неё расчитываем 1. Базис. функции и 2. Три произв. Базис. Функций == ТОЧКА СОПРЯЖЕНИЯ
span = Func_1.FindSpan(n_vert, p, u0, U)
Func_1.DersBasisFuns(span, u0, p, p, U, ders)
print("*u0=", u0, "  ders=\n", ders)

#  Производные БАЗИСНЫх ФУНКЦИИ в начальной  точке  Q-кривой
N_000 = ders[0, 0];  N_100 = ders[0, 1];  N_200 = ders[0, 2];  N_300 = ders[0, 3]  # НУЛЕВЫЕ ПРОИЗВОДНЫЕ = сама функция
N_010 = ders[1, 0];  N_110 = ders[1, 1];  N_210 = ders[1, 2];  N_310 = ders[1, 3]  # ПЕРВЫЕ ПРОИЗВОДНЫЕ
N_020 = ders[2, 0];  N_120 = ders[2, 1];  N_220 = ders[2, 2];  N_320 = ders[2, 3]  # ВТОРЫЕ ПРОИЗВОДНЫЕ
N_030 = ders[3, 0];  N_130 = ders[3, 1];  N_230 = ders[3, 2];  N_330 = ders[3, 3]  # ТРЕТЬИ ПРОИЗВОДНЫЕ
