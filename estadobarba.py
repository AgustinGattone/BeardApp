import random

barba_list = ['Afeitada', 'Sin afeitar']

def estado_barba():
    barba_item = random.choice(barba_list)
    print ("La barba este mes", barba_item)
