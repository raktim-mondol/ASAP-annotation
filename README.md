# ASAP-annotation
How to create mask from ASAP annotation (.xml file)


### Download
https://github.com/computationalpathologygroup/ASAP/releases/tag/1.9

This annotation works on python 3.6 does NOT work on 3.7
Adding ASAP bin folder to windows environment variable does not work
So when creating mask I used to enter in the following location then run the python code. 
C:\Program Files\ASAP 1.8\bin

Now importing following line should work

import multiresolutionimageinterface


See example code: https://github.com/3dimaging/DeepLearningCamelyon/blob/master/1%20-%20WSI%20Visualization%20with%20Annotation/Mask%20Generation


WARNING:

In the following main WEBSITE masking code is WRONG.
https://camelyon17.grand-challenge.org/Data/


annotation_mask = mir.AnnotationToMask() \
label_map = {'_0': 255, '_1': 255, '_2': 0}\
NOT>>>>label_map = {'_0': 1, '_1': 1, '_2': 0}  >>> THIS IS WRONG\
conversion_order = ['_0', '_1', '_2']
