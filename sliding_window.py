import numpy as np
from PIL import Image #i will not use it here
px=8
pic=np.linspace(1,px*px,px*px).reshape(px,px) #i will use just numbers for demonstration


def sliding_window(pic,w_size,step): #pic matrix after covertiog it to numpy array, size of the window, step size
	w_sizeo=w_size      #window original size
	w_size=w_size-1

	vector=pic.ravel()    #covert the matrix into a vector , python preform better with liner iteration
	for j in range(0,pic.shape[0],step):  #will itrate the matrix lines 'after we convert it to vector'
		windo=[]                         #an array to contain the window pixels data
		for i in range(j,len(vector)-w_size,pic.shape[0]):   
			if float(i+w_size)%(pic.shape[0])<w_size:
				pass
			else:
				windo.append(vector[i:w_size+i+1])
				if np.array(windo).shape[0]==w_sizeo:
					print np.array(windo),'\n'
					windo=[]


sliding_window(pic,3,2)
