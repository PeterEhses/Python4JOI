import numpy as np
import glob, json, os, pickle

# create datastores
image_vectors = []
vector_set = []
second_image = []
chart_data = []
maximum_imgs = 20480
output = []
# build a list of image vectors
vector_files = glob.glob('image_vectors_predefined/*.npz')[:maximum_imgs]
number = 0
number2 = 0

f = open("./Full Attribute Scores/target-filenames.txt","r")
lines = f.read()
line_ar = lines.split("\n")
for x in line_ar:
  temp = x.split(",")
  output.append(temp[1])
print(output)

for c, i in enumerate(vector_files):
  if number < 100:
    number += 1
  else:
    number = 0
    number2 += 100
    print(' * loaded',number2, ' of ', len(vector_files), 'image vectors')
  
  image_vectors.append(np.loadtxt(i))
  istrip = i[:-4]
  istrip = istrip[25:]
  if istrip in output:
      #print(istrip)
      vector_set.append(np.loadtxt(i))
  #print(' * loaded', c+1, 'of', len(vector_files), 'image vectors')

with open('imagevec.pickle', 'wb') as handle:
    pickle.dump(image_vectors, handle, protocol=pickle.HIGHEST_PROTOCOL)
with open('vecset.pickle', 'wb') as handle:
    pickle.dump(vector_set, handle, protocol=pickle.HIGHEST_PROTOCOL)
