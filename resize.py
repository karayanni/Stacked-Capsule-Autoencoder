commit 071dc8f77a29df335a1a196b19c1311e66baf459 (HEAD -> master, origin/master, 
origin/HEAD)
Author: roymatza <62014251+roymatza@users.noreply.github.com>
Date:   Sat Aug 29 21:30:34 2020 +0300

    Add files via upload
    
    resize.py: data resizing (change size and paths in the script)
    
    train_boneage_colab.ipynb: Notebook for training on colab the model with the
 BoneAge using the modified torch-scae code.

diff --git a/resize.py b/resize.py
new file mode 100644
index 0000000..5406a79
--- /dev/null
+++ b/resize.py
@@ -0,0 +1,44 @@
+from PIL import Image, ImageOps
+import pathlib
+import glob
+import os
+
+desired_size = 256
+home_path = str(pathlib.Path.home())
+im_pth = home_path + "/dl-proj/boneage-dataset/boneage-training-dataset/boneage
-training-dataset/"
+im_resized_pth = home_path + "/dl-proj/boneage-dataset/boneage-training-dataset
/boneage-training-dataset-preprocessed/"
+file_ext =".png"
