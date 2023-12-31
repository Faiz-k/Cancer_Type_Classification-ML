The dataset bdiag.csv contains quantitative information from digitized images of a diagnostic test (fine needle aspirate (FNA) test on breast mass) for the diagnosis of breast cancer. The variables describe characteristics of the cell nuclei present in the image.

Variables Information:

ID number
Diagnosis (M = malignant, B = benign)
and ten real-valued features are computed for each cell nucleus:

radius (mean of distances from center to points on the perimeter)
texture (standard deviation of gray-scale values)
perimeter
area
smoothness (local variation in radius lengths)
compactness (perimeter^2 / area - 1.0)
concavity (severity of concave portions of the contour)
concave points (number of concave portions of the contour)
symmetry
fractal dimension (“coastline approximation” - 1)
The mean, standard error and “worst” or largest (mean of the three largest values) of these features were computed for each image, resulting in 30 features. For instance, field 3 is Mean Radius, field 13 is Radius SE, field 23 is Worst Radius.

This database is also available through the UW CS ftp server: ftp ftp.cs.wisc.edu cd math-prog/cpo-dataset/machine-learn/WDBC/


The dataset bdiag.csv, included several imaging details from patients that had a biopsy to test for breast cancer.
The variable Diagnosis classifies the biopsied tissue as M = malignant or B = benign.

Fit a logistic regression to predict Diagnosis using texture_mean and radius_mean.

Build the confusion matrix for the model above

Calculate the area and the ROC curve for the model in a).

Plot the scatter plot for texture_mean and radius_mean and draw the border line for the prediction of Diagnosis based on the model in a)

If you wanted to use the model above to predict the result of the biopsy, but wanted to decrease the chances of a false negative test, what strategy could you use?
