# create_tsne_projection.py
from MulticoreTSNE import MulticoreTSNE as TSNE
import numpy as np
import glob, json, os, pickle

# create datastores
image_vectors = []
second_image = []
chart_data = []
maximum_imgs = 20480

# build a list of image vectors
vector_files = glob.glob('image_vectors/*.npz')[:maximum_imgs]
number = 0
number2 = 0
for c, i in enumerate(vector_files):
  if number < 100:
    number += 1
  else:
    number = 0
    number2 += 100
    print(' * loaded',number2, ' of ', len(vector_files), 'image vectors')
  image_vectors.append(np.loadtxt(i))
  #print(' * loaded', c+1, 'of', len(vector_files), 'image vectors')

with open('imagevec.pickle', 'wb') as handle:
    pickle.dump(image_vectors, handle, protocol=pickle.HIGHEST_PROTOCOL)

single_vector = glob.glob('imagevector/*.npz')[:maximum_imgs]
for c, i in enumerate(single_vector):
  second_image.append(np.loadtxt(i))
  print(' * loaded', c+1, 'of', len(single_vector), 'second image vectors')

print('done loading')
# build the tsne model on the image vectors
modell = TSNE(n_jobs = 8, random_state=0)
print('model')
#np.set_printoptions(suppress=True)
print('suppress')
fit_model = modell.fit_transform( np.array(image_vectors) )
print('fitted')

# store the coordinates of each image in the chart data
for c, i in enumerate(fit_model):
  chart_data.append({
    'x': float(i[0]),
    'y': float(i[1]),
    'idx': c
  })

second_model = modell.fit_transform( np.array(second_image, ndmin=2))

for c, i in enumerate(second_model):
  print(i)
  chart_data.append({
    'x': float(i[0]),
    'y': float(i[1]),
    'idx': str(c)+"new"
  })
  
print('enumerated')

with open('image_tsne_projections.json', 'w') as out:
  print('out')
  json.dump(chart_data, out)
