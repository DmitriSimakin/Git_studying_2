
"""
Created on Tue Apr 13 15:18:06 2021

@author: Сергей Валентинович
"""

import matplotlib.pyplot as plt
import numpy as np



colors = ['']*17

colors[0]  ='b' #Синий
colors[1]  ='g' #Зелёный
colors[2]  ='r' #Красный
colors[3]  ='c' #Бирюзовый
colors[4]  ='b' #Фиолетовый / Пурпурный
colors[5]  ='y' #Желтый
colors[6]  ='k' #Черный
colors[7]  ='w' #Белый
colors[8]  ='goldenrod' # См. Полную Таблицу Цветов в Mathplotlib

colors[9]  ='grey' #Серый
colors[10]  ='lightgrey' # Светло_Серый
colors[11]  ='darkgrey' # Темно_Серый
colors[12]  ='dimgrey' # Тускло_Серый
colors[13]  ='navajowhite' # Грязно_Серый

colors[14] ='magenta' #Пурпурно-Красный
colors[15] ='floralwhite' #См. Полную Таблицу Цветов в Mathplotlib
colors[16] ='skyblue' #См. Полную Таблицу Цветов в Mathplotlib


#***********************************************************************************
#***********************************************************************************    
def plot_Trace (datax, datay, datax1, datay1, 
                 X_breakpoint,Y_breakpoint,
                y_min, y_max, x_min, x_max,
                Title, labels_legend1, labels_legend2,
                labels_legend3):
    
# Рисует:
# 1. Контр.Многоугольник
# 2. Один Сплайн.
#
#    
    
    #fig, ax = plt.subplots()
    #figsize(23, 5)
    # Размер Графиков Одинаковый для всех - Здается в Графике 0.
    fig, ax = plt.subplots(figsize=(9, 5)) # ДВА графика. Это  Одна строка и ДВА столбца = 2 Графика 
                                  # Если только ОДИН график, то вместо axesх[0] везде будет ax и fig, ax = plt.subplots()
    #plt.figsize(23, 5)
    labels = ["σ" +"$_{i}$", # в этом графике не используется
              chr(945) +"$_{i+1}$",
              "Banner_2",
               "123",
               "456",
              ]
    n= np.size(datax)
    
#    if (nx_max>n): 
#        print("**!!!************ ")
#        print("**!!!  nx_max>n  **!!!")
#        print("**!!!************ ")
#        stop
#    else:
#        pass
    
                    
    
#    data1=data[nx_min:nx_max]
#    n1= np.arange(np.size(data1))


    ax.set_facecolor(colors[11])

    
    ax.plot( #Рисуем точки Контр. Многоуг. и Соединяем их Тонкой Линией
             datax, datay, #массивы "X" и "Y"
             linestyle='-', linewidth=0.3, color=colors[6], alpha=0.9, # линия и МАРКЕРЫ
             marker='o', markersize=7, markerfacecolor=colors[12], markeredgewidth=2, markeredgecolor=colors[6],# маркеры точек
             label=labels_legend1, zorder=2)
    ax.plot( #Рисуем Сплайн
             datax1, datay1, #массивы "X" и "Y"
             linestyle='-', linewidth=2, color=colors[6], alpha=0.9, # линия и МАРКЕРЫ
             marker=' ', markersize=5, markerfacecolor=colors[12], markeredgewidth=2, markeredgecolor=colors[6],# маркеры точек
             label=labels_legend2, zorder=2)
    
    ax.plot( #Рисуем Точку Смены Полиномов
             X_breakpoint,Y_breakpoint, #массивы "X" и "Y"
             linestyle='-', linewidth=0.3, color=colors[6], alpha=0.9, # линия и МАРКЕРЫ
             marker='o', markersize=12, markerfacecolor=colors[2], markeredgewidth=2, markeredgecolor=colors[6],# маркеры точек
             label=labels_legend3, zorder=2)
    
    #plt.text (x=20, y=71, s="Mu_real_mean=%.1f" %mean_observed, fontsize=14) 
    #plt.text (x=20, y=68, s="Std_real = %.1f" %std_observed, fontsize=14) 
    #ax.plot(n, (Alf_samples[:,1]+0), #массивы "X" и "Y"
    #         linestyle='-', linewidth=0.3, color=colors[6], alpha=0.9, # линия и МАРКЕРЫ
    #         marker='o', markersize=5, markerfacecolor=colors[10], markeredgewidth=1, markeredgecolor=colors[10],# маркеры точек
    #         label=labels[1], zorder=2)
    
    
    
    
    ax.set_xlabel("ось Х")
    ax.set_ylabel("ось Y")
    #ax.set_title("Сэмплы " + chr(945) +"$_{i}$,  " + chr(945) +
    #            "$_{i+1}$"+f"  ,(i={0})",fontsize=16)
    ax.set_title(Title)
    #ax.set_title("1234")

    
    #ax.legend(loc="lower right")
    #ax.legend(loc="upper left")
    ax.legend(loc="upper right",  fontsize=10)
    #ax.legend(loc="lower left")
    
    
    
    ax.set_xlim(x_min, x_max);#"-2" - всё Верно !!! SM
    ax.set_ylim(y_min, y_max);
    
    ax.grid(True, ls=':', c=colors[6],alpha=0.3, zorder=0 )
    plt.show()
    
    #print("** From plot_trace_1_1_1 **")

    #print("-1-1-1-1  -", end="")
    #print("56")
                
               
    return
    

#***********************************************************************************
#***********************************************************************************   


#***********************************************************************************
#***********************************************************************************    
def plot_Trace_Lines_4 (datax_1, datay_1, datax_2, datay_2,
                        datax1, datay1, datax2, datay2, 
                           #datax3, datay3, datax4, datay4,
                           y_min, y_max, x_min, x_max,
                Title, labels_legend1, labels_legend2,
                       labels_legend3, labels_legend4,
                ):

# Рисует:
# 1. Контр.Многоугольник
# 2. 4-ре Сплайна.
#
#    
    
    
    #fig, ax = plt.subplots()
    #figsize(23, 5)
    # Размер Графиков Одинаковый для всех - Здается в Графике 0.
    fig, ax = plt.subplots(figsize=(9.0, 5)) # ДВА графика. Это  Одна строка и ДВА столбца = 2 Графика 
                                  # Если только ОДИН график, то вместо axesх[0] везде будет ax и fig, ax = plt.subplots()
    #plt.figsize(23, 5)
    labels = ["σ" +"$_{i}$", # в этом графике не используется
              chr(945) +"$_{i+1}$",
              "Banner_2",
               "123",
               "456",
              ]
    n= np.size(datax_1)
    
#    if (nx_max>n): 
#        print("**!!!************ ")
#        print("**!!!  nx_max>n  **!!!")
#        print("**!!!************ ")
#        stop
#    else:
#        pass
    
                    
    
#    data1=data[nx_min:nx_max]
#    n1= np.arange(np.size(data1))


    ax.set_facecolor(colors[11])

    
    ax.plot(datax_1, datay_1, #массивы "X" и "Y"
             linestyle='-', linewidth=0.3, color=colors[6], alpha=0.9, # линия и МАРКЕРЫ
             marker='o', markersize=8, markerfacecolor=colors[2], markeredgewidth=2, markeredgecolor=colors[6],# маркеры точек
             label=labels_legend1, zorder=2)
             
    ax.plot(datax1, datay1, #массивы "X" и "Y"
             linestyle='-', linewidth=2, color=colors[2], alpha=0.9, # линия и МАРКЕРЫ
             marker=' ', markersize=3, markerfacecolor=colors[6], markeredgewidth=2, markeredgecolor=colors[6],# маркеры точек
             label=labels_legend2, zorder=2)


    ax.plot(datax_2, datay_2, #массивы "X" и "Y"
             linestyle='-', linewidth=0.3, color=colors[6], alpha=0.9, # линия и МАРКЕРЫ
             marker='o', markersize=8, markerfacecolor=colors[4], markeredgewidth=2, markeredgecolor=colors[6],# маркеры точек
             label=labels_legend3, zorder=2)
           
    ax.plot(datax2, datay2, #массивы "X" и "Y"
             linestyle='-', linewidth=2, color=colors[4], alpha=0.9, # линия и МАРКЕРЫ
             marker=' ', markersize=3, markerfacecolor=colors[4], markeredgewidth=2, markeredgecolor=colors[6],# маркеры точек
             label=labels_legend4, zorder=2)
   

             
    """
    ax.plot(datax2, datay2, #массивы "X" и "Y"
             linestyle='--', linewidth=2, color=colors[10], alpha=0.9, # линия и МАРКЕРЫ
             marker=' ', markersize=3, markerfacecolor=colors[10], markeredgewidth=2, markeredgecolor=colors[10],# маркеры точек
             label=labels_legend3, zorder=2)
 
    ax.plot(datax3, datay3, #массивы "X" и "Y"
             linestyle='-', linewidth=2, color=colors[2], alpha=0.9, # линия и МАРКЕРЫ
             marker=' ', markersize=2, markerfacecolor=colors[2], markeredgewidth=2, markeredgecolor=colors[2],# маркеры точек
             label=labels_legend4, zorder=2)

    ax.plot(datax4, datay4, #массивы "X" и "Y"
             linestyle='-', linewidth=2, color=colors[4], alpha=0.9, # линия и МАРКЕРЫ
             marker=' ', markersize=2, markerfacecolor=colors[4], markeredgewidth=2, markeredgecolor=colors[4],# маркеры точек
   """



    #ax.annotate("p-value ={0}".format(pvalue), xy = (0.21, 0.005), xytext=(0.15, 2), # печать значения p-value  
    #        arrowprops=dict(facecolor='black',                                   # рисуем кривую стрелку
    #                        arrowstyle='->', 
    #                        connectionstyle='angle3,angleA=-60,angleB=40'))
    
    """
    ax.annotate("$Степень=1$", fontsize=13, xytext=(5.0, 1.2),# координаты надписи и Начала Стрелки 
                                          xy = (8.5, 6.3), # координаты окончания стрелки
                arrowprops=dict(facecolor='black',                                   # рисуем кривую стрелку
                           arrowstyle='->'))  #, 
                           #connectionstyle='angle3,angleA=0,angleB=1000'))#искревление стрелки
    #ax.arrow_patch.set_color("gold")
    ax.annotate("$Степень=2$", fontsize=13, xytext=(-0.9,12.0),# координаты надписи и Начала Стрелки 
                                          xy = (3.6, 10.0), # координаты окончания стрелки
                color=colors[10],
                arrowprops=dict(color=colors[10],                                   # рисуем кривую стрелку
                           arrowstyle='->'))  #, 
                           #connectionstyle='angle3,angleA=0,angleB=1000'))#искревление стрелки    



    ax.annotate("$Степень=3$", fontsize=13, xytext=(15.0,11.5),# координаты надписи и Начала Стрелки 
                                          xy = (13.7, 9.5), # координаты окончания стрелки
                color=colors[2],
                arrowprops=dict(color=colors[2], # рисуем кривую стрелку
                           arrowstyle='->'))  #, 
                           #connectionstyle='angle3,angleA=0,angleB=1000'))#искревление стрелки  
                           
    ax.annotate("$Степень=6$", fontsize=13, xytext=(9.0,2.6),# координаты надписи и Начала Стрелки 
                                          xy = (13.4, 7.2), # координаты окончания стрелки
                color=colors[4],
                arrowprops=dict(color=colors[4], # рисуем кривую стрелку
                           arrowstyle='->'))  #, 
                           #connectionstyle='angle3,angleA=0,angleB=1000'))#искревление стрелки  
   """

    

    #ax.text (x=0.4, y=1.0, s="$B_{0}$", fontsize=13)
    #ax.text (x=1.4, y=2.9, s="$B_{1}$", fontsize=13)
    #ax.text (x=4.2, y=2.9, s="$B_{2}$", fontsize=13)  
    #ax.text (x=3.2, y=1.0, s="$B_{3}$", fontsize=13)
    
    
    #plt.text (x=20, y=71, s="Mu_real_mean=%.1f" %mean_observed, fontsize=14) 
    #plt.text (x=20, y=68, s="Std_real = %.1f" %std_observed, fontsize=14) 
    #ax.plot(n, (Alf_samples[:,1]+0), #массивы "X" и "Y"
    #         linestyle='-', linewidth=0.3, color=colors[6], alpha=0.9, # линия и МАРКЕРЫ
    #         marker='o', markersize=5, markerfacecolor=colors[10], markeredgewidth=1, markeredgecolor=colors[10],# маркеры точек
    #         label=labels[1], zorder=2)
    
    
    
    
    ax.set_xlabel("ось Х")
    ax.set_ylabel("ось Y")
    #ax.set_title("Сэмплы " + chr(945) +"$_{i}$,  " + chr(945) +
    #            "$_{i+1}$"+f"  ,(i={0})",fontsize=16)
    ax.set_title(Title)
    #ax.set_title("1234")

    
    #ax.legend(loc="lower right")
    #ax.legend(loc="upper left")
    ax.legend(loc="upper right",  fontsize=10)
    #ax.legend(loc="lower left")
    
    
    
    ax.set_xlim(x_min, x_max);#"-2" - всё Верно !!! SM
    ax.set_ylim(y_min, y_max);
    
    ax.grid(True, ls=':', c=colors[6],alpha=0.3, zorder=0 )
    plt.show()
    
    #print("** From plot_trace_1_1_1 **")

    #print("-1-1-1-1  -", end="")
    #print("56")
                
               
    return
    


#***********************************************************************************
#***********************************************************************************   



#***********************************************************************************
#***********************************************************************************    
def plot_Trace_Double (datax_B1, datay_B1, datax_B2, datay_B2,
                       datax1, datay1, datax2, datay2,
                       
                       y_min, y_max, x_min, x_max,
                Title, labels_legend_B1, labels_legend_1,
                       labels_legend_B2, labels_legend_2):
    
# Рисует:
# 1. ДВА Контр.МногоугольникА
# 2. ДВА  Сплайна
#
#    
    
    #fig, ax = plt.subplots()
    #figsize(23, 5)
    # Размер Графиков Одинаковый для всех - Здается в Графике 0.
    fig, ax = plt.subplots(figsize=(9, 5)) # ДВА графика. Это  Одна строка и ДВА столбца = 2 Графика 
                                  # Если только ОДИН график, то вместо axesх[0] везде будет ax и fig, ax = plt.subplots()
    #plt.figsize(23, 5)
    labels = ["σ" +"$_{i}$", # в этом графике не используется
              chr(945) +"$_{i+1}$",
              "Banner_2",
               "123",
               "456",
              ]
    n= np.size(datax_B1)
    
#    if (nx_max>n): 
#        print("**!!!************ ")
#        print("**!!!  nx_max>n  **!!!")
#        print("**!!!************ ")
#        stop
#    else:
#        pass
    
                    
    
#    data1=data[nx_min:nx_max]
#    n1= np.arange(np.size(data1))


    ax.set_facecolor(colors[11])

 # ПЕРВЫЙ Многоуг. и ПЕРВЫЙ Сплайн
    #"""
    ax.plot( #Рисуем точки Контр. Многоуг. и Соединяем их Тонкой Линией
             datax_B1, datay_B1, #массивы "X" и "Y"
             linestyle='-', linewidth=0.3, color=colors[6], alpha=0.9, # линия и МАРКЕРЫ
             marker='o', markersize=7, markerfacecolor=colors[12], markeredgewidth=2, markeredgecolor=colors[6],# маркеры точек
             label=labels_legend_B1, zorder=2)
    ax.plot( #Рисуем Сплайн
             datax1, datay1, #массивы "X" и "Y"
             linestyle='-', linewidth=2, color=colors[6], alpha=0.9, # линия и МАРКЕРЫ
             marker=' ', markersize=5, markerfacecolor=colors[12], markeredgewidth=2, markeredgecolor=colors[6],# маркеры точек
             label=labels_legend_1, zorder=2)
    #"""
 # ВТОРОЙ Многоуг. и ВТОРОЙ Сплайн
    
    ax.plot( #Рисуем точки Контр. Многоуг. и Соединяем их Тонкой Линией
             datax_B2, datay_B2, #массивы "X" и "Y"
             linestyle='--', linewidth=1.3, color=colors[6], alpha=0.5, # линия и МАРКЕРЫ
             marker='s', # #""s=Квадратики ""
             markersize=7, markerfacecolor=colors[12], markeredgewidth=2, markeredgecolor=colors[6],# маркеры точек
             label=labels_legend_B2, zorder=2)
    ax.plot( #Рисуем Сплайн
             datax2, datay2, #массивы "X" и "Y"
             linestyle='--', linewidth=2, color=colors[6], alpha=0.9, # линия и МАРКЕРЫ
             marker=' ', markersize=5, markerfacecolor=colors[12], markeredgewidth=2, markeredgecolor=colors[6],# маркеры точек
             label=labels_legend_2, zorder=2)    
    
    
    #plt.text (x=20, y=71, s="Mu_real_mean=%.1f" %mean_observed, fontsize=14) 
    #plt.text (x=20, y=68, s="Std_real = %.1f" %std_observed, fontsize=14) 
    #ax.plot(n, (Alf_samples[:,1]+0), #массивы "X" и "Y"
    #         linestyle='-', linewidth=0.3, color=colors[6], alpha=0.9, # линия и МАРКЕРЫ
    #         marker='o', markersize=5, markerfacecolor=colors[10], markeredgewidth=1, markeredgecolor=colors[10],# маркеры точек
    #         label=labels[1], zorder=2)
    
    
    
    
    ax.set_xlabel("ось Х")
    ax.set_ylabel("ось Y")
    #ax.set_title("Сэмплы " + chr(945) +"$_{i}$,  " + chr(945) +
    #            "$_{i+1}$"+f"  ,(i={0})",fontsize=16)
    ax.set_title(Title)
    #ax.set_title("1234")

    
    #ax.legend(loc="lower right")
    #ax.legend(loc="upper left")
    ax.legend(loc="upper right",  fontsize=10)
    #ax.legend(loc="lower left")
    
    
    
    ax.set_xlim(x_min, x_max);#"-2" - всё Верно !!! SM
    ax.set_ylim(y_min, y_max);
    
    ax.grid(True, ls=':', c=colors[6],alpha=0.3, zorder=0 )
    plt.show()
    
    #print("** From plot_trace_1_1_1 **")

    #print("-1-1-1-1  -", end="")
    #print("56")
                
               
    return
    

#***********************************************************************************
#***********************************************************************************   









#***********************************************************************************
#***********************************************************************************    
def plot_Trace_Lines_3_for_Mergin_1 (Control_Point1_x, Control_Point1_y, 
                                     Control_Point2_x, Control_Point2_y,
                                     Control_Point3_x, Control_Point3_y,
                                     
                                     datax1, datay1,
                                     datax2, datay2, 
                                     datax3, datay3,
                          
                           y_min, y_max, x_min, x_max,
                Title, labels_legend1, labels_legend2,
                labels_legend3, labels_legend4,labels_legend5,labels_legend6 ):

# Рисует:
# 1. Контр.Многоугольник
# 2. 4-ре Сплайна.
#
#    
    
    
    #fig, ax = plt.subplots()
    #figsize(23, 5)
    # Размер Графиков Одинаковый для всех - Здается в Графике 0.
    fig, ax = plt.subplots(figsize=(9.0, 5)) # ДВА графика. Это  Одна строка и ДВА столбца = 2 Графика 
                                  # Если только ОДИН график, то вместо axesх[0] везде будет ax и fig, ax = plt.subplots()
    #plt.figsize(23, 5)
    labels = ["σ" +"$_{i}$", # в этом графике не используется
              chr(945) +"$_{i+1}$",
              "Banner_2",
               "123",
               "456",
              ]
    n= np.size(Control_Point1_x)
    
#    if (nx_max>n): 
#        print("**!!!************ ")
#        print("**!!!  nx_max>n  **!!!")
#        print("**!!!************ ")
#        stop
#    else:
#        pass
    
                    
    
#    data1=data[nx_min:nx_max]
#    n1= np.arange(np.size(data1))


    ax.set_facecolor(colors[11])
    
##################################################################################################################################################    

#   Первый Контр-Многоуг.    
    ax.plot(Control_Point1_x, Control_Point1_y, #массивы "X" и "Y"
             linestyle='-', linewidth=0.3, color=colors[6], alpha=0.9, # линия и МАРКЕРЫ
             marker='o', markersize=8, markerfacecolor=colors[12], markeredgewidth=2, markeredgecolor=colors[6],# маркеры точек
             label=labels_legend1, zorder=2)
    
#  Первый Сплайн    
    ax.plot(datax1, datay1, #массивы "X" и "Y"
             linestyle='--', linewidth=4, color=colors[6], alpha=0.9, # линия и МАРКЕРЫ
             marker=' ', markersize=3, markerfacecolor=colors[12], markeredgewidth=2, markeredgecolor=colors[6],# маркеры точек
             label=labels_legend2, zorder=2)
    
##################################################################################################################################################    
    
#   Второй Контр-Многоуг.             
    ax.plot(Control_Point2_x, Control_Point2_y, #массивы "X" и "Y"
             linestyle='-', linewidth=0.3, color=colors[6], alpha=0.9, # линия и МАРКЕРЫ
             marker='o', markersize=8, markerfacecolor=colors[12], markeredgewidth=2, markeredgecolor=colors[6],# маркеры точек
             label=labels_legend3, zorder=2)      

#  Второй Сплайн     
    ax.plot(datax2, datay2, #массивы "X" и "Y"
             linestyle='--', linewidth=2, color=colors[10], alpha=0.9, # линия и МАРКЕРЫ
             marker=' ', markersize=3, markerfacecolor=colors[10], markeredgewidth=2, markeredgecolor=colors[10],# маркеры точек
             label=labels_legend4, zorder=2)
    
##################################################################################################################################################    
    
#   Третий Контр-Многоуг.             
    ax.plot(Control_Point3_x, Control_Point3_y, #массивы "X" и "Y"
             linestyle='-', linewidth=0.3, color=colors[6], alpha=0.9, # линия и МАРКЕРЫ
             marker='s', markersize=8, markerfacecolor=colors[12], markeredgewidth=2, markeredgecolor=colors[6],# маркеры точек
             label=labels_legend5, zorder=2)      

#  Третий Сплайн     
    ax.plot(datax3, datay3, #массивы "X" и "Y"
             linestyle='-', linewidth=2, color=colors[6], alpha=0.9, # линия и МАРКЕРЫ
             marker=' ', markersize=3, markerfacecolor=colors[10], markeredgewidth=2, markeredgecolor=colors[10],# маркеры точек
             label=labels_legend6, zorder=2)
    
    
    """
    ax.plot(datax3, datay3, #массивы "X" и "Y"
             linestyle='-', linewidth=2, color=colors[2], alpha=0.9, # линия и МАРКЕРЫ
             marker=' ', markersize=2, markerfacecolor=colors[2], markeredgewidth=2, markeredgecolor=colors[2],# маркеры точек
             label=labels_legend4, zorder=2)

    ax.plot(datax4, datay4, #массивы "X" и "Y"
             linestyle='-', linewidth=2, color=colors[4], alpha=0.9, # линия и МАРКЕРЫ
             marker=' ', markersize=2, markerfacecolor=colors[4], markeredgewidth=2, markeredgecolor=colors[4],# маркеры точек
             label=labels_legend5, zorder=2)


    """

    #ax.annotate("p-value ={0}".format(pvalue), xy = (0.21, 0.005), xytext=(0.15, 2), # печать значения p-value  
    #        arrowprops=dict(facecolor='black',                                   # рисуем кривую стрелку
    #                        arrowstyle='->', 
    #                        connectionstyle='angle3,angleA=-60,angleB=40'))
    
    """
    ax.annotate("$Степень=1$", fontsize=13, xytext=(5.0, 1.2),# координаты надписи и Начала Стрелки 
                                          xy = (8.5, 6.3), # координаты окончания стрелки
                arrowprops=dict(facecolor='black',                                   # рисуем кривую стрелку
                           arrowstyle='->'))  #, 
                           #connectionstyle='angle3,angleA=0,angleB=1000'))#искревление стрелки
    #ax.arrow_patch.set_color("gold")
    ax.annotate("$Степень=2$", fontsize=13, xytext=(-0.9,12.0),# координаты надписи и Начала Стрелки 
                                          xy = (3.6, 10.0), # координаты окончания стрелки
                color=colors[10],
                arrowprops=dict(color=colors[10],                                   # рисуем кривую стрелку
                           arrowstyle='->'))  #, 
                           #connectionstyle='angle3,angleA=0,angleB=1000'))#искревление стрелки    



    ax.annotate("$Степень=3$", fontsize=13, xytext=(15.0,11.5),# координаты надписи и Начала Стрелки 
                                          xy = (13.7, 9.5), # координаты окончания стрелки
                color=colors[2],
                arrowprops=dict(color=colors[2], # рисуем кривую стрелку
                           arrowstyle='->'))  #, 
                           #connectionstyle='angle3,angleA=0,angleB=1000'))#искревление стрелки  
                           
    ax.annotate("$Степень=6$", fontsize=13, xytext=(9.0,2.6),# координаты надписи и Начала Стрелки 
                                          xy = (13.4, 7.2), # координаты окончания стрелки
                color=colors[4],
                arrowprops=dict(color=colors[4], # рисуем кривую стрелку
                           arrowstyle='->'))  #, 
                           #connectionstyle='angle3,angleA=0,angleB=1000'))#искревление стрелки  
   """

    

    #ax.text (x=0.4, y=1.0, s="$B_{0}$", fontsize=13)
    #ax.text (x=1.4, y=2.9, s="$B_{1}$", fontsize=13)
    #ax.text (x=4.2, y=2.9, s="$B_{2}$", fontsize=13)  
    #ax.text (x=3.2, y=1.0, s="$B_{3}$", fontsize=13)
    
    
    #plt.text (x=20, y=71, s="Mu_real_mean=%.1f" %mean_observed, fontsize=14) 
    #plt.text (x=20, y=68, s="Std_real = %.1f" %std_observed, fontsize=14) 
    #ax.plot(n, (Alf_samples[:,1]+0), #массивы "X" и "Y"
    #         linestyle='-', linewidth=0.3, color=colors[6], alpha=0.9, # линия и МАРКЕРЫ
    #         marker='o', markersize=5, markerfacecolor=colors[10], markeredgewidth=1, markeredgecolor=colors[10],# маркеры точек
    #         label=labels[1], zorder=2)
    
    
    
    
    ax.set_xlabel("ось Х")
    ax.set_ylabel("ось Y")
    #ax.set_title("Сэмплы " + chr(945) +"$_{i}$,  " + chr(945) +
    #            "$_{i+1}$"+f"  ,(i={0})",fontsize=16)
    ax.set_title(Title)
    #ax.set_title("1234")

    
    #ax.legend(loc="lower right")
    #ax.legend(loc="upper left")
    ax.legend(loc="upper right",  fontsize=10)
    #ax.legend(loc="lower left")
    
    
    
    ax.set_xlim(x_min, x_max);#"-2" - всё Верно !!! SM
    ax.set_ylim(y_min, y_max);
    
    ax.grid(True, ls=':', c=colors[6],alpha=0.3, zorder=0 )
    plt.show()
    
    #print("** From plot_trace_1_1_1 **")

    #print("-1-1-1-1  -", end="")
    #print("56")
                
               
    return
    

#***********************************************************************************
#***********************************************************************************   





def plot_Trace_Lines_2_for_Mergin_12 (                                     
                                     datax1, datay1,                                    
                                     datax3, datay3,
                          
                           y_min, y_max, x_min, x_max,
                Title, labels_legend1, labels_legend2,
                 ):

# Рисует:
# 1. Контр.Многоугольник
# 2. 4-ре Сплайна.
#
#    
    
    
    #fig, ax = plt.subplots()
    #figsize(23, 5)
    # Размер Графиков Одинаковый для всех - Здается в Графике 0.
    fig, ax = plt.subplots(figsize=(9.0, 5)) # ДВА графика. Это  Одна строка и ДВА столбца = 2 Графика 
                                  # Если только ОДИН график, то вместо axesх[0] везде будет ax и fig, ax = plt.subplots()
    #plt.figsize(23, 5)
    labels = ["σ" +"$_{i}$", # в этом графике не используется
              chr(945) +"$_{i+1}$",
              "Banner_2",
               "123",
               "456",
              ]
    
#    if (nx_max>n): 
#        print("**!!!************ ")
#        print("**!!!  nx_max>n  **!!!")
#        print("**!!!************ ")
#        stop
#    else:
#        pass
    
                    
    
#    data1=data[nx_min:nx_max]
#    n1= np.arange(np.size(data1))


    ax.set_facecolor(colors[11])
 
    
    print("**!!!************ ")
##################################################################################################################################################    

    
#  Первый Сплайн    
    ax.plot(datax1, datay1, #массивы "X" и "Y"
             linestyle='--', linewidth=6, color=colors[6], alpha=0.9, # линия и МАРКЕРЫ
             marker=' ', markersize=3, markerfacecolor=colors[12], markeredgewidth=2, markeredgecolor=colors[6],# маркеры точек
             label=labels_legend1, zorder=2)
    
##################################################################################################################################################    
    

#  Третий Сплайн          
    ax.plot(datax3, datay3, #массивы "X" и "Y"
             linestyle='-', linewidth=2, color=colors[6], alpha=0.9, # линия и МАРКЕРЫ
             marker=' ', markersize=3, markerfacecolor=colors[10], markeredgewidth=2, markeredgecolor=colors[10],# маркеры точек
             label=labels_legend2, zorder=2)
        
    
    
    
    ax.set_xlabel("ось Х")
    ax.set_ylabel("ось Y")
    #ax.set_title("Сэмплы " + chr(945) +"$_{i}$,  " + chr(945) +
    #            "$_{i+1}$"+f"  ,(i={0})",fontsize=16)
    ax.set_title(Title)
    #ax.set_title("1234")
   


    
    #ax.legend(loc="lower right")
    #ax.legend(loc="upper left")
    ax.legend(loc="upper right",  fontsize=10)
    #ax.legend(loc="lower left")
    
    
    
    ax.set_xlim(x_min, x_max);#"-2" - всё Верно !!! SM
    ax.set_ylim(y_min, y_max);
    
    ax.grid(True, ls=':', c=colors[6],alpha=0.3, zorder=0 )
    plt.show()
    
    #print("** From plot_trace_1_1_1 **")

    #print("-1-1-1-1  -", end="")
    #print("56")
                
               
    return
    

#***********************************************************************************
#***********************************************************************************   








#***********************************************************************************
#***********************************************************************************    
def plot_Trace_Lines_3_for_Mergin_1_plus_4_Points (X1,Y1,X2,Y2,X3,Y3,X4,Y4,
                                                   Control_Point1_x, Control_Point1_y, 
                                                   Control_Point2_x, Control_Point2_y,
                                                   Control_Point3_x, Control_Point3_y,
                                     
                                                  datax1, datay1,
                                                  datax2, datay2, 
                                                  datax3, datay3,
                          
                           y_min, y_max, x_min, x_max,
                Title, labels_legend1, labels_legend2,
                labels_legend3, labels_legend4,labels_legend5,labels_legend6,labels_legend7 ):

# Рисует:
# 1. Контр.Многоугольник
# 2. 4-ре Сплайна.
#
#    
    
    
    #fig, ax = plt.subplots()
    #figsize(23, 5)
    # Размер Графиков Одинаковый для всех - Здается в Графике 0.
    fig, ax = plt.subplots(figsize=(9.0, 5)) # ДВА графика. Это  Одна строка и ДВА столбца = 2 Графика 
                                  # Если только ОДИН график, то вместо axesх[0] везде будет ax и fig, ax = plt.subplots()
    #plt.figsize(23, 5)
    labels = ["σ" +"$_{i}$", # в этом графике не используется
              chr(945) +"$_{i+1}$",
              "Banner_2",
               "123",
               "456",
              ]
    n= np.size(Control_Point1_x)
    
#    if (nx_max>n): 
#        print("**!!!************ ")
#        print("**!!!  nx_max>n  **!!!")
#        print("**!!!************ ")
#        stop
#    else:
#        pass
    
                    
    
#    data1=data[nx_min:nx_max]
#    n1= np.arange(np.size(data1))


    ax.set_facecolor(colors[11])
    
##################################################################################################################################################    
    """
#   Первый Контр-Многоуг.    
    ax.plot(Control_Point1_x, Control_Point1_y, #массивы "X" и "Y"
             linestyle='-', linewidth=0.3, color=colors[6], alpha=0.9, # линия и МАРКЕРЫ
             marker='o', markersize=8, markerfacecolor=colors[12], markeredgewidth=2, markeredgecolor=colors[6],# маркеры точек
             label=labels_legend1, zorder=2)
    """    
#  Первый Сплайн    
    ax.plot(datax1, datay1, #массивы "X" и "Y"
             linestyle='--', linewidth=2, color=colors[6], alpha=0.9, # линия и МАРКЕРЫ
             marker=' ', markersize=3, markerfacecolor=colors[12], markeredgewidth=2, markeredgecolor=colors[6],# маркеры точек
             label=labels_legend2, zorder=2)
    
##################################################################################################################################################    
    """    
#   Второй Контр-Многоуг.             
    ax.plot(Control_Point2_x, Control_Point2_y, #массивы "X" и "Y"
             linestyle='-', linewidth=0.3, color=colors[6], alpha=0.9, # линия и МАРКЕРЫ
             marker='o', markersize=8, markerfacecolor=colors[12], markeredgewidth=2, markeredgecolor=colors[6],# маркеры точек
             label=labels_legend3, zorder=2)      
    """
#  Второй Сплайн     
    ax.plot(datax2, datay2, #массивы "X" и "Y"
             linestyle='--', linewidth=2, color=colors[10], alpha=0.9, # линия и МАРКЕРЫ
             marker=' ', markersize=3, markerfacecolor=colors[10], markeredgewidth=2, markeredgecolor=colors[10],# маркеры точек
             label=labels_legend4, zorder=2)
    
##################################################################################################################################################    
    """    
#   Третий Контр-Многоуг.             
    ax.plot(Control_Point3_x, Control_Point3_y, #массивы "X" и "Y"
             linestyle='-', linewidth=0.3, color=colors[6], alpha=0.9, # линия и МАРКЕРЫ
             marker='s', markersize=8, markerfacecolor=colors[12], markeredgewidth=2, markeredgecolor=colors[6],# маркеры точек
             label=labels_legend5, zorder=2)      
    """
#  Третий Сплайн     
    ax.plot(datax3, datay3, #массивы "X" и "Y"
             linestyle='-', linewidth=2, color=colors[6], alpha=0.9, # линия и МАРКЕРЫ
             marker=' ', markersize=3, markerfacecolor=colors[10], markeredgewidth=2, markeredgecolor=colors[10],# маркеры точек
             label=labels_legend6, zorder=2)
    
    
 #  1-я Точка Ограничений  
    ax.plot(X1, Y1,  #массивы "X" и "Y"
             linestyle='', linewidth=6, color=colors[2], alpha=0.9, # линия и МАРКЕРЫ
             marker='o', markersize=5, markerfacecolor=colors[2], markeredgewidth=3, markeredgecolor=colors[2],# маркеры точек
             label=labels_legend7, zorder=2)
 #  2,3,4-я Точки Ограничений  
    ax.plot(X2, Y2,X3, Y3, X4, Y4, #массивы "X" и "Y"
             linestyle='', linewidth=6, color=colors[2], alpha=0.9, # линия и МАРКЕРЫ
             marker='o', markersize=6, markerfacecolor=colors[2], markeredgewidth=3, markeredgecolor=colors[2],# маркеры точек
              zorder=2)  
    
    
    ax.set_xlabel("ось Х")
    ax.set_ylabel("ось Y")
    #ax.set_title("Сэмплы " + chr(945) +"$_{i}$,  " + chr(945) +
    #            "$_{i+1}$"+f"  ,(i={0})",fontsize=16)
    ax.set_title(Title)
    #ax.set_title("1234")

    
    #ax.legend(loc="lower right")
    #ax.legend(loc="upper left")
    ax.legend(loc="upper right",  fontsize=10)
    #ax.legend(loc="lower left")
    
    
    
    ax.set_xlim(x_min, x_max);#"-2" - всё Верно !!! SM
    ax.set_ylim(y_min, y_max);
    
    ax.grid(True, ls=':', c=colors[6],alpha=0.3, zorder=0 )
    plt.show()
    
    #print("** From plot_trace_1_1_1 **")

    #print("-1-1-1-1  -", end="")
    #print("56")
                
               
    return
    

#***********************************************************************************
#***********************************************************************************   


#***********************************************************************************
#***********************************************************************************    
def plot_Trace_Lines_2_for_Mergin_a (Control_Point1_x, Control_Point1_y, Control_Point2_x, Control_Point2_y,
                                     datax1, datay1, datax2, datay2, y_min, y_max, x_min, x_max,
                                     Title, labels_legend1, labels_legend2, labels_legend3, labels_legend4):

# Рисует:
# 1. Контр.Многоугольник
# 2. 4-ре Сплайна.
#
#    
    
    
    #fig, ax = plt.subplots()
    #figsize(23, 5)
    # Размер Графиков Одинаковый для всех - Здается в Графике 0.
    fig, ax = plt.subplots(figsize=(9.0, 5)) # ДВА графика. Это  Одна строка и ДВА столбца = 2 Графика 
                                  # Если только ОДИН график, то вместо axesх[0] везде будет ax и fig, ax = plt.subplots()
    #plt.figsize(23, 5)
    labels = ["σ" +"$_{i}$", # в этом графике не используется
              chr(945) +"$_{i+1}$",
              "Banner_2",
               "123",
               "456",
              ]
    n= np.size(Control_Point1_x)
    
#    if (nx_max>n): 
#        print("**!!!************ ")
#        print("**!!!  nx_max>n  **!!!")
#        print("**!!!************ ")
#        stop
#    else:
#        pass
    
                    
    
#    data1=data[nx_min:nx_max]
#    n1= np.arange(np.size(data1))


    ax.set_facecolor(colors[7])
    
##################################################################################################################################################    

#   Первый Контр-Многоуг.    
    ax.plot(Control_Point1_x, Control_Point1_y, #массивы "X" и "Y"
             linestyle='-', linewidth=0.3, color=colors[6], alpha=0.9, # линия и МАРКЕРЫ
             marker='o', markersize=8, markerfacecolor=colors[6], markeredgewidth=2, markeredgecolor=colors[6],# маркеры точек
             label=labels_legend1, zorder=2)
    
#  Первый Сплайн    
    ax.plot(datax1, datay1, #массивы "X" и "Y"
             linestyle='--', linewidth=2, color=colors[6], alpha=0.9, # линия и МАРКЕРЫ
             marker=' ', markersize=3, markerfacecolor=colors[6], markeredgewidth=2, markeredgecolor=colors[6],# маркеры точек
             label=labels_legend2, zorder=2)
    
##################################################################################################################################################    
    
#   Второй Контр-Многоуг.             
    ax.plot(Control_Point2_x, Control_Point2_y, #массивы "X" и "Y"
             linestyle='-', linewidth=0.3, color=colors[12], alpha=0.9, # линия и МАРКЕРЫ
             marker='o', markersize=8, markerfacecolor=colors[12], markeredgewidth=2, markeredgecolor=colors[12],# маркеры точек
             label=labels_legend3, zorder=2)      

#  Второй Сплайн     
    ax.plot(datax2, datay2, #массивы "X" и "Y"
             linestyle='--', linewidth=2, color=colors[12], alpha=0.9, # линия и МАРКЕРЫ
             marker=' ', markersize=3, markerfacecolor=colors[12], markeredgewidth=2, markeredgecolor=colors[12],# маркеры точек
             label=labels_legend4, zorder=2)
    
##################################################################################################################################################    





 
    """    
#   Третий Контр-Многоуг.             
    ax.plot(Control_Point3_x, Control_Point3_y, #массивы "X" и "Y"
             linestyle='-', linewidth=0.3, color=colors[6], alpha=0.9, # линия и МАРКЕРЫ
             marker='s', markersize=8, markerfacecolor=colors[12], markeredgewidth=2, markeredgecolor=colors[6],# маркеры точек
             label=labels_legend5, zorder=2)      

#  Третий Сплайн     
    ax.plot(datax3, datay3, #массивы "X" и "Y"
             linestyle='-', linewidth=2, color=colors[6], alpha=0.9, # линия и МАРКЕРЫ
             marker=' ', markersize=3, markerfacecolor=colors[10], markeredgewidth=2, markeredgecolor=colors[10],# маркеры точек
             label=labels_legend6, zorder=2)
    """
    
    """
    ax.plot(datax3, datay3, #массивы "X" и "Y"
             linestyle='-', linewidth=2, color=colors[2], alpha=0.9, # линия и МАРКЕРЫ
             marker=' ', markersize=2, markerfacecolor=colors[2], markeredgewidth=2, markeredgecolor=colors[2],# маркеры точек
             label=labels_legend4, zorder=2)

    ax.plot(datax4, datay4, #массивы "X" и "Y"
             linestyle='-', linewidth=2, color=colors[4], alpha=0.9, # линия и МАРКЕРЫ
             marker=' ', markersize=2, markerfacecolor=colors[4], markeredgewidth=2, markeredgecolor=colors[4],# маркеры точек
             label=labels_legend5, zorder=2)


    """

    #ax.annotate("p-value ={0}".format(pvalue), xy = (0.21, 0.005), xytext=(0.15, 2), # печать значения p-value  
    #        arrowprops=dict(facecolor='black',                                   # рисуем кривую стрелку
    #                        arrowstyle='->', 
    #                        connectionstyle='angle3,angleA=-60,angleB=40'))
    
    """
    ax.annotate("$Степень=1$", fontsize=13, xytext=(5.0, 1.2),# координаты надписи и Начала Стрелки 
                                          xy = (8.5, 6.3), # координаты окончания стрелки
                arrowprops=dict(facecolor='black',                                   # рисуем кривую стрелку
                           arrowstyle='->'))  #, 
                           #connectionstyle='angle3,angleA=0,angleB=1000'))#искревление стрелки
    #ax.arrow_patch.set_color("gold")
    ax.annotate("$Степень=2$", fontsize=13, xytext=(-0.9,12.0),# координаты надписи и Начала Стрелки 
                                          xy = (3.6, 10.0), # координаты окончания стрелки
                color=colors[10],
                arrowprops=dict(color=colors[10],                                   # рисуем кривую стрелку
                           arrowstyle='->'))  #, 
                           #connectionstyle='angle3,angleA=0,angleB=1000'))#искревление стрелки    



    ax.annotate("$Степень=3$", fontsize=13, xytext=(15.0,11.5),# координаты надписи и Начала Стрелки 
                                          xy = (13.7, 9.5), # координаты окончания стрелки
                color=colors[2],
                arrowprops=dict(color=colors[2], # рисуем кривую стрелку
                           arrowstyle='->'))  #, 
                           #connectionstyle='angle3,angleA=0,angleB=1000'))#искревление стрелки  
                           
    ax.annotate("$Степень=6$", fontsize=13, xytext=(9.0,2.6),# координаты надписи и Начала Стрелки 
                                          xy = (13.4, 7.2), # координаты окончания стрелки
                color=colors[4],
                arrowprops=dict(color=colors[4], # рисуем кривую стрелку
                           arrowstyle='->'))  #, 
                           #connectionstyle='angle3,angleA=0,angleB=1000'))#искревление стрелки  
   """

    

    #ax.text (x=0.4, y=1.0, s="$B_{0}$", fontsize=13)
    #ax.text (x=1.4, y=2.9, s="$B_{1}$", fontsize=13)
    #ax.text (x=4.2, y=2.9, s="$B_{2}$", fontsize=13)  
    #ax.text (x=3.2, y=1.0, s="$B_{3}$", fontsize=13)
    
    
    #plt.text (x=20, y=71, s="Mu_real_mean=%.1f" %mean_observed, fontsize=14) 
    #plt.text (x=20, y=68, s="Std_real = %.1f" %std_observed, fontsize=14) 
    #ax.plot(n, (Alf_samples[:,1]+0), #массивы "X" и "Y"
    #         linestyle='-', linewidth=0.3, color=colors[6], alpha=0.9, # линия и МАРКЕРЫ
    #         marker='o', markersize=5, markerfacecolor=colors[10], markeredgewidth=1, markeredgecolor=colors[10],# маркеры точек
    #         label=labels[1], zorder=2)
    
    
    
    
    ax.set_xlabel("ось Х")
    ax.set_ylabel("ось Y")
    #ax.set_title("Сэмплы " + chr(945) +"$_{i}$,  " + chr(945) +
    #            "$_{i+1}$"+f"  ,(i={0})",fontsize=16)
    ax.set_title(Title)
    #ax.set_title("1234")

    
    #ax.legend(loc="lower right")
    #ax.legend(loc="upper left")
    ax.legend(loc="upper right",  fontsize=10)
    #ax.legend(loc="lower left")
    
    
    
    ax.set_xlim(x_min, x_max);#"-2" - всё Верно !!! SM
    ax.set_ylim(y_min, y_max);
    
    ax.grid(True, ls=':', c=colors[6],alpha=0.3, zorder=0 )
    #ax.imshow(fig, cmap=map, interpolation='nearest')
    #plt.subplot(212)
    #plt.imshow(fig,map='Greys', interpolation='nearest')
    plt.show()
    
    #print("** From plot_trace_1_1_1 **")

    #print("-1-1-1-1  -", end="")
    #print("56")
                
               
    return
    



#***********************************************************************************
#***********************************************************************************   


#***********************************************************************************
#***********************************************************************************    
def plot_Trace_Lines_4_for_Mergin_1 (Control_Point1_x, Control_Point1_y, 
                                     Control_Point1_2_x, Control_Point1_2_y,
                                     Control_Point2_x, Control_Point2_y,
                                     Control_Point2_2_x, Control_Point2_2_y,
                                     
                                     datax1, datay1,
                                     datax1_2, datay1_2, 
                                     datax2, datay2,
                                     datax2_2, datay2_2,
                                     
                           y_min, y_max, x_min, x_max,
                Title, labels_legend1, labels_legend2,
                labels_legend3, labels_legend4,labels_legend5,labels_legend6, labels_legend7,labels_legend8):

# Рисует:
# 1. Контр.Многоугольник
# 2. 4-ре Сплайна.
#
#    
    
    
    #fig, ax = plt.subplots()
    #figsize(23, 5)
    # Размер Графиков Одинаковый для всех - Здается в Графике 0.
    fig, ax = plt.subplots(figsize=(9.0, 5)) # ДВА графика. Это  Одна строка и ДВА столбца = 2 Графика 
                                  # Если только ОДИН график, то вместо axesх[0] везде будет ax и fig, ax = plt.subplots()
    #plt.figsize(23, 5)
    labels = ["σ" +"$_{i}$", # в этом графике не используется
              chr(945) +"$_{i+1}$",
              "Banner_2",
               "123",
               "456",
              ]
    n= np.size(Control_Point1_x)
    
#    if (nx_max>n): 
#        print("**!!!************ ")
#        print("**!!!  nx_max>n  **!!!")
#        print("**!!!************ ")
#        stop
#    else:
#        pass
    
                    
    
#    data1=data[nx_min:nx_max]
#    n1= np.arange(np.size(data1))


    ax.set_facecolor(colors[11])
   
##################################################################################################################################################    

#   P Контр-Многоуг.  
     
#    ax.plot(Control_Point1_x, Control_Point1_y, #массивы "X" и "Y"
#             linestyle='-', linewidth=0.3, color=colors[6], alpha=0.9, # линия и МАРКЕРЫ
#             marker='o', markersize=8, markerfacecolor=colors[12], markeredgewidth=2, markeredgecolor=colors[6],# маркеры точек
#             label=labels_legend1, zorder=2)
    
#  P  Сплайн    
    ax.plot(datax1, datay1, #массивы "X" и "Y"
             linestyle='--', linewidth=2, color=colors[6], alpha=0.9, # линия и МАРКЕРЫ
             marker=' ', markersize=3, markerfacecolor=colors[12], markeredgewidth=2, markeredgecolor=colors[6],# маркеры точек
             label=labels_legend2, zorder=2)
    
##################################################################################################################################################    
       
#   Второй Контр-Многоуг. P с крышкой 
              
    ax.plot(Control_Point1_2_x, Control_Point1_2_y, #массивы "X" и "Y"
             linestyle='-', linewidth=0.3, color=colors[6], alpha=0.9, # линия и МАРКЕРЫ
             marker='s', markersize=8, markerfacecolor=colors[6], markeredgewidth=2, markeredgecolor=colors[6],# маркеры точек
             label=labels_legend3, zorder=2)    
   

#  P с крышкой Сплайн     
    ax.plot(datax1_2, datay1_2, #массивы "X" и "Y"
             linestyle='dotted', linewidth=4, color=colors[6], alpha=0.9, # линия и МАРКЕРЫ
             marker=' ', markersize=3, markerfacecolor=colors[10], markeredgewidth=2, markeredgecolor=colors[10],# маркеры точек
             label=labels_legend4, zorder=2)
   
##################################################################################################################################################    
    
#   Q Контр-Многоуг.  
    
#    ax.plot(Control_Point2_x, Control_Point2_y, #массивы "X" и "Y"
#             linestyle='-', linewidth=0.3, color=colors[6], alpha=0.9, # линия и МАРКЕРЫ
#             marker='o', markersize=8, markerfacecolor=colors[6], markeredgewidth=2, markeredgecolor=colors[6],# маркеры точек
#             label=labels_legend5, zorder=2)
    
    
#  Q Сплайн    
    ax.plot(datax2, datay2, #массивы "X" и "Y"
             linestyle='--', linewidth=2, color=colors[10], alpha=0.9, # линия и МАРКЕРЫ
             marker=' ', markersize=3, markerfacecolor=colors[12], markeredgewidth=2, markeredgecolor=colors[10],# маркеры точек
             label=labels_legend6, zorder=2)
    
##################################################################################################################################################    
       
#   Четверный Контр-Многоуг. 
              
    ax.plot(Control_Point2_2_x, Control_Point2_2_y, #массивы "X" и "Y"
             linestyle='-', linewidth=0.3, color=colors[10], alpha=0.9, # линия и МАРКЕРЫ
             marker='s', markersize=8, markerfacecolor=colors[10], markeredgewidth=2, markeredgecolor=colors[10],# маркеры точек
             label=labels_legend7, zorder=2)  
      

#  Q с крышкой Сплайн      
    ax.plot(datax2_2, datay2_2, #массивы "X" и "Y"
             linestyle='dotted', linewidth=4, color=colors[10], alpha=0.9, # линия и МАРКЕРЫ
             marker=' ', markersize=3, markerfacecolor=colors[10], markeredgewidth=2, markeredgecolor=colors[10],# маркеры точек
             label=labels_legend8, zorder=2)
   
##################################################################################################################################################    

     


    #ax.annotate("p-value ={0}".format(pvalue), xy = (0.21, 0.005), xytext=(0.15, 2), # печать значения p-value  
    #        arrowprops=dict(facecolor='black',                                   # рисуем кривую стрелку
    #                        arrowstyle='->', 
    #                        connectionstyle='angle3,angleA=-60,angleB=40'))
    
    """
    ax.annotate("$Степень=1$", fontsize=13, xytext=(5.0, 1.2),# координаты надписи и Начала Стрелки 
                                          xy = (8.5, 6.3), # координаты окончания стрелки
                arrowprops=dict(facecolor='black',                                   # рисуем кривую стрелку
                           arrowstyle='->'))  #, 
                           #connectionstyle='angle3,angleA=0,angleB=1000'))#искревление стрелки
    #ax.arrow_patch.set_color("gold")
    ax.annotate("$Степень=2$", fontsize=13, xytext=(-0.9,12.0),# координаты надписи и Начала Стрелки 
                                          xy = (3.6, 10.0), # координаты окончания стрелки
                color=colors[10],
                arrowprops=dict(color=colors[10],                                   # рисуем кривую стрелку
                           arrowstyle='->'))  #, 
                           #connectionstyle='angle3,angleA=0,angleB=1000'))#искревление стрелки    



    ax.annotate("$Степень=3$", fontsize=13, xytext=(15.0,11.5),# координаты надписи и Начала Стрелки 
                                          xy = (13.7, 9.5), # координаты окончания стрелки
                color=colors[2],
                arrowprops=dict(color=colors[2], # рисуем кривую стрелку
                           arrowstyle='->'))  #, 
                           #connectionstyle='angle3,angleA=0,angleB=1000'))#искревление стрелки  
                           
    ax.annotate("$Степень=6$", fontsize=13, xytext=(9.0,2.6),# координаты надписи и Начала Стрелки 
                                          xy = (13.4, 7.2), # координаты окончания стрелки
                color=colors[4],
                arrowprops=dict(color=colors[4], # рисуем кривую стрелку
                           arrowstyle='->'))  #, 
                           #connectionstyle='angle3,angleA=0,angleB=1000'))#искревление стрелки  
   """

    

    #ax.text (x=0.4, y=1.0, s="$B_{0}$", fontsize=13)
    #ax.text (x=1.4, y=2.9, s="$B_{1}$", fontsize=13)
    #ax.text (x=4.2, y=2.9, s="$B_{2}$", fontsize=13)  
    #ax.text (x=3.2, y=1.0, s="$B_{3}$", fontsize=13)
    
    
    #plt.text (x=20, y=71, s="Mu_real_mean=%.1f" %mean_observed, fontsize=14) 
    #plt.text (x=20, y=68, s="Std_real = %.1f" %std_observed, fontsize=14) 
    #ax.plot(n, (Alf_samples[:,1]+0), #массивы "X" и "Y"
    #         linestyle='-', linewidth=0.3, color=colors[6], alpha=0.9, # линия и МАРКЕРЫ
    #         marker='o', markersize=5, markerfacecolor=colors[10], markeredgewidth=1, markeredgecolor=colors[10],# маркеры точек
    #         label=labels[1], zorder=2)
    
    
    
    
    ####ax.set_xlabel("ось Х")
    #####ax.set_ylabel("ось Y")
    #ax.set_title("Сэмплы " + chr(945) +"$_{i}$,  " + chr(945) +
    #            "$_{i+1}$"+f"  ,(i={0})",fontsize=16)
    ax.set_title(Title)
    #ax.set_title("1234")

    
    #ax.legend(loc="lower right")
    #ax.legend(loc="upper left")
    ax.legend(loc="upper right",  fontsize=10)
    #ax.legend(loc="lower left")
    
    
    
    ax.set_xlim(x_min, x_max);#"-2" - всё Верно !!! SM
    ax.set_ylim(y_min, y_max);
    
    ax.grid(True, ls=':', c=colors[6],alpha=0.3, zorder=0 )
    plt.show()
    
    #print("** From plot_trace_1_1_1 **")

    #print("-1-1-1-1  -", end="")
    #print("56")
                
               
    return
    



#***********************************************************************************
#***********************************************************************************   



#***********************************************************************************
#***********************************************************************************   


#***********************************************************************************
#***********************************************************************************    
def plot_Trace_Lines_2_for_Mergin_1 (Control_Point1_x, Control_Point1_y, 
                                     Control_Point1_2_x, Control_Point1_2_y,
                                     
                                     
                                     datax1, datay1,
                                     datax1_2, datay1_2, 
                                    
                                     
                           y_min, y_max, x_min, x_max,
                Title, labels_legend1, labels_legend2,
                labels_legend3, labels_legend4):

# Рисует:
# 1. Контр.Многоугольник
# 2. 4-ре Сплайна.
#
#    
    
    
    #fig, ax = plt.subplots()
    #figsize(23, 5)
    # Размер Графиков Одинаковый для всех - Здается в Графике 0.
    fig, ax = plt.subplots(figsize=(9.0, 5)) # ДВА графика. Это  Одна строка и ДВА столбца = 2 Графика 
                                  # Если только ОДИН график, то вместо axesх[0] везде будет ax и fig, ax = plt.subplots()
    #plt.figsize(23, 5)
    labels = ["σ" +"$_{i}$", # в этом графике не используется
              chr(945) +"$_{i+1}$",
              "Banner_2",
               "123",
               "456",
              ]
    n= np.size(Control_Point1_x)
    
#    if (nx_max>n): 
#        print("**!!!************ ")
#        print("**!!!  nx_max>n  **!!!")
#        print("**!!!************ ")
#        stop
#    else:
#        pass
    
                    
    
#    data1=data[nx_min:nx_max]
#    n1= np.arange(np.size(data1))


    ax.set_facecolor(colors[11])
   
##################################################################################################################################################    

#   Первый Контр-Многоуг.    
    ax.plot(Control_Point1_x, Control_Point1_y, #массивы "X" и "Y"
             linestyle='-', linewidth=0.3, color=colors[2], alpha=0.9, # линия и МАРКЕРЫ
             marker='s', markersize=8, markerfacecolor=colors[2], markeredgewidth=2, markeredgecolor=colors[6],# маркеры точек
             label=labels_legend1, zorder=2)
    
#  Первый Сплайн    
    ax.plot(datax1, datay1, #массивы "X" и "Y"
             linestyle='--', linewidth=2, color=colors[2], alpha=0.9, # линия и МАРКЕРЫ
             marker=' ', markersize=3, markerfacecolor=colors[2], markeredgewidth=2, markeredgecolor=colors[2],# маркеры точек
             label=labels_legend2, zorder=2)
    
##################################################################################################################################################    
       
#   Второй Контр-Многоуг.             
    ax.plot(Control_Point1_2_x, Control_Point1_2_y, #массивы "X" и "Y"
             linestyle='-', linewidth=0.3, color=colors[2], alpha=0.9, # линия и МАРКЕРЫ
             marker='o', markersize=8, markerfacecolor=colors[2], markeredgewidth=2, markeredgecolor=colors[6],# маркеры точек
             label=labels_legend3, zorder=2)      

#  Второй Сплайн     
    ax.plot(datax1_2, datay1_2, #массивы "X" и "Y"
             linestyle='dotted', linewidth=3, color=colors[2], alpha=0.9, # линия и МАРКЕРЫ
             marker=' ', markersize=3, markerfacecolor=colors[10], markeredgewidth=2, markeredgecolor=colors[10],# маркеры точек
             label=labels_legend4, zorder=2)
   
##################################################################################################################################################    
    


    #ax.annotate("p-value ={0}".format(pvalue), xy = (0.21, 0.005), xytext=(0.15, 2), # печать значения p-value  
    #        arrowprops=dict(facecolor='black',                                   # рисуем кривую стрелку
    #                        arrowstyle='->', 
    #                        connectionstyle='angle3,angleA=-60,angleB=40'))
    
    """
    ax.annotate("$Степень=1$", fontsize=13, xytext=(5.0, 1.2),# координаты надписи и Начала Стрелки 
                                          xy = (8.5, 6.3), # координаты окончания стрелки
                arrowprops=dict(facecolor='black',                                   # рисуем кривую стрелку
                           arrowstyle='->'))  #, 
                           #connectionstyle='angle3,angleA=0,angleB=1000'))#искревление стрелки
    #ax.arrow_patch.set_color("gold")
    ax.annotate("$Степень=2$", fontsize=13, xytext=(-0.9,12.0),# координаты надписи и Начала Стрелки 
                                          xy = (3.6, 10.0), # координаты окончания стрелки
                color=colors[10],
                arrowprops=dict(color=colors[10],                                   # рисуем кривую стрелку
                           arrowstyle='->'))  #, 
                           #connectionstyle='angle3,angleA=0,angleB=1000'))#искревление стрелки    



    ax.annotate("$Степень=3$", fontsize=13, xytext=(15.0,11.5),# координаты надписи и Начала Стрелки 
                                          xy = (13.7, 9.5), # координаты окончания стрелки
                color=colors[2],
                arrowprops=dict(color=colors[2], # рисуем кривую стрелку
                           arrowstyle='->'))  #, 
                           #connectionstyle='angle3,angleA=0,angleB=1000'))#искревление стрелки  
                           
    ax.annotate("$Степень=6$", fontsize=13, xytext=(9.0,2.6),# координаты надписи и Начала Стрелки 
                                          xy = (13.4, 7.2), # координаты окончания стрелки
                color=colors[4],
                arrowprops=dict(color=colors[4], # рисуем кривую стрелку
                           arrowstyle='->'))  #, 
                           #connectionstyle='angle3,angleA=0,angleB=1000'))#искревление стрелки  
   """

    

    #ax.text (x=0.4, y=1.0, s="$B_{0}$", fontsize=13)
    #ax.text (x=1.4, y=2.9, s="$B_{1}$", fontsize=13)
    #ax.text (x=4.2, y=2.9, s="$B_{2}$", fontsize=13)  
    #ax.text (x=3.2, y=1.0, s="$B_{3}$", fontsize=13)
    
    
    #plt.text (x=20, y=71, s="Mu_real_mean=%.1f" %mean_observed, fontsize=14) 
    #plt.text (x=20, y=68, s="Std_real = %.1f" %std_observed, fontsize=14) 
    #ax.plot(n, (Alf_samples[:,1]+0), #массивы "X" и "Y"
    #         linestyle='-', linewidth=0.3, color=colors[6], alpha=0.9, # линия и МАРКЕРЫ
    #         marker='o', markersize=5, markerfacecolor=colors[10], markeredgewidth=1, markeredgecolor=colors[10],# маркеры точек
    #         label=labels[1], zorder=2)
    
    
    
    
    ax.set_xlabel("ось Х")
    ax.set_ylabel("ось Y")
    #ax.set_title("Сэмплы " + chr(945) +"$_{i}$,  " + chr(945) +
    #            "$_{i+1}$"+f"  ,(i={0})",fontsize=16)
    ax.set_title(Title)
    #ax.set_title("1234")

    
    #ax.legend(loc="lower right")
    #ax.legend(loc="upper left")
    ax.legend(loc="upper right",  fontsize=10)
    #ax.legend(loc="lower left")
    
    
    
    ax.set_xlim(x_min, x_max);#"-2" - всё Верно !!! SM
    ax.set_ylim(y_min, y_max);
    
    ax.grid(True, ls=':', c=colors[6],alpha=0.3, zorder=0 )
    plt.show()
    
    #print("** From plot_trace_1_1_1 **")

    #print("-1-1-1-1  -", end="")
    #print("56")
                
               
    return
    



#***********************************************************************************
#***********************************************************************************   



#***********************************************************************************
#***********************************************************************************    
def plot_Trace_3_Lines_2 (datax, datay, datax1, datay1, datax2, datay2,  y_min, y_max, x_min, x_max,
                Title, labels_legend1, labels_legend2):
    
    
    
    #fig, ax = plt.subplots()
    #figsize(23, 5)
    # Размер Графиков Одинаковый для всех - Здается в Графике 0.
    fig, ax = plt.subplots(figsize=(7.0, 5)) # ДВА графика. Это  Одна строка и ДВА столбца = 2 Графика 
                                  # Если только ОДИН график, то вместо axesх[0] везде будет ax и fig, ax = plt.subplots()
    #plt.figsize(23, 5)
    labels = ["σ" +"$_{i}$", # в этом графике не используется
              chr(945) +"$_{i+1}$",
              "Banner_2",
               "123",
               "456",
              ]
    n= np.size(datax)
    
#    if (nx_max>n): 
#        print("**!!!************ ")
#        print("**!!!  nx_max>n  **!!!")
#        print("**!!!************ ")
#        stop
#    else:
#        pass
    
                    
    
#    data1=data[nx_min:nx_max]
#    n1= np.arange(np.size(data1))


    ax.set_facecolor(colors[11])

    
    ax.plot(datax, datay, #массивы "X" и "Y"
             linestyle='-', linewidth=0.3, color=colors[6], alpha=0.9, # линия и МАРКЕРЫ
             marker='o', markersize=8, markerfacecolor=colors[12], markeredgewidth=2, markeredgecolor=colors[6],# маркеры точек
             #label=labels_legend1, zorder=2)
             )
    ax.plot(datax1, datay1, #массивы "X" и "Y"
             linestyle='-', linewidth=2, color=colors[6], alpha=0.9, # линия и МАРКЕРЫ
             marker=' ', markersize=3, markerfacecolor=colors[12], markeredgewidth=2, markeredgecolor=colors[6],# маркеры точек
             #label=labels_legend2, zorder=2)
             )

    ax.plot(datax2, datay2, #массивы "X" и "Y"
             linestyle='', linewidth=2, color=colors[10], alpha=0.9, # линия и МАРКЕРЫ
             marker=' ', markersize=3, markerfacecolor=colors[10], markeredgewidth=2, markeredgecolor=colors[10],# маркеры точек
             )

    #ax.plot(datax3, datay3, #массивы "X" и "Y"
    #         linestyle=' ', linewidth=3, color=colors[2], alpha=0.9, # линия и МАРКЕРЫ
    #         marker='o', markersize=2, markerfacecolor=colors[2], markeredgewidth=2, markeredgecolor=colors[2],# маркеры точек
    #         )


    #ax.annotate("p-value ={0}".format(pvalue), xy = (0.21, 0.005), xytext=(0.15, 2), # печать значения p-value  
    #        arrowprops=dict(facecolor='black',                                   # рисуем кривую стрелку
    #                        arrowstyle='->', 
    #                        connectionstyle='angle3,angleA=-60,angleB=40'))
    
    # Надпись w=1
#    ax.annotate("$w_{1}=1$", fontsize=13, xytext=(5,2.2),# координаты надписи и Начала Стрелки 
#                                          xy = (4.3, 5.6), # координаты окончания стрелки
#                arrowprops=dict(facecolor='black',                                   # рисуем кривую стрелку
#                           arrowstyle='->'))  #, 
#                           #connectionstyle='angle3,angleA=0,angleB=1000'))#искревление стрелки
    # Надпись w=0.4
#    ax.annotate("$w_{1}=0.4$", fontsize=13, xytext=(8.8,3.6),# координаты надписи и Начала Стрелки 
#                                          xy = (5.6, 6.0), # координаты окончания стрелки
#                color=colors[10],
#                arrowprops=dict(color=colors[10],                                   # рисуем кривую стрелку
#                           arrowstyle='->'))  #, 
                           #connectionstyle='angle3,angleA=0,angleB=1000'))#искревление стрелки    



#    ax.annotate("$w_{1}=0$", fontsize=13, xytext=(9.3,5.3),# координаты надписи и Начала Стрелки 
#                                          xy = (8.9, 6.5), # координаты окончания стрелки
#                color=colors[2],
#                arrowprops=dict(color=colors[2],                                   # рисуем кривую стрелку
#                           arrowstyle='->'))  #, 
                           #connectionstyle='angle3,angleA=0,angleB=1000'))#искревление стрелки  




    #ax.text (x=0.4, y=1.0, s="$B_{0}$", fontsize=13)
    #ax.text (x=1.4, y=2.9, s="$B_{1}$", fontsize=13)
    #ax.text (x=4.2, y=2.9, s="$B_{2}$", fontsize=13)  
    #ax.text (x=3.2, y=1.0, s="$B_{3}$", fontsize=13)
    
    
    #plt.text (x=20, y=71, s="Mu_real_mean=%.1f" %mean_observed, fontsize=14) 
    #plt.text (x=20, y=68, s="Std_real = %.1f" %std_observed, fontsize=14) 
    #ax.plot(n, (Alf_samples[:,1]+0), #массивы "X" и "Y"
    #         linestyle='-', linewidth=0.3, color=colors[6], alpha=0.9, # линия и МАРКЕРЫ
    #         marker='o', markersize=5, markerfacecolor=colors[10], markeredgewidth=1, markeredgecolor=colors[10],# маркеры точек
    #         label=labels[1], zorder=2)
    
    
    
    
    ax.set_xlabel("ось Х")
    ax.set_ylabel("ось Y")
    #ax.set_title("Сэмплы " + chr(945) +"$_{i}$,  " + chr(945) +
    #            "$_{i+1}$"+f"  ,(i={0})",fontsize=16)
    ax.set_title(Title)
    #ax.set_title("1234")

    
    #ax.legend(loc="lower right")
    #ax.legend(loc="upper left")
    #ax.legend(loc="upper right",  fontsize=10)
    #ax.legend(loc="lower left")
    
    
    
    ax.set_xlim(x_min, x_max);#"-2" - всё Верно !!! SM
    ax.set_ylim(y_min, y_max);
    
    ax.grid(True, ls=':', c=colors[6],alpha=0.3, zorder=0 )
    plt.show()
    
    #print("** From plot_trace_1_1_1 **")

    #print("-1-1-1-1  -", end="")
    #print("56")
                
               
    return
    

#***********************************************************************************
#***********************************************************************************   






#***********************************************************************************
#***********************************************************************************    
def plot_Trace_2 (datax, datay, datax1, datay1, y_min, y_max, x_min, x_max,
                Title, labels_legend1, labels_legend2):
    
    
    
    #fig, ax = plt.subplots()
    #figsize(23, 5)
    # Размер Графиков Одинаковый для всех - Здается в Графике 0.
    fig, ax = plt.subplots(figsize=(7, 5)) # ДВА графика. Это  Одна строка и ДВА столбца = 2 Графика 
                                  # Если только ОДИН график, то вместо axesх[0] везде будет ax и fig, ax = plt.subplots()
    #plt.figsize(23, 5)
    labels = ["σ" +"$_{i}$", # в этом графике не используется
              chr(945) +"$_{i+1}$",
              "Banner_2",
               "123",
               "456",
              ]
    n= np.size(datax)
    
#    if (nx_max>n): 
#        print("**!!!************ ")
#        print("**!!!  nx_max>n  **!!!")
#        print("**!!!************ ")
#        stop
#    else:
#        pass
    
                    
    
#    data1=data[nx_min:nx_max]
#    n1= np.arange(np.size(data1))


    ax.set_facecolor(colors[11])

    
    ax.plot(datax, datay, #массивы "X" и "Y"
             linestyle='-', linewidth=0.3, color=colors[6], alpha=0.9, # линия и МАРКЕРЫ
             marker='o', markersize=7, markerfacecolor=colors[12], markeredgewidth=2, markeredgecolor=colors[6],# маркеры точек
             label=labels_legend1, zorder=2)
    ax.plot(datax1, datay1, #массивы "X" и "Y"
             linestyle=' ', linewidth=4, color=colors[6], alpha=0.9, # линия и МАРКЕРЫ
             marker='o', markersize=10, markerfacecolor=colors[6], markeredgewidth=2, markeredgecolor=colors[6],# маркеры точек
             label=labels_legend2, zorder=2)
    
    #plt.text (x=20, y=71, s="Mu_real_mean=%.1f" %mean_observed, fontsize=14) 
    #plt.text (x=20, y=68, s="Std_real = %.1f" %std_observed, fontsize=14) 
    #ax.plot(n, (Alf_samples[:,1]+0), #массивы "X" и "Y"
    #         linestyle='-', linewidth=0.3, color=colors[6], alpha=0.9, # линия и МАРКЕРЫ
    #         marker='o', markersize=5, markerfacecolor=colors[10], markeredgewidth=1, markeredgecolor=colors[10],# маркеры точек
    #         label=labels[1], zorder=2)
    
    
    
    
    ax.set_xlabel("ось Х")
    ax.set_ylabel("ось Y")
    #ax.set_title("Сэмплы " + chr(945) +"$_{i}$,  " + chr(945) +
    #            "$_{i+1}$"+f"  ,(i={0})",fontsize=16)
    ax.set_title(Title)
    #ax.set_title("1234")

    
    #ax.legend(loc="lower right")
    ax.legend(loc="upper left")
    #ax.legend(loc="upper right",  fontsize=10)
    #ax.legend(loc="lower left")
    
    
    
    ax.set_xlim(x_min, x_max);#"-2" - всё Верно !!! SM
    ax.set_ylim(y_min, y_max);
    
    ax.grid(True, ls=':', c=colors[6],alpha=0.3, zorder=0 )
    plt.show()
    
    #print("** From plot_trace_1_1_1 **")

    #print("-1-1-1-1  -", end="")
    #print("56")
                
               
    return
    

#***********************************************************************************
#***********************************************************************************   


#***********************************************************************************
#***********************************************************************************    
def plot_Trace_1 (datax, datay, datax1, datay1, y_min, y_max, x_min, x_max,
                Title, labels_legend1, labels_legend2):
    
    
    
    #fig, ax = plt.subplots()
    #figsize(23, 5)
    # Размер Графиков Одинаковый для всех - Здается в Графике 0.
    fig, ax = plt.subplots(figsize=(4, 3)) # ДВА графика. Это  Одна строка и ДВА столбца = 2 Графика 
                                  # Если только ОДИН график, то вместо axesх[0] везде будет ax и fig, ax = plt.subplots()
    #plt.figsize(23, 5)
    labels = ["σ" +"$_{i}$", # в этом графике не используется
              chr(945) +"$_{i+1}$",
              "Banner_2",
               "123",
               "456",
              ]
    n= np.size(datax)
    
#    if (nx_max>n): 
#        print("**!!!************ ")
#        print("**!!!  nx_max>n  **!!!")
#        print("**!!!************ ")
#        stop
#    else:
#        pass
    
                    
    
#    data1=data[nx_min:nx_max]
#    n1= np.arange(np.size(data1))


    ax.set_facecolor(colors[11])

    
    ax.plot(datax, datay, #массивы "X" и "Y"
             linestyle='-', linewidth=0.3, color=colors[6], alpha=0.9, # линия и МАРКЕРЫ
             marker='o', markersize=8, markerfacecolor=colors[12], markeredgewidth=2, markeredgecolor=colors[6],# маркеры точек
             label=labels_legend1, zorder=2)
    ax.plot(datax1, datay1, #массивы "X" и "Y"
             linestyle='-', linewidth=2, color=colors[6], alpha=0.9, # линия и МАРКЕРЫ
             marker=' ', markersize=3, markerfacecolor=colors[12], markeredgewidth=2, markeredgecolor=colors[6],# маркеры точек
             label=labels_legend2, zorder=2)


    #ax.annotate("p-value ={0}".format(pvalue), xy = (0.21, 0.005), xytext=(0.15, 2), # печать значения p-value  
    #        arrowprops=dict(facecolor='black',                                   # рисуем кривую стрелку
    #                        arrowstyle='->', 
    #                        connectionstyle='angle3,angleA=-60,angleB=40'))
    
    
    ax.text (x=0.4, y=1.0, s="$B_{0}$", fontsize=13)
    ax.text (x=1.4, y=2.9, s="$B_{1}$", fontsize=13)
    ax.text (x=4.2, y=2.9, s="$B_{2}$", fontsize=13)  
    ax.text (x=3.2, y=1.0, s="$B_{3}$", fontsize=13)
    
    
    #plt.text (x=20, y=71, s="Mu_real_mean=%.1f" %mean_observed, fontsize=14) 
    #plt.text (x=20, y=68, s="Std_real = %.1f" %std_observed, fontsize=14) 
    #ax.plot(n, (Alf_samples[:,1]+0), #массивы "X" и "Y"
    #         linestyle='-', linewidth=0.3, color=colors[6], alpha=0.9, # линия и МАРКЕРЫ
    #         marker='o', markersize=5, markerfacecolor=colors[10], markeredgewidth=1, markeredgecolor=colors[10],# маркеры точек
    #         label=labels[1], zorder=2)
    
    
    
    
    ax.set_xlabel("ось Х")
    ax.set_ylabel("ось Y")
    #ax.set_title("Сэмплы " + chr(945) +"$_{i}$,  " + chr(945) +
    #            "$_{i+1}$"+f"  ,(i={0})",fontsize=16)
    ax.set_title(Title)
    #ax.set_title("1234")

    
    #ax.legend(loc="lower right")
    ax.legend(loc="upper left")
    #ax.legend(loc="upper right",  fontsize=10)
    #ax.legend(loc="lower left")
    
    
    
    ax.set_xlim(x_min, x_max);#"-2" - всё Верно !!! SM
    ax.set_ylim(y_min, y_max);
    
    ax.grid(True, ls=':', c=colors[6],alpha=0.3, zorder=0 )
    plt.show()
    
    #print("** From plot_trace_1_1_1 **")

    #print("-1-1-1-1  -", end="")
    #print("56")
                
               
    return
    

#***********************************************************************************
#***********************************************************************************   



#***********************************************************************************
#***********************************************************************************    
def plot_Trace_3_Lines_1 (datax, datay, datax1, datay1, datax2, datay2, datax3, datay3, y_min, y_max, x_min, x_max,
                Title, labels_legend1, labels_legend2):
    
    
    
    #fig, ax = plt.subplots()
    #figsize(23, 5)
    # Размер Графиков Одинаковый для всех - Здается в Графике 0.
    fig, ax = plt.subplots(figsize=(3.0, 3)) # ДВА графика. Это  Одна строка и ДВА столбца = 2 Графика 
                                  # Если только ОДИН график, то вместо axesх[0] везде будет ax и fig, ax = plt.subplots()
    #plt.figsize(23, 5)
    labels = ["σ" +"$_{i}$", # в этом графике не используется
              chr(945) +"$_{i+1}$",
              "Banner_2",
               "123",
               "456",
              ]
    n= np.size(datax)
    
#    if (nx_max>n): 
#        print("**!!!************ ")
#        print("**!!!  nx_max>n  **!!!")
#        print("**!!!************ ")
#        stop
#    else:
#        pass
    
                    
    
#    data1=data[nx_min:nx_max]
#    n1= np.arange(np.size(data1))


    ax.set_facecolor(colors[11])

    
    ax.plot(datax, datay, #массивы "X" и "Y"
             linestyle='-', linewidth=0.3, color=colors[6], alpha=0.9, # линия и МАРКЕРЫ
             marker='o', markersize=8, markerfacecolor=colors[12], markeredgewidth=2, markeredgecolor=colors[6],# маркеры точек
             #label=labels_legend1, zorder=2)
             )
    ax.plot(datax1, datay1, #массивы "X" и "Y"
             linestyle='-', linewidth=2, color=colors[6], alpha=0.9, # линия и МАРКЕРЫ
             marker=' ', markersize=3, markerfacecolor=colors[12], markeredgewidth=2, markeredgecolor=colors[6],# маркеры точек
             #label=labels_legend2, zorder=2)
             )

    ax.plot(datax2, datay2, #массивы "X" и "Y"
             linestyle='--', linewidth=2, color=colors[10], alpha=0.9, # линия и МАРКЕРЫ
             marker=' ', markersize=3, markerfacecolor=colors[10], markeredgewidth=2, markeredgecolor=colors[10],# маркеры точек
             )
 
    ax.plot(datax3, datay3, #массивы "X" и "Y"
             linestyle=' ', linewidth=3, color=colors[2], alpha=0.9, # линия и МАРКЕРЫ
             marker='o', markersize=2, markerfacecolor=colors[2], markeredgewidth=2, markeredgecolor=colors[2],# маркеры точек
             )



    #ax.annotate("p-value ={0}".format(pvalue), xy = (0.21, 0.005), xytext=(0.15, 2), # печать значения p-value  
    #        arrowprops=dict(facecolor='black',                                   # рисуем кривую стрелку
    #                        arrowstyle='->', 
    #                        connectionstyle='angle3,angleA=-60,angleB=40'))
    
 
    ax.annotate("$w_{1}=1$", fontsize=13, xytext=(5,2.2),# координаты надписи и Начала Стрелки 
                                          xy = (4.3, 5.6), # координаты окончания стрелки
                arrowprops=dict(facecolor='black',                                   # рисуем кривую стрелку
                           arrowstyle='->'))  #, 
                           #connectionstyle='angle3,angleA=0,angleB=1000'))#искревление стрелки

    ax.annotate("$w_{1}=2$", fontsize=13, xytext=(8.8,3.6),# координаты надписи и Начала Стрелки 
                                          xy = (5.0, 7.0), # координаты окончания стрелки
                color=colors[10],
                arrowprops=dict(color=colors[10],                                   # рисуем кривую стрелку
                           arrowstyle='->'))  #, 
                           #connectionstyle='angle3,angleA=0,angleB=1000'))#искревление стрелки    



    ax.annotate("$w_{1}=10$", fontsize=13, xytext=(9.3,5.3),# координаты надписи и Начала Стрелки 
                                          xy = (5.2, 7.9), # координаты окончания стрелки
                 color=colors[2],
                arrowprops=dict( color=colors[2],                                   # рисуем кривую стрелку
                           arrowstyle='->'))  #, 
                           #connectionstyle='angle3,angleA=0,angleB=1000'))#искревление стрелки  




    #ax.text (x=0.4, y=1.0, s="$B_{0}$", fontsize=13)
    #ax.text (x=1.4, y=2.9, s="$B_{1}$", fontsize=13)
    #ax.text (x=4.2, y=2.9, s="$B_{2}$", fontsize=13)  
    #ax.text (x=3.2, y=1.0, s="$B_{3}$", fontsize=13)
    
    
    #plt.text (x=20, y=71, s="Mu_real_mean=%.1f" %mean_observed, fontsize=14) 
    #plt.text (x=20, y=68, s="Std_real = %.1f" %std_observed, fontsize=14) 
    #ax.plot(n, (Alf_samples[:,1]+0), #массивы "X" и "Y"
    #         linestyle='-', linewidth=0.3, color=colors[6], alpha=0.9, # линия и МАРКЕРЫ
    #         marker='o', markersize=5, markerfacecolor=colors[10], markeredgewidth=1, markeredgecolor=colors[10],# маркеры точек
    #         label=labels[1], zorder=2)
    
    
    
    
    ax.set_xlabel("ось Х")
    ax.set_ylabel("ось Y")
    #ax.set_title("Сэмплы " + chr(945) +"$_{i}$,  " + chr(945) +
    #            "$_{i+1}$"+f"  ,(i={0})",fontsize=16)
    ax.set_title(Title)
    #ax.set_title("1234")

    
    #ax.legend(loc="lower right")
    #ax.legend(loc="upper left")
    #ax.legend(loc="upper right",  fontsize=10)
    #ax.legend(loc="lower left")
    
    
    
    ax.set_xlim(x_min, x_max);#"-2" - всё Верно !!! SM
    ax.set_ylim(y_min, y_max);
    
    ax.grid(True, ls=':', c=colors[6],alpha=0.3, zorder=0 )
    plt.show()
    
    #print("** From plot_trace_1_1_1 **")

    #print("-1-1-1-1  -", end="")
    #print("56")
                
               
    return
    

#***********************************************************************************
#***********************************************************************************   




#***********************************************************************************
#***********************************************************************************    
def plot_Trace_3_Lines_3 (datax, datay, datax1, datay1, datax2, datay2, datax3, datay3, y_min, y_max, x_min, x_max,
                Title, labels_legend1, labels_legend2):
    
    
    
    #fig, ax = plt.subplots()
    #figsize(23, 5)
    # Размер Графиков Одинаковый для всех - Здается в Графике 0.
    fig, ax = plt.subplots(figsize=(3.0, 3)) # ДВА графика. Это  Одна строка и ДВА столбца = 2 Графика 
                                  # Если только ОДИН график, то вместо axesх[0] везде будет ax и fig, ax = plt.subplots()
    #plt.figsize(23, 5)
    labels = ["σ" +"$_{i}$", # в этом графике не используется
              chr(945) +"$_{i+1}$",
              "Banner_2",
               "123",
               "456",
              ]
    n= np.size(datax)
    
#    if (nx_max>n): 
#        print("**!!!************ ")
#        print("**!!!  nx_max>n  **!!!")
#        print("**!!!************ ")
#        stop
#    else:
#        pass
    
                    
    
#    data1=data[nx_min:nx_max]
#    n1= np.arange(np.size(data1))


    ax.set_facecolor(colors[11])

    
    ax.plot(datax, datay, #массивы "X" и "Y"
             linestyle='-', linewidth=0.3, color=colors[6], alpha=0.9, # линия и МАРКЕРЫ
             marker='o', markersize=8, markerfacecolor=colors[12], markeredgewidth=2, markeredgecolor=colors[6],# маркеры точек
             #label=labels_legend1, zorder=2)
             )
    ax.plot(datax1, datay1, #массивы "X" и "Y"
             linestyle='-', linewidth=2, color=colors[6], alpha=0.9, # линия и МАРКЕРЫ
             marker=' ', markersize=3, markerfacecolor=colors[12], markeredgewidth=2, markeredgecolor=colors[6],# маркеры точек
             #label=labels_legend2, zorder=2)
             )

    ax.plot(datax2, datay2, #массивы "X" и "Y"
             linestyle='--', linewidth=2, color=colors[10], alpha=0.9, # линия и МАРКЕРЫ
             marker=' ', markersize=3, markerfacecolor=colors[10], markeredgewidth=2, markeredgecolor=colors[10],# маркеры точек
             )
 
    ax.plot(datax3, datay3, #массивы "X" и "Y"
             linestyle=' ', linewidth=3, color=colors[2], alpha=0.9, # линия и МАРКЕРЫ
             marker='o', markersize=2, markerfacecolor=colors[2], markeredgewidth=2, markeredgecolor=colors[2],# маркеры точек
             )



    #ax.annotate("p-value ={0}".format(pvalue), xy = (0.21, 0.005), xytext=(0.15, 2), # печать значения p-value  
    #        arrowprops=dict(facecolor='black',                                   # рисуем кривую стрелку
    #                        arrowstyle='->', 
    #                        connectionstyle='angle3,angleA=-60,angleB=40'))
    
 
    ax.annotate("$w_{1}=0$", fontsize=13, xytext=(6.9,2.2),# координаты надписи и Начала Стрелки 
                                          xy = (5.3, 4.6), # координаты окончания стрелки
                arrowprops=dict(facecolor='black',                                   # рисуем кривую стрелку
                           arrowstyle='->'))  #, 
                           #connectionstyle='angle3,angleA=0,angleB=1000'))#искревление стрелки
    #ax.arrow_patch.set_color("gold")
    ax.annotate("$w_{1}=-0.15$", fontsize=13, xytext=(8.8,3.4),# координаты надписи и Начала Стрелки 
                                          xy = (7.9, 5.0), # координаты окончания стрелки
                color=colors[10],
                arrowprops=dict(color=colors[10],                                   # рисуем кривую стрелку
                           arrowstyle='->'))  #, 
                           #connectionstyle='angle3,angleA=0,angleB=1000'))#искревление стрелки    



    ax.annotate("$w_{1}=-0.27$", fontsize=13, xytext=(1.7,6.9),# координаты надписи и Начала Стрелки 
                                          xy = (10.3, 5.0), # координаты окончания стрелки
                color=colors[2],
                arrowprops=dict(color=colors[2], # рисуем кривую стрелку
                           arrowstyle='->'))  #, 
                           #connectionstyle='angle3,angleA=0,angleB=1000'))#искревление стрелки  




    #ax.text (x=0.4, y=1.0, s="$B_{0}$", fontsize=13)
    #ax.text (x=1.4, y=2.9, s="$B_{1}$", fontsize=13)
    #ax.text (x=4.2, y=2.9, s="$B_{2}$", fontsize=13)  
    #ax.text (x=3.2, y=1.0, s="$B_{3}$", fontsize=13)
    
    
    #plt.text (x=20, y=71, s="Mu_real_mean=%.1f" %mean_observed, fontsize=14) 
    #plt.text (x=20, y=68, s="Std_real = %.1f" %std_observed, fontsize=14) 
    #ax.plot(n, (Alf_samples[:,1]+0), #массивы "X" и "Y"
    #         linestyle='-', linewidth=0.3, color=colors[6], alpha=0.9, # линия и МАРКЕРЫ
    #         marker='o', markersize=5, markerfacecolor=colors[10], markeredgewidth=1, markeredgecolor=colors[10],# маркеры точек
    #         label=labels[1], zorder=2)
    
    
    
    
    ax.set_xlabel("ось Х")
    ax.set_ylabel("ось Y")
    #ax.set_title("Сэмплы " + chr(945) +"$_{i}$,  " + chr(945) +
    #            "$_{i+1}$"+f"  ,(i={0})",fontsize=16)
    ax.set_title(Title)
    #ax.set_title("1234")

    
    #ax.legend(loc="lower right")
    #ax.legend(loc="upper left")
    #ax.legend(loc="upper right",  fontsize=10)
    #ax.legend(loc="lower left")
    
    
    
    ax.set_xlim(x_min, x_max);#"-2" - всё Верно !!! SM
    ax.set_ylim(y_min, y_max);
    
    ax.grid(True, ls=':', c=colors[6],alpha=0.3, zorder=0 )
    plt.show()
    
    #print("** From plot_trace_1_1_1 **")

    #print("-1-1-1-1  -", end="")
    #print("56")
                
               
    return
    

#***********************************************************************************
#***********************************************************************************   



#***********************************************************************************
#***********************************************************************************    
def plot_Trace_31_Lines_3 (datax, datay, datax1, datay1, datax2, datay2, datax3, datay3, y_min, y_max, x_min, x_max,
                Title, labels_legend1, labels_legend2):
    
    
    
    #fig, ax = plt.subplots()
    #figsize(23, 5)
    # Размер Графиков Одинаковый для всех - Здается в Графике 0.
    fig, ax = plt.subplots(figsize=(6.0, 3)) # ДВА графика. Это  Одна строка и ДВА столбца = 2 Графика 
                                  # Если только ОДИН график, то вместо axesх[0] везде будет ax и fig, ax = plt.subplots()
    #plt.figsize(23, 5)
    labels = ["σ" +"$_{i}$", # в этом графике не используется
              chr(945) +"$_{i+1}$",
              "Banner_2",
               "123",
               "456",
              ]
    n= np.size(datax)
    
#    if (nx_max>n): 
#        print("**!!!************ ")
#        print("**!!!  nx_max>n  **!!!")
#        print("**!!!************ ")
#        stop
#    else:
#        pass
    
                    
    
#    data1=data[nx_min:nx_max]
#    n1= np.arange(np.size(data1))


    ax.set_facecolor(colors[11])

    
    ax.plot(datax, datay, #массивы "X" и "Y"
             linestyle='-', linewidth=0.3, color=colors[6], alpha=0.9, # линия и МАРКЕРЫ
             marker='o', markersize=8, markerfacecolor=colors[12], markeredgewidth=2, markeredgecolor=colors[6],# маркеры точек
             #label=labels_legend1, zorder=2)
             )
    ax.plot(datax1, datay1, #массивы "X" и "Y"
             linestyle='-', linewidth=2, color=colors[6], alpha=0.9, # линия и МАРКЕРЫ
             marker=' ', markersize=3, markerfacecolor=colors[12], markeredgewidth=2, markeredgecolor=colors[6],# маркеры точек
             #label=labels_legend2, zorder=2)
             )

    ax.plot(datax2, datay2, #массивы "X" и "Y"
             linestyle='--', linewidth=2, color=colors[10], alpha=0.9, # линия и МАРКЕРЫ
             marker=' ', markersize=3, markerfacecolor=colors[10], markeredgewidth=2, markeredgecolor=colors[10],# маркеры точек
             )
 
    ax.plot(datax3, datay3, #массивы "X" и "Y"
             linestyle=' ', linewidth=3, color=colors[2], alpha=0.9, # линия и МАРКЕРЫ
             marker='o', markersize=2, markerfacecolor=colors[2], markeredgewidth=2, markeredgecolor=colors[2],# маркеры точек
             )



    #ax.annotate("p-value ={0}".format(pvalue), xy = (0.21, 0.005), xytext=(0.15, 2), # печать значения p-value  
    #        arrowprops=dict(facecolor='black',                                   # рисуем кривую стрелку
    #                        arrowstyle='->', 
    #                        connectionstyle='angle3,angleA=-60,angleB=40'))
    
 
    ax.annotate("$Кратность=1$", fontsize=13, xytext=(0.3,-0.2),# координаты надписи и Начала Стрелки 
                                          xy = (2.0, 4.1), # координаты окончания стрелки
                arrowprops=dict(facecolor='black',                                   # рисуем кривую стрелку
                           arrowstyle='->'))  #, 
                           #connectionstyle='angle3,angleA=0,angleB=1000'))#искревление стрелки
    #ax.arrow_patch.set_color("gold")
    ax.annotate("$Кратность=2$", fontsize=13, xytext=(2.2,1.4),# координаты надписи и Начала Стрелки 
                                          xy = (2.8, 8.0), # координаты окончания стрелки
                color=colors[10],
                arrowprops=dict(color=colors[10],                                   # рисуем кривую стрелку
                           arrowstyle='->'))  #, 
                           #connectionstyle='angle3,angleA=0,angleB=1000'))#искревление стрелки    



    ax.annotate("$Кратность=3$", fontsize=13, xytext=(5.0,8.5),# координаты надписи и Начала Стрелки 
                                          xy = (3.3, 8.5), # координаты окончания стрелки
                color=colors[2],
                arrowprops=dict(color=colors[2], # рисуем кривую стрелку
                           arrowstyle='->'))  #, 
                           #connectionstyle='angle3,angleA=0,angleB=1000'))#искревление стрелки  




    #ax.text (x=0.4, y=1.0, s="$B_{0}$", fontsize=13)
    #ax.text (x=1.4, y=2.9, s="$B_{1}$", fontsize=13)
    #ax.text (x=4.2, y=2.9, s="$B_{2}$", fontsize=13)  
    #ax.text (x=3.2, y=1.0, s="$B_{3}$", fontsize=13)
    
    
    #plt.text (x=20, y=71, s="Mu_real_mean=%.1f" %mean_observed, fontsize=14) 
    #plt.text (x=20, y=68, s="Std_real = %.1f" %std_observed, fontsize=14) 
    #ax.plot(n, (Alf_samples[:,1]+0), #массивы "X" и "Y"
    #         linestyle='-', linewidth=0.3, color=colors[6], alpha=0.9, # линия и МАРКЕРЫ
    #         marker='o', markersize=5, markerfacecolor=colors[10], markeredgewidth=1, markeredgecolor=colors[10],# маркеры точек
    #         label=labels[1], zorder=2)
    
    
    
    
    ax.set_xlabel("ось Х")
    ax.set_ylabel("ось Y")
    #ax.set_title("Сэмплы " + chr(945) +"$_{i}$,  " + chr(945) +
    #            "$_{i+1}$"+f"  ,(i={0})",fontsize=16)
    ax.set_title(Title)
    #ax.set_title("1234")

    
    #ax.legend(loc="lower right")
    #ax.legend(loc="upper left")
    #ax.legend(loc="upper right",  fontsize=10)
    #ax.legend(loc="lower left")
    
    
    
    ax.set_xlim(x_min, x_max);#"-2" - всё Верно !!! SM
    ax.set_ylim(y_min, y_max);
    
    ax.grid(True, ls=':', c=colors[6],alpha=0.3, zorder=0 )
    plt.show()
    
    #print("** From plot_trace_1_1_1 **")

    #print("-1-1-1-1  -", end="")
    #print("56")
                
               
    return
    

#***********************************************************************************
#***********************************************************************************   



#***********************************************************************************
#***********************************************************************************    
def plot_Trace_32_Lines_3 (datax, datay, datax1, datay1, datax2, datay2, 
                           datax3, datay3, datax4, datay4,
                           y_min, y_max, x_min, x_max,
                Title, labels_legend1, labels_legend2,
                labels_legend3, labels_legend4,labels_legend5):
    
    
    
    #fig, ax = plt.subplots()
    #figsize(23, 5)
    # Размер Графиков Одинаковый для всех - Здается в Графике 0.
    fig, ax = plt.subplots(figsize=(9.0, 5)) # ДВА графика. Это  Одна строка и ДВА столбца = 2 Графика 
                                  # Если только ОДИН график, то вместо axesх[0] везде будет ax и fig, ax = plt.subplots()
    #plt.figsize(23, 5)
    labels = ["σ" +"$_{i}$", # в этом графике не используется
              chr(945) +"$_{i+1}$",
              "Banner_2",
               "123",
               "456",
              ]
    n= np.size(datax)
    
#    if (nx_max>n): 
#        print("**!!!************ ")
#        print("**!!!  nx_max>n  **!!!")
#        print("**!!!************ ")
#        stop
#    else:
#        pass
    
                    
    
#    data1=data[nx_min:nx_max]
#    n1= np.arange(np.size(data1))


    ax.set_facecolor(colors[11])

    
    ax.plot(datax, datay, #массивы "X" и "Y"
             linestyle='-', linewidth=0.3, color=colors[6], alpha=0.9, # линия и МАРКЕРЫ
             marker='o', markersize=8, markerfacecolor=colors[12], markeredgewidth=2, markeredgecolor=colors[6],# маркеры точек
             label=labels_legend1, zorder=2)
             
    ax.plot(datax1, datay1, #массивы "X" и "Y"
             linestyle='-', linewidth=2, color=colors[6], alpha=0.9, # линия и МАРКЕРЫ
             marker=' ', markersize=3, markerfacecolor=colors[12], markeredgewidth=2, markeredgecolor=colors[6],# маркеры точек
             label=labels_legend2, zorder=2)
             

    ax.plot(datax2, datay2, #массивы "X" и "Y"
             linestyle='--', linewidth=2, color=colors[10], alpha=0.9, # линия и МАРКЕРЫ
             marker=' ', markersize=3, markerfacecolor=colors[10], markeredgewidth=2, markeredgecolor=colors[10],# маркеры точек
             label=labels_legend3, zorder=2)
 
    ax.plot(datax3, datay3, #массивы "X" и "Y"
             linestyle=' ', linewidth=3, color=colors[2], alpha=0.9, # линия и МАРКЕРЫ
             marker='o', markersize=2, markerfacecolor=colors[2], markeredgewidth=2, markeredgecolor=colors[2],# маркеры точек
             label=labels_legend4, zorder=2)

    ax.plot(datax4, datay4, #массивы "X" и "Y"
             linestyle=' ', linewidth=3, color=colors[4], alpha=0.9, # линия и МАРКЕРЫ
             marker='o', markersize=2, markerfacecolor=colors[4], markeredgewidth=2, markeredgecolor=colors[4],# маркеры точек
             label=labels_legend5, zorder=2)




    #ax.annotate("p-value ={0}".format(pvalue), xy = (0.21, 0.005), xytext=(0.15, 2), # печать значения p-value  
    #        arrowprops=dict(facecolor='black',                                   # рисуем кривую стрелку
    #                        arrowstyle='->', 
    #                        connectionstyle='angle3,angleA=-60,angleB=40'))
    
 
    ax.annotate("$Степень=1$", fontsize=13, xytext=(5.0, 1.2),# координаты надписи и Начала Стрелки 
                                          xy = (8.5, 6.3), # координаты окончания стрелки
                arrowprops=dict(facecolor='black',                                   # рисуем кривую стрелку
                           arrowstyle='->'))  #, 
                           #connectionstyle='angle3,angleA=0,angleB=1000'))#искревление стрелки
    #ax.arrow_patch.set_color("gold")
    ax.annotate("$Степень=2$", fontsize=13, xytext=(-0.9,12.0),# координаты надписи и Начала Стрелки 
                                          xy = (3.6, 10.0), # координаты окончания стрелки
                color=colors[10],
                arrowprops=dict(color=colors[10],                                   # рисуем кривую стрелку
                           arrowstyle='->'))  #, 
                           #connectionstyle='angle3,angleA=0,angleB=1000'))#искревление стрелки    



    ax.annotate("$Степень=3$", fontsize=13, xytext=(15.0,11.5),# координаты надписи и Начала Стрелки 
                                          xy = (13.7, 9.5), # координаты окончания стрелки
                color=colors[2],
                arrowprops=dict(color=colors[2], # рисуем кривую стрелку
                           arrowstyle='->'))  #, 
                           #connectionstyle='angle3,angleA=0,angleB=1000'))#искревление стрелки  
                           
    ax.annotate("$Степень=6$", fontsize=13, xytext=(9.0,2.6),# координаты надписи и Начала Стрелки 
                                          xy = (13.4, 7.2), # координаты окончания стрелки
                color=colors[4],
                arrowprops=dict(color=colors[4], # рисуем кривую стрелку
                           arrowstyle='->'))  #, 
                           #connectionstyle='angle3,angleA=0,angleB=1000'))#искревление стрелки  




    #ax.text (x=0.4, y=1.0, s="$B_{0}$", fontsize=13)
    #ax.text (x=1.4, y=2.9, s="$B_{1}$", fontsize=13)
    #ax.text (x=4.2, y=2.9, s="$B_{2}$", fontsize=13)  
    #ax.text (x=3.2, y=1.0, s="$B_{3}$", fontsize=13)
    
    
    #plt.text (x=20, y=71, s="Mu_real_mean=%.1f" %mean_observed, fontsize=14) 
    #plt.text (x=20, y=68, s="Std_real = %.1f" %std_observed, fontsize=14) 
    #ax.plot(n, (Alf_samples[:,1]+0), #массивы "X" и "Y"
    #         linestyle='-', linewidth=0.3, color=colors[6], alpha=0.9, # линия и МАРКЕРЫ
    #         marker='o', markersize=5, markerfacecolor=colors[10], markeredgewidth=1, markeredgecolor=colors[10],# маркеры точек
    #         label=labels[1], zorder=2)
    
    
    
    
    ax.set_xlabel("ось Х")
    ax.set_ylabel("ось Y")
    #ax.set_title("Сэмплы " + chr(945) +"$_{i}$,  " + chr(945) +
    #            "$_{i+1}$"+f"  ,(i={0})",fontsize=16)
    ax.set_title(Title)
    #ax.set_title("1234")

    
    ax.legend(loc="lower right")
    #ax.legend(loc="upper left")
    #ax.legend(loc="upper right",  fontsize=10)
    #ax.legend(loc="lower left")
    
    
    
    ax.set_xlim(x_min, x_max);#"-2" - всё Верно !!! SM
    ax.set_ylim(y_min, y_max);
    
    ax.grid(True, ls=':', c=colors[6],alpha=0.3, zorder=0 )
    plt.show()
    
    #print("** From plot_trace_1_1_1 **")

    #print("-1-1-1-1  -", end="")
    #print("56")
                
               
    return
    

#***********************************************************************************
#***********************************************************************************   
