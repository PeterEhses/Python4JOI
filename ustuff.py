import numpy as np
import umap
import pickle
import glob
import time
import socket
from scipy.spatial.distance import cdist
maximum_imgs = 20480

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port

def closest_node(node, nodes):
    swap = cdist(nodes, [node])
    print(swap)
    return np.argmin(swap)
    #return nodes[cdist([node], nodes).argmin()]

#make model

#das passiert immer also braucht es keine funktion?
print("init")
lasttime = time.time()
fit = umap.UMAP(n_neighbors=15, random_state=42, metric='euclidean')
print("loading vecs")
print( "---%s seconds---" % (time.time()-lasttime))
lasttime = time.time()
image_vectors = pickle.load( open( "imagevec.pickle", "rb" ) )
print("loaded, fitting")
print( "---%s seconds---" % (time.time()-lasttime))
lasttime = time.time()
u = fit.fit_transform(image_vectors)
print("fit, loading vecset")
print( "---%s seconds---" % (time.time()-lasttime))
lasttime = time.time()


#internet zeug das ich nicht verstehe
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
print("host started")
while True:
    try:
        print("trying connection")
        s.listen(1)
        conn, addr = s.accept()
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            
            if not data: break
            print("starting analysis")

            #fit relevant set
            vecsel = pickle.load( open( "vecset.pickle", "rb" ) )

            #print("loaded, loading new vector")
            #print( "---%s seconds---" % (time.time()-lasttime))
            lasttime = time.time()
            new_vec = glob.glob('image_vectors/*.npz')[:maximum_imgs]

            for c, i in enumerate(new_vec):
                vecsel.append(np.loadtxt(i))
            print("loaded, transforming new set")
            #print( "---%s seconds---" % (time.time()-lasttime))
            #lasttime = time.time()
            newset = fit.transform(vecsel)
            ##print("done")
            ##print( "---%s seconds---" % (time.time()-lasttime))
            ##lasttime = time.time()
            ##print(newset)




            n_img = newset[len(newset)-1]
            newset = newset[:-1]
            result = closest_node(n_img, newset)
            print( "---%s seconds---" % (time.time()-lasttime))
            lasttime = time.time()
            print(result)
            f = open("./Full Attribute Scores/target-filenames.txt","r")
            lines = f.read()
            line_ar = lines.split("\n")
            output = []
            for x in line_ar:
              temp = x.split(",")
              output.append(temp[1])
            print(output[result-1])




            
            #print(data) # Paging Python!
            # do whatever you need to do with the data
            conn.sendall(bytes(output[result-1], 'utf-8'))
            #break
        conn.close()
    except:
        print("Connection idk")


