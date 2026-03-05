Diminishing Gradient : Makes the Weights Constant

Exploding Gradient Problem :

Gradient will be to high ; Loss function will swing heavily



**LeNet5**: Limited capacity , shallow architecture

Outdated pooling average pooling

Lack of modern  Regularization



Next one that came :

**AlexNet(2012)**

* AlexNet(2012):  227 x 227 pixels conversion of images
* Key Features : Local Response Normalization (LRN)
* Data Augmentation: Random Cropping , horizontal Flipping, RGB intensity Variations



Dropout Regularization:

* Uses 11 x 11 filters
* ILSVRC(bench mark challenge): ImageNet Large Scale Visual Recognition Challenge : High resolution images
* 1.2 Million training Images
* 1K images per category , with 1k categories: 50000 validation 150000 testing images
* Stride size < filter dim == Overlap pooling



## ***26/02/2026***



**VGG NET**

* (Also called VGG 16)
* Introduced by University of Oxford
* Visual Geometric Group
* 16 weight layers ( 13 convo + 3 FC)
* Uses 3 x 3 convolution Filter
* Very deep but simple architecture
* Transfer Learning
* fc removed and replaced by our Model instead

**Freeze the layers of VGG16**

1. Do not disturb the remaining stuff, we are not disturb the convo layer.....
2. fully freezing all layers
3. or Partially convo layers ( last few layers)
4. layer.trainable = true ; would let all be trained



## **05/03/2026**



###### **GoogLeNet (2014) : InceptionNetV1** 

1. Going Deeper with Convolutions : Christian Szegedy 
2. 22 Layers, Multiple convolutions were done parallelly on the same layer, (1x1.3x3,5x5). Parallelism
3. Introduced 1 x 1 convolution
4. Less parameters than other models( 5 Million)Computationally Efficient
5. Uses Global average pooling ,Reduces the no of learnable parameters

6\. multiclass == Softmax 

7\. Inception Modules 



**Inception V3** 

1. 48 Layers
2. 5 x 5 -> two 3 x 3 , 3 x 3 -> 1 x 3 and 3 x 1 
3. 299 x 299 input image size
4. ~23 Million Param
5. RMSProp, 96.1%
