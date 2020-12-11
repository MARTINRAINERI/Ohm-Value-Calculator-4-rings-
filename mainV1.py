
from tkinter import *
from tkinter import ttk


####Building

root = Tk()
root.geometry('1500x750')
root.title('Ohm Value Calculator')
root.resizable(0,0)

#### Functions







###Widgets

#background

main_canvas = Canvas(root, height = 750, width =1500, bg ='#527CB3')
main_canvas.place(x=0,y=0)

quit_button = Button(root, text = 'Close',font = ('Calibri', '15', 'bold'),fg = 'white',bg ='#A11A56',overrelief = 'groove',height = 1 , width = 10, command = root.destroy)
quit_button.place(x = 695, y = 670)

frame_l = Frame(root, height = 450, width = 680, bg ='#62B0F0')
frame_l.place(x=10,y=200)

frame_r = Frame(root, height = 450, width = 680, bg ='#62B0F0')
frame_r.place(x=810,y=200)



label_1 = Label(root, text = ' Welcome to the Ohm Value Calculator, how can I help you ? ', font = ('Calibri', '28', 'bold'), bg ='#527CB3', fg='#FFFFFF')
label_1.place(x = 300, y= 30)
label_1_b = Label(root, text = ' ( 4 rings version ) ', font = ('Calibri', '28', 'bold'), bg ='#527CB3', fg='#FFFFFF')
label_1_b.place(x = 600, y= 70)


#Left Part : Value to color code

def trigger_VTCC():
    value = spinbox.get()
    if float(value) >= 0.01:
        frame_l = Frame(root, height = 100, width = 650, bg ='#62B0F0')
        frame_l.place(x=40,y=450)
        result = ValueToColor(float(value))
        label_result = Label(root, text = result+'\n for the first 3 rings', font = ('Calibri', '20', 'bold'), bg ='#62B0F0', fg='#FFFFFF')
        label_result.place(x = 120, y= 450)
    elif float(value) < 0.01:
        frame_l = Frame(root, height = 100, width = 650, bg ='#62B0F0')
        frame_l.place(x=40,y=450)
        label_result = Label(root, text = 'Please enter a value above 0.01', font = ('Calibri', '20', 'bold'), bg ='#62B0F0', fg='#FFFFFF')
        label_result.place(x = 120, y= 450)

label_2 = Label(root, text = 'Give me the value you are looking for , I will\n  tell you  the color code you need', font = ('Calibri', '20', 'bold'), bg ='#62B0F0', fg='#FFFFFF')
label_2.place(x = 70, y= 200)

label_3 = Label(root, text = 'Your value : ', font = ('Calibri', '15', 'bold'), bg ='#62B0F0', fg='#FFFFFF')
label_3.place(x = 120, y= 343)

left_btn = Button(root, text = 'submit',font = ('Calibri', '15'),bg ='#62B0F0', fg='#FFFFFF',overrelief = 'groove',height = 1, command = trigger_VTCC)
left_btn.place(x = 400, y= 340)


spinbox = Spinbox(root,bg = '#FFFFFF', from_ = 0.01,to = 99000000000 , wrap = True, width =12)
spinbox.place(x = 260, y= 350,)



#Right part : Color code to value

def trigger_CCTV():
    first_value = first.get()
    second_value = second.get()
    third_value = third.get()
    fourth_value = fourth.get()
    value = ColourToValue(first_value,second_value,third_value,fourth_value)[0]
    tolerance = ColourToValue(first_value,second_value,third_value,fourth_value)[1]
    frame_r = Frame(root, height = 100, width = 630, bg ='#62B0F0')
    frame_r.place(x=830,y=500)
    label_result_1 = Label(root, text = 'The value of your resistance is : '+value+' Ohm , ', font = ('Calibri', '18', 'bold'), bg ='#62B0F0', fg='#FFFFFF')
    label_result_1.place(x = 830, y= 500)
    label_result_2 = Label(root, text = 'with a tolerance of '+tolerance+' % . ', font = ('Calibri', '18', 'bold'), bg ='#62B0F0', fg='#FFFFFF')
    label_result_2.place(x = 830, y= 535)

label_4 = Label(root, text = 'Give me a color code,\n I will tell you  the value of your resistance (in Ohms)', font = ('Calibri', '20', 'bold'), bg ='#62B0F0', fg='#FFFFFF')
label_4.place(x = 850, y= 200)

label_first = Label(root, text = 'First ring', font = ('Calibri', '18','bold'), bg ='#62B0F0', fg='#FFFFFF')
label_first.place(x = 851, y= 315)

first = ttk.Combobox(root,values = ['brown', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'grey', 'white'])
first.place(x= 830, y = 350)

label_second = Label(root, text = 'Second ring', font = ('Calibri', '18','bold'), bg ='#62B0F0', fg='#FFFFFF')
label_second.place(x = 1006, y= 315)

second = ttk.Combobox(root,values = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'grey', 'white'])
second.place(x= 995, y = 350)

label_third = Label(root, text = 'Third ring', font = ('Calibri', '18','bold'), bg ='#62B0F0', fg='#FFFFFF')
label_third.place(x = 1180, y= 315)

third = ttk.Combobox(root,values = ['silver', 'gold', 'black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'grey', 'white'])
third.place(x= 1160, y = 350)

label_fourth = Label(root, text = 'Fourth ring', font = ('Calibri', '18','bold'), bg ='#62B0F0', fg='#FFFFFF')
label_fourth.place(x = 1330, y= 315)

fourth = ttk.Combobox(root,values = ['none', 'silver', 'gold', 'brown', 'red', 'green', 'blue', 'purple', 'grey'])
fourth.place(x= 1320, y = 350)

right_btn = Button(root,text = 'submit',font = ('Calibri', '15'),bg ='#62B0F0', fg='#FFFFFF',overrelief = 'groove',height = 1, command = trigger_CCTV )
right_btn.place(x = 1115, y= 430)

#Interaction widgets


### Main loop

root.mainloop()


### Main functions (adapted for the GUI)
table = [['none',0,0,0,20],['silver',0,0,0.01,10],['gold',0,0,0.1,5],['black',0,0,1,0],['brown',1,1,10,1],['red',2,2,100,2],['orange',3,3,1000,0],['yellow',4,4,10000,0],['green',5,5,100000,0.5],['blue',6,6,1000000,0.25],['purple',7,7,10000000,0.1],['grey',8,8,100000000,0.05],['white',9,9,1000000000,0]]

colours = []
first_ring_options=[]
second_ring_options=[]
third_ring_options=[]
fourth_ring_options=[]

for i in range(len(table)):
    colours.append(table[i][0])

for i in range(4,len(table)):
    first_ring_options.append(table[i][0])

for i in range(3,len(table)):
    second_ring_options.append(table[i][0])

for i in range(1,len(table)):
    third_ring_options.append(table[i][0])

for i in [0,1,2,4,5,8,9,10,11]:
    fourth_ring_options.append(table[i][0])

def ValueToColor(value):
    if value >= 100:
        power = 0
        while value > 100:
            value = value/10
            power += 1
        first = int(value//10)
        second = int((value%10)//1)
        first_ring_color = first_ring_options[first-1]
        second_ring_color = second_ring_options[second]
        third_ring_color = third_ring_options[power+2]
        return('The color code will be : '+first_ring_color+', '+second_ring_color+', '+third_ring_color+' ')
    elif value<10:
        power = 0
        while value < 10:
            value = value*10
            power += 1
        first = int(round(value)//10)
        second = int((round(value)%10)//1)
        first_ring_color = first_ring_options[first-1]
        second_ring_color = second_ring_options[second]
        third_ring_color = third_ring_options[power-2]
        return('The color code will be : '+first_ring_color+', '+second_ring_color+', '+third_ring_color+'')
    elif value < 100 and value >= 10:
    #here it is quite simpler since we directly get the digits
        first = int(round(value)//10)
        second = int((round(value)%10)//1)
        first_ring_color = first_ring_options[first-1]
        second_ring_color = second_ring_options[second]
        third_ring_color = 'none'
        return('The color code will be : '+first_ring_color+', '+second_ring_color+', '+third_ring_color+' ')

def ColourToValue(ring1,ring2,ring3,ring4):
    first_digit = table[colours.index(ring1)][1]
    second_digit = table[colours.index(ring2)][2]
    third_digit = table[colours.index(ring3)][3]
    fourth_digit = table[colours.index(ring4)][4]
    value = str((first_digit*10+second_digit)*third_digit)
    tolerance = str(fourth_digit)
    return(value,tolerance)


