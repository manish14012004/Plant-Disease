
# Plant Disease Detection

This repository contains the code for a plant disease detection system that uses machine learning algorithms and image processing techniques to identify diseases in plant leaves. The goal is to help farmers detect plant diseases early and take the necessary measures to treat them, thereby improving crop yield and quality.

## Features

- Detects common plant diseases in crops like **Tomato** and **Corn**.
- Leverages **Convolutional Neural Networks (CNNs)** for image classification.
- Provides disease-specific insights and treatment recommendations.
- Easy-to-use interface for uploading plant leaf images and receiving instant feedback.
- Built-in dataset preprocessing, image augmentation, and model training functionalities.

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [Model Training](#model-training)
4. [Dataset](#dataset)
5. [Results](#results)
6. [Contributing](#contributing)
7. [License](#license)

## Installation

To run the project locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/manish14012004/Plant-Disease.git
   cd Plant-Disease
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Download the dataset (if necessary) and place it in the appropriate directory:

Plant Village Dataset for plant disease images.
Usage
To test the pre-trained model, upload images of diseased plant leaves to the /uploads folder or provide an image URL.

Run the detection script:

bash
Copy code
python detect_disease.py --image /path/to/your/image.jpg
The system will output the detected disease, along with suggestions for treatment.

Model Training
To train the model from scratch:

Ensure you have the dataset available.

Run the following command to train the model:

bash
Copy code
python train_model.py
Adjust hyperparameters like the learning rate, batch size, and epochs in the config.py file for better results.

Dataset
The Plant Village dataset is used for model training and testing. It contains labeled images of healthy and diseased plant leaves, covering multiple crops and diseases.

Results
The model achieves high accuracy on detecting plant diseases, including:

Tomato Diseases: Early Blight, Late Blight, Bacterial Spot
Corn Diseases: Northern Corn Leaf Blight, Gray Leaf Spot, Anthracnose
Sample predictions:

Image	Predicted Disease	Confidence
Tomato Leaf 1	Early Blight	92%
Corn Leaf 2	Northern Corn Leaf Blight	89%
Contributing
Contributions are welcome! If you'd like to improve the code or add new features, please follow these steps:

Fork the repository.
Create a new branch: git checkout -b feature-branch-name.
Make your changes and commit them: git commit -m 'Add some feature'.
Push to the branch: git push origin feature-branch-name.
Open a pull request.
License
This project is licensed under the MIT License. See the LICENSE file for details.

csharp
Copy code

You can customize this based on your specific project details!
