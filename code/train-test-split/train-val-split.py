import os
import shutil
import random
from math import ceil

def split_dataset(dataset_dir, train_dir, val_dir, test_dir, train_ratio=0.6, val_ratio=0.2, test_ratio=0.2):
    # Ensure the output directories exist
    if not os.path.exists(train_dir):
        os.makedirs(train_dir)
    if not os.path.exists(val_dir):
        os.makedirs(val_dir)
    if not os.path.exists(test_dir):
        os.makedirs(test_dir)

    # Iterate over each class in the dataset directory
    for class_name in os.listdir(dataset_dir):
        class_dir = os.path.join(dataset_dir, class_name)
        
        if os.path.isdir(class_dir):
            # Ensure class directories exist in train, val, and test directories
            train_class_dir = os.path.join(train_dir, class_name)
            val_class_dir = os.path.join(val_dir, class_name)
            test_class_dir = os.path.join(test_dir, class_name)
            if not os.path.exists(train_class_dir):
                os.makedirs(train_class_dir)
            if not os.path.exists(val_class_dir):
                os.makedirs(val_class_dir)
            if not os.path.exists(test_class_dir):
                os.makedirs(test_class_dir)

            # Get all samples in the class directory
            samples = os.listdir(class_dir)
            random.shuffle(samples)

            # Split the samples
            split_index1 = ceil(len(samples) * train_ratio)
            split_index2 = ceil(len(samples) * (train_ratio + val_ratio))

            train_samples = samples[:split_index1]
            val_samples = samples[split_index1:split_index2]
            test_samples = samples[split_index2:]

            # Copy the samples to the respective directories
            for sample in train_samples:
                src = os.path.join(class_dir, sample)
                dst = os.path.join(train_class_dir, sample)
                shutil.copy(src, dst)

            for sample in val_samples:
                src = os.path.join(class_dir, sample)
                dst = os.path.join(val_class_dir, sample)
                shutil.copy(src, dst)

            for sample in test_samples:
                src = os.path.join(class_dir, sample)
                dst = os.path.join(test_class_dir, sample)
                shutil.copy(src, dst)

            print(f'Class "{class_name}": {len(train_samples)} train samples, {len(val_samples)} val samples, {len(test_samples)} test samples')

# Define your dataset directory and output directories
dataset_dir = r'../../dataset/augmented'
train_dir = r'../../dataset/train-augment-dataset/train'
val_dir = r'../../dataset/train-augment-dataset/valid'
test_dir = r'../../dataset/train-augment-dataset/test'

# Split the dataset
split_dataset(dataset_dir, train_dir, val_dir, test_dir)
print("train-val-test split completed")
