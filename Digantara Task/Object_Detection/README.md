
Project Title: Object Detection in Satellite Imagery   

Overview:   
This project performs unsupervised segmentation of high-resolution satellite TIFF images using a combination of deep learning (ResNet18 features), texture analysis (standard deviation), and KMeans clustering. The output includes cluster maps, standard deviation heatmaps, and overlay visualizations.   

How to Run:   
1. Install dependencies using pip:   
   pip install torch torchvision numpy matplotlib rasterio scikit-learn scikit-image   

2. Organize the project directory as follows:   
   /CV_Projects/   
   └── Digantara/   
       ├── 1_1.tif   
       ├── 1_2.tif   
       ├── 1_3.tif   
       └── resnet_cluster_maps/    # This will be created automatically for outputs    

3. Configure the script:    
   - Set `tiff_img_path` to the directory containing the .tif files.   
   - Choose `patch_size`, `number_clusters`, and `batch_size` as needed.   

4. Run the segmentation script (e.g., ObjectDetection.ipynb). This will generate:   
   - Cluster maps (.png)   
   - Standard deviation heatmaps   
   - Evaluation metrics (Silhouette Score, Calinski-Harabasz, Davies-Bouldin)   

5. Run the overlay script to generate overlay images of segmentation over original images.   
   - The overlay maps will be saved in the `resnet_cluster_maps` directory with the suffix `_overlay.png`.   

Output Folder: resnet_cluster_maps/   
- 1_1_clusters.png   
- 1_1_overlay.png   
- 1_2_clusters.png   
- 1_2_overlay.png   
- etc.   

Author: Suparna C   
Date: July 14, 2025   
