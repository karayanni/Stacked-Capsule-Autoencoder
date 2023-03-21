# Stacked-Capsule-Autoencoder for bone age assessment

Stacked-Capsule-Autoencoder (SCAE) is An unsupervised method that combines Transformers and Capsule Networks to exploit spatial relations of different parts of an image.

- Stacked Capsule Autoencoders - NeurIPS 2019

In this repository, we implement, train and test the suggested SCAE for bone age assessment task - RSNA Pediatric Bone Age Challenge (2017).

The original BoneAge DS is heavy - images are around 1MB so we used https://github.com/karayanni/data-processing for preprocessing to make SCAE reasonable (too heavy otherwise).
