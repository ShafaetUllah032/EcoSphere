from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import os
from PIL import Image
import numpy as np
import pickle
import tensorflow
from tensorflow.keras.preprocessing import image
from tensorflow.keras.layers import GlobalMaxPooling2D
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input
from sklearn.neighbors import NearestNeighbors
from numpy.linalg import norm

feature_list = np.array(pickle.load(open('../embeddings.pkl', 'rb')))
filenames = pickle.load(open('../filenames.pkl', 'rb'))

model = ResNet50(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
model.trainable = False

model = tensorflow.keras.Sequential([
    model,
    GlobalMaxPooling2D()
])


def save_uploaded_file(uploaded_file):
    try:
        with open(os.path.join('uploads', uploaded_file.name), 'wb') as f:
            f.write(uploaded_file.read())
        return 1
    except:
        return 0


def feature_extraction(img_path, model):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    expanded_img_array = np.expand_dims(img_array, axis=0)
    preprocessed_img = preprocess_input(expanded_img_array)
    result = model.predict(preprocessed_img).flatten()
    normalized_result = result / norm(result)

    return normalized_result


def recommend(features, feature_list):
    neighbors = NearestNeighbors(n_neighbors=6, algorithm='brute', metric='euclidean')
    neighbors.fit(feature_list)

    distances, indices = neighbors.kneighbors([features])

    return indices


# Create your views here.
async def mlapp(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['myfile']
        save_uploaded_file(uploaded_file)
        features = feature_extraction(os.path.join("uploads", uploaded_file.name), model)
        indices = recommend(features, feature_list)
        print(filenames[indices[0][0]])
        return render(request, "mlapp/result.html",
                      {'img1': filenames[indices[0][0]],
                       'img2': filenames[indices[0][1]],
                       'img3': filenames[indices[0][2]],
                       'img4': filenames[indices[0][3]],
                       'img5': filenames[indices[0][4]]
                       })

    return render(request, 'mlapp/ml.html')
