import numpy as np
from PIL import Image

# ---- IGNORE THIS PART -----------------------------------------
def load_image(filename, new_width=140):
    image = Image.open(filename)
    width, height = image.size
    aspect_ratio = height/width
    new_height = aspect_ratio * new_width * 0.45
    return np.array(image.resize((new_width, int(new_height))))
# ---- IGNORE THIS PART -----------------------------------------

 
def min_max_scaling(array):
    # aus Aufgabe 1 kopieren, wenn fertig und funktionsfähig
    norm_arr = (array-np.min(array)) / (np.max(array)-np.min(array))
    return norm_arr

def get_numpy_array_infos(array):
    # aus Aufgabe 1 kopieren, wenn fertig und funktionsfähig
    print(array.dtype)
    print(array.size)
    print(array.shape)
    print(np.min(array))
    print(np.max(array))
    pass


def image_to_grayscale(image):
    new_arr = np.empty((image.shape[0],image.shape[1]))
    for x in range(len(image)):
        for y in range(len(image[x])):
            pixel = image[x][y]
            avg = (int(pixel[0]) + int(pixel[1] + int(pixel[2]))) // 3
            new_arr[x][y] = avg
    
    
    return new_arr
        
def image_to_ascii(image):
    chars = ["@", "B", "&", "#", "S", "$", "%", "p", "o", "*", "!", ";", ":", ".", " "]
    num_chars = len(chars)
    image_ascii = ""
    
    # hier euer Code vom Bild als Numpy-Array zum ASCII-Bild als String
    
    #Informationen zu dem Array ausgeben lassen über die Funktion aus Aufgabe 1.2
    get_numpy_array_infos(image)
    
    #Konvertiere zu einem Graustufenbild über die Funktion aus Aufgabe 2.1
    gray_image = image_to_grayscale(image)
    
    #Normieren des Arrays über die Funktion aus Aufgabe 1.3
    gray_image=min_max_scaling(gray_image)
    print(gray_image)
    #Erneut die Informationen des vorbearbeitenden Arrays ausgeben und vergleichen
    print("Old Array:")
    get_numpy_array_infos(image)
    print("New Array:")
    get_numpy_array_infos(gray_image)    
    
    #Konvertierung jedes Pixelwerts zu einem bestimmten Zeichen
    
    
    
    #Zuweisung Zeichen
    for x in gray_image:
         
        for pixel in x:
            i=int(pixel * (num_chars-1))
            image_ascii+= chars[i]
        image_ascii+="\n"
    
    
    #Ausgabe    
    print(image_ascii)
    pass
    


# Die Bilddatei muss im gleichen Ordner wie das Pythonskript sein
filename = "/home/sven/code/Pra_4/ProgDSKI-Praktikum-main/Pra_4/bike.png"
# Das Bild wird in die Variable image als NumPy-Array gelade 
image = load_image(filename,100)




"""Main"""
image_to_ascii(image)
