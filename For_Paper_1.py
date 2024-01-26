# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 14:56:12 2021

@author: Сергей Валентинович
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st
import math


colors = ['']*13

colors[0]  ='b' #Синий
colors[1]  ='g' #Зелёный
colors[2]  ='r' #Красный
colors[3]  ='с' #Бирюзовый
colors[4]  ='b' #Фиолетовый / Пурпурный
colors[5]  ='y' #Желтый
colors[6]  ='k' #Черный
colors[7]  ='w' #Белый
colors[8]  ='goldenrod' # См. Полную Таблицу Цветов в Mathplotlib
colors[9]  ='grey' #Серый
colors[10] ='magenta' #Пурпурно-Красный
colors[11] ='floralwhite' #См. Полную Таблицу Цветов в Mathplotlib


print('  ')
print('  ')
print('  ')
print('  ')
print('********************************************************')
print('********************************************************')
print('********************************************************')

print (np.pi,'  ',np.sin(np.pi/6))



import Func_1
import Plots_1
import Input_Data



#%% = Начало Блока.  Если блок Выделить, то его можно выполнить Ctrl + Enter
#************************************************************************
#************************************************************************
#************************************************************************

# ГЛАДКОЕ СОПРЯЖЕНИЕ 2-х БЕЗЬЕ 3-ей степени
# НАЧАЛО БЛОКА -  Дискретная Коэффициентная Метрика




# Строим контрольный многоугольник и Куб. Сплайн из Piegl, Fig. 5.18 и Fig. 5.19

#Input_Data.Input_P_Q_Fig_2a_Hu_SM_2001__1(P,HP,Q,HQ,R,HR);


P = np.zeros([4,2])
HP = np.zeros([4])
HP=[1,1,1,1]

Q = np.zeros([4,2])
HQ = np.zeros([4])
HQ=[1,1,1,1]


P[0,:]=[2.5,0]
P[1,:]=[3.33,2.5]
P[2,:]=[5.7, 3.7]
P[3,:]=[6.6-0.1,3.7-0.2]


Q[0,:]=[6.6-0.1,3.7+0.4]
Q[1,:]=[11,4.5]
Q[2,:]=[14,3.3]
Q[3,:]=[19,1]


R= np.zeros([4,2])
HR = np.zeros([4])
HR=[1,1,1,1]

print("*P=\n",P)


n_vert=np.shape(P)[0]-1
print("** n_vert=",n_vert)



#Input_Data.

# Расчет Кубич. Сплайна
p=3
m_not=n_vert+1+p;    
print("*1* p=",p," n_vert=",n_vert," m_not=",m_not)  

U = np.zeros([m_not+1]); 
Input_Data.Calculation_U_Open_Uniform(p,n_vert,m_not,U)  
u_start1=U[p] 
u_stop1=U[n_vert+1]
print("*U=",U,"\n u_start1=",u_start1," (index_start=",p,") u_stop1=",u_stop1, " (index_stop=",n_vert+1,")")

V = np.zeros([m_not+1]);                 
Input_Data.Calculation_U_Open_Uniform(p,n_vert,m_not,V) 
v_start1=V[p] 
v_stop1=V[n_vert+1]
print("*V=",V,"\n v_start1=",v_start1," (index_start=",p,") v_stop1=",v_stop1, " (index_stop=",n_vert+1,")")

T = np.zeros([m_not+1]);                 
Input_Data.Calculation_U_Open_Uniform(p,n_vert,m_not,T) 
t_start1=T[p] 
t_stop1=T[n_vert+1]
print("*T=",T,"\n t_start1=",t_start1," (index_start=",p,") t_stop1=",t_stop1, " (index_stop=",n_vert+1,")")

##################################################################################################################
# Расчет Первой Безье-крив. (=Р - кривая) 
#  ders - для заданного "u" массив BASIS функций и  все их (до р) производныЕ
ders_p1 = np.zeros([p+1,p+1])

# C2 - массив, в нем для заданного "u" возвращаются C2[0,:]- x,y - сплайна
#                               для заданного "u"  C2[1,:]- x,y - 1-вой ПРОИЗВОДНОЙ сплайна
#                               для заданного "u"  C2[0,:]- x,y - 2-ой ПРОИЗВОДНОЙ сплайна
#                               для заданного "u"  C2[p,:]- x,y -"p"-ой ПРОИЗВОДНОЙ сплайна
C2_NURBS_p1=np.zeros([p+1,2]) # идекс "2" для 2D задачи, "3" - для 3D

n_u1=60
data_CurvePoin_and_Deriv_NURBS_p1 = np.zeros([(n_u1+1),(p+1),2])


for iu in range(n_u1+1):
    u_i=(iu/n_u1)*(u_stop1-u_start1) +  u_start1
    
    Func_1.CurvePoin_and_Deriv_NURBS(n_vert,p,U,P,HP,u_i,C2_NURBS_p1,ders_p1)
    # В массиве на след. строке Хранятся Кубич. Сплайн
    data_CurvePoin_and_Deriv_NURBS_p1[iu,:,:]=C2_NURBS_p1

##################################################################################################################




##################################################################################################################
# Расчет Второрй Безье-крив. (=Q - кривая) 
#  ders - для заданного "u" массив BASIS функций и  все их (до р) производныЕ
ders_p2 = np.zeros([p+1,p+1])

# C2 - массив, в нем для заданного "u" возвращаются C2[0,:]- x,y - сплайна
#                               для заданного "u"  C2[1,:]- x,y - 1-вой ПРОИЗВОДНОЙ сплайна
#                               для заданного "u"  C2[0,:]- x,y - 2-ой ПРОИЗВОДНОЙ сплайна
#                               для заданного "u"  C2[p,:]- x,y -"p"-ой ПРОИЗВОДНОЙ сплайна
C2_NURBS_p2=np.zeros([p+1,2]) # идекс "2" для 2D задачи, "3" - для 3D

n_u2=60
data_CurvePoin_and_Deriv_NURBS_p2 = np.zeros([(n_u2+1),(p+1),2])


for iv in range(n_u2+1):
    v_i=(iv/n_u2)*(v_stop1-v_start1) +  v_start1
    
    Func_1.CurvePoin_and_Deriv_NURBS(n_vert,p,V,Q,HQ,v_i,C2_NURBS_p2,ders_p2)
    # В массиве на след. строке Хранятся Кубич. Сплайн
    data_CurvePoin_and_Deriv_NURBS_p2[iv,:,:]=C2_NURBS_p2

##################################################################################################################






Title="Исходные данные Для СОПРЯЖЕНИЯ- 2 Безье 3-й Степени"
Title=' '

labels_legend1="P Многоугольник"
labels_legend2="P Безье Кривая"
labels_legend3="Q Многоугольник"
labels_legend4="Q Безье Кривая"


y_min=-1; y_max=7.0
x_min=0; x_max=20

Plots_1.plot_Trace_Lines_2_for_Mergin_a (P[:,0],P[:,1],
                                         Q[:,0],Q[:,1],
                                        
                                            data_CurvePoin_and_Deriv_NURBS_p1[:,0,0],data_CurvePoin_and_Deriv_NURBS_p1[:,0,1] ,                             
                                            data_CurvePoin_and_Deriv_NURBS_p2[:,0,0],data_CurvePoin_and_Deriv_NURBS_p2[:,0,1] ,
                                            
                                           
                                               y_min, y_max, x_min, x_max,
                                               Title, labels_legend1, labels_legend2,
                                                labels_legend3, labels_legend4)




#stop
########################################################################################################################################
########################################################################################################################################
########################################################################################################################################


#************************************************************************
#%% = Окончание Блока.  Если блок Выделить, то его можно выполнить Ctrl + Enter



# Начало Блока ДИСКРЕТ. НОРМА 



#%% = Начало Блока.  Если блок Выделить, то его можно выполнить Ctrl + Enter
#************************************************************************
#************************************************************************
#************************************************************************


# Блок ДИСКРЕТ. НОРМА  без Ограничений 


Eps1 = np.zeros([4,2])
Del1 = np.zeros([4,2])
Lam1 = np.zeros([4,2])
X1 = np.zeros([12,2])
X1_1 = np.zeros([12,2])
Matrix_A1= np.zeros([12,12]) 
Matrix_B1= np.zeros([12,2])

p=3
ders = np.zeros([p+1,p+1]) # массив, в котором - в 1-ой строке - Базисные Функции
                           #                   -   2-строка - первые Производ. Базисных Функции 
                           #                       3-строка - вторые Производ. Базисных Функции и т.д. ........

u0=1.0 # Конечна ТОЧКА НА Р-кривой, для неё расчитываем 1. Базис. функции и 2. Три произв. Базис. Функций == ТОЧКА СОПРЯЖЕНИЯ
span = Func_1.FindSpan(n_vert,p,u0,U);
Func_1.DersBasisFuns(span,u0,p,p,U,ders)
print("*u0=",u0, "  ders=\n",ders)

#  Производные БАЗИСНЫх ФУНКЦИИ в конечной точке  Р-кривой

N_001= ders[0,0];   N_101= ders[0,1]; N_201= ders[0,2]; N_301= ders[0,3] # НУЛЕВЫЕ ПРОИЗВОДНЫЕ = сама функция
N_011= ders[1,0];   N_111= ders[1,1]; N_211= ders[1,2]; N_311= ders[1,3] # ПЕРВЫЕ ПРОИЗВОДНЫЕ
N_021= ders[2,0];   N_121= ders[2,1]; N_221= ders[2,2]; N_321= ders[2,3] # ВТОРЫЕ ПРОИЗВОДНЫЕ
N_031= ders[3,0];   N_131= ders[3,1]; N_231= ders[3,2]; N_331= ders[3,3] # ТРЕТЬИ ПРОИЗВОДНЫЕ

#stop

u0=0.0 # # Начальная  ТОЧКА НА Q-кривой, для неё расчитываем 1. Базис. функции и 2. Три произв. Базис. Функций == ТОЧКА СОПРЯЖЕНИЯ
span = Func_1.FindSpan(n_vert,p,u0,U);
Func_1.DersBasisFuns(span,u0,p,p,U,ders)
print("*u0=",u0, "  ders=\n",ders)
#  Производные БАЗИСНЫх ФУНКЦИИ в начальной  точке  Q-кривой
N_000= ders[0,0];   N_100= ders[0,1]; N_200= ders[0,2]; N_300= ders[0,3] # НУЛЕВЫЕ ПРОИЗВОДНЫЕ = сама функция
N_010= ders[1,0];   N_110= ders[1,1]; N_210= ders[1,2]; N_310= ders[1,3] # ПЕРВЫЕ ПРОИЗВОДНЫЕ
N_020= ders[2,0];   N_120= ders[2,1]; N_220= ders[2,2]; N_320= ders[2,3] # ВТОРЫЕ ПРОИЗВОДНЫЕ
N_030= ders[3,0];   N_130= ders[3,1]; N_230= ders[3,2]; N_330= ders[3,3] # ТРЕТЬИ ПРОИЗВОДНЫЕ

#stop
####################################################################################################################
####################################################################################################################

# **!! ЭТО МАТРИЦА ДЛЯ НЕзакрепленныз (СВОБОДНЫХ) ГРАНИЦ
#      ДИСРЕТНАЯ НОРМА


Matrix_A1[0,0]=2;  Matrix_A1[0,8]=N_001; Matrix_A1[0,9]=N_011;  Matrix_A1[0,10]=N_021;  Matrix_A1[0,11]=N_031
Matrix_A1[1,1]=2;  Matrix_A1[1,8]=N_101; Matrix_A1[1,9]=N_111;  Matrix_A1[1,10]=N_121;  Matrix_A1[1,11]=N_131
Matrix_A1[2,2]=2;  Matrix_A1[2,8]=N_201; Matrix_A1[2,9]=N_211;  Matrix_A1[2,10]=N_221;  Matrix_A1[2,11]=N_231
Matrix_A1[3,3]=2;  Matrix_A1[3,8]=N_301; Matrix_A1[3,9]=N_311;  Matrix_A1[3,10]=N_321;  Matrix_A1[3,11]=N_331

Matrix_A1[4,4]=2;  Matrix_A1[4,8]=-N_000; Matrix_A1[4,9]=-N_010;  Matrix_A1[4,10]=-N_020;  Matrix_A1[4,11]=-N_030
Matrix_A1[5,5]=2;  Matrix_A1[5,8]=-N_100; Matrix_A1[5,9]=-N_110;  Matrix_A1[5,10]=-N_120;  Matrix_A1[5,11]=-N_130
Matrix_A1[6,6]=2;  Matrix_A1[6,8]=-N_200; Matrix_A1[6,9]=-N_210;  Matrix_A1[6,10]=-N_220;  Matrix_A1[6,11]=-N_230
Matrix_A1[7,7]=2;  Matrix_A1[7,8]=-N_300; Matrix_A1[7,9]=-N_310;  Matrix_A1[7,10]=-N_320;  Matrix_A1[7,11]=-N_330

Matrix_A1[8,0] =N_001; Matrix_A1[8,1] =N_101;  Matrix_A1[8,2] =N_201;  Matrix_A1[8,3] =N_301; Matrix_A1[8,4] =-N_000;  Matrix_A1[8,5] =-N_100;  Matrix_A1[8,6] =-N_200;  Matrix_A1[8,7] =-N_300;
Matrix_A1[9,0] =N_011; Matrix_A1[9,1] =N_111;  Matrix_A1[9,2] =N_211;  Matrix_A1[9,3] =N_311; Matrix_A1[9,4] =-N_010;  Matrix_A1[9,5] =-N_110;  Matrix_A1[9,6] =-N_210;  Matrix_A1[9,7] =-N_310;
Matrix_A1[10,0]=N_021; Matrix_A1[10,1]=N_121;  Matrix_A1[10,2]=N_221;  Matrix_A1[10,3]=N_321; Matrix_A1[10,4]=-N_020;  Matrix_A1[10,5]=-N_120;  Matrix_A1[10,6]=-N_220;  Matrix_A1[10,7]=-N_320;
Matrix_A1[11,0]=N_031; Matrix_A1[11,1]=N_131;  Matrix_A1[11,2]=N_231;  Matrix_A1[11,3]=N_331; Matrix_A1[11,4]=-N_030;  Matrix_A1[11,5]=-N_130;  Matrix_A1[11,6]=-N_230;  Matrix_A1[11,7]=-N_330;




Matrix_B1[8,:]  = -P[0,:]*N_001 + Q[0,:]*N_000  -P[1,:]*N_101 + Q[1,:]*N_100  -P[2,:]*N_201 + Q[2,:]*N_200  -P[3,:]*N_301 + Q[3,:]*N_300
Matrix_B1[9,:]  = -P[0,:]*N_011 + Q[0,:]*N_010  -P[1,:]*N_111 + Q[1,:]*N_110  -P[2,:]*N_211 + Q[2,:]*N_210  -P[3,:]*N_311 + Q[3,:]*N_310
Matrix_B1[10,:] = -P[0,:]*N_021 + Q[0,:]*N_020  -P[1,:]*N_121 + Q[1,:]*N_120  -P[2,:]*N_221 + Q[2,:]*N_220  -P[3,:]*N_321 + Q[3,:]*N_320
Matrix_B1[11,:] = -P[0,:]*N_031 + Q[0,:]*N_030  -P[1,:]*N_131 + Q[1,:]*N_130  -P[2,:]*N_231 + Q[2,:]*N_230  -P[3,:]*N_331 + Q[3,:]*N_330

print("* Matrix_A1\n",Matrix_A1)
print("* Matrix_B1\n",Matrix_B1)
#stop

print("*** РЕШЕНИЕ *СЛАУ* ДЛЯ НЕзакрепленных ГРАНИЦ ***")
print("\n det(Matrix_A1)=", np.linalg.det(Matrix_A1))
print(" rank(Matrix_A1)=", np.linalg.matrix_rank(Matrix_A1))
print(" число Обусловленности(Matrix_A1)=", np.linalg.cond(Matrix_A1))
print(" rank(A1_&_B1)= ", np.linalg.matrix_rank(np.hstack((Matrix_A1,Matrix_B1))))
print(" число Обусловленности(A1&_B1=", np.linalg.cond(np.hstack((Matrix_A1,Matrix_B1))))



X1= np.linalg.solve(Matrix_A1, Matrix_B1)
print("***Решение системы:\n",X1)

#Lam = np.linalg.solve(Matrix_A, Matrix_B)
X1_1, res, r, s = np.linalg.lstsq(Matrix_A1, Matrix_B1, rcond=None)
print ("***Псевдорешение системы:\n", X1_1)


print ("Число Сочетаний -- math.comb(3, 2)= ",math.comb(3, 2))

Eps1=X1_1[0:4,:]
Del1=X1_1[4:8,:]




#Mu=1
#Lam_Scalar=Mu/(1+Mu) 
Lam_Scalar=0.5 
Lam_Scalar=0.5
P_0=P+Eps1
P_1 = np.zeros([4,2])
P_2 = np.zeros([4,2])
P_3 = np.zeros([4,2])

P_0_0=P[0,:]+Eps1[0,:]
P_0_1=P[1,:]+Eps1[1,:]
P_0_2=P[2,:]+Eps1[2,:]
P_0_3=P[3,:]+Eps1[3,:]

        
P_1_1=(1-1/Lam_Scalar)*P_0_0 +  (1/Lam_Scalar)*P_0_1      
P_1_2=(1-1/Lam_Scalar)*P_0_1 +  (1/Lam_Scalar)*P_0_2
P_1_3=(1-1/Lam_Scalar)*P_0_2 +  (1/Lam_Scalar)*P_0_3

P_2_2=(1-1/Lam_Scalar)*P_1_1 +  (1/Lam_Scalar)*P_1_2
P_2_3=(1-1/Lam_Scalar)*P_1_2 +  (1/Lam_Scalar)*P_1_3

P_3_3=(1-1/Lam_Scalar)*P_2_2 +  (1/Lam_Scalar)*P_2_3

R[0,:]=P_0_0
R[1,:]=P_1_1
R[2,:]=P_2_2
R[3,:]=P_3_3




##################################################################################################################
# Расчет Первой-НОВОЙ Безье-крив. (=P_с_Крышкой ) 
P_Krish=P+Eps1

#  ders - для заданного "u" массив BASIS функций и  все их (до р) производныЕ
ders_p3 = np.zeros([p+1,p+1])

# C2 - массив, в нем для заданного "u" возвращаются C2[0,:]- x,y - сплайна
#                               для заданного "u"  C2[1,:]- x,y - 1-вой ПРОИЗВОДНОЙ сплайна
#                               для заданного "u"  C2[0,:]- x,y - 2-ой ПРОИЗВОДНОЙ сплайна
#                               для заданного "u"  C2[p,:]- x,y -"p"-ой ПРОИЗВОДНОЙ сплайна
C2_NURBS_p3=np.zeros([p+1,2]) # идекс "2" для 2D задачи, "3" - для 3D

n_u3=60
data_CurvePoin_and_Deriv_NURBS_P_Krish = np.zeros([(n_u3+1),(p+1),2])

#stop

for it in range(n_u3+1):
    t_i=(it/n_u2)*(t_stop1-t_start1) +  t_start1
    
    Func_1.CurvePoin_and_Deriv_NURBS(n_vert,p,T,P_Krish,HP,t_i,C2_NURBS_p3,ders_p3)
    # В массиве на след. строке Хранятся Кубич. Сплайн
    data_CurvePoin_and_Deriv_NURBS_P_Krish[it,:,:]=C2_NURBS_p3

##################################################################################################################
#stop

##################################################################################################################
# Расчет Второй-НОВОЙ Безье-крив. (=Q_с_Крышкой) 
Q_Krish=Q+Del1

#  ders - для заданного "u" массив BASIS функций и  все их (до р) производныЕ
ders_p3 = np.zeros([p+1,p+1])

# C2 - массив, в нем для заданного "u" возвращаются C2[0,:]- x,y - сплайна
#                               для заданного "u"  C2[1,:]- x,y - 1-вой ПРОИЗВОДНОЙ сплайна
#                               для заданного "u"  C2[0,:]- x,y - 2-ой ПРОИЗВОДНОЙ сплайна
#                               для заданного "u"  C2[p,:]- x,y -"p"-ой ПРОИЗВОДНОЙ сплайна
C2_NURBS_p3=np.zeros([p+1,2]) # идекс "2" для 2D задачи, "3" - для 3D

n_u3=60
data_CurvePoin_and_Deriv_NURBS_Q_Krish = np.zeros([(n_u1+1),(p+1),2])



for it in range(n_u3+1):
    t_i=(it/n_u2)*(t_stop1-t_start1) +  t_start1
    
    Func_1.CurvePoin_and_Deriv_NURBS(n_vert,p,T,Q_Krish,HQ,t_i,C2_NURBS_p3,ders_p3)
    # В массиве на след. строке Хранятся Кубич. Сплайн
    data_CurvePoin_and_Deriv_NURBS_Q_Krish[it,:,:]=C2_NURBS_p3

##################################################################################################################


#stop





Title=" *0*11"
#Title=" "
labels_legend1="P Многоугольник (заданный)"
labels_legend2="P Безье Кривая (заданная)"

labels_legend3="Многоугольник Р с крышкой"
labels_legend4="P с крышкой"

labels_legend5="Q Многоугольник (заданный)"
labels_legend6="Q Безье Кривая (заданная)"

labels_legend7="Многоугольник Q с крышкой"
labels_legend8="Q с крышкой"

#y_min=-1
#y_max=40.0

#x_min=-1
#x_max=90


#   ГРАФИК для ОТЧЕТА-СТАТЬИ - ДИСКРЕТ. НОРМА
Plots_1.plot_Trace_Lines_4_for_Mergin_1 (P[:,0],P[:,1],
                                         P_Krish[:,0],P_Krish[:,1],
                                         Q[:,0],Q[:,1],
                                       Q_Krish[:,0],Q_Krish[:,1],
                                            data_CurvePoin_and_Deriv_NURBS_p1[:,0,0],data_CurvePoin_and_Deriv_NURBS_p1[:,0,1] ,  
                                             data_CurvePoin_and_Deriv_NURBS_P_Krish[:,0,0],    data_CurvePoin_and_Deriv_NURBS_P_Krish[:,0,1],
                                            data_CurvePoin_and_Deriv_NURBS_p2[:,0,0],data_CurvePoin_and_Deriv_NURBS_p2[:,0,1] ,
                                              data_CurvePoin_and_Deriv_NURBS_Q_Krish[:,0,0],    data_CurvePoin_and_Deriv_NURBS_Q_Krish[:,0,1], 
                                           
                                               y_min, y_max, x_min, x_max,
                                               Title, labels_legend1, labels_legend2,
                                                labels_legend3, labels_legend4,labels_legend5,labels_legend6,labels_legend7,labels_legend8)










##################################################################################################################
# Расчет Третьей Безье-крив. (=R - кривая) 
#  ders - для заданного "u" массив BASIS функций и  все их (до р) производныЕ
ders_p3 = np.zeros([p+1,p+1])

# C2 - массив, в нем для заданного "u" возвращаются C2[0,:]- x,y - сплайна
#                               для заданного "u"  C2[1,:]- x,y - 1-вой ПРОИЗВОДНОЙ сплайна
#                               для заданного "u"  C2[0,:]- x,y - 2-ой ПРОИЗВОДНОЙ сплайна
#                               для заданного "u"  C2[p,:]- x,y -"p"-ой ПРОИЗВОДНОЙ сплайна
C2_NURBS_R=np.zeros([p+1,2]) # идекс "2" для 2D задачи, "3" - для 3D

n_u3=60
data_CurvePoin_and_Deriv_NURBS_R = np.zeros([(n_u3+1),(p+1),2])


for it in range(n_u3+1):
    t_i=(it/n_u2)*(t_stop1-t_start1) +  t_start1
    
    Func_1.CurvePoin_and_Deriv_NURBS(n_vert,p,T,R,HR,t_i,C2_NURBS_R,ders_p3)
    # В массиве на след. строке Хранятся Кубич. Сплайн
    data_CurvePoin_and_Deriv_NURBS_R[it,:,:]=C2_NURBS_R

##################################################################################################################

#stop



Title="Окончательное решение - ДИСКРЕТ. НОРМА *** ОБЕ КОНЕЧНЫЕ ТОЧКИ НЕзафиксированы (СВОБОДНЫЕ) ***"
Title="1*11 "

labels_legend1="P Многоугольник (заданный)"
labels_legend2="P Безье Кривая (заданная)"
labels_legend3="Q Многоугольник (заданный)"
labels_legend4="Q Безье Кривая (заданная)"
labels_legend5="R Многоугольник (апроксимация Р и Q)"
labels_legend6="R Безье Кривая (апроксимация Р и Q)"




#   ГРАФИК для ОТЧЕТА-СТАТЬИ - ДИСКРЕТ. НОРМА
# 
Plots_1.plot_Trace_Lines_3_for_Mergin_1 (P[:,0],P[:,1],
                                         Q[:,0],Q[:,1],
                                         R[:,0],R[:,1],
                                            data_CurvePoin_and_Deriv_NURBS_p1[:,0,0],data_CurvePoin_and_Deriv_NURBS_p1[:,0,1] ,                             
                                            data_CurvePoin_and_Deriv_NURBS_p2[:,0,0],data_CurvePoin_and_Deriv_NURBS_p2[:,0,1] ,
                                            data_CurvePoin_and_Deriv_NURBS_R[:,0,0],data_CurvePoin_and_Deriv_NURBS_R[:,0,1] ,    
                                           
                                               y_min, y_max, x_min, x_max,
                                               Title, labels_legend1, labels_legend2,
                                                labels_legend3, labels_legend4,labels_legend5,labels_legend6)









#stop


#
#   ВЫДЕЛЕНИЕ ИЗ Кривой R кривой  X22
#
X22 = np.zeros([4,2])

Matrix_A22= np.zeros([4,4]) 
Matrix_B22= np.zeros([4,2])

Lam=0.5
ders_p3_0 = np.zeros([p+1,p+1])
ders_p3_Lam = np.zeros([p+1,p+1])
ders_p3_1 = np.zeros([p+1,p+1])

Func_1.CurvePoin_and_Deriv_NURBS(n_vert,p,T,P_Krish,HP,0.0,C2_NURBS_p3,ders_p3_0)
Func_1.CurvePoin_and_Deriv_NURBS(n_vert,p,T,P_Krish,HP,Lam,C2_NURBS_p3,ders_p3_Lam)
Func_1.CurvePoin_and_Deriv_NURBS(n_vert,p,T,P_Krish,HP,1.0,C2_NURBS_p3,ders_p3_1)






Matrix_A22[0,0]=ders_p3_0[0,0];    Matrix_A22[0,1]=ders_p3_0[0,1];    Matrix_A22[0,2]=ders_p3_0[0,2];    Matrix_A22[0,3]=ders_p3_0[0,3];
Matrix_A22[1,0]=ders_p3_0[1,0];    Matrix_A22[1,1]=ders_p3_0[1,1];    Matrix_A22[1,2]=ders_p3_0[1,2];    Matrix_A22[1,3]=ders_p3_0[1,3];
Matrix_A22[2,0]=ders_p3_1[0,0];    Matrix_A22[2,1]=ders_p3_1[0,1];    Matrix_A22[2,2]=ders_p3_1[0,2];    Matrix_A22[2,3]=ders_p3_1[0,3];
Matrix_A22[3,0]=ders_p3_1[1,0];    Matrix_A22[3,1]=ders_p3_1[1,1];    Matrix_A22[3,2]=ders_p3_1[1,2];    Matrix_A22[3,3]=ders_p3_1[1,3];



Matrix_B22[0,:]  =      (R[0,:]*ders_p3_0[0,0]   + R[1,:]*ders_p3_0[0,1]   + R[2,:]*ders_p3_0[0,2]   + R[3,:]*ders_p3_0[0,3])
Matrix_B22[1,:]  = Lam* (R[0,:]*ders_p3_0[1,0]   + R[1,:]*ders_p3_0[1,1]   + R[2,:]*ders_p3_0[1,2]   + R[3,:]*ders_p3_0[1,3])
Matrix_B22[2,:]  =      (R[0,:]*ders_p3_Lam[0,0] + R[1,:]*ders_p3_Lam[0,1] + R[2,:]*ders_p3_Lam[0,2] + R[3,:]*ders_p3_Lam[0,3])
Matrix_B22[3,:]  = Lam* (R[0,:]*ders_p3_Lam[1,0] + R[1,:]*ders_p3_Lam[1,1] + R[2,:]*ders_p3_Lam[1,2] + R[3,:]*ders_p3_Lam[1,3])








print("*** 333 *** РЕШЕНИЕ *СЛАУ* ДЛЯ НЕзакрепленных ГРАНИЦ ***")
print("\n det(Matrix_A22)=", np.linalg.det(Matrix_A22))
print(" rank(Matrix_A22)=", np.linalg.matrix_rank(Matrix_A22))
print(" число Обусловленности(Matrix_A22)=", np.linalg.cond(Matrix_A22))
print(" rank(A22_&_B22)= ", np.linalg.matrix_rank(np.hstack((Matrix_A22,Matrix_B22))))
print(" число Обусловленности(A22&_B22=", np.linalg.cond(np.hstack((Matrix_A22,Matrix_B22))))

X22= np.linalg.solve(Matrix_A22, Matrix_B22)
print("***Решение системы:\n",X22)

# Решение НеСогласованной Системы
X22, res, r, s = np.linalg.lstsq(Matrix_A22, Matrix_B22, rcond=None)
print("***Решение системы НЕСОГЛАСОВАННОЕ:\n",X22)

print((R[0,:]*ders_p3_0[0,0]   + R[1,:]*ders_p3_0[0,1]   + R[2,:]*ders_p3_0[0,2]   + R[3,:]*ders_p3_0[0,3]),  (X22[0,:]*ders_p3_0[0,0]   + X22[1,:]*ders_p3_0[0,1]   + X22[2,:]*ders_p3_0[0,2]   + X22[3,:]*ders_p3_0[0,3]))
print((R[0,:]*ders_p3_0[1,0]   + R[1,:]*ders_p3_0[1,1]   + R[2,:]*ders_p3_0[1,2]   + R[3,:]*ders_p3_0[1,3]),  (X22[0,:]*ders_p3_0[1,0]   + X22[1,:]*ders_p3_0[1,1]   + X22[2,:]*ders_p3_0[1,2]   + X22[3,:]*ders_p3_0[1,3]))
print((R[0,:]*ders_p3_0[2,0]   + R[1,:]*ders_p3_0[2,1]   + R[2,:]*ders_p3_0[2,2]   + R[3,:]*ders_p3_0[2,3]),  (X22[0,:]*ders_p3_0[2,0]   + X22[1,:]*ders_p3_0[2,1]   + X22[2,:]*ders_p3_0[2,2]   + X22[3,:]*ders_p3_0[2,3]))
print((R[0,:]*ders_p3_0[3,0]   + R[1,:]*ders_p3_0[3,1]   + R[2,:]*ders_p3_0[3,2]   + R[3,:]*ders_p3_0[3,3]),  (X22[0,:]*ders_p3_0[3,0]   + X22[1,:]*ders_p3_0[3,1]   + X22[2,:]*ders_p3_0[3,2]   + X22[3,:]*ders_p3_0[3,3]))



##################################################################################################################
# Расчет Третьей Безье-крив. (=R - кривая) 
#  ders - для заданного "u" массив BASIS функций и  все их (до р) производныЕ
ders_p3 = np.zeros([p+1,p+1])

# C2 - массив, в нем для заданного "u" возвращаются C2[0,:]- x,y - сплайна
#                               для заданного "u"  C2[1,:]- x,y - 1-вой ПРОИЗВОДНОЙ сплайна
#                               для заданного "u"  C2[0,:]- x,y - 2-ой ПРОИЗВОДНОЙ сплайна
#                               для заданного "u"  C2[p,:]- x,y -"p"-ой ПРОИЗВОДНОЙ сплайна
C2_NURBS_p3=np.zeros([p+1,2]) # идекс "2" для 2D задачи, "3" - для 3D

n_u3=60
data_CurvePoin_and_Deriv_NURBS_X22 = np.zeros([(n_u3+1),(p+1),2])


for it in range(n_u3+1):
    t_i=(it/n_u2)*(t_stop1-t_start1) +  t_start1
    
    Func_1.CurvePoin_and_Deriv_NURBS(n_vert,p,T,X22,HR,t_i,C2_NURBS_p3,ders_p3)
    # В массиве на след. строке Хранятся Кубич. Сплайн
    data_CurvePoin_and_Deriv_NURBS_X22[it,:,:]=C2_NURBS_p3

##################################################################################################################




Title="** СРАВНЕНИЕ X22 и R   ***"
#Title=" **333"

labels_legend1="X22 Безье Кривая"
labels_legend2="R  Безье Кривая"



Array_0=Q_Krish
Array_0[:,:]=0
data_CurvePoin_and_Deriv_NURBS_p2[:,:,:]=0

#   ГРАФИК для ОТЧЕТА-СТАТЬИ - ДИСКРЕТ. НОРМА
# 
Plots_1.plot_Trace_Lines_2_for_Mergin_12 (  data_CurvePoin_and_Deriv_NURBS_X22[:,0,0],data_CurvePoin_and_Deriv_NURBS_X22[:,0,1],
                                            data_CurvePoin_and_Deriv_NURBS_R[:,0,0],data_CurvePoin_and_Deriv_NURBS_R[:,0,1] ,    
                                           
                                               y_min, y_max, x_min, x_max,
                                               Title, labels_legend1, labels_legend2)



#
#   ОКОНЧАНИЕ ВЫДЕЛЕНИЯ ИЗ Кривой R кривой X22
#



#   НАЧАЛО
#   Апроксимация 2-х полностью сопряженных кривых (P_c_крышкой и Q_c_крышкой)  R кривой  
#
R = np.zeros([4,2])

Matrix_A22= np.zeros([4,4]) 
Matrix_B22= np.zeros([4,2])

Lam=0.5

ders_p3_0 = np.zeros([p+1,p+1])
ders_p3_Lam = np.zeros([p+1,p+1])
ders_p3_1 = np.zeros([p+1,p+1])

Func_1.CurvePoin_and_Deriv_NURBS(n_vert,p,T,P_Krish,HP,0.0,C2_NURBS_p3,ders_p3_0)
Func_1.CurvePoin_and_Deriv_NURBS(n_vert,p,T,P_Krish,HP,Lam,C2_NURBS_p3,ders_p3_Lam)
Func_1.CurvePoin_and_Deriv_NURBS(n_vert,p,T,P_Krish,HP,1.0,C2_NURBS_p3,ders_p3_1)






Matrix_A22[0,0]=ders_p3_0[0,0];    Matrix_A22[0,1]=ders_p3_0[0,1];    Matrix_A22[0,2]=ders_p3_0[0,2];    Matrix_A22[0,3]=ders_p3_0[0,3];
Matrix_A22[1,0]=ders_p3_0[1,0]*Lam;    Matrix_A22[1,1]=ders_p3_0[1,1]*Lam;    Matrix_A22[1,2]=ders_p3_0[1,2]*Lam;    Matrix_A22[1,3]=ders_p3_0[1,3]*Lam;

Matrix_A22[2,0]=ders_p3_Lam[0,0];    Matrix_A22[2,1]=ders_p3_Lam[0,1];    Matrix_A22[2,2]=ders_p3_Lam[0,2];    Matrix_A22[2,3]=ders_p3_Lam[0,3];
Matrix_A22[3,0]=ders_p3_Lam[1,0]*Lam;    Matrix_A22[3,1]=ders_p3_Lam[1,1]*Lam;    Matrix_A22[3,2]=ders_p3_Lam[1,2]*Lam;    Matrix_A22[3,3]=ders_p3_Lam[1,3]*Lam;




Matrix_B22[0,:]  =      (P_Krish[0,:]*ders_p3_0[0,0]   + P_Krish[1,:]*ders_p3_0[0,1]   + P_Krish[2,:]*ders_p3_0[0,2]   + P_Krish[3,:]*ders_p3_0[0,3])
Matrix_B22[1,:]  =      (P_Krish[0,:]*ders_p3_0[1,0]   + P_Krish[1,:]*ders_p3_0[1,1]   + P_Krish[2,:]*ders_p3_0[1,2]   + P_Krish[3,:]*ders_p3_0[1,3])
Matrix_B22[2,:]  =      (P_Krish[0,:]*ders_p3_1[0,0] + P_Krish[1,:]*ders_p3_1[0,1] + P_Krish[2,:]*ders_p3_1[0,2] + P_Krish[3,:]*ders_p3_1[0,3])
Matrix_B22[3,:]  =      (P_Krish[0,:]*ders_p3_1[1,0] + P_Krish[1,:]*ders_p3_1[1,1] + P_Krish[2,:]*ders_p3_1[1,2] + P_Krish[3,:]*ders_p3_1[1,3])








print("*** 333 *** РЕШЕНИЕ *СЛАУ* ДЛЯ НЕзакрепленных ГРАНИЦ ***")
print("\n det(Matrix_A22)=", np.linalg.det(Matrix_A22))
print(" rank(Matrix_A22)=", np.linalg.matrix_rank(Matrix_A22))
print(" число Обусловленности(Matrix_A22)=", np.linalg.cond(Matrix_A22))
print(" rank(A22_&_B22)= ", np.linalg.matrix_rank(np.hstack((Matrix_A22,Matrix_B22))))
print(" число Обусловленности(A22&_B22=", np.linalg.cond(np.hstack((Matrix_A22,Matrix_B22))))

X22= np.linalg.solve(Matrix_A22, Matrix_B22)
print("***Решение системы:\n",X22)

# Решение НеСогласованной Системы
X22, res, r, s = np.linalg.lstsq(Matrix_A22, Matrix_B22, rcond=None)
print("***Решение системы НЕСОГЛАСОВАННОЕ:\n",X22)

print((P_Krish[0,:]*ders_p3_0[0,0]   + P_Krish[1,:]*ders_p3_0[0,1]   + P_Krish[2,:]*ders_p3_0[0,2]   + P_Krish[3,:]*ders_p3_0[0,3]),  (X22[0,:]*ders_p3_0[0,0]   + X22[1,:]*ders_p3_0[0,1]   + X22[2,:]*ders_p3_0[0,2]   + X22[3,:]*ders_p3_0[0,3]))
print((P_Krish[0,:]*ders_p3_0[1,0]   + P_Krish[1,:]*ders_p3_0[1,1]   + P_Krish[2,:]*ders_p3_0[1,2]   + P_Krish[3,:]*ders_p3_0[1,3]),  (X22[0,:]*ders_p3_0[1,0]   + X22[1,:]*ders_p3_0[1,1]   + X22[2,:]*ders_p3_0[1,2]   + X22[3,:]*ders_p3_0[1,3]))
print((P_Krish[0,:]*ders_p3_0[2,0]   + P_Krish[1,:]*ders_p3_0[2,1]   + P_Krish[2,:]*ders_p3_0[2,2]   + P_Krish[3,:]*ders_p3_0[2,3]),  (X22[0,:]*ders_p3_0[2,0]   + X22[1,:]*ders_p3_0[2,1]   + X22[2,:]*ders_p3_0[2,2]   + X22[3,:]*ders_p3_0[2,3]))
print((P_Krish[0,:]*ders_p3_0[3,0]   + P_Krish[1,:]*ders_p3_0[3,1]   + P_Krish[2,:]*ders_p3_0[3,2]   + P_Krish[3,:]*ders_p3_0[3,3]),  (X22[0,:]*ders_p3_0[3,0]   + X22[1,:]*ders_p3_0[3,1]   + X22[2,:]*ders_p3_0[3,2]   + X22[3,:]*ders_p3_0[3,3]))



##################################################################################################################
# Расчет Третьей Безье-крив. (=R - кривая) 
#  ders - для заданного "u" массив BASIS функций и  все их (до р) производныЕ
ders_p3 = np.zeros([p+1,p+1])

# C2 - массив, в нем для заданного "u" возвращаются C2[0,:]- x,y - сплайна
#                               для заданного "u"  C2[1,:]- x,y - 1-вой ПРОИЗВОДНОЙ сплайна
#                               для заданного "u"  C2[0,:]- x,y - 2-ой ПРОИЗВОДНОЙ сплайна
#                               для заданного "u"  C2[p,:]- x,y -"p"-ой ПРОИЗВОДНОЙ сплайна
C2_NURBS_p3=np.zeros([p+1,2]) # идекс "2" для 2D задачи, "3" - для 3D

n_u3_p3=600
data_CurvePoin_and_Deriv_NURBS_X22 = np.zeros([(n_u3_p3+1),(p+1),2])


for it in range(n_u3_p3+1):
    t_i=(it/n_u3_p3)*(t_stop1-t_start1) +  t_start1
    
    Func_1.CurvePoin_and_Deriv_NURBS(n_vert,p,T,X22,HR,t_i,C2_NURBS_p3,ders_p3)
    # В массиве на след. строке Хранятся Кубич. Сплайн
    data_CurvePoin_and_Deriv_NURBS_X22[it,:,:]=C2_NURBS_p3

##################################################################################################################




Title="** 222  СРАВНЕНИЕ 2  X22 и R   ***"
#Title=" **333"

labels_legend1="X22 Безье Кривая"
labels_legend2="R  Безье Кривая"



Array_0=Q_Krish
Array_0[:,:]=0
data_CurvePoin_and_Deriv_NURBS_p2[:,:,:]=0

#   ГРАФИК для ОТЧЕТА-СТАТЬИ - ДИСКРЕТ. НОРМА
# 
Plots_1.plot_Trace_Lines_2_for_Mergin_12 (  data_CurvePoin_and_Deriv_NURBS_X22[:,0,0],data_CurvePoin_and_Deriv_NURBS_X22[:,0,1],
                                            data_CurvePoin_and_Deriv_NURBS_R[:,0,0],data_CurvePoin_and_Deriv_NURBS_R[:,0,1] ,    
                                           
                                               -10, y_max, x_min, 30,
                                               Title, labels_legend1, labels_legend2)



#   ОКОНЧАНИЕ
#   Апроксимация 2-х полностью сопряженных кривых (P_c_крышкой и Q_c_крышкой)  R кривой  
#






#stop







"""

Matrix_A2= np.zeros([4,4]) 
Matrix_B2= np.zeros([4,2])



ders_p3_R = np.zeros([p+1,p+1])
Func_1.CurvePoin_and_Deriv_NURBS(n_vert,p,T,R,HR,0.0,C2_NURBS_p3,ders_p3_R)

Matrix_A2[0,0]=1;  Matrix_A2[0,1]=0;  Matrix_A2[0,2]=0;  Matrix_A2[0,3]=0;
Matrix_A2[1,0]=ders_p3_R[1,0];  Matrix_A2[1,1]=ders_p3_R[1,1];  Matrix_A2[1,2]=ders_p3_R[1,2];  Matrix_A2[1,3]=ders_p3_R[1,3];
Matrix_A2[2,0]=ders_p3_R[2,0];  Matrix_A2[2,1]=ders_p3_R[2,1];  Matrix_A2[2,2]=ders_p3_R[2,2];  Matrix_A2[2,3]=ders_p3_R[2,3];
Matrix_A2[3,0]=ders_p3_R[3,0];  Matrix_A2[3,1]=ders_p3_R[3,1];  Matrix_A2[3,2]=ders_p3_R[3,2];  Matrix_A2[3,3]=ders_p3_R[3,3];

Matrix_B2[0,:]  = P_Krish_0_derivative
Matrix_B2[1,:]  = P_Krish_1_derivative
Matrix_B2[2,:]  = P_Krish_2_derivative
Matrix_B2[3,:]  = P_Krish_3_derivative


print("*** 22 ***РЕШЕНИЕ *СЛАУ* ДЛЯ НЕзакрепленных ГРАНИЦ ***")
print("\n det(Matrix_A2)=", np.linalg.det(Matrix_A2))
print(" rank(Matrix_A2)=", np.linalg.matrix_rank(Matrix_A2))
print(" число Обусловленности(Matrix_A2)=", np.linalg.cond(Matrix_A2))
print(" rank(A2_&_B2)= ", np.linalg.matrix_rank(np.hstack((Matrix_A2,Matrix_B2))))
print(" число Обусловленности(A2&_B2=", np.linalg.cond(np.hstack((Matrix_A2,Matrix_B2))))

X2= np.linalg.solve(Matrix_A2, Matrix_B2)
print("***Решение системы:\n",X2)

# Решение НеСогласованной Системы
#X2, res, r, s = np.linalg.lstsq(Matrix_A2, Matrix_B2, rcond=None)


##################################################################################################################
# Расчет Третьей Безье-крив. (=R - кривая) 
#  ders - для заданного "u" массив BASIS функций и  все их (до р) производныЕ
ders_p3 = np.zeros([p+1,p+1])

# C2 - массив, в нем для заданного "u" возвращаются C2[0,:]- x,y - сплайна
#                               для заданного "u"  C2[1,:]- x,y - 1-вой ПРОИЗВОДНОЙ сплайна
#                               для заданного "u"  C2[0,:]- x,y - 2-ой ПРОИЗВОДНОЙ сплайна
#                               для заданного "u"  C2[p,:]- x,y -"p"-ой ПРОИЗВОДНОЙ сплайна
C2_NURBS_p3=np.zeros([p+1,2]) # идекс "2" для 2D задачи, "3" - для 3D

n_u3=60
data_CurvePoin_and_Deriv_NURBS_p3 = np.zeros([(n_u3+1),(p+1),2])


for it in range(n_u3+1):
    t_i=(it/n_u2)*(t_stop1-t_start1) +  t_start1
    
    Func_1.CurvePoin_and_Deriv_NURBS(n_vert,p,T,X2,HR,t_i,C2_NURBS_p3,ders_p3)
    # В массиве на след. строке Хранятся Кубич. Сплайн
    data_CurvePoin_and_Deriv_NURBS_p3[it,:,:]=C2_NURBS_p3

##################################################################################################################

#stop



Title="Окончательное решение - ДИСКРЕТ. НОРМА *** ОБЕ КОНЕЧНЫЕ ТОЧКИ НЕзафиксированы (СВОБОДНЫЕ) ***"
Title=" "

labels_legend1="P Многоугольник (заданный)"
labels_legend2="P Безье Кривая (заданная)"
labels_legend3="Q Многоугольник (заданный)"
labels_legend4="Q Безье Кривая (заданная)"
labels_legend5="R Многоугольник (апроксимация Р и Q)"
labels_legend6="R Безье Кривая (апроксимация Р и Q)"




#   ГРАФИК для ОТЧЕТА-СТАТЬИ - ДИСКРЕТ. НОРМА
# 
Plots_1.plot_Trace_Lines_3_for_Mergin_1 (P[:,0],P[:,1],
                                         Q[:,0],Q[:,1],
                                         X2[:,0],X2[:,1],
                                            data_CurvePoin_and_Deriv_NURBS_p1[:,0,0],data_CurvePoin_and_Deriv_NURBS_p1[:,0,1] ,                             
                                            data_CurvePoin_and_Deriv_NURBS_p2[:,0,0],data_CurvePoin_and_Deriv_NURBS_p2[:,0,1] ,
                                            data_CurvePoin_and_Deriv_NURBS_p3[:,0,0],data_CurvePoin_and_Deriv_NURBS_p3[:,0,1] ,    
                                           
                                               y_min, y_max, x_min, x_max,
                                               Title, labels_legend1, labels_legend2,
                                                labels_legend3, labels_legend4,labels_legend5,labels_legend6)







stop
"""
########################################################################################################################################
########################################################################################################################################
########################################################################################################################################
#************************************************************************
#%% = Окончание Блока.  Если блок Выделить, то его можно выполнить Ctrl + Enter
# Окончание Блока ДИСКРЕТ. НОРМА без ограничений 




#%% = Начало Блока.  Если блок Выделить, то его можно выполнить Ctrl + Enter
#************************************************************************
#************************************************************************
#************************************************************************


# Блок ДИСКРЕТ. НОРМА  Ограничение = 4-ре точки  


Eps1 = np.zeros([4,2])
Del1 = np.zeros([4,2])
Lam1 = np.zeros([8,2])
X1 = np.zeros([16,2])
X1_1 = np.zeros([16,2])
Matrix_A1= np.zeros([16,16]) 
Matrix_B1= np.zeros([16,2])

p=3
ders = np.zeros([p+1,p+1]) # массив, в котором - в 1-ой строке - Базисные Функции
                           #                   -   2-строка - первые Производ. Базисных Функции 
                           #                       3-строка - вторые Производ. Базисных Функции и т.д. ........
                           
# Блок ДИСКРЕТ. НОРМА  ДОПОЛНИТЕЛЬНЫЕ Ограничение = Заданы 4-ре точки                            
u1=0.0  # в статье эти точки называются u0, u1, v0, v1
u2=0.5
v1=0.1
v2=1.0


span = Func_1.FindSpan(n_vert,p,u1,U);
Func_1.DersBasisFuns(span,u1,p,p,U,ders)   
N_00u1=ders[0,0]; N_10u1=ders[0,1]; N_20u1=ders[0,2]; N_30u1=ders[0,3]

span = Func_1.FindSpan(n_vert,p,u2,U);
Func_1.DersBasisFuns(span,u2,p,p,U,ders)   
N_00u2=ders[0,0]; N_10u2=ders[0,1]; N_20u2=ders[0,2]; N_30u2=ders[0,3]

span = Func_1.FindSpan(n_vert,p,v1,U);
Func_1.DersBasisFuns(span,v1,p,p,U,ders)   
N_00v1=ders[0,0]; N_10v1=ders[0,1]; N_20v1=ders[0,2]; N_30v1=ders[0,3]

span = Func_1.FindSpan(n_vert,p,v2,U);
Func_1.DersBasisFuns(span,v2,p,p,U,ders)   
N_00v2=ders[0,0]; N_10v2=ders[0,1]; N_20v2=ders[0,2]; N_30v2=ders[0,3]
# ОКОНЧАНИЕ - Расчет Допол. Ограничений Закончили                        

u0=1.0 # Конечна ТОЧКА НА Р-кривой, для неё расчитываем 1. Базис. функции и 2. Три произв. Базис. Функций == ТОЧКА СОПРЯЖЕНИЯ
span = Func_1.FindSpan(n_vert,p,u0,U);
Func_1.DersBasisFuns(span,u0,p,p,U,ders)
print("*u0=",u0, "  ders=\n",ders)

#  Производные БАЗИСНЫх ФУНКЦИИ в конечной точке  Р-кривой

N_001= ders[0,0];   N_101= ders[0,1]; N_201= ders[0,2]; N_301= ders[0,3] # НУЛЕВЫЕ ПРОИЗВОДНЫЕ = сама функция
N_011= ders[1,0];   N_111= ders[1,1]; N_211= ders[1,2]; N_311= ders[1,3] # ПЕРВЫЕ ПРОИЗВОДНЫЕ
N_021= ders[2,0];   N_121= ders[2,1]; N_221= ders[2,2]; N_321= ders[2,3] # ВТОРЫЕ ПРОИЗВОДНЫЕ
N_031= ders[3,0];   N_131= ders[3,1]; N_231= ders[3,2]; N_331= ders[3,3] # ТРЕТЬИ ПРОИЗВОДНЫЕ

#stop

u0=0.0 # # Начальная  ТОЧКА НА Q-кривой, для неё расчитываем 1. Базис. функции и 2. Три произв. Базис. Функций == ТОЧКА СОПРЯЖЕНИЯ
span = Func_1.FindSpan(n_vert,p,u0,U);
Func_1.DersBasisFuns(span,u0,p,p,U,ders)
print("*u0=",u0, "  ders=\n",ders)
#  Производные БАЗИСНЫх ФУНКЦИИ в начальной  точке  Q-кривой
N_000= ders[0,0];   N_100= ders[0,1]; N_200= ders[0,2]; N_300= ders[0,3] # НУЛЕВЫЕ ПРОИЗВОДНЫЕ = сама функция
N_010= ders[1,0];   N_110= ders[1,1]; N_210= ders[1,2]; N_310= ders[1,3] # ПЕРВЫЕ ПРОИЗВОДНЫЕ
N_020= ders[2,0];   N_120= ders[2,1]; N_220= ders[2,2]; N_320= ders[2,3] # ВТОРЫЕ ПРОИЗВОДНЫЕ
N_030= ders[3,0];   N_130= ders[3,1]; N_230= ders[3,2]; N_330= ders[3,3] # ТРЕТЬИ ПРОИЗВОДНЫЕ

#stop
####################################################################################################################
####################################################################################################################

# **!! ЭТО МАТРИЦА ДЛЯ НЕзакрепленныз (СВОБОДНЫХ) ГРАНИЦ
#      ДИСРЕТНАЯ НОРМА


Matrix_A1[0,0]=2;  Matrix_A1[0,8]=N_001;   Matrix_A1[0,9]=N_011;   Matrix_A1[0,10]=N_021;   Matrix_A1[0,11]=N_031;   Matrix_A1[0,12]=N_00u1;  Matrix_A1[0,13]=N_00u2
Matrix_A1[1,1]=2;  Matrix_A1[1,8]=N_101;   Matrix_A1[1,9]=N_111;   Matrix_A1[1,10]=N_121;   Matrix_A1[1,11]=N_131;   Matrix_A1[1,12]=N_10u1;  Matrix_A1[1,13]=N_10u2
Matrix_A1[2,2]=2;  Matrix_A1[2,8]=N_201;   Matrix_A1[2,9]=N_211;   Matrix_A1[2,10]=N_221;   Matrix_A1[2,11]=N_231;   Matrix_A1[2,12]=N_20u1;  Matrix_A1[2,13]=N_20u2
Matrix_A1[3,3]=2;  Matrix_A1[3,8]=N_301;   Matrix_A1[3,9]=N_311;   Matrix_A1[3,10]=N_321;   Matrix_A1[3,11]=N_331;   Matrix_A1[3,12]=N_30u1;  Matrix_A1[3,13]=N_30u2

Matrix_A1[4,4]=2;  Matrix_A1[4,8]=-N_000;  Matrix_A1[4,9]=-N_010;  Matrix_A1[4,10]=-N_020;  Matrix_A1[4,11]=-N_030;  Matrix_A1[4,14]=N_00v1;  Matrix_A1[4,15]=N_00v2  
Matrix_A1[5,5]=2;  Matrix_A1[5,8]=-N_100;  Matrix_A1[5,9]=-N_110;  Matrix_A1[5,10]=-N_120;  Matrix_A1[5,11]=-N_130;  Matrix_A1[5,14]=N_10v1;  Matrix_A1[5,15]=N_10v2 
Matrix_A1[6,6]=2;  Matrix_A1[6,8]=-N_200;  Matrix_A1[6,9]=-N_210;  Matrix_A1[6,10]=-N_220;  Matrix_A1[6,11]=-N_230;  Matrix_A1[6,14]=N_20v1;  Matrix_A1[6,15]=N_20v2 
Matrix_A1[7,7]=2;  Matrix_A1[7,8]=-N_300;  Matrix_A1[7,9]=-N_310;  Matrix_A1[7,10]=-N_320;  Matrix_A1[7,11]=-N_330;  Matrix_A1[7,14]=N_30v1;  Matrix_A1[7,15]=N_30v2 

Matrix_A1[8,0] =N_001; Matrix_A1[8,1] =N_101;  Matrix_A1[8,2] =N_201;  Matrix_A1[8,3] =N_301; Matrix_A1[8,4] =-N_000;  Matrix_A1[8,5] =-N_100;  Matrix_A1[8,6] =-N_200;  Matrix_A1[8,7] =-N_300;
Matrix_A1[9,0] =N_011; Matrix_A1[9,1] =N_111;  Matrix_A1[9,2] =N_211;  Matrix_A1[9,3] =N_311; Matrix_A1[9,4] =-N_010;  Matrix_A1[9,5] =-N_110;  Matrix_A1[9,6] =-N_210;  Matrix_A1[9,7] =-N_310;
Matrix_A1[10,0]=N_021; Matrix_A1[10,1]=N_121;  Matrix_A1[10,2]=N_221;  Matrix_A1[10,3]=N_321; Matrix_A1[10,4]=-N_020;  Matrix_A1[10,5]=-N_120;  Matrix_A1[10,6]=-N_220;  Matrix_A1[10,7]=-N_320;
Matrix_A1[11,0]=N_031; Matrix_A1[11,1]=N_131;  Matrix_A1[11,2]=N_231;  Matrix_A1[11,3]=N_331; Matrix_A1[11,4]=-N_030;  Matrix_A1[11,5]=-N_130;  Matrix_A1[11,6]=-N_230;  Matrix_A1[11,7]=-N_330;

Matrix_A1[12,0]=N_00u1;  Matrix_A1[12,1]=N_10u1; Matrix_A1[12,2]=N_20u1;  Matrix_A1[12,3]=N_30u1
Matrix_A1[13,0]=N_00u2;  Matrix_A1[13,1]=N_10u2; Matrix_A1[13,2]=N_20u2;  Matrix_A1[13,3]=N_30u2

Matrix_A1[14,4]=N_00v1;  Matrix_A1[14,5]=N_10v1; Matrix_A1[14,6]=N_20v1;  Matrix_A1[14,7]=N_30v1
Matrix_A1[15,4]=N_00v2;  Matrix_A1[15,5]=N_10v2; Matrix_A1[15,6]=N_20v2;  Matrix_A1[15,7]=N_30v2

Matrix_B1[8,:]  = -P[0,:]*N_001 + Q[0,:]*N_000  -P[1,:]*N_101 + Q[1,:]*N_100  -P[2,:]*N_201 + Q[2,:]*N_200  -P[3,:]*N_301 + Q[3,:]*N_300
Matrix_B1[9,:]  = -P[0,:]*N_011 + Q[0,:]*N_010  -P[1,:]*N_111 + Q[1,:]*N_110  -P[2,:]*N_211 + Q[2,:]*N_210  -P[3,:]*N_311 + Q[3,:]*N_310
Matrix_B1[10,:] = -P[0,:]*N_021 + Q[0,:]*N_020  -P[1,:]*N_121 + Q[1,:]*N_120  -P[2,:]*N_221 + Q[2,:]*N_220  -P[3,:]*N_321 + Q[3,:]*N_320
Matrix_B1[11,:] = -P[0,:]*N_031 + Q[0,:]*N_030  -P[1,:]*N_131 + Q[1,:]*N_130  -P[2,:]*N_231 + Q[2,:]*N_230  -P[3,:]*N_331 + Q[3,:]*N_330

print("* Matrix_A1\n",Matrix_A1)
print("* Matrix_B1\n",Matrix_B1)
#stop

print("*** РЕШЕНИЕ *СЛАУ* ДЛЯ НЕзакрепленных ГРАНИЦ ***")
print("\n det(Matrix_A1)=", np.linalg.det(Matrix_A1))
print(" rank(Matrix_A1)=", np.linalg.matrix_rank(Matrix_A1))
print(" число Обусловленности(Matrix_A1)=", np.linalg.cond(Matrix_A1))
print(" rank(A1_&_B1)= ", np.linalg.matrix_rank(np.hstack((Matrix_A1,Matrix_B1))))
print(" число Обусловленности(A1&_B1=", np.linalg.cond(np.hstack((Matrix_A1,Matrix_B1))))



X1= np.linalg.solve(Matrix_A1, Matrix_B1)
print("***Решение системы:\n",X1)

#Lam = np.linalg.solve(Matrix_A, Matrix_B)
X1_1, res, r, s = np.linalg.lstsq(Matrix_A1, Matrix_B1, rcond=None)
print ("***Псевдорешение системы:\n", X1_1)


print ("Число Сочетаний -- math.comb(3, 2)= ",math.comb(3, 2))

Eps1=X1_1[0:4,:]
Del1=X1_1[4:8,:]




#Mu=1
#Lam_Scalar=Mu/(1+Mu) 
Lam_Scalar=0.5 
P_0=P+Eps1
P_1 = np.zeros([4,2])
P_2 = np.zeros([4,2])
P_3 = np.zeros([4,2])

P_0_0=P[0,:]+Eps1[0,:]
P_0_1=P[1,:]+Eps1[1,:]
P_0_2=P[2,:]+Eps1[2,:]
P_0_3=P[3,:]+Eps1[3,:]

        
P_1_1=(1-1/Lam_Scalar)*P_0_0 +  (1/Lam_Scalar)*P_0_1      
P_1_2=(1-1/Lam_Scalar)*P_0_1 +  (1/Lam_Scalar)*P_0_2
P_1_3=(1-1/Lam_Scalar)*P_0_2 +  (1/Lam_Scalar)*P_0_3

P_2_2=(1-1/Lam_Scalar)*P_1_1 +  (1/Lam_Scalar)*P_1_2
P_2_3=(1-1/Lam_Scalar)*P_1_2 +  (1/Lam_Scalar)*P_1_3

P_3_3=(1-1/Lam_Scalar)*P_2_2 +  (1/Lam_Scalar)*P_2_3

R[0,:]=P_0_0
R[1,:]=P_1_1
R[2,:]=P_2_2
R[3,:]=P_3_3




##################################################################################################################
# Расчет Первой-НОВОЙ Безье-крив. (=P_с_Крышкой ) 
P_Krish=P+Eps1

#  ders - для заданного "u" массив BASIS функций и  все их (до р) производныЕ
ders_p3 = np.zeros([p+1,p+1])

# C2 - массив, в нем для заданного "u" возвращаются C2[0,:]- x,y - сплайна
#                               для заданного "u"  C2[1,:]- x,y - 1-вой ПРОИЗВОДНОЙ сплайна
#                               для заданного "u"  C2[0,:]- x,y - 2-ой ПРОИЗВОДНОЙ сплайна
#                               для заданного "u"  C2[p,:]- x,y -"p"-ой ПРОИЗВОДНОЙ сплайна
C2_NURBS_p3=np.zeros([p+1,2]) # идекс "2" для 2D задачи, "3" - для 3D

n_u3=60
data_CurvePoin_and_Deriv_NURBS_P_Krish = np.zeros([(n_u3+1),(p+1),2])

#stop

for it in range(n_u3+1):
    t_i=(it/n_u2)*(t_stop1-t_start1) +  t_start1
    
    Func_1.CurvePoin_and_Deriv_NURBS(n_vert,p,T,P_Krish,HP,t_i,C2_NURBS_p3,ders_p3)
    # В массиве на след. строке Хранятся Кубич. Сплайн
    data_CurvePoin_and_Deriv_NURBS_P_Krish[it,:,:]=C2_NURBS_p3

##################################################################################################################

# Расчет Координат точек, в которых заданы Ограничения
#точка u1
Func_1.CurvePoin_and_Deriv_NURBS(n_vert,p,T,P_Krish,HP,u1,C2_NURBS_p3,ders_p3) #точка u1
X1=C2_NURBS_p3[0,0]; Y1=C2_NURBS_p3[0,1]

#точка u2
Func_1.CurvePoin_and_Deriv_NURBS(n_vert,p,T,P_Krish,HP,u2,C2_NURBS_p3,ders_p3) #точка u2
X2=C2_NURBS_p3[0,0]; Y2=C2_NURBS_p3[0,1]
#stop

##################################################################################################################
# Расчет Второй-НОВОЙ Безье-крив. (=Q_с_Крышкой) 
Q_Krish=Q+Del1

#  ders - для заданного "u" массив BASIS функций и  все их (до р) производныЕ
ders_p3 = np.zeros([p+1,p+1])

# C2 - массив, в нем для заданного "u" возвращаются C2[0,:]- x,y - сплайна
#                               для заданного "u"  C2[1,:]- x,y - 1-вой ПРОИЗВОДНОЙ сплайна
#                               для заданного "u"  C2[0,:]- x,y - 2-ой ПРОИЗВОДНОЙ сплайна
#                               для заданного "u"  C2[p,:]- x,y -"p"-ой ПРОИЗВОДНОЙ сплайна
C2_NURBS_p3=np.zeros([p+1,2]) # идекс "2" для 2D задачи, "3" - для 3D

n_u3=60
data_CurvePoin_and_Deriv_NURBS_Q_Krish = np.zeros([(n_u1+1),(p+1),2])



for it in range(n_u3+1):
    t_i=(it/n_u2)*(t_stop1-t_start1) +  t_start1
    
    Func_1.CurvePoin_and_Deriv_NURBS(n_vert,p,T,Q_Krish,HQ,t_i,C2_NURBS_p3,ders_p3)
    # В массиве на след. строке Хранятся Кубич. Сплайн
    data_CurvePoin_and_Deriv_NURBS_Q_Krish[it,:,:]=C2_NURBS_p3

##################################################################################################################

# Расчет Координат точек, в которых заданы Ограничения
#точка v1
Func_1.CurvePoin_and_Deriv_NURBS(n_vert,p,T,Q_Krish,HP,v1,C2_NURBS_p3,ders_p3) #точка v1
X3=C2_NURBS_p3[0,0]; Y3=C2_NURBS_p3[0,1]

#точка v2
Func_1.CurvePoin_and_Deriv_NURBS(n_vert,p,T,Q_Krish,HP,v2,C2_NURBS_p3,ders_p3) #точка v2
X4=C2_NURBS_p3[0,0]; Y4=C2_NURBS_p3[0,1]
#stop


#stop





Title=" *1*11"
Title=" "
labels_legend1="P Многоугольник (заданный)"
labels_legend2="P Безье Кривая (заданная)"

labels_legend3="Многоугольник Р с крышкой"
labels_legend4="P с крышкой"

labels_legend5="Q Многоугольник (заданный)"
labels_legend6="Q Безье Кривая (заданная)"

labels_legend7="Многоугольник Q с крышкой"
labels_legend8="Q с крышкой"

#y_min=-1
#y_max=40.0

#x_min=-1
#x_max=90


#   ГРАФИК для ОТЧЕТА-СТАТЬИ - ДИСКРЕТ. НОРМА
Plots_1.plot_Trace_Lines_4_for_Mergin_1 (P[:,0],P[:,1],
                                         P_Krish[:,0],P_Krish[:,1],
                                         Q[:,0],Q[:,1],
                                       Q_Krish[:,0],Q_Krish[:,1],
                                            data_CurvePoin_and_Deriv_NURBS_p1[:,0,0],data_CurvePoin_and_Deriv_NURBS_p1[:,0,1] ,  
                                             data_CurvePoin_and_Deriv_NURBS_P_Krish[:,0,0],    data_CurvePoin_and_Deriv_NURBS_P_Krish[:,0,1],
                                            data_CurvePoin_and_Deriv_NURBS_p2[:,0,0],data_CurvePoin_and_Deriv_NURBS_p2[:,0,1] ,
                                              data_CurvePoin_and_Deriv_NURBS_Q_Krish[:,0,0],    data_CurvePoin_and_Deriv_NURBS_Q_Krish[:,0,1], 
                                           
                                               y_min, y_max, x_min, x_max,
                                               Title, labels_legend1, labels_legend2,
                                                labels_legend3, labels_legend4,labels_legend5,labels_legend6,labels_legend7,labels_legend8)








#stop




##################################################################################################################
# Расчет Третьей Безье-крив. (=R - кривая) 
#  ders - для заданного "u" массив BASIS функций и  все их (до р) производныЕ
ders_p3 = np.zeros([p+1,p+1])

# C2 - массив, в нем для заданного "u" возвращаются C2[0,:]- x,y - сплайна
#                               для заданного "u"  C2[1,:]- x,y - 1-вой ПРОИЗВОДНОЙ сплайна
#                               для заданного "u"  C2[0,:]- x,y - 2-ой ПРОИЗВОДНОЙ сплайна
#                               для заданного "u"  C2[p,:]- x,y -"p"-ой ПРОИЗВОДНОЙ сплайна
C2_NURBS_p3=np.zeros([p+1,2]) # идекс "2" для 2D задачи, "3" - для 3D

n_u3=60
data_CurvePoin_and_Deriv_NURBS_p3 = np.zeros([(n_u3+1),(p+1),2])


for it in range(n_u3+1):
    t_i=(it/n_u2)*(t_stop1-t_start1) +  t_start1
    
    Func_1.CurvePoin_and_Deriv_NURBS(n_vert,p,T,R,HR,t_i,C2_NURBS_p3,ders_p3)
    # В массиве на след. строке Хранятся Кубич. Сплайн
    data_CurvePoin_and_Deriv_NURBS_p3[it,:,:]=C2_NURBS_p3

##################################################################################################################

#stop



Title="Окончательное решение - ДИСКРЕТ. НОРМА *** ОБЕ КОНЕЧНЫЕ ТОЧКИ НЕзафиксированы (СВОБОДНЫЕ) ***"
Title=" "

labels_legend1="P Многоугольник (заданный)"
labels_legend2="P Безье Кривая (заданная)"
labels_legend3="Q Многоугольник (заданный)"
labels_legend4="Q Безье Кривая (заданная)"
labels_legend5="R Многоугольник (апроксимация Р и Q)"
labels_legend6="R Безье Кривая (апроксимация Р и Q)"
labels_legend7="точки ограничений"




#   ГРАФИК для ОТЧЕТА-СТАТЬИ - ДИСКРЕТ. НОРМА
# 
Plots_1.plot_Trace_Lines_3_for_Mergin_1_plus_4_Points (X1,Y1,X2,Y2,X3,Y3,X4,Y4,
                                         P[:,0],P[:,1],
                                         Q[:,0],Q[:,1],
                                         R[:,0],R[:,1],
                                            data_CurvePoin_and_Deriv_NURBS_p1[:,0,0],data_CurvePoin_and_Deriv_NURBS_p1[:,0,1] ,                             
                                            data_CurvePoin_and_Deriv_NURBS_p2[:,0,0],data_CurvePoin_and_Deriv_NURBS_p2[:,0,1] ,
                                            data_CurvePoin_and_Deriv_NURBS_p3[:,0,0],data_CurvePoin_and_Deriv_NURBS_p3[:,0,1] ,    
                                           
                                               y_min, y_max, x_min, x_max,
                                               Title, labels_legend1, labels_legend2,
                                                labels_legend3, labels_legend4,labels_legend5,labels_legend6,labels_legend7)









########################################################################################################################################
########################################################################################################################################
########################################################################################################################################
#************************************************************************
#%% = Окончание Блока.  Если блок Выделить, то его можно выполнить Ctrl + Enter
# Окончание Блока ДИСКРЕТ. НОРМА без ограничений 






# Окончание Блока ДИСКРЕТ. НОРМА
#stop


# Начало Блока ИНТЕГЛАЛЬ. НОРМА


#%% = Начало Блока.  Если блок Выделить, то его можно выполнить Ctrl + Enter
#************************************************************************
#************************************************************************
#************************************************************************


# Блок ИНТЕГЛАЛЬ. НОРМА Без Ограничений


Eps1 = np.zeros([4,2])
Del1 = np.zeros([4,2])
Lam1 = np.zeros([4,2])
X1 = np.zeros([12,2])
X1_1 = np.zeros([12,2])
Matrix_A1= np.zeros([12,12]) 
Matrix_B1= np.zeros([12,2])

p=3
ders = np.zeros([p+1,p+1]) # массив, в котором - в 1-ой строке - Базисные Функции
                           #                   -   2-строка - первые Производ. Базисных Функции 
                           #                       3-строка - вторые Производ. Базисных Функции и т.д. ........

# Расчет  ИНТЕГРАЛОВ 

n_for_Integration=200
t_start1=0
t_stop1=1
del_t=(t_stop1-t_start1)/n_for_Integration

N_00=0; N_01=0; N_02=0; N_03=0
N_10=0; N_11=0; N_12=0; N_13=0
N_20=0; N_21=0; N_22=0; N_23=0
N_30=0; N_31=0; N_32=0; N_33=0

for it in range(n_for_Integration+1):
    t_i=(it/n_for_Integration)*(t_stop1-t_start1) +  t_start1
   
    span = Func_1.FindSpan(n_vert,p,t_i,U);
    Func_1.DersBasisFuns(span,t_i,p,p,U,ders)
    
    N_00=N_00 + 2*ders[0,0]*ders[0,0]*del_t
    N_01=N_01 + 2*ders[0,0]*ders[0,1]*del_t
    N_02=N_02 + 2*ders[0,0]*ders[0,2]*del_t
    N_03=N_03 + 2*ders[0,0]*ders[0,3]*del_t
    
    N_10=N_10 + 2*ders[0,1]*ders[0,0]*del_t
    N_11=N_11 + 2*ders[0,1]*ders[0,1]*del_t
    N_12=N_12 + 2*ders[0,1]*ders[0,2]*del_t
    N_13=N_13 + 2*ders[0,1]*ders[0,3]*del_t
    
    N_20=N_20 + 2*ders[0,2]*ders[0,0]*del_t
    N_21=N_21 + 2*ders[0,2]*ders[0,1]*del_t
    N_22=N_22 + 2*ders[0,2]*ders[0,2]*del_t
    N_23=N_23 + 2*ders[0,2]*ders[0,3]*del_t
    
    N_30=N_30 + 2*ders[0,3]*ders[0,0]*del_t
    N_31=N_31 + 2*ders[0,3]*ders[0,1]*del_t
    N_32=N_32 + 2*ders[0,3]*ders[0,2]*del_t
    N_33=N_33 + 2*ders[0,3]*ders[0,3]*del_t
    


#  Производные Через БАЗИСНЫЕ ФУНКЦИИ

u0=1.0 # Конечна ТОЧКА НА Р-кривой, для неё расчитываем 1. Базис. функции и 2. Три произв. Базис. Функций == ТОЧКА СОПРЯЖЕНИЯ
span = Func_1.FindSpan(n_vert,p,u0,U);
Func_1.DersBasisFuns(span,u0,p,p,U,ders)
print("*u0=",u0, "  ders=\n",ders)

N_001= ders[0,0];   N_101= ders[0,1]; N_201= ders[0,2]; N_301= ders[0,3] # НУЛЕВЫЕ ПРОИЗВОДНЫЕ = сама функция
N_011= ders[1,0];   N_111= ders[1,1]; N_211= ders[1,2]; N_311= ders[1,3] # ПЕРВЫЕ ПРОИЗВОДНЫЕ
N_021= ders[2,0];   N_121= ders[2,1]; N_221= ders[2,2]; N_321= ders[2,3] # ВТОРЫЕ ПРОИЗВОДНЫЕ
N_031= ders[3,0];   N_131= ders[3,1]; N_231= ders[3,2]; N_331= ders[3,3] # ТРЕТЬИ ПРОИЗВОДНЫЕ

#stop

u0=0.0 # ТОЧКА НА Q-кривой, для которой заданы ограничения (ТОЧКА И ТРИ ПРОИЗВОДНЫЕ)== ТОЧКА СОПРЯЖЕНИЯ
span = Func_1.FindSpan(n_vert,p,u0,U);
Func_1.DersBasisFuns(span,u0,p,p,U,ders)
print("*u0=",u0, "  ders=\n",ders)

N_000= ders[0,0];   N_100= ders[0,1]; N_200= ders[0,2]; N_300= ders[0,3] # НУЛЕВЫЕ ПРОИЗВОДНЫЕ = сама функция
N_010= ders[1,0];   N_110= ders[1,1]; N_210= ders[1,2]; N_310= ders[1,3] # ПЕРВЫЕ ПРОИЗВОДНЫЕ
N_020= ders[2,0];   N_120= ders[2,1]; N_220= ders[2,2]; N_320= ders[2,3] # ВТОРЫЕ ПРОИЗВОДНЫЕ
N_030= ders[3,0];   N_130= ders[3,1]; N_230= ders[3,2]; N_330= ders[3,3] # ТРЕТЬИ ПРОИЗВОДНЫЕ

####################################################################################################################
####################################################################################################################

# ИНТЕГРАЛЬ.  НОРМА
# **!! ЭТО МАТРИЦА ДЛЯ НЕзакрепленныз (СВОБОДНЫХ) ГРАНИЦ

Matrix_A1[0,0]=N_00;  Matrix_A1[0,1]=N_10;  Matrix_A1[0,2]=N_20;  Matrix_A1[0,3]=N_30;  Matrix_A1[0,8]= N_001; Matrix_A1[0,9]= N_011;  Matrix_A1[0,10]= N_021;  Matrix_A1[0,11]= N_031
Matrix_A1[1,0]=N_01;  Matrix_A1[1,1]=N_11;  Matrix_A1[1,2]=N_21;  Matrix_A1[1,3]=N_31;  Matrix_A1[1,8]= N_101; Matrix_A1[1,9]= N_111;  Matrix_A1[1,10]= N_121;  Matrix_A1[1,11]= N_131
Matrix_A1[2,0]=N_02;  Matrix_A1[2,1]=N_12;  Matrix_A1[2,2]=N_22;  Matrix_A1[2,3]=N_32;  Matrix_A1[2,8]= N_201; Matrix_A1[2,9]= N_211;  Matrix_A1[2,10]= N_221;  Matrix_A1[2,11]= N_231
Matrix_A1[3,0]=N_03;  Matrix_A1[3,1]=N_13;  Matrix_A1[3,2]=N_23;  Matrix_A1[3,3]=N_33;  Matrix_A1[3,8]= N_301; Matrix_A1[3,9]= N_311;  Matrix_A1[3,10]= N_321;  Matrix_A1[3,11]= N_331

Matrix_A1[4,4]=N_00;  Matrix_A1[4,5]=N_10;  Matrix_A1[4,6]=N_20;  Matrix_A1[4,7]=N_30;  Matrix_A1[4,8]=-N_000; Matrix_A1[4,9]=-N_010;  Matrix_A1[4,10]=-N_020;  Matrix_A1[4,11]=-N_030
Matrix_A1[5,4]=N_01;  Matrix_A1[5,5]=N_11;  Matrix_A1[5,6]=N_21;  Matrix_A1[5,7]=N_31;  Matrix_A1[5,8]=-N_100; Matrix_A1[5,9]=-N_110;  Matrix_A1[5,10]=-N_120;  Matrix_A1[5,11]=-N_130
Matrix_A1[6,4]=N_02;  Matrix_A1[6,5]=N_12;  Matrix_A1[6,6]=N_22;  Matrix_A1[6,7]=N_32;  Matrix_A1[6,8]=-N_200; Matrix_A1[6,9]=-N_210;  Matrix_A1[6,10]=-N_220;  Matrix_A1[6,11]=-N_230
Matrix_A1[7,4]=N_03;  Matrix_A1[7,5]=N_13;  Matrix_A1[7,6]=N_23;  Matrix_A1[7,7]=N_33;  Matrix_A1[7,8]=-N_300; Matrix_A1[7,9]=-N_310;  Matrix_A1[7,10]=-N_320;  Matrix_A1[7,11]=-N_330

Matrix_A1[8,0] =N_001; Matrix_A1[8,1] =N_101;  Matrix_A1[8,2] =N_201;  Matrix_A1[8,3] =N_301; Matrix_A1[8,4] =-N_000;  Matrix_A1[8,5] =-N_100;  Matrix_A1[8,6] =-N_200;  Matrix_A1[8,7] =-N_300;
Matrix_A1[9,0] =N_011; Matrix_A1[9,1] =N_111;  Matrix_A1[9,2] =N_211;  Matrix_A1[9,3] =N_311; Matrix_A1[9,4] =-N_010;  Matrix_A1[9,5] =-N_110;  Matrix_A1[9,6] =-N_210;  Matrix_A1[9,7] =-N_310;
Matrix_A1[10,0]=N_021; Matrix_A1[10,1]=N_121;  Matrix_A1[10,2]=N_221;  Matrix_A1[10,3]=N_321; Matrix_A1[10,4]=-N_020;  Matrix_A1[10,5]=-N_120;  Matrix_A1[10,6]=-N_220;  Matrix_A1[10,7]=-N_320;
Matrix_A1[11,0]=N_031; Matrix_A1[11,1]=N_131;  Matrix_A1[11,2]=N_231;  Matrix_A1[11,3]=N_331; Matrix_A1[11,4]=-N_030;  Matrix_A1[11,5]=-N_130;  Matrix_A1[11,6]=-N_230;  Matrix_A1[11,7]=-N_330;




Matrix_B1[8,:]  = -P[0,:]*N_001 + Q[0,:]*N_000  -P[1,:]*N_101 + Q[1,:]*N_100  -P[2,:]*N_201 + Q[2,:]*N_200  -P[3,:]*N_301 + Q[3,:]*N_300
Matrix_B1[9,:]  = -P[0,:]*N_011 + Q[0,:]*N_010  -P[1,:]*N_111 + Q[1,:]*N_110  -P[2,:]*N_211 + Q[2,:]*N_210  -P[3,:]*N_311 + Q[3,:]*N_310
Matrix_B1[10,:] = -P[0,:]*N_021 + Q[0,:]*N_020  -P[1,:]*N_121 + Q[1,:]*N_120  -P[2,:]*N_221 + Q[2,:]*N_220  -P[3,:]*N_321 + Q[3,:]*N_320
Matrix_B1[11,:] = -P[0,:]*N_031 + Q[0,:]*N_030  -P[1,:]*N_131 + Q[1,:]*N_130  -P[2,:]*N_231 + Q[2,:]*N_230  -P[3,:]*N_331 + Q[3,:]*N_330

#print("* Matrix_A1\n",Matrix_A1)
#print("* Matrix_B1\n",Matrix_B1)
#stop

print("*** РЕШЕНИЕ *СЛАУ* ДЛЯ НЕзакрепленных ГРАНИЦ ***")
print("\n det(Matrix_A1)=", np.linalg.det(Matrix_A1))
print(" rank(Matrix_A1)=", np.linalg.matrix_rank(Matrix_A1))
print(" число Обусловленности(Matrix_A1)=", np.linalg.cond(Matrix_A1))
print(" rank(A1_&_B1)= ", np.linalg.matrix_rank(np.hstack((Matrix_A1,Matrix_B1))))
print(" число Обусловленности(A1&_B1=", np.linalg.cond(np.hstack((Matrix_A1,Matrix_B1))))



X1= np.linalg.solve(Matrix_A1, Matrix_B1)
print("***Решение системы:\n",X1)

#Lam = np.linalg.solve(Matrix_A, Matrix_B)
X1_1, res, r, s = np.linalg.lstsq(Matrix_A1, Matrix_B1, rcond=None)
print ("***Псевдорешение системы:\n", X1_1)


print ("Число Сочетаний -- math.comb(3, 2)= ",math.comb(3, 2))

Eps1=X1_1[0:4,:]
Del1=X1_1[4:8,:]




#Mu=1
#Lam_Scalar=Mu/(1+Mu) 
Lam_Scalar=0.5 
P_0=P+Eps1
P_1 = np.zeros([4,2])
P_2 = np.zeros([4,2])
P_3 = np.zeros([4,2])

P_0_0=P[0,:]+Eps1[0,:]
P_0_1=P[1,:]+Eps1[1,:]
P_0_2=P[2,:]+Eps1[2,:]
P_0_3=P[3,:]+Eps1[3,:]

        
P_1_1=(1-1/Lam_Scalar)*P_0_0 +  (1/Lam_Scalar)*P_0_1      
P_1_2=(1-1/Lam_Scalar)*P_0_1 +  (1/Lam_Scalar)*P_0_2
P_1_3=(1-1/Lam_Scalar)*P_0_2 +  (1/Lam_Scalar)*P_0_3

P_2_2=(1-1/Lam_Scalar)*P_1_1 +  (1/Lam_Scalar)*P_1_2
P_2_3=(1-1/Lam_Scalar)*P_1_2 +  (1/Lam_Scalar)*P_1_3

P_3_3=(1-1/Lam_Scalar)*P_2_2 +  (1/Lam_Scalar)*P_2_3

R[0,:]=P_0_0
R[1,:]=P_1_1
R[2,:]=P_2_2
R[3,:]=P_3_3




##################################################################################################################
# Расчет Первой-НОВОЙ Безье-крив. (=P_с_Крышкой ) 
P_Krish=P+Eps1

#  ders - для заданного "u" массив BASIS функций и  все их (до р) производныЕ
ders_p3 = np.zeros([p+1,p+1])

# C2 - массив, в нем для заданного "u" возвращаются C2[0,:]- x,y - сплайна
#                               для заданного "u"  C2[1,:]- x,y - 1-вой ПРОИЗВОДНОЙ сплайна
#                               для заданного "u"  C2[0,:]- x,y - 2-ой ПРОИЗВОДНОЙ сплайна
#                               для заданного "u"  C2[p,:]- x,y -"p"-ой ПРОИЗВОДНОЙ сплайна
C2_NURBS_p3=np.zeros([p+1,2]) # идекс "2" для 2D задачи, "3" - для 3D

n_u3=60
data_CurvePoin_and_Deriv_NURBS_P_Krish = np.zeros([(n_u3+1),(p+1),2])

#stop

for it in range(n_u3+1):
    t_i=(it/n_u2)*(t_stop1-t_start1) +  t_start1
    
    Func_1.CurvePoin_and_Deriv_NURBS(n_vert,p,T,P_Krish,HP,t_i,C2_NURBS_p3,ders_p3)
    # В массиве на след. строке Хранятся Кубич. Сплайн
    data_CurvePoin_and_Deriv_NURBS_P_Krish[it,:,:]=C2_NURBS_p3

##################################################################################################################
#stop

##################################################################################################################
# Расчет Второй-НОВОЙ Безье-крив. (=Q_с_Крышкой) 
Q_Krish=Q+Del1

#  ders - для заданного "u" массив BASIS функций и  все их (до р) производныЕ
ders_p3 = np.zeros([p+1,p+1])

# C2 - массив, в нем для заданного "u" возвращаются C2[0,:]- x,y - сплайна
#                               для заданного "u"  C2[1,:]- x,y - 1-вой ПРОИЗВОДНОЙ сплайна
#                               для заданного "u"  C2[0,:]- x,y - 2-ой ПРОИЗВОДНОЙ сплайна
#                               для заданного "u"  C2[p,:]- x,y -"p"-ой ПРОИЗВОДНОЙ сплайна
C2_NURBS_p3=np.zeros([p+1,2]) # идекс "2" для 2D задачи, "3" - для 3D

n_u3=60
data_CurvePoin_and_Deriv_NURBS_Q_Krish = np.zeros([(n_u1+1),(p+1),2])



for it in range(n_u3+1):
    t_i=(it/n_u2)*(t_stop1-t_start1) +  t_start1
    
    Func_1.CurvePoin_and_Deriv_NURBS(n_vert,p,T,Q_Krish,HQ,t_i,C2_NURBS_p3,ders_p3)
    # В массиве на след. строке Хранятся Кубич. Сплайн
    data_CurvePoin_and_Deriv_NURBS_Q_Krish[it,:,:]=C2_NURBS_p3

##################################################################################################################


#stop





Title=" *1*11"
Title=" "
labels_legend1="P Многоугольник (заданный)"
labels_legend2="P Безье Кривая (заданная)"

labels_legend3="Многоугольник Р с крышкой"
labels_legend4="P с крышкой"

labels_legend5="Q Многоугольник (заданный)"
labels_legend6="Q Безье Кривая (заданная)"

labels_legend7="Многоугольник Q с крышкой"
labels_legend8="Q с крышкой"

#y_min=-1
#y_max=40.0

#x_min=-1
#x_max=90


#   ГРАФИК для ОТЧЕТА-СТАТЬИ - ДИСКРЕТ. НОРМА
Plots_1.plot_Trace_Lines_4_for_Mergin_1 (P[:,0],P[:,1],
                                         P_Krish[:,0],P_Krish[:,1],
                                         Q[:,0],Q[:,1],
                                       Q_Krish[:,0],Q_Krish[:,1],
                                            data_CurvePoin_and_Deriv_NURBS_p1[:,0,0],data_CurvePoin_and_Deriv_NURBS_p1[:,0,1] ,  
                                             data_CurvePoin_and_Deriv_NURBS_P_Krish[:,0,0],    data_CurvePoin_and_Deriv_NURBS_P_Krish[:,0,1],
                                            data_CurvePoin_and_Deriv_NURBS_p2[:,0,0],data_CurvePoin_and_Deriv_NURBS_p2[:,0,1] ,
                                              data_CurvePoin_and_Deriv_NURBS_Q_Krish[:,0,0],    data_CurvePoin_and_Deriv_NURBS_Q_Krish[:,0,1], 
                                           
                                               y_min, y_max, x_min, x_max,
                                               Title, labels_legend1, labels_legend2,
                                                labels_legend3, labels_legend4,labels_legend5,labels_legend6,labels_legend7,labels_legend8)












#stop




##################################################################################################################
# Расчет Третьей Безье-крив. (=R - кривая) 
#  ders - для заданного "u" массив BASIS функций и  все их (до р) производныЕ
ders_p3 = np.zeros([p+1,p+1])

# C2 - массив, в нем для заданного "u" возвращаются C2[0,:]- x,y - сплайна
#                               для заданного "u"  C2[1,:]- x,y - 1-вой ПРОИЗВОДНОЙ сплайна
#                               для заданного "u"  C2[0,:]- x,y - 2-ой ПРОИЗВОДНОЙ сплайна
#                               для заданного "u"  C2[p,:]- x,y -"p"-ой ПРОИЗВОДНОЙ сплайна
C2_NURBS_p3=np.zeros([p+1,2]) # идекс "2" для 2D задачи, "3" - для 3D

n_u3=60
data_CurvePoin_and_Deriv_NURBS_p3 = np.zeros([(n_u3+1),(p+1),2])


for it in range(n_u3+1):
    t_i=(it/n_u2)*(t_stop1-t_start1) +  t_start1
    
    Func_1.CurvePoin_and_Deriv_NURBS(n_vert,p,T,R,HR,t_i,C2_NURBS_p3,ders_p3)
    # В массиве на след. строке Хранятся Кубич. Сплайн
    data_CurvePoin_and_Deriv_NURBS_p3[it,:,:]=C2_NURBS_p3

##################################################################################################################

#stop



Title="Окончательное решение - ДИСКРЕТ. НОРМА *** ОБЕ КОНЕЧНЫЕ ТОЧКИ НЕзафиксированы (СВОБОДНЫЕ) ***"
Title=" "

labels_legend1="P Многоугольник (заданный)"
labels_legend2="P Безье Кривая (заданная)"
labels_legend3="Q Многоугольник (заданный)"
labels_legend4="Q Безье Кривая (заданная)"
labels_legend5="R Многоугольник (апроксимация Р и Q)"
labels_legend6="R Безье Кривая (апроксимация Р и Q)"




#   ГРАФИК для ОТЧЕТА-СТАТЬИ - ДИСКРЕТ. НОРМА
# 
Plots_1.plot_Trace_Lines_3_for_Mergin_1 (P[:,0],P[:,1],
                                         Q[:,0],Q[:,1],
                                         R[:,0],R[:,1],
                                            data_CurvePoin_and_Deriv_NURBS_p1[:,0,0],data_CurvePoin_and_Deriv_NURBS_p1[:,0,1] ,                             
                                            data_CurvePoin_and_Deriv_NURBS_p2[:,0,0],data_CurvePoin_and_Deriv_NURBS_p2[:,0,1] ,
                                            data_CurvePoin_and_Deriv_NURBS_p3[:,0,0],data_CurvePoin_and_Deriv_NURBS_p3[:,0,1] ,    
                                           
                                               y_min, y_max, x_min, x_max,
                                               Title, labels_legend1, labels_legend2,
                                                labels_legend3, labels_legend4,labels_legend5,labels_legend6)






#stop

########################################################################################################################################
########################################################################################################################################
########################################################################################################################################





# Блок ИНТЕГЛАЛЬ. НОРМА c Ограничениями
# ОГРАНИЧЕНИЯ:  1. Задана Точка
#               


Eps1 = np.zeros([4,2])
Del1 = np.zeros([4,2])
Lam1 = np.zeros([5,2])
X1 = np.zeros([13,2])
X1_1 = np.zeros([13,2])
Matrix_A1= np.zeros([13,13]) 
Matrix_B1= np.zeros([13,2])

p=3
ders = np.zeros([p+1,p+1]) # массив, в котором - в 1-ой строке - Базисные Функции
                           #                   -   2-строка - первые Производ. Базисных Функции 
                           #                       3-строка - вторые Производ. Базисных Функции и т.д. ........

u00=0.43 # ТОЧКА НА Р-кривой, для которой заданы ограничения (ТОЧКА И ДВЕ ПРОИЗВОДНЫЕ).
span = Func_1.FindSpan(n_vert,p,u00,U);
Func_1.DersBasisFuns(span,u00,p,p,U,ders)   
N_00u0=ders[0,0]; N_10u0=ders[0,1]; N_20u0=ders[0,2]; N_30u0=ders[0,3]
N_01u0=ders[1,0]; N_11u0=ders[1,1]; N_21u0=ders[1,2]; N_31u0=ders[1,3]


##################################################################################################################


# Расчет  ИНТЕГРАЛОВ 

n_for_Integration=200
t_start1=0
t_stop1=1
del_t=(t_stop1-t_start1)/n_for_Integration

N_00=0; N_01=0; N_02=0; N_03=0
N_10=0; N_11=0; N_12=0; N_13=0
N_20=0; N_21=0; N_22=0; N_23=0
N_30=0; N_31=0; N_32=0; N_33=0

for it in range(n_for_Integration+1):
    t_i=(it/n_for_Integration)*(t_stop1-t_start1) +  t_start1
   
    span = Func_1.FindSpan(n_vert,p,t_i,U);
    Func_1.DersBasisFuns(span,t_i,p,p,U,ders)
    
    N_00=N_00 + 2*ders[0,0]*ders[0,0]*del_t
    N_01=N_01 + 2*ders[0,0]*ders[0,1]*del_t
    N_02=N_02 + 2*ders[0,0]*ders[0,2]*del_t
    N_03=N_03 + 2*ders[0,0]*ders[0,3]*del_t
    
    N_10=N_10 + 2*ders[0,1]*ders[0,0]*del_t
    N_11=N_11 + 2*ders[0,1]*ders[0,1]*del_t
    N_12=N_12 + 2*ders[0,1]*ders[0,2]*del_t
    N_13=N_13 + 2*ders[0,1]*ders[0,3]*del_t
    
    N_20=N_20 + 2*ders[0,2]*ders[0,0]*del_t
    N_21=N_21 + 2*ders[0,2]*ders[0,1]*del_t
    N_22=N_22 + 2*ders[0,2]*ders[0,2]*del_t
    N_23=N_23 + 2*ders[0,2]*ders[0,3]*del_t
    
    N_30=N_30 + 2*ders[0,3]*ders[0,0]*del_t
    N_31=N_31 + 2*ders[0,3]*ders[0,1]*del_t
    N_32=N_32 + 2*ders[0,3]*ders[0,2]*del_t
    N_33=N_33 + 2*ders[0,3]*ders[0,3]*del_t
    


#  Производные Через БАЗИСНЫЕ ФУНКЦИИ

u0=1.0 # Конечна ТОЧКА НА Р-кривой, для неё расчитываем 1. Базис. функции и 2. Три произв. Базис. Функций == ТОЧКА СОПРЯЖЕНИЯ
span = Func_1.FindSpan(n_vert,p,u0,U);
Func_1.DersBasisFuns(span,u0,p,p,U,ders)
print("*u0=",u0, "  ders=\n",ders)
N_001= ders[0,0];   N_101= ders[0,1]; N_201= ders[0,2]; N_301= ders[0,3] # НУЛЕВЫЕ ПРОИЗВОДНЫЕ = сама функция
N_011= ders[1,0];   N_111= ders[1,1]; N_211= ders[1,2]; N_311= ders[1,3] # ПЕРВЫЕ ПРОИЗВОДНЫЕ
N_021= ders[2,0];   N_121= ders[2,1]; N_221= ders[2,2]; N_321= ders[2,3] # ВТОРЫЕ ПРОИЗВОДНЫЕ
N_031= ders[3,0];   N_131= ders[3,1]; N_231= ders[3,2]; N_331= ders[3,3] # ТРЕТЬИ ПРОИЗВОДНЫЕ

#stop

u0=0.0 # ТОЧКА НА Q-кривой, для которой заданы ограничения (ТОЧКА И ТРИ ПРОИЗВОДНЫЕ) == ТОЧКА СОПРЯЖЕНИЯ
span = Func_1.FindSpan(n_vert,p,u0,U);
Func_1.DersBasisFuns(span,u0,p,p,U,ders)
print("*u0=",u0, "  ders=\n",ders)

N_000= ders[0,0];   N_100= ders[0,1]; N_200= ders[0,2]; N_300= ders[0,3] # НУЛЕВЫЕ ПРОИЗВОДНЫЕ = сама функция
N_010= ders[1,0];   N_110= ders[1,1]; N_210= ders[1,2]; N_310= ders[1,3] # ПЕРВЫЕ ПРОИЗВОДНЫЕ
N_020= ders[2,0];   N_120= ders[2,1]; N_220= ders[2,2]; N_320= ders[2,3] # ВТОРЫЕ ПРОИЗВОДНЫЕ
N_030= ders[3,0];   N_130= ders[3,1]; N_230= ders[3,2]; N_330= ders[3,3] # ТРЕТЬИ ПРОИЗВОДНЫЕ

####################################################################################################################
####################################################################################################################

# ИНТЕГРАЛЬ.  НОРМА
# **!! ЭТО МАТРИЦА ДЛЯ НЕзакрепленныз (СВОБОДНЫХ) ГРАНИЦ

#Matrix_A1[0,0]=1;  # так как Закреплен. Концы

Matrix_A1[0,0]=N_00;  Matrix_A1[0,1]=N_10;  Matrix_A1[0,2]=N_20;  Matrix_A1[0,3]=N_30;  Matrix_A1[0,8]= N_001; Matrix_A1[0,9]= N_011;  Matrix_A1[0,10]= N_021;  Matrix_A1[0,11]= N_031;  Matrix_A1[1,12]= N_00u0;  
Matrix_A1[1,0]=N_01;  Matrix_A1[1,1]=N_11;  Matrix_A1[1,2]=N_21;  Matrix_A1[1,3]=N_31;  Matrix_A1[1,8]= N_101; Matrix_A1[1,9]= N_111;  Matrix_A1[1,10]= N_121;  Matrix_A1[1,11]= N_131;  Matrix_A1[1,12]= N_10u0;  
Matrix_A1[2,0]=N_02;  Matrix_A1[2,1]=N_12;  Matrix_A1[2,2]=N_22;  Matrix_A1[2,3]=N_32;  Matrix_A1[2,8]= N_201; Matrix_A1[2,9]= N_211;  Matrix_A1[2,10]= N_221;  Matrix_A1[2,11]= N_231;  Matrix_A1[2,12]= N_20u0;  
Matrix_A1[3,0]=N_03;  Matrix_A1[3,1]=N_13;  Matrix_A1[3,2]=N_23;  Matrix_A1[3,3]=N_33;  Matrix_A1[3,8]= N_301; Matrix_A1[3,9]= N_311;  Matrix_A1[3,10]= N_321;  Matrix_A1[3,11]= N_331;  Matrix_A1[3,12]= N_30u0;  

Matrix_A1[4,4]=N_00;  Matrix_A1[4,5]=N_10;  Matrix_A1[4,6]=N_20;  Matrix_A1[4,7]=N_30;  Matrix_A1[4,8]=-N_000; Matrix_A1[4,9]=-N_010;  Matrix_A1[4,10]=-N_020;  Matrix_A1[4,11]=-N_030
Matrix_A1[5,4]=N_01;  Matrix_A1[5,5]=N_11;  Matrix_A1[5,6]=N_21;  Matrix_A1[5,7]=N_31;  Matrix_A1[5,8]=-N_100; Matrix_A1[5,9]=-N_110;  Matrix_A1[5,10]=-N_120;  Matrix_A1[5,11]=-N_130
Matrix_A1[6,4]=N_02;  Matrix_A1[6,5]=N_12;  Matrix_A1[6,6]=N_22;  Matrix_A1[6,7]=N_32;  Matrix_A1[6,8]=-N_200; Matrix_A1[6,9]=-N_210;  Matrix_A1[6,10]=-N_220;  Matrix_A1[6,11]=-N_230
Matrix_A1[7,4]=N_03;  Matrix_A1[7,5]=N_13;  Matrix_A1[7,6]=N_23;  Matrix_A1[7,7]=N_33;  Matrix_A1[7,8]=-N_300; Matrix_A1[7,9]=-N_310;  Matrix_A1[7,10]=-N_320;  Matrix_A1[7,11]=-N_330

#Matrix_A1[7,7]=1;  # так как Закреплен. Концы

Matrix_A1[8,0] =N_001; Matrix_A1[8,1] =N_101;  Matrix_A1[8,2] =N_201;  Matrix_A1[8,3] =N_301; Matrix_A1[8,4] =-N_000;  Matrix_A1[8,5] =-N_100;  Matrix_A1[8,6] =-N_200;  Matrix_A1[8,7] =-N_300;
Matrix_A1[9,0] =N_011; Matrix_A1[9,1] =N_111;  Matrix_A1[9,2] =N_211;  Matrix_A1[9,3] =N_311; Matrix_A1[9,4] =-N_010;  Matrix_A1[9,5] =-N_110;  Matrix_A1[9,6] =-N_210;  Matrix_A1[9,7] =-N_310;
Matrix_A1[10,0]=N_021; Matrix_A1[10,1]=N_121;  Matrix_A1[10,2]=N_221;  Matrix_A1[10,3]=N_321; Matrix_A1[10,4]=-N_020;  Matrix_A1[10,5]=-N_120;  Matrix_A1[10,6]=-N_220;  Matrix_A1[10,7]=-N_320;
Matrix_A1[11,0]=N_031; Matrix_A1[11,1]=N_131;  Matrix_A1[11,2]=N_231;  Matrix_A1[11,3]=N_331; Matrix_A1[11,4]=-N_030;  Matrix_A1[11,5]=-N_130;  Matrix_A1[11,6]=-N_230;  Matrix_A1[11,7]=-N_330;

Matrix_A1[12,0]= N_00u0;  Matrix_A1[12,1]= N_10u0;  Matrix_A1[12,2]= N_20u0;  Matrix_A1[12,3]= N_30u0; 


Matrix_B1[8,:]  = -P[0,:]*N_001 + Q[0,:]*N_000  -P[1,:]*N_101 + Q[1,:]*N_100  -P[2,:]*N_201 + Q[2,:]*N_200  -P[3,:]*N_301 + Q[3,:]*N_300
Matrix_B1[9,:]  = -P[0,:]*N_011 + Q[0,:]*N_010  -P[1,:]*N_111 + Q[1,:]*N_110  -P[2,:]*N_211 + Q[2,:]*N_210  -P[3,:]*N_311 + Q[3,:]*N_310
Matrix_B1[10,:] = -P[0,:]*N_021 + Q[0,:]*N_020  -P[1,:]*N_121 + Q[1,:]*N_120  -P[2,:]*N_221 + Q[2,:]*N_220  -P[3,:]*N_321 + Q[3,:]*N_320
Matrix_B1[11,:] = -P[0,:]*N_031 + Q[0,:]*N_030  -P[1,:]*N_131 + Q[1,:]*N_130  -P[2,:]*N_231 + Q[2,:]*N_230  -P[3,:]*N_331 + Q[3,:]*N_330

#print("* Matrix_A1\n",Matrix_A1)
#print("* Matrix_B1\n",Matrix_B1)
#stop

print("*** РЕШЕНИЕ *СЛАУ* c ОГРАНИЧЕНИЯМИ ***")
print("\n det(Matrix_A1)=", np.linalg.det(Matrix_A1))
print(" rank(Matrix_A1)=", np.linalg.matrix_rank(Matrix_A1))
print(" число Обусловленности(Matrix_A1)=", np.linalg.cond(Matrix_A1))
print(" rank(A1_&_B1)= ", np.linalg.matrix_rank(np.hstack((Matrix_A1,Matrix_B1))))
print(" число Обусловленности(A1&_B1=", np.linalg.cond(np.hstack((Matrix_A1,Matrix_B1))))



X1= np.linalg.solve(Matrix_A1, Matrix_B1)
print("***Решение системы:\n",X1)

#Lam = np.linalg.solve(Matrix_A, Matrix_B)
X1_1, res, r, s = np.linalg.lstsq(Matrix_A1, Matrix_B1, rcond=None)
print ("***Псевдорешение системы:\n", X1_1)


print ("**  Число Сочетаний -- math.comb(3, 2)= ",math.comb(3, 2))

Eps1=X1[0:4,:]
Del1=X1[4:8,:]




#Mu=1
#Lam_Scalar=Mu/(1+Mu) 
Lam_Scalar=0.5 
P_0=P+Eps1
P_1 = np.zeros([4,2])
P_2 = np.zeros([4,2])
P_3 = np.zeros([4,2])

P_0_0=P[0,:]+Eps1[0,:]
P_0_1=P[1,:]+Eps1[1,:]
P_0_2=P[2,:]+Eps1[2,:]
P_0_3=P[3,:]+Eps1[3,:]

        
P_1_1=(1-1/Lam_Scalar)*P_0_0 +  (1/Lam_Scalar)*P_0_1      
P_1_2=(1-1/Lam_Scalar)*P_0_1 +  (1/Lam_Scalar)*P_0_2
P_1_3=(1-1/Lam_Scalar)*P_0_2 +  (1/Lam_Scalar)*P_0_3

P_2_2=(1-1/Lam_Scalar)*P_1_1 +  (1/Lam_Scalar)*P_1_2
P_2_3=(1-1/Lam_Scalar)*P_1_2 +  (1/Lam_Scalar)*P_1_3

P_3_3=(1-1/Lam_Scalar)*P_2_2 +  (1/Lam_Scalar)*P_2_3

R[0,:]=P_0_0
R[1,:]=P_1_1
R[2,:]=P_2_2
R[3,:]=P_3_3




##################################################################################################################
# Расчет Первой-НОВОЙ Безье-крив. (=P_с_Крышкой ) 
P_Krish=P+Eps1

#  ders - для заданного "u" массив BASIS функций и  все их (до р) производныЕ
ders_p3 = np.zeros([p+1,p+1])

# C2 - массив, в нем для заданного "u" возвращаются C2[0,:]- x,y - сплайна
#                               для заданного "u"  C2[1,:]- x,y - 1-вой ПРОИЗВОДНОЙ сплайна
#                               для заданного "u"  C2[0,:]- x,y - 2-ой ПРОИЗВОДНОЙ сплайна
#                               для заданного "u"  C2[p,:]- x,y -"p"-ой ПРОИЗВОДНОЙ сплайна
C2_NURBS_p3=np.zeros([p+1,2]) # идекс "2" для 2D задачи, "3" - для 3D

n_u3=60
data_CurvePoin_and_Deriv_NURBS_P_Krish = np.zeros([(n_u3+1),(p+1),2])

#stop

for it in range(n_u3+1):
    t_i=(it/n_u2)*(t_stop1-t_start1) +  t_start1
    
    Func_1.CurvePoin_and_Deriv_NURBS(n_vert,p,T,P_Krish,HP,t_i,C2_NURBS_p3,ders_p3)
    # В массиве на след. строке Хранятся Кубич. Сплайн
    data_CurvePoin_and_Deriv_NURBS_P_Krish[it,:,:]=C2_NURBS_p3

##################################################################################################################
#stop

##################################################################################################################
# Расчет Второй-НОВОЙ Безье-крив. (=Q_с_Крышкой) 
Q_Krish=Q+Del1

#  ders - для заданного "u" массив BASIS функций и  все их (до р) производныЕ
ders_p3 = np.zeros([p+1,p+1])

# C2 - массив, в нем для заданного "u" возвращаются C2[0,:]- x,y - сплайна
#                               для заданного "u"  C2[1,:]- x,y - 1-вой ПРОИЗВОДНОЙ сплайна
#                               для заданного "u"  C2[0,:]- x,y - 2-ой ПРОИЗВОДНОЙ сплайна
#                               для заданного "u"  C2[p,:]- x,y -"p"-ой ПРОИЗВОДНОЙ сплайна
C2_NURBS_p3=np.zeros([p+1,2]) # идекс "2" для 2D задачи, "3" - для 3D

n_u3=60
data_CurvePoin_and_Deriv_NURBS_Q_Krish = np.zeros([(n_u1+1),(p+1),2])



for it in range(n_u3+1):
    t_i=(it/n_u2)*(t_stop1-t_start1) +  t_start1
    
    Func_1.CurvePoin_and_Deriv_NURBS(n_vert,p,T,Q_Krish,HQ,t_i,C2_NURBS_p3,ders_p3)
    # В массиве на след. строке Хранятся Кубич. Сплайн
    data_CurvePoin_and_Deriv_NURBS_Q_Krish[it,:,:]=C2_NURBS_p3

##################################################################################################################


#stop


##################################################################################################################
# Расчет Третьей Безье-крив. (=R - кривая) 
#  ders - для заданного "u" массив BASIS функций и  все их (до р) производныЕ
ders_p3 = np.zeros([p+1,p+1])

# C2 - массив, в нем для заданного "u" возвращаются C2[0,:]- x,y - сплайна
#                               для заданного "u"  C2[1,:]- x,y - 1-вой ПРОИЗВОДНОЙ сплайна
#                               для заданного "u"  C2[0,:]- x,y - 2-ой ПРОИЗВОДНОЙ сплайна
#                               для заданного "u"  C2[p,:]- x,y -"p"-ой ПРОИЗВОДНОЙ сплайна
C2_NURBS_p3=np.zeros([p+1,2]) # идекс "2" для 2D задачи, "3" - для 3D

n_u3=60
data_CurvePoin_and_Deriv_NURBS_p3 = np.zeros([(n_u3+1),(p+1),2])


for it in range(n_u3+1):
    t_i=(it/n_u2)*(t_stop1-t_start1) +  t_start1
    
    Func_1.CurvePoin_and_Deriv_NURBS(n_vert,p,T,R,HR,t_i,C2_NURBS_p3,ders_p3)
    # В массиве на след. строке Хранятся Кубич. Сплайн
    data_CurvePoin_and_Deriv_NURBS_p3[it,:,:]=C2_NURBS_p3

##################################################################################################################





# Расчет Координат точек, в которых заданы Ограничения
#точка u1
Func_1.CurvePoin_and_Deriv_NURBS(n_vert,p,T,P_Krish,HP,u00,C2_NURBS_p3,ders_p3) #точка u1
X11=C2_NURBS_p3[0,0]; Y11=C2_NURBS_p3[0,1]


#stop



Title="Окончательное решение - ДИСКРЕТ. НОРМА *** ОБЕ КОНЕЧНЫЕ ТОЧКИ НЕзафиксированы (СВОБОДНЫЕ) ***"
Title=" "

labels_legend1="P Многоугольник (заданный)"
labels_legend2="P Безье Кривая (заданная)"
labels_legend3="Q Многоугольник (заданный)"
labels_legend4="Q Безье Кривая (заданная)"
labels_legend5="R Многоугольник (апроксимация Р и Q)"
labels_legend6="R Безье Кривая (апроксимация Р и Q)"
labels_legend7="точка ограничений"



X12=X11; Y12=Y11;  X13=X11; Y13=Y11;  X14=X11; Y14=Y11;
#   ГРАФИК для ОТЧЕТА-СТАТЬИ - ДИСКРЕТ. НОРМА
# 
print ("**  ОГРАНИЧЕНИЕ = ТОЧКА")
Plots_1.plot_Trace_Lines_3_for_Mergin_1_plus_4_Points (X11,Y11,X12,Y12,X13,Y13,X14,Y14,
                                         P[:,0],P[:,1],
                                         Q[:,0],Q[:,1],
                                         R[:,0],R[:,1],
                                            data_CurvePoin_and_Deriv_NURBS_p1[:,0,0],data_CurvePoin_and_Deriv_NURBS_p1[:,0,1] ,                             
                                            data_CurvePoin_and_Deriv_NURBS_p2[:,0,0],data_CurvePoin_and_Deriv_NURBS_p2[:,0,1] ,
                                            data_CurvePoin_and_Deriv_NURBS_p3[:,0,0],data_CurvePoin_and_Deriv_NURBS_p3[:,0,1] ,    
                                           
                                               y_min, y_max, x_min, x_max,
                                               Title, labels_legend1, labels_legend2,
                                                labels_legend3, labels_legend4,labels_legend5,labels_legend6,labels_legend7)


#stop

########################################################################################################################################
########################################################################################################################################
########################################################################################################################################


# Блок ИНТЕГЛАЛЬ. НОРМА c Ограничениями
# ОГРАНИЧЕНИЯ:  1. Задана ТОЧКА и  ПЕРВАЯ ПРОИЗВОДНАЯ в ней
#               


Eps1 = np.zeros([4,2])
Del1 = np.zeros([4,2])
Lam1 = np.zeros([6,2])
X1 = np.zeros([14,2])
X1_1 = np.zeros([14,2])
Matrix_A1= np.zeros([14,14]) 
Matrix_B1= np.zeros([14,2])

p=3
ders = np.zeros([p+1,p+1]) # массив, в котором - в 1-ой строке - Базисные Функции
                           #                   -   2-строка - первые Производ. Базисных Функции 
                           #                       3-строка - вторые Производ. Базисных Функции и т.д. ........

# u00 ==  ТОЧКА НА Р-кривой, для которой заданы ограничения (ТОЧКА И ПЕРВАЯ ПРОИЗВОДНАЯ).
span = Func_1.FindSpan(n_vert,p,u00,U);
Func_1.DersBasisFuns(span,u00,p,p,U,ders)   
N_00u0=ders[0,0]; N_10u0=ders[0,1]; N_20u0=ders[0,2]; N_30u0=ders[0,3]
N_01u0=ders[1,0]; N_11u0=ders[1,1]; N_21u0=ders[1,2]; N_31u0=ders[1,3]


##################################################################################################################


# Расчет  ИНТЕГРАЛОВ 

n_for_Integration=200
t_start1=0
t_stop1=1
del_t=(t_stop1-t_start1)/n_for_Integration

N_00=0; N_01=0; N_02=0; N_03=0
N_10=0; N_11=0; N_12=0; N_13=0
N_20=0; N_21=0; N_22=0; N_23=0
N_30=0; N_31=0; N_32=0; N_33=0

for it in range(n_for_Integration+1):
    t_i=(it/n_for_Integration)*(t_stop1-t_start1) +  t_start1
   
    span = Func_1.FindSpan(n_vert,p,t_i,U);
    Func_1.DersBasisFuns(span,t_i,p,p,U,ders)
    
    N_00=N_00 + 2*ders[0,0]*ders[0,0]*del_t
    N_01=N_01 + 2*ders[0,0]*ders[0,1]*del_t
    N_02=N_02 + 2*ders[0,0]*ders[0,2]*del_t
    N_03=N_03 + 2*ders[0,0]*ders[0,3]*del_t
    
    N_10=N_10 + 2*ders[0,1]*ders[0,0]*del_t
    N_11=N_11 + 2*ders[0,1]*ders[0,1]*del_t
    N_12=N_12 + 2*ders[0,1]*ders[0,2]*del_t
    N_13=N_13 + 2*ders[0,1]*ders[0,3]*del_t
    
    N_20=N_20 + 2*ders[0,2]*ders[0,0]*del_t
    N_21=N_21 + 2*ders[0,2]*ders[0,1]*del_t
    N_22=N_22 + 2*ders[0,2]*ders[0,2]*del_t
    N_23=N_23 + 2*ders[0,2]*ders[0,3]*del_t
    
    N_30=N_30 + 2*ders[0,3]*ders[0,0]*del_t
    N_31=N_31 + 2*ders[0,3]*ders[0,1]*del_t
    N_32=N_32 + 2*ders[0,3]*ders[0,2]*del_t
    N_33=N_33 + 2*ders[0,3]*ders[0,3]*del_t
    


#  Производные Через БАЗИСНЫЕ ФУНКЦИИ

u0=1.0 # Конечна ТОЧКА НА Р-кривой, для неё расчитываем 1. Базис. функции и 2. Три произв. Базис. Функций == ТОЧКА СОПРЯЖЕНИЯ
span = Func_1.FindSpan(n_vert,p,u0,U);
Func_1.DersBasisFuns(span,u0,p,p,U,ders)
print("*u0=",u0, "  ders=\n",ders)
N_001= ders[0,0];   N_101= ders[0,1]; N_201= ders[0,2]; N_301= ders[0,3] # НУЛЕВЫЕ ПРОИЗВОДНЫЕ = сама функция
N_011= ders[1,0];   N_111= ders[1,1]; N_211= ders[1,2]; N_311= ders[1,3] # ПЕРВЫЕ ПРОИЗВОДНЫЕ
N_021= ders[2,0];   N_121= ders[2,1]; N_221= ders[2,2]; N_321= ders[2,3] # ВТОРЫЕ ПРОИЗВОДНЫЕ
N_031= ders[3,0];   N_131= ders[3,1]; N_231= ders[3,2]; N_331= ders[3,3] # ТРЕТЬИ ПРОИЗВОДНЫЕ

#stop

u0=0.0 # ТОЧКА НА Q-кривой, для которой заданы ограничения (ТОЧКА И ТРИ ПРОИЗВОДНЫЕ) == ТОЧКА СОПРЯЖЕНИЯ
span = Func_1.FindSpan(n_vert,p,u0,U);
Func_1.DersBasisFuns(span,u0,p,p,U,ders)
print("*u0=",u0, "  ders=\n",ders)

N_000= ders[0,0];   N_100= ders[0,1]; N_200= ders[0,2]; N_300= ders[0,3] # НУЛЕВЫЕ ПРОИЗВОДНЫЕ = сама функция
N_010= ders[1,0];   N_110= ders[1,1]; N_210= ders[1,2]; N_310= ders[1,3] # ПЕРВЫЕ ПРОИЗВОДНЫЕ
N_020= ders[2,0];   N_120= ders[2,1]; N_220= ders[2,2]; N_320= ders[2,3] # ВТОРЫЕ ПРОИЗВОДНЫЕ
N_030= ders[3,0];   N_130= ders[3,1]; N_230= ders[3,2]; N_330= ders[3,3] # ТРЕТЬИ ПРОИЗВОДНЫЕ

####################################################################################################################
####################################################################################################################

# ИНТЕГРАЛЬ.  НОРМА
# **!! ЭТО МАТРИЦА ДЛЯ НЕзакрепленныз (СВОБОДНЫХ) ГРАНИЦ

#Matrix_A1[0,0]=1;  # так как Закреплен. Концы

Matrix_A1[0,0]=N_00;  Matrix_A1[0,1]=N_10;  Matrix_A1[0,2]=N_20;  Matrix_A1[0,3]=N_30;  Matrix_A1[0,8]= N_001; Matrix_A1[0,9]= N_011;  Matrix_A1[0,10]= N_021;  Matrix_A1[0,11]= N_031;  Matrix_A1[1,12]= N_00u0;  Matrix_A1[1,13]= N_01u0;
Matrix_A1[1,0]=N_01;  Matrix_A1[1,1]=N_11;  Matrix_A1[1,2]=N_21;  Matrix_A1[1,3]=N_31;  Matrix_A1[1,8]= N_101; Matrix_A1[1,9]= N_111;  Matrix_A1[1,10]= N_121;  Matrix_A1[1,11]= N_131;  Matrix_A1[1,12]= N_10u0;  Matrix_A1[1,13]= N_11u0;
Matrix_A1[2,0]=N_02;  Matrix_A1[2,1]=N_12;  Matrix_A1[2,2]=N_22;  Matrix_A1[2,3]=N_32;  Matrix_A1[2,8]= N_201; Matrix_A1[2,9]= N_211;  Matrix_A1[2,10]= N_221;  Matrix_A1[2,11]= N_231;  Matrix_A1[2,12]= N_20u0;  Matrix_A1[2,13]= N_21u0;  
Matrix_A1[3,0]=N_03;  Matrix_A1[3,1]=N_13;  Matrix_A1[3,2]=N_23;  Matrix_A1[3,3]=N_33;  Matrix_A1[3,8]= N_301; Matrix_A1[3,9]= N_311;  Matrix_A1[3,10]= N_321;  Matrix_A1[3,11]= N_331;  Matrix_A1[3,12]= N_30u0;  Matrix_A1[3,13]= N_31u0;

Matrix_A1[4,4]=N_00;  Matrix_A1[4,5]=N_10;  Matrix_A1[4,6]=N_20;  Matrix_A1[4,7]=N_30;  Matrix_A1[4,8]=-N_000; Matrix_A1[4,9]=-N_010;  Matrix_A1[4,10]=-N_020;  Matrix_A1[4,11]=-N_030
Matrix_A1[5,4]=N_01;  Matrix_A1[5,5]=N_11;  Matrix_A1[5,6]=N_21;  Matrix_A1[5,7]=N_31;  Matrix_A1[5,8]=-N_100; Matrix_A1[5,9]=-N_110;  Matrix_A1[5,10]=-N_120;  Matrix_A1[5,11]=-N_130
Matrix_A1[6,4]=N_02;  Matrix_A1[6,5]=N_12;  Matrix_A1[6,6]=N_22;  Matrix_A1[6,7]=N_32;  Matrix_A1[6,8]=-N_200; Matrix_A1[6,9]=-N_210;  Matrix_A1[6,10]=-N_220;  Matrix_A1[6,11]=-N_230
Matrix_A1[7,4]=N_03;  Matrix_A1[7,5]=N_13;  Matrix_A1[7,6]=N_23;  Matrix_A1[7,7]=N_33;  Matrix_A1[7,8]=-N_300; Matrix_A1[7,9]=-N_310;  Matrix_A1[7,10]=-N_320;  Matrix_A1[7,11]=-N_330

#Matrix_A1[7,7]=1;  # так как Закреплен. Концы

Matrix_A1[8,0] =N_001; Matrix_A1[8,1] =N_101;  Matrix_A1[8,2] =N_201;  Matrix_A1[8,3] =N_301; Matrix_A1[8,4] =-N_000;  Matrix_A1[8,5] =-N_100;  Matrix_A1[8,6] =-N_200;  Matrix_A1[8,7] =-N_300;
Matrix_A1[9,0] =N_011; Matrix_A1[9,1] =N_111;  Matrix_A1[9,2] =N_211;  Matrix_A1[9,3] =N_311; Matrix_A1[9,4] =-N_010;  Matrix_A1[9,5] =-N_110;  Matrix_A1[9,6] =-N_210;  Matrix_A1[9,7] =-N_310;
Matrix_A1[10,0]=N_021; Matrix_A1[10,1]=N_121;  Matrix_A1[10,2]=N_221;  Matrix_A1[10,3]=N_321; Matrix_A1[10,4]=-N_020;  Matrix_A1[10,5]=-N_120;  Matrix_A1[10,6]=-N_220;  Matrix_A1[10,7]=-N_320;
Matrix_A1[11,0]=N_031; Matrix_A1[11,1]=N_131;  Matrix_A1[11,2]=N_231;  Matrix_A1[11,3]=N_331; Matrix_A1[11,4]=-N_030;  Matrix_A1[11,5]=-N_130;  Matrix_A1[11,6]=-N_230;  Matrix_A1[11,7]=-N_330;

Matrix_A1[12,0]= N_00u0;  Matrix_A1[12,1]= N_10u0;  Matrix_A1[12,2]= N_20u0;  Matrix_A1[12,3]= N_30u0; 
Matrix_A1[13,0]= N_01u0;  Matrix_A1[13,1]= N_11u0;  Matrix_A1[13,2]= N_21u0;  Matrix_A1[13,3]= N_31u0; 

Matrix_B1[8,:]  = -P[0,:]*N_001 + Q[0,:]*N_000  -P[1,:]*N_101 + Q[1,:]*N_100  -P[2,:]*N_201 + Q[2,:]*N_200  -P[3,:]*N_301 + Q[3,:]*N_300
Matrix_B1[9,:]  = -P[0,:]*N_011 + Q[0,:]*N_010  -P[1,:]*N_111 + Q[1,:]*N_110  -P[2,:]*N_211 + Q[2,:]*N_210  -P[3,:]*N_311 + Q[3,:]*N_310
Matrix_B1[10,:] = -P[0,:]*N_021 + Q[0,:]*N_020  -P[1,:]*N_121 + Q[1,:]*N_120  -P[2,:]*N_221 + Q[2,:]*N_220  -P[3,:]*N_321 + Q[3,:]*N_320
Matrix_B1[11,:] = -P[0,:]*N_031 + Q[0,:]*N_030  -P[1,:]*N_131 + Q[1,:]*N_130  -P[2,:]*N_231 + Q[2,:]*N_230  -P[3,:]*N_331 + Q[3,:]*N_330

#print("* Matrix_A1\n",Matrix_A1)
#print("* Matrix_B1\n",Matrix_B1)
#stop

print("*** РЕШЕНИЕ *СЛАУ* c ОГРАНИЧЕНИЯМИ ***")
print("\n det(Matrix_A1)=", np.linalg.det(Matrix_A1))
print(" rank(Matrix_A1)=", np.linalg.matrix_rank(Matrix_A1))
print(" число Обусловленности(Matrix_A1)=", np.linalg.cond(Matrix_A1))
print(" rank(A1_&_B1)= ", np.linalg.matrix_rank(np.hstack((Matrix_A1,Matrix_B1))))
print(" число Обусловленности(A1&_B1=", np.linalg.cond(np.hstack((Matrix_A1,Matrix_B1))))



X1= np.linalg.solve(Matrix_A1, Matrix_B1)
print("***Решение системы:\n",X1)

#Lam = np.linalg.solve(Matrix_A, Matrix_B)
X1_1, res, r, s = np.linalg.lstsq(Matrix_A1, Matrix_B1, rcond=None)
print ("***Псевдорешение системы:\n", X1_1)


print ("**  Число Сочетаний -- math.comb(3, 2)= ",math.comb(3, 2))

Eps1=X1[0:4,:]
Del1=X1[4:8,:]




#Mu=1
#Lam_Scalar=Mu/(1+Mu) 
Lam_Scalar=0.5 
P_0=P+Eps1
P_1 = np.zeros([4,2])
P_2 = np.zeros([4,2])
P_3 = np.zeros([4,2])

P_0_0=P[0,:]+Eps1[0,:]
P_0_1=P[1,:]+Eps1[1,:]
P_0_2=P[2,:]+Eps1[2,:]
P_0_3=P[3,:]+Eps1[3,:]

        
P_1_1=(1-1/Lam_Scalar)*P_0_0 +  (1/Lam_Scalar)*P_0_1      
P_1_2=(1-1/Lam_Scalar)*P_0_1 +  (1/Lam_Scalar)*P_0_2
P_1_3=(1-1/Lam_Scalar)*P_0_2 +  (1/Lam_Scalar)*P_0_3

P_2_2=(1-1/Lam_Scalar)*P_1_1 +  (1/Lam_Scalar)*P_1_2
P_2_3=(1-1/Lam_Scalar)*P_1_2 +  (1/Lam_Scalar)*P_1_3

P_3_3=(1-1/Lam_Scalar)*P_2_2 +  (1/Lam_Scalar)*P_2_3

R[0,:]=P_0_0
R[1,:]=P_1_1
R[2,:]=P_2_2
R[3,:]=P_3_3




##################################################################################################################
# Расчет Первой-НОВОЙ Безье-крив. (=P_с_Крышкой ) 
P_Krish=P+Eps1

#  ders - для заданного "u" массив BASIS функций и  все их (до р) производныЕ
ders_p3 = np.zeros([p+1,p+1])

# C2 - массив, в нем для заданного "u" возвращаются C2[0,:]- x,y - сплайна
#                               для заданного "u"  C2[1,:]- x,y - 1-вой ПРОИЗВОДНОЙ сплайна
#                               для заданного "u"  C2[0,:]- x,y - 2-ой ПРОИЗВОДНОЙ сплайна
#                               для заданного "u"  C2[p,:]- x,y -"p"-ой ПРОИЗВОДНОЙ сплайна
C2_NURBS_p3=np.zeros([p+1,2]) # идекс "2" для 2D задачи, "3" - для 3D

n_u3=60
data_CurvePoin_and_Deriv_NURBS_P_Krish = np.zeros([(n_u3+1),(p+1),2])

#stop

for it in range(n_u3+1):
    t_i=(it/n_u2)*(t_stop1-t_start1) +  t_start1
    
    Func_1.CurvePoin_and_Deriv_NURBS(n_vert,p,T,P_Krish,HP,t_i,C2_NURBS_p3,ders_p3)
    # В массиве на след. строке Хранятся Кубич. Сплайн
    data_CurvePoin_and_Deriv_NURBS_P_Krish[it,:,:]=C2_NURBS_p3

##################################################################################################################
#stop

##################################################################################################################
# Расчет Второй-НОВОЙ Безье-крив. (=Q_с_Крышкой) 
Q_Krish=Q+Del1

#  ders - для заданного "u" массив BASIS функций и  все их (до р) производныЕ
ders_p3 = np.zeros([p+1,p+1])

# C2 - массив, в нем для заданного "u" возвращаются C2[0,:]- x,y - сплайна
#                               для заданного "u"  C2[1,:]- x,y - 1-вой ПРОИЗВОДНОЙ сплайна
#                               для заданного "u"  C2[0,:]- x,y - 2-ой ПРОИЗВОДНОЙ сплайна
#                               для заданного "u"  C2[p,:]- x,y -"p"-ой ПРОИЗВОДНОЙ сплайна
C2_NURBS_p3=np.zeros([p+1,2]) # идекс "2" для 2D задачи, "3" - для 3D

n_u3=60
data_CurvePoin_and_Deriv_NURBS_Q_Krish = np.zeros([(n_u1+1),(p+1),2])



for it in range(n_u3+1):
    t_i=(it/n_u2)*(t_stop1-t_start1) +  t_start1
    
    Func_1.CurvePoin_and_Deriv_NURBS(n_vert,p,T,Q_Krish,HQ,t_i,C2_NURBS_p3,ders_p3)
    # В массиве на след. строке Хранятся Кубич. Сплайн
    data_CurvePoin_and_Deriv_NURBS_Q_Krish[it,:,:]=C2_NURBS_p3

##################################################################################################################


#stop


##################################################################################################################
# Расчет Третьей Безье-крив. (=R - кривая) 
#  ders - для заданного "u" массив BASIS функций и  все их (до р) производныЕ
ders_p3 = np.zeros([p+1,p+1])

# C2 - массив, в нем для заданного "u" возвращаются C2[0,:]- x,y - сплайна
#                               для заданного "u"  C2[1,:]- x,y - 1-вой ПРОИЗВОДНОЙ сплайна
#                               для заданного "u"  C2[0,:]- x,y - 2-ой ПРОИЗВОДНОЙ сплайна
#                               для заданного "u"  C2[p,:]- x,y -"p"-ой ПРОИЗВОДНОЙ сплайна
C2_NURBS_p3=np.zeros([p+1,2]) # идекс "2" для 2D задачи, "3" - для 3D

n_u3=60
data_CurvePoin_and_Deriv_NURBS_p3 = np.zeros([(n_u3+1),(p+1),2])


for it in range(n_u3+1):
    t_i=(it/n_u2)*(t_stop1-t_start1) +  t_start1
    
    Func_1.CurvePoin_and_Deriv_NURBS(n_vert,p,T,R,HR,t_i,C2_NURBS_p3,ders_p3)
    # В массиве на след. строке Хранятся Кубич. Сплайн
    data_CurvePoin_and_Deriv_NURBS_p3[it,:,:]=C2_NURBS_p3

##################################################################################################################





# Расчет Координат точек, в которых заданы Ограничения
#точка u1
Func_1.CurvePoin_and_Deriv_NURBS(n_vert,p,T,P_Krish,HP,u00,C2_NURBS_p3,ders_p3) #точка u1
X11=C2_NURBS_p3[0,0]; Y11=C2_NURBS_p3[0,1]


#stop



Title="Окончательное решение - ДИСКРЕТ. НОРМА *** ОБЕ КОНЕЧНЫЕ ТОЧКИ НЕзафиксированы (СВОБОДНЫЕ) ***"
Title=" "

labels_legend1="P Многоугольник (заданный)"
labels_legend2="P Безье Кривая (заданная)"
labels_legend3="Q Многоугольник (заданный)"
labels_legend4="Q Безье Кривая (заданная)"
labels_legend5="R Многоугольник (апроксимация Р и Q)"
labels_legend6="R Безье Кривая (апроксимация Р и Q)"
labels_legend7="точка ограничений"



X12=X11; Y12=Y11;  X13=X11; Y13=Y11;  X14=X11; Y14=Y11;
#   ГРАФИК для ОТЧЕТА-СТАТЬИ - ДИСКРЕТ. НОРМА
# 
print ("**  ОГРАНИЧЕНИЕ = ТОЧКА & ПЕРВАЯ ПРОИЗВОДНАЯ")
Plots_1.plot_Trace_Lines_3_for_Mergin_1_plus_4_Points (X11,Y11,X12,Y12,X13,Y13,X14,Y14,
                                         P[:,0],P[:,1],
                                         Q[:,0],Q[:,1],
                                         R[:,0],R[:,1],
                                            data_CurvePoin_and_Deriv_NURBS_p1[:,0,0],data_CurvePoin_and_Deriv_NURBS_p1[:,0,1] ,                             
                                            data_CurvePoin_and_Deriv_NURBS_p2[:,0,0],data_CurvePoin_and_Deriv_NURBS_p2[:,0,1] ,
                                            data_CurvePoin_and_Deriv_NURBS_p3[:,0,0],data_CurvePoin_and_Deriv_NURBS_p3[:,0,1] ,    
                                           
                                               y_min, y_max, x_min, x_max,
                                               Title, labels_legend1, labels_legend2,
                                                labels_legend3, labels_legend4,labels_legend5,labels_legend6,labels_legend7)


#stop





########################################################################################################################################
########################################################################################################################################
########################################################################################################################################





# Блок ИНТЕГЛАЛЬ. НОРМА c Ограничениями
# ОГРАНИЧЕНИЯ:   Точка и Две Производные в Этой Точке


Eps1 = np.zeros([4,2])
Del1 = np.zeros([4,2])
Lam1 = np.zeros([7,2])
X1 = np.zeros([15,2])
X1_1 = np.zeros([15,2])
Matrix_A1= np.zeros([15,15]) 
Matrix_B1= np.zeros([15,2])

p=3
ders = np.zeros([p+1,p+1]) # массив, в котором - в 1-ой строке - Базисные Функции
                           #                   -   2-строка - первые Производ. Базисных Функции 
                           #                       3-строка - вторые Производ. Базисных Функции и т.д. ........

# u00 =- ТОЧКА НА Р-кривой, для которой заданы ограничения (ТОЧКА И ДВЕ ПРОИЗВОДНЫЕ).
span = Func_1.FindSpan(n_vert,p,u00,U);
Func_1.DersBasisFuns(span,u00,p,p,U,ders)   
N_00u0=ders[0,0]; N_10u0=ders[0,1]; N_20u0=ders[0,2]; N_30u0=ders[0,3]
N_01u0=ders[1,0]; N_11u0=ders[1,1]; N_21u0=ders[1,2]; N_31u0=ders[1,3]
N_02u0=ders[2,0]; N_12u0=ders[2,1]; N_22u0=ders[2,2]; N_32u0=ders[2,3]

# Расчет  ИНТЕГРАЛОВ 

n_for_Integration=200
t_start1=0
t_stop1=1
del_t=(t_stop1-t_start1)/n_for_Integration

N_00=0; N_01=0; N_02=0; N_03=0
N_10=0; N_11=0; N_12=0; N_13=0
N_20=0; N_21=0; N_22=0; N_23=0
N_30=0; N_31=0; N_32=0; N_33=0

for it in range(n_for_Integration+1):
    t_i=(it/n_for_Integration)*(t_stop1-t_start1) +  t_start1
   
    span = Func_1.FindSpan(n_vert,p,t_i,U);
    Func_1.DersBasisFuns(span,t_i,p,p,U,ders)
    
    N_00=N_00 + 2*ders[0,0]*ders[0,0]*del_t
    N_01=N_01 + 2*ders[0,0]*ders[0,1]*del_t
    N_02=N_02 + 2*ders[0,0]*ders[0,2]*del_t
    N_03=N_03 + 2*ders[0,0]*ders[0,3]*del_t
    
    N_10=N_10 + 2*ders[0,1]*ders[0,0]*del_t
    N_11=N_11 + 2*ders[0,1]*ders[0,1]*del_t
    N_12=N_12 + 2*ders[0,1]*ders[0,2]*del_t
    N_13=N_13 + 2*ders[0,1]*ders[0,3]*del_t
    
    N_20=N_20 + 2*ders[0,2]*ders[0,0]*del_t
    N_21=N_21 + 2*ders[0,2]*ders[0,1]*del_t
    N_22=N_22 + 2*ders[0,2]*ders[0,2]*del_t
    N_23=N_23 + 2*ders[0,2]*ders[0,3]*del_t
    
    N_30=N_30 + 2*ders[0,3]*ders[0,0]*del_t
    N_31=N_31 + 2*ders[0,3]*ders[0,1]*del_t
    N_32=N_32 + 2*ders[0,3]*ders[0,2]*del_t
    N_33=N_33 + 2*ders[0,3]*ders[0,3]*del_t
    


#  Производные Через БАЗИСНЫЕ ФУНКЦИИ

u0=1.0 # Конечна ТОЧКА НА Р-кривой, для неё расчитываем 1. Базис. функции и 2. Три произв. Базис. Функций == ТОЧКА СОПРЯЖЕНИЯ
span = Func_1.FindSpan(n_vert,p,u0,U);
Func_1.DersBasisFuns(span,u0,p,p,U,ders)
print("*u0=",u0, "  ders=\n",ders)
N_001= ders[0,0];   N_101= ders[0,1]; N_201= ders[0,2]; N_301= ders[0,3] # НУЛЕВЫЕ ПРОИЗВОДНЫЕ = сама функция
N_011= ders[1,0];   N_111= ders[1,1]; N_211= ders[1,2]; N_311= ders[1,3] # ПЕРВЫЕ ПРОИЗВОДНЫЕ
N_021= ders[2,0];   N_121= ders[2,1]; N_221= ders[2,2]; N_321= ders[2,3] # ВТОРЫЕ ПРОИЗВОДНЫЕ
N_031= ders[3,0];   N_131= ders[3,1]; N_231= ders[3,2]; N_331= ders[3,3] # ТРЕТЬИ ПРОИЗВОДНЫЕ

#stop

u0=0.0 # ТОЧКА НА Q-кривой, для которой заданы ограничения (ТОЧКА И ТРИ ПРОИЗВОДНЫЕ) == ТОЧКА СОПРЯЖЕНИЯ
span = Func_1.FindSpan(n_vert,p,u0,U);
Func_1.DersBasisFuns(span,u0,p,p,U,ders)
print("*u0=",u0, "  ders=\n",ders)

N_000= ders[0,0];   N_100= ders[0,1]; N_200= ders[0,2]; N_300= ders[0,3] # НУЛЕВЫЕ ПРОИЗВОДНЫЕ = сама функция
N_010= ders[1,0];   N_110= ders[1,1]; N_210= ders[1,2]; N_310= ders[1,3] # ПЕРВЫЕ ПРОИЗВОДНЫЕ
N_020= ders[2,0];   N_120= ders[2,1]; N_220= ders[2,2]; N_320= ders[2,3] # ВТОРЫЕ ПРОИЗВОДНЫЕ
N_030= ders[3,0];   N_130= ders[3,1]; N_230= ders[3,2]; N_330= ders[3,3] # ТРЕТЬИ ПРОИЗВОДНЫЕ

####################################################################################################################
####################################################################################################################

# ИНТЕГРАЛЬ.  НОРМА
# **!! ЭТО МАТРИЦА ДЛЯ НЕзакрепленныз (СВОБОДНЫХ) ГРАНИЦ

#Matrix_A1[0,0]=1;  # так как Закреплен. Концы

Matrix_A1[0,0]=N_00;  Matrix_A1[0,1]=N_10;  Matrix_A1[0,2]=N_20;  Matrix_A1[0,3]=N_30;  Matrix_A1[0,8]= N_001; Matrix_A1[0,9]= N_011;  Matrix_A1[0,10]= N_021;  Matrix_A1[0,11]= N_031;  Matrix_A1[1,12]= N_00u0;  Matrix_A1[1,13]= N_01u0;  Matrix_A1[1,14]= N_02u0
Matrix_A1[1,0]=N_01;  Matrix_A1[1,1]=N_11;  Matrix_A1[1,2]=N_21;  Matrix_A1[1,3]=N_31;  Matrix_A1[1,8]= N_101; Matrix_A1[1,9]= N_111;  Matrix_A1[1,10]= N_121;  Matrix_A1[1,11]= N_131;  Matrix_A1[1,12]= N_10u0;  Matrix_A1[1,13]= N_11u0;  Matrix_A1[1,14]= N_12u0
Matrix_A1[2,0]=N_02;  Matrix_A1[2,1]=N_12;  Matrix_A1[2,2]=N_22;  Matrix_A1[2,3]=N_32;  Matrix_A1[2,8]= N_201; Matrix_A1[2,9]= N_211;  Matrix_A1[2,10]= N_221;  Matrix_A1[2,11]= N_231;  Matrix_A1[2,12]= N_20u0;  Matrix_A1[2,13]= N_21u0;  Matrix_A1[2,14]= N_22u0
Matrix_A1[3,0]=N_03;  Matrix_A1[3,1]=N_13;  Matrix_A1[3,2]=N_23;  Matrix_A1[3,3]=N_33;  Matrix_A1[3,8]= N_301; Matrix_A1[3,9]= N_311;  Matrix_A1[3,10]= N_321;  Matrix_A1[3,11]= N_331;  Matrix_A1[3,12]= N_30u0;  Matrix_A1[3,13]= N_31u0;  Matrix_A1[3,14]= N_32u0

Matrix_A1[4,4]=N_00;  Matrix_A1[4,5]=N_10;  Matrix_A1[4,6]=N_20;  Matrix_A1[4,7]=N_30;  Matrix_A1[4,8]=-N_000; Matrix_A1[4,9]=-N_010;  Matrix_A1[4,10]=-N_020;  Matrix_A1[4,11]=-N_030
Matrix_A1[5,4]=N_01;  Matrix_A1[5,5]=N_11;  Matrix_A1[5,6]=N_21;  Matrix_A1[5,7]=N_31;  Matrix_A1[5,8]=-N_100; Matrix_A1[5,9]=-N_110;  Matrix_A1[5,10]=-N_120;  Matrix_A1[5,11]=-N_130
Matrix_A1[6,4]=N_02;  Matrix_A1[6,5]=N_12;  Matrix_A1[6,6]=N_22;  Matrix_A1[6,7]=N_32;  Matrix_A1[6,8]=-N_200; Matrix_A1[6,9]=-N_210;  Matrix_A1[6,10]=-N_220;  Matrix_A1[6,11]=-N_230
Matrix_A1[7,4]=N_03;  Matrix_A1[7,5]=N_13;  Matrix_A1[7,6]=N_23;  Matrix_A1[7,7]=N_33;  Matrix_A1[7,8]=-N_300; Matrix_A1[7,9]=-N_310;  Matrix_A1[7,10]=-N_320;  Matrix_A1[7,11]=-N_330

#Matrix_A1[7,7]=1;  # так как Закреплен. Концы

Matrix_A1[8,0] =N_001; Matrix_A1[8,1] =N_101;  Matrix_A1[8,2] =N_201;  Matrix_A1[8,3] =N_301; Matrix_A1[8,4] =-N_000;  Matrix_A1[8,5] =-N_100;  Matrix_A1[8,6] =-N_200;  Matrix_A1[8,7] =-N_300;
Matrix_A1[9,0] =N_011; Matrix_A1[9,1] =N_111;  Matrix_A1[9,2] =N_211;  Matrix_A1[9,3] =N_311; Matrix_A1[9,4] =-N_010;  Matrix_A1[9,5] =-N_110;  Matrix_A1[9,6] =-N_210;  Matrix_A1[9,7] =-N_310;
Matrix_A1[10,0]=N_021; Matrix_A1[10,1]=N_121;  Matrix_A1[10,2]=N_221;  Matrix_A1[10,3]=N_321; Matrix_A1[10,4]=-N_020;  Matrix_A1[10,5]=-N_120;  Matrix_A1[10,6]=-N_220;  Matrix_A1[10,7]=-N_320;
Matrix_A1[11,0]=N_031; Matrix_A1[11,1]=N_131;  Matrix_A1[11,2]=N_231;  Matrix_A1[11,3]=N_331; Matrix_A1[11,4]=-N_030;  Matrix_A1[11,5]=-N_130;  Matrix_A1[11,6]=-N_230;  Matrix_A1[11,7]=-N_330;

Matrix_A1[12,0]= N_00u0;  Matrix_A1[12,1]= N_10u0;  Matrix_A1[12,2]= N_20u0;  Matrix_A1[12,3]= N_30u0; 
Matrix_A1[13,0]= N_01u0;  Matrix_A1[13,1]= N_11u0;  Matrix_A1[13,2]= N_21u0;  Matrix_A1[13,3]= N_31u0; 
Matrix_A1[14,0]= N_02u0;  Matrix_A1[14,1]= N_12u0;  Matrix_A1[14,2]= N_22u0;  Matrix_A1[14,3]= N_32u0; 

Matrix_B1[8,:]  = -P[0,:]*N_001 + Q[0,:]*N_000  -P[1,:]*N_101 + Q[1,:]*N_100  -P[2,:]*N_201 + Q[2,:]*N_200  -P[3,:]*N_301 + Q[3,:]*N_300
Matrix_B1[9,:]  = -P[0,:]*N_011 + Q[0,:]*N_010  -P[1,:]*N_111 + Q[1,:]*N_110  -P[2,:]*N_211 + Q[2,:]*N_210  -P[3,:]*N_311 + Q[3,:]*N_310
Matrix_B1[10,:] = -P[0,:]*N_021 + Q[0,:]*N_020  -P[1,:]*N_121 + Q[1,:]*N_120  -P[2,:]*N_221 + Q[2,:]*N_220  -P[3,:]*N_321 + Q[3,:]*N_320
Matrix_B1[11,:] = -P[0,:]*N_031 + Q[0,:]*N_030  -P[1,:]*N_131 + Q[1,:]*N_130  -P[2,:]*N_231 + Q[2,:]*N_230  -P[3,:]*N_331 + Q[3,:]*N_330

#print("* Matrix_A1\n",Matrix_A1)
#print("* Matrix_B1\n",Matrix_B1)
#stop

print("*** РЕШЕНИЕ *СЛАУ* c ОГРАНИЧЕНИЯМИ ***")
print("\n det(Matrix_A1)=", np.linalg.det(Matrix_A1))
print(" rank(Matrix_A1)=", np.linalg.matrix_rank(Matrix_A1))
print(" число Обусловленности(Matrix_A1)=", np.linalg.cond(Matrix_A1))
print(" rank(A1_&_B1)= ", np.linalg.matrix_rank(np.hstack((Matrix_A1,Matrix_B1))))
print(" число Обусловленности(A1&_B1=", np.linalg.cond(np.hstack((Matrix_A1,Matrix_B1))))



X1= np.linalg.solve(Matrix_A1, Matrix_B1)
print("***Решение системы:\n",X1)

#Lam = np.linalg.solve(Matrix_A, Matrix_B)
X1_1, res, r, s = np.linalg.lstsq(Matrix_A1, Matrix_B1, rcond=None)
print ("***Псевдорешение системы:\n", X1_1)


print ("**  Число Сочетаний -- math.comb(3, 2)= ",math.comb(3, 2))

Eps1=X1[0:4,:]
Del1=X1[4:8,:]




#Mu=1
#Lam_Scalar=Mu/(1+Mu) 
Lam_Scalar=0.5 
P_0=P+Eps1
P_1 = np.zeros([4,2])
P_2 = np.zeros([4,2])
P_3 = np.zeros([4,2])

P_0_0=P[0,:]+Eps1[0,:]
P_0_1=P[1,:]+Eps1[1,:]
P_0_2=P[2,:]+Eps1[2,:]
P_0_3=P[3,:]+Eps1[3,:]

        
P_1_1=(1-1/Lam_Scalar)*P_0_0 +  (1/Lam_Scalar)*P_0_1      
P_1_2=(1-1/Lam_Scalar)*P_0_1 +  (1/Lam_Scalar)*P_0_2
P_1_3=(1-1/Lam_Scalar)*P_0_2 +  (1/Lam_Scalar)*P_0_3

P_2_2=(1-1/Lam_Scalar)*P_1_1 +  (1/Lam_Scalar)*P_1_2
P_2_3=(1-1/Lam_Scalar)*P_1_2 +  (1/Lam_Scalar)*P_1_3

P_3_3=(1-1/Lam_Scalar)*P_2_2 +  (1/Lam_Scalar)*P_2_3

R[0,:]=P_0_0
R[1,:]=P_1_1
R[2,:]=P_2_2
R[3,:]=P_3_3




##################################################################################################################
# Расчет Первой-НОВОЙ Безье-крив. (=P_с_Крышкой ) 
P_Krish=P+Eps1

#  ders - для заданного "u" массив BASIS функций и  все их (до р) производныЕ
ders_p3 = np.zeros([p+1,p+1])

# C2 - массив, в нем для заданного "u" возвращаются C2[0,:]- x,y - сплайна
#                               для заданного "u"  C2[1,:]- x,y - 1-вой ПРОИЗВОДНОЙ сплайна
#                               для заданного "u"  C2[0,:]- x,y - 2-ой ПРОИЗВОДНОЙ сплайна
#                               для заданного "u"  C2[p,:]- x,y -"p"-ой ПРОИЗВОДНОЙ сплайна
C2_NURBS_p3=np.zeros([p+1,2]) # идекс "2" для 2D задачи, "3" - для 3D

n_u3=60
data_CurvePoin_and_Deriv_NURBS_P_Krish = np.zeros([(n_u3+1),(p+1),2])

#stop

for it in range(n_u3+1):
    t_i=(it/n_u2)*(t_stop1-t_start1) +  t_start1
    
    Func_1.CurvePoin_and_Deriv_NURBS(n_vert,p,T,P_Krish,HP,t_i,C2_NURBS_p3,ders_p3)
    # В массиве на след. строке Хранятся Кубич. Сплайн
    data_CurvePoin_and_Deriv_NURBS_P_Krish[it,:,:]=C2_NURBS_p3

##################################################################################################################
#stop

##################################################################################################################
# Расчет Второй-НОВОЙ Безье-крив. (=Q_с_Крышкой) 
Q_Krish=Q+Del1

#  ders - для заданного "u" массив BASIS функций и  все их (до р) производныЕ
ders_p3 = np.zeros([p+1,p+1])

# C2 - массив, в нем для заданного "u" возвращаются C2[0,:]- x,y - сплайна
#                               для заданного "u"  C2[1,:]- x,y - 1-вой ПРОИЗВОДНОЙ сплайна
#                               для заданного "u"  C2[0,:]- x,y - 2-ой ПРОИЗВОДНОЙ сплайна
#                               для заданного "u"  C2[p,:]- x,y -"p"-ой ПРОИЗВОДНОЙ сплайна
C2_NURBS_p3=np.zeros([p+1,2]) # идекс "2" для 2D задачи, "3" - для 3D

n_u3=60
data_CurvePoin_and_Deriv_NURBS_Q_Krish = np.zeros([(n_u1+1),(p+1),2])



for it in range(n_u3+1):
    t_i=(it/n_u2)*(t_stop1-t_start1) +  t_start1
    
    Func_1.CurvePoin_and_Deriv_NURBS(n_vert,p,T,Q_Krish,HQ,t_i,C2_NURBS_p3,ders_p3)
    # В массиве на след. строке Хранятся Кубич. Сплайн
    data_CurvePoin_and_Deriv_NURBS_Q_Krish[it,:,:]=C2_NURBS_p3

##################################################################################################################


#stop





##################################################################################################################
# Расчет Третьей Безье-крив. (=R - кривая) 
#  ders - для заданного "u" массив BASIS функций и  все их (до р) производныЕ
ders_p3 = np.zeros([p+1,p+1])

# C2 - массив, в нем для заданного "u" возвращаются C2[0,:]- x,y - сплайна
#                               для заданного "u"  C2[1,:]- x,y - 1-вой ПРОИЗВОДНОЙ сплайна
#                               для заданного "u"  C2[0,:]- x,y - 2-ой ПРОИЗВОДНОЙ сплайна
#                               для заданного "u"  C2[p,:]- x,y -"p"-ой ПРОИЗВОДНОЙ сплайна
C2_NURBS_p3=np.zeros([p+1,2]) # идекс "2" для 2D задачи, "3" - для 3D

n_u3=60
data_CurvePoin_and_Deriv_NURBS_p3 = np.zeros([(n_u3+1),(p+1),2])


for it in range(n_u3+1):
    t_i=(it/n_u2)*(t_stop1-t_start1) +  t_start1
    
    Func_1.CurvePoin_and_Deriv_NURBS(n_vert,p,T,R,HR,t_i,C2_NURBS_p3,ders_p3)
    # В массиве на след. строке Хранятся Кубич. Сплайн
    data_CurvePoin_and_Deriv_NURBS_p3[it,:,:]=C2_NURBS_p3

##################################################################################################################

#stop


# Расчет Координат точек, в которых заданы Ограничения
#точка u1
Func_1.CurvePoin_and_Deriv_NURBS(n_vert,p,T,P_Krish,HP,u00,C2_NURBS_p3,ders_p3) #точка u1
X11=C2_NURBS_p3[0,0]; Y11=C2_NURBS_p3[0,1]


#stop



Title="Окончательное решение - ДИСКРЕТ. НОРМА *** ОБЕ КОНЕЧНЫЕ ТОЧКИ НЕзафиксированы (СВОБОДНЫЕ) ***"
Title=" "

labels_legend1="P Многоугольник (заданный)"
labels_legend2="P Безье Кривая (заданная)"
labels_legend3="Q Многоугольник (заданный)"
labels_legend4="Q Безье Кривая (заданная)"
labels_legend5="R Многоугольник (апроксимация Р и Q)"
labels_legend6="R Безье Кривая (апроксимация Р и Q)"
labels_legend7="точка ограничений"



X12=X11; Y12=Y11;  X13=X11; Y13=Y11;  X14=X11; Y14=Y11;
#   ГРАФИК для ОТЧЕТА-СТАТЬИ - ДИСКРЕТ. НОРМА
# 
print ("**  ОГРАНИЧЕНИЕ = ТОЧКА & ДВЕ ПРОИЗВОДНЫЕ")
Plots_1.plot_Trace_Lines_3_for_Mergin_1_plus_4_Points (X11,Y11,X12,Y12,X13,Y13,X14,Y14,
                                         P[:,0],P[:,1],
                                         Q[:,0],Q[:,1],
                                         R[:,0],R[:,1],
                                            data_CurvePoin_and_Deriv_NURBS_p1[:,0,0],data_CurvePoin_and_Deriv_NURBS_p1[:,0,1] ,                             
                                            data_CurvePoin_and_Deriv_NURBS_p2[:,0,0],data_CurvePoin_and_Deriv_NURBS_p2[:,0,1] ,
                                            data_CurvePoin_and_Deriv_NURBS_p3[:,0,0],data_CurvePoin_and_Deriv_NURBS_p3[:,0,1] ,    
                                           
                                               y_min, y_max, x_min, x_max,
                                               Title, labels_legend1, labels_legend2,
                                                labels_legend3, labels_legend4,labels_legend5,labels_legend6,labels_legend7)







########################################################################################################################################
########################################################################################################################################
########################################################################################################################################







#************************************************************************
#%% = Окончание Блока.  Если блок Выделить, то его можно выполнить Ctrl + Enter








#stop
