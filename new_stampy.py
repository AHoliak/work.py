
from tkinter import *
from random import randint

root = Tk()
root.title('pick a stampy winner')
root.iconbitmap('~/Desktop/stampy.ico')
root.geometry("400x400")
entries = ['Olha Grynenko', 'Mariia Scherban', 'Olha Kolomiets', 'Vladyslav Bartko', 'Anastasiia Boiko', 'Karyna Sych', 'Alina Iv', 'Sonya Kats', 'Iana Guzhyk', 'Roman Chuhan', 'Olya Savchenko', 'Inna Berezina', 'Liudmila Chepizhenko', 'Oleksandra Shvedova', 'Anastasiia Kozhema', 'Anton Kostiuchenko', 'Maryna Hoian', 'Tani Kusso', 'Viktoria Potemska', 'Luda Scherbinina', 'Yana Spivakova', 'Iryna Osipa', 'Ania Shkarlinska', 'Alina Melnychenko', 'Mykola Terelya', 'Marina Nikolaeva', 'Bohdan Syvolodskyi']
def pick():
	entries = ['Olha Grynenko', 'Mariia Scherban', 'Olha Kolomiets', 'Vladyslav Bartko', 'Anastasiia Boiko', 'Karyna Sych', 'Alina Iv', 'Sonya Kats', 'Iana Guzhyk', 'Roman Chuhan', 'Olya Savchenko', 'Inna Berezina', 'Liudmila Chepizhenko', 'Oleksandra Shvedova', 'Anastasiia Kozhema', 'Anton Kostiuchenko', 'Maryna Hoian', 'Tani Kusso', 'Viktoria Potemska', 'Luda Scherbinina', 'Yana Spivakova', 'Iryna Osipa', 'Ania Shkarlinska', 'Alina Melnychenko', 'Mykola Terelya', 'Marina Nikolaeva', 'Bohdan Syvolodskyi']
	our_number = len(entries)-1
	for i in range(2):
		rando = randint(0, our_number)
	winnerLabel = Label(root, text=entries[rando], font=("Helvetica", 18))
	winnerLabel.pack(pady=50)


topLabel = Label(root, text = "руській воєнний корабль іді на ...", font=("Helvetica", 24))
topLabel.pack(pady=20)
winButton = Button(root, text = "обрати нового власника марки", font=("Helvetica", 24), command=pick)
winButton.pack(pady=20)


root.mainloop()
