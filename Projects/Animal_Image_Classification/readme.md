# Animal Image Classification   

A deep learning project to classify images of animals into 15 different categories using transfer learning.   

## Dataset   
- **Categories**: 15 animal classes   
- **Images per category**: ~120-130 images   
- **Total images**: 1,944 images  
- **Split**: 80% training (1,555 images), 20% validation (389 images)   

## Model Architecture   
- **Base Model**: ResNet18 (pretrained on ImageNet)   
- **Transfer Learning**: Fine-tuned the final fully connected layer for 15 classes   
- **Input Size**: 224x224 pixels   
- **Optimization**: Adam optimizer with learning rate 1e-4   

## Data Augmentation   
- Random horizontal flip  
- Random rotation (10 degrees)   
- Color jitter (brightness and contrast)   
- Standard ImageNet normalization   

## Results   
- **Simple CNN**: ~71.9% validation accuracy   
- **ResNet18 (Transfer Learning)**: **88.9% validation accuracy**   

## Features   
- Early stopping to prevent overfitting   
- Model checkpointing (saves best model)   
- Data augmentation for better generalization   

## Requirements   
- PyTorch   
- torchvision   
- PIL (Pillow)   
- matplotlib
- scikit-learn   

## Usage   

### Training   
```python
python Animal_Image_Classification.ipynb
```

### Loading Saved Model    
```python   
import torch   
import torchvision.models as models   
import torch.nn as nn   

# Load model architecture   
model = models.resnet18(pretrained=False)   
num_ftrs = model.fc.in_features   
model.fc = nn.Linear(num_ftrs, 15)  # 15 classes   

# Load trained weights     
model.load_state_dict(torch.load('models/best_resnet18.pth'))    
model.eval()     
```

## Key Techniques Used    
- Transfer Learning with pretrained ResNet18    
- Data augmentation for improved generalization   
- Early stopping to prevent overfitting   
- Proper train/validation split with stratification   
 
## Performance    
The transfer learning approach significantly outperformed the simple CNN baseline, achieving 88.9% validation accuracy compared to 71.98% with a custom CNN architecture.   
