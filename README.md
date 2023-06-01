# Dog breed classification

## Presentation of the project :

### Objective:

Develop an algorithm capable of classifying according to the breed of dog in the image.

This objective can be likened to a task of supervised classification task.

### Data :
Use of data available on [Vision Stanford](http://vision.stanford.edu/aditya86/ImageNetDogs/). 

Comprising images of dogs classified by breed in different different folders.

There are 120 breeds represented with a total of 20 430 images.

Each folder corresponds to a particular breed of dog with a unique ID.

Number of images per dog breed :
![img per breed](data/readme-images/nb_images_per_breed.png)

Example of image :
![pekinese example](data/readme-images/pekinese_dog.png)

Model from Scratch

CNN model : 

- Keras implementation

![keras CNN implementation](data/readme-images/keras_CNN.png)

evaluation :
![evaluation keras model](/data/readme-images/graph_eval_CNN.png)

DenseNet121 :

![DenseNet121 model](data/readme-images/DenseNet_model.png)

evaluation :
![DenseNet121 evaluation](data/readme-images/DenseNet_evaluation.png)
