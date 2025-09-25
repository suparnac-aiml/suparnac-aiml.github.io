# American Sign Language (ASL) Real-Time Detection   

This project implements real-time American Sign Language (ASL) alphabet detection using a webcam and a deep learning model. The model is trained on ASL hand sign images and deployed for live inference, identifying signs from A-Z and special classes (del, nothing, space) directly from webcam input.    

## Features    

- Real-time sign language letter recognition from webcam video   
- Supports 29 classes (A-Z, del, space, nothing)   
- Bounding box guides user hand placement for best results   
- Prediction smoothing and confidence display for stable results   
- Runs on Mac mini with Apple Silicon GPU acceleration   

## Dataset Details   

The model was trained on the publicly available ASL Alphabet dataset, which contains images of hand signs representing letters A through Z, along with special classes such as "del" (delete), "nothing," and "space." The dataset includes thousands of images with variations in hand shape, lighting, and background for robustness.   

## Requirements   

- Python 3.8+   
- PyTorch   
- torchvision   
- numpy   
- opencv-python  
- pillow   

Install all dependencies with:    
pip install torch torchvision opencv-python pillow numpy   


## Usage   

1. **Train the model** on the provided ASL dataset (see code files for training script).   
2. Place the trained weights file (`best_model_asl.pth`) in your project directory.   
3. Run the real-time detection script:   
   python asl_realtime_detection.py    
               OR    
   Run the .ipynb script from yuor notebook    

4. Position your hand in the green bounding box area on the webcam.   
5. The predicted ASL letter and its confidence will be displayed in red.   
6. Press `q` to quit.   

## Notes (Future Improvements)   

- For best results, use good lighting and a contrasting background (preferably plain background).   
- Some letters may need further fine-tuning or more training samples (like J, Z and N).   
- The code uses prediction smoothing for more robust live results.   



