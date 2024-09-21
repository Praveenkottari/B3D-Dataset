# BD3: Building Defects Detection Dataset

Download the [BD3-Dataset](https://indianinstituteofscience-my.sharepoint.com/:f:/g/personal/praveenkotta_iisc_ac_in/Et7Ki_ILnGtBi1oFpOioPGcBp4zzUodaYsJ5UV3tve1Geg?e=3zxutQ).

The inspection of urban built environments is critical to maintaining structural integrity and safety. However, traditional manual inspection methods are often time-consuming, labor-intensive, prone to human error, and difficult to scale across large urban environments. These limitations become particularly evident in fast-growing cities, where aging infrastructure and the demand for regular inspection outpace the capacity of human inspectors. To overcome these challenges, the use of automated building inspection techniques powered by computer vision has gained significant interest. By employing technologies such as drones and multi-robot systems, these techniques promise to make building inspections faster, more accurate, and scalable. Despite these advances, a major barrier to the development and deployment of robust automated inspection systems is the lack of comprehensive and publicly available datasets. Most existing datasets fail to capture a wide range of structural defects or do not provide enough diversity in image samples, limiting the ability of machine learning models to generalize across different environments and defect types.

To address this gap, we present **BD3: Building Defects Detection Dataset**, specifically designed to evaluate and develop computer vision techniques for automated building inspections. 
BD3 consists of two subsets: 

- **Original dataset**: 3,965 RGB images annotated to cover six common structural defects, along with normal wall images.
- **Augmented dataset**: 14,000 images created using geometric transformations (rotations, flips) and color adjustments (brightness, contrast, saturation, and hue). This augmentation datset is intended to enhance the dataset's diversity, improving the robustness and generalizability of models trained on BD3.

By making BD3 publicly available, we aim to accelerate the development of reliable and scalable automated inspection systems that can help ensure the safety and longevity of our urban infrastructure.

## Building Defects Details

The BD3 dataset contains six defect classes and normal wall images. Below are the descriptions of these defect classes along with the number of image samples available for each:

| Defect Name  | Description                                                                    | Number of Images |
|--------------|--------------------------------------------------------------------------------|-----------------:|
| **Algae**    | Fungi resembling green, brown, or black patches or slime on the surface        | 624              |
| **Major Crack** | Cracks with visible gaps                                                    | 620              |
| **Minor Crack** | Cracks without visible gaps                                                 | 580              |
| **Peeling**  | Loss of the outer covering of paint                                            | 520              |
| **Spalling** | Surface break exposing inner material                                          | 500              |
| **Stain**    | Visible man-made or natural color marks                                        | 521              |
| **Normal**   | Clean walls with no visible signs of defects                                   | 600              |

## Sample Images

<table border="0" style="text-align: center;">
  <tr>
    <td style="text-align: center;"><img src="example-imgs/cls00_441.jpg" width="200" /><br><b>(a) Algae</b></td>
    <td style="text-align: center;"><img src="example-imgs/cls01_087.jpg" width="200" /><br><b>(b) Major Crack</b></td>
    <td style="text-align: center;"><img src="example-imgs/cls02_031.jpg" width="200" /><br><b>(c) Minor Crack</b></td>
    <td style="text-align: center;"><img src="example-imgs/cls03_018.jpg" width="200" /><br><b>(d) Peeling</b></td>
  </tr>
  <tr>
    <td style="text-align: center;"><img src="example-imgs/cls05_008.jpg" width="200" /><br><b>(e) Spalling</b></td>
    <td style="text-align: center;"><img src="example-imgs/cls06_082.jpg" width="200" /><br><b>(f) Stain</b></td>
    <td style="text-align: center;"><img src="example-imgs/cls04_057.jpg" width="200" /><br><b>(g) Normal</b></td>
  </tr>
</table>



## Dataset folder structure
    .
    ├── ...
    ├── train                   # train folder
    │   ├── cls00              
    │   ├──   ├── cls00_001.jpg               
    │   ├──   :                 
    │   └── cls06              
    └── val                     # validation folder
    └── test                    # test folder
    

## Preprocessing and Model Training

The codebase folder [code](https://github.com/Praveenkottari/BD3-Dataset/tree/main/code) contains all the files and notebooks used for the experiments.

[data-augment-technq](https://github.com/Praveenkottari/BD3-Dataset/tree/main/code/data-augment-Technq): This subfolder provides a notebook that applies several augmentation techniques to generate additional data samples.

[data-process](https://github.com/Praveenkottari/BD3-Dataset/tree/main/code/data-process): This folder contains Python scripts for renaming, resizing, and other preprocessing activities.

[train-test-split](https://github.com/Praveenkottari/BD3-Dataset/tree/main/code/train-test-split) : This folder includes a Python script for splitting the dataset into training and testing sets based on a custom ratio.

[model-train](https://github.com/Praveenkottari/BD3-Dataset/tree/main/code/model-train): This folder is a collection of all the notebooks used for model training in this study. Each model has its own separate notebook.

The notebooks and Python scripts mentioned above can be reused by cloning this repository to your local machine. You can also download the notebooks, make necessary changes to datasets, file paths, or other configurations, and use them for training and testing.

## Deep Learnign models

| 	model	 | 	architecture	 | 	document	 | 
| 	:-----:	 | 	:-----:	 | 	:-----:	 | 
| 	ViT16	| 	Transformer	| 	[paper](https://arxiv.org/abs/2010.11929)	 | 
| 	VGG16 	| 	CNN	| 	[paper](https://arxiv.org/abs/1409.1556)	 | 
| 	ResNet18	| 	CNN	| 	[paper](https://arxiv.org/abs/1512.03385)	 | 
| 	Alexnet	| 	CNN	| 	[paper](https://proceedings.neurips.cc/paper_files/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf)	 | 
| 	MobileNet-V2	| 	CNN	| 	[paper](MobileNet-V2)	 | 

