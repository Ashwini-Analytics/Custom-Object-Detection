# Machine Learning

## Data Pre-Processing

The data needs to be pre processed before use as the data is in .mp4 format and we need to convert videos to frames. For this purpose you can use ```video_to_frame.py``` program. 

To run the code just type 
    
     $ Python video_to_frame.py

## Annotations

Annotations for darkflow needs to be in .xml format. For annotations in ```.xml``` you should use LabelImg. LabelImg can be downloaded from [here](https://github.com/tzutalin/labelImg)

#### Requirements for LabelImg

  Python 2.6, [PyQt 4.8](https://www.riverbankcomputing.com/software/pyqt/download) , [lxml](http://lxml.de/installation.html)(only for Windows user)
  
#### Download LabelImg

 ##### Building from source
 
  - Ubuntu Linux
    
    Python 2 + Qt4
      
         $ sudo apt-get install pyqt4-dev-tools

         $ sudo pip install lxml

         $ make qt4py2

         $ python labelImg.py

         $ python labelImg.py [IMAGE_PATH] [PRE-DEFINED CLASS FILE]

   - Windows
     
      Open cmd and go to labelImg directory

          $ pyrcc4 -o resources.py resources.qrc

          $ python labelImg.py

          $ python labelImg.py [IMAGE_PATH] [PRE-DEFINED CLASS FILE]

  - macOS
     
     Python 2 + Qt4

         $ brew install qt qt4

         $ brew install libxml2

         $ make qt4py2

         $ python labelImg.py

         $ python  labelImg.py [IMAGE_PATH] [PRE-DEFINED CLASS FILE]
         
 
#### After Installation 

- In ```data/predefined_classes.txt``` define the list of classes that will be used for your training.

- Build and launch using the instructions above.

- Right below ```"Save"``` button in toolbar, click "PascalVOC" button to switch to YOLO format.

- You may use ```Open/OpenDIR``` to process single or multiple images. After every image click save.

- A txt file of yolo format will be saved in the same folder as your image with same name. A file named ```"classes.txt"``` is saved to that folder too. "classes.txt" defines the list of class names that your yolo label refers to.

## Model

  For training custom detection we have used [Darkflow](https://github.com/thtrieu/darkflow). Darkflow is state-of-the-art real-time object detection model. The paper for this can be found [here](https://arxiv.org/pdf/1612.08242.pdf).
  
    - Download or Clone the repository 
    
#### Requirements

       Python3, tensorflow 1.0, numpy, opencv 3.
 
#### Build the model
    
    - You can choose one of the following three ways to get started with darkflow.

     
      1. python3 setup.py build_ext --inplace (before using this make sure Cython is installed. NOTE: If installing this way you will have to use ./flow in the cloned darkflow directory instead of flow as darkflow is not installed globally.)
   
      2. pip install -e .

      3. pip install .



## Configuration of model

   - Custom detection (I have done this for 2 classes)
       
         1. Create a copy of the configuration file tiny-yolo-voc.cfg and rename it according to your preference tiny-yolo-voc-2c.cfg (It is crucial that you leave the original tiny-yolo-voc.cfg file unchanged).
         
         2. In tiny-yolo-voc-2c.cfg, change classes in the [region] layer ( of the last layer) to the number of classes you are going to train for. In our case, classes are set to 2.
         
         3. In tiny-yolo-voc-2c.cfg, change filters in the [convolutional] layer (the second to last layer) to num * (classes + 5). In our case, num is 5 and classes are 2 so 5 * (2 + 5) = 35 therefore filters are set to 35.
         
         4. Change labels.txt to include the label(s) you want to train on (number of labels should be the same as the number of classes you set in tiny-yolo-voc-2c.cfg file). In our case, labels.txt will contain 2 labels.
         
## Model Training

   Before training make sure that you a weights file in ```/darkflow/bin``` folder and you have seperate folders for annotations and image.
    
      $ python flow --model cfg/tiny-yolo-voc-2c.cfg --load bin/tiny-yolo-voc.weights --train --annotation train/Annotations --dataset train/Images --gpu 1.0
           
           
 Train the model till ```10,000``` steps. 
           
## Model Testing 
           
   
   To test the model you need to have weights file that is been generated after training. You will find that in ```/bin``` folder.
   
   For a demo that runs on the CPU:

    $ python flow --model cfg/new.cfg --load bin/new.weights --demo videofile.avi

    
   For a demo that runs 100% on the GPU:

    $ python flow --model cfg/new.cfg --load bin/new.weights --demo videofile.avi --gpu 1.0
    
## To train the model on AWS

1. Login to AWS account
2. Go to Services -> EC2
3. Click on launch instance
4. Choose the appropriate AMI 
5. Choose AMI instance (The pricing of AMI instance can be found [here](https://aws.amazon.com/ec2/pricing/on-demand/))
6. Add storage and configure security. And then Launch it.
7. You need to create a new Keypair and download it.
8. Click on your instance and connect it.
9. Open your Command prompt 
     
       $ cd Downloads
       $ chmod 400 key.pem
       $ ssh -i "key.pem" ec2-user@ec2-52-91-175-244.compute-1.amazonaws.com
       $ sudo apt-get update 
     - Download or clone Darkflow(If you are going to train on darkflow).
10. Before training the model check the dependencies.



## Transfer files to AWS

   There are 2 methods of transfering the files.
   
   #### 1. Through AWS Storage
   The charges for storage can be found [here](https://aws.amazon.com/govcloud-us/pricing/s3/).
      
     AWS Provide storage facility to store your data and can use it whenever it is been needed.
     But for this storage they charge some certain amount. 
     
     To create the bucket, follow the instructions:
      
      1. Login to AWS account
      2. Go to services -> S3
      3. Create a New Bucket and add permissions.
      
 #### 2. Through FileZila
 
 You can download FileZila from [here](https://filezilla-project.org/download.php?type=client)
 
      FileZila is used for trasfering the files. we are going to use FileZila for transfering the files from desktop to AWS EC2 instance. 
      (NOTE: Make sure to launch the Instance)
      
      For transfering file from desktop to AWS instance :
      
      1. Download FileZila Client and Install it
      2. In Host, copy paste the DNS of AWS EC2 instance ( In our case ,ec2-52-91-175-244.compute-1.amazonaws.com). You can find this after you have launched the EC2 instance.
      3. Username as ubuntu and no need to give the password.
      4. Port = 22 
      5. Click on Quickconnect and then you can copy the files and folders (copying might take some time depending on the size of the file, so I recommend you to make a zip file and then transfer it).

 
