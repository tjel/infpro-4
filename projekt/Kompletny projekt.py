#!/usr/bin/python

from easygui import *
import sys
from numpy import *

def silnia(n):
	if n == 1:
		return 1
	elif n == 0:
		return 1
#Technicznie, silnia z ujemnej liczby to ujemna nieskonczonosc,
#ale bedziemy korzystac w naszych dzialaniach
	
	elif n < 0:
		return -100000000000000.0
	else:
		return n * silnia(n-1)

while 1:
	msg ="Ktora opcje wybierasz?"
	title = "Wybierz sciezke"
	choices = ["j,m", "m1,m2"]
	choice = choicebox(msg, title, choices)
	if choice != None:
		pass
	else:
		sys.exit(0)
	
	if choice == "j,m":
		msg = "Podaj liczby"
		title = "Clebsch-Gordan kalkulator"
		fieldNames = ["j1","j2","j","m"]
		fieldValues = []  # startujemy z pustymi wartosciami
		fieldValues = multenterbox(msg,title, fieldNames)
		# upewnij sie ze pola nie zostaly puste
		while 1:
			if fieldValues == None: break
			errmsg = ""
			for i in range(len(fieldNames)):
				if fieldValues[i].strip() == "":
					errmsg = errmsg + ('"%s" jest puste.\n\n' % fieldNames[i])
			if errmsg == "": break # nie znaleziono bledow
			fieldValues = multenterbox(errmsg, title, fieldNames, fieldValues)
	
		#Wybieramy liczby kwantowe od uzytkownika, definujac przy tym warunki
		
		j1=float(fieldValues[0])
		j2=float(fieldValues[1])
		j=float(fieldValues[2])
		m=float(fieldValues[3])
		z=0
		a=0.0
		b=0.0
		c=0.0
		l=""
		#Najpierw sprawdzamy warunki liczbowe
		if abs(m)>j:
			print "Przepraszamy ale |m| jest wieksze j"
		elif (j1+j2)<j:
			print "Przepraszamy ale j jest w zlej relacji."
		elif abs(j1-j2)>j:
			print "Przepraszamy ale j jest w zlej relacji."
		#Glowny program, ktory oblicza wspolrzedne Clebscha-Gordana.
		else:
			for m1 in arange(-j1-1,(j1+1)):
			
				for m2 in arange(-j2-1,(j2+1)):
		#Warunki ktore musza dac 0.			
					if (m1+m2) != m:
						d=0
					elif (j1-j2-m)%1!=0.0:
						d=0
					elif (j1-j2+m)%1!=0.0:
						d=0
					else:
						c=0.0
						z=0
		#Algorytm rownan.				
						a=((silnia(j1+j2-j)*silnia(j1-j2+j)*silnia(-j1+j2+j))/(silnia(j1+j2+j+1.0)))**.5
						b=(silnia(j1+m1)*silnia(j1-m1)*silnia(j2+m2)*silnia(j2-m2)*silnia(j-m)*silnia(j+m))**.5
						while z<(j1-m1+3):
			
							c+=((-1.0)**(z+j1-j2+m))/(silnia(z)*silnia(j1+j2-j-z)*silnia(j1-m1-z)*silnia(j2+m2-z)*silnia(j-j2+m1+z)*silnia(j-j1-m2+z))
							z+=1
						d=((-1.0)**(j1-j2+m))*((2.0*j+1.0)**.5)*a*b*c
						if abs(d)> .0001:
							l+= "\n|"+str(m1)+str(m2)+">"+str(d)
		msgbox(l,"Wynik")
	elif choice == "m1,m2":
		msg = "Podaj liczby"
		title = "Clebsch-Gordan kalkulator"
		fieldNames = ["j1","j2","m1","m2"]
		fieldValues = []  # Startujemy z pustymi polami
		fieldValues = multenterbox(msg,title, fieldNames)
		# upewniamy sie ze zadne pole nie zostalo puste
		while 1:
			if fieldValues == None: break
			errmsg = ""
			for i in range(len(fieldNames)):
				if fieldValues[i].strip() == "":
					errmsg = errmsg + ('"%s" jest puste.\n\n' % fieldNames[i])
			if errmsg == "": break # nie znaleziono problemow
			fieldValues = multenterbox(errmsg, title, fieldNames, fieldValues)
	
		#Pobieramy liczby kwantowe od uzytkownika, definiujac warunki
		j1=float(fieldValues[0])
		j2=float(fieldValues[1])
		m1=float(fieldValues[2])
		m2=float(fieldValues[3])
		z=0
		a=0.0
		b=0.0
		c=0.0
		l=""
		
		
		#Glowny program, ktory oblicza wspolrzedne
		for j in arange(abs(j1-j2)-1,(j1+j2)+1):
		
			for m in arange(-j-1,j+2):
			
		#Definiujemy warunki, ktore musza wynosic 0		
				if abs(m)>j:
					d=0
                                elif (m1+m2)!= m:
					d=0
				elif (j1-j2-m)%1!=0.0:
					d=0
				elif (j1-j2+m)%1!=0.0:
					d=0
				else:
				
					c=0.0
					z=0
		#Algorytm, nie jest zgrabny, ale dziala
					a=((silnia(j1+j2-j)*silnia(j1-j2+j)*silnia(-j1+j2+j))/(silnia(j1+j2+j+1.0)))**.5
					b=(silnia(j1+m1)*silnia(j1-m1)*silnia(j2+m2)*silnia(j2-m2)*silnia(j+m)*silnia(j-m))**.5
					while z<(j1-m1+3):
			
						c+=((-1.0)**(z+j1-j2+m))/(silnia(z)*silnia(j1+j2-j-z)*silnia(j1-m1-z)*silnia(j2+m2-z)*silnia(j-j2+m1+z)*silnia(j-j1-m2+z))
						z+=1
					d=(-1.0)**(j1-j2+m)*(2.0*j+1.0)**.5*a*b*c	
					if abs(d)> .0001:
						l+= "\n|"+str(j)+str(m)+">"+str(d)
		msgbox(l,"Wynik")
