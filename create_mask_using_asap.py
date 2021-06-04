# -*- coding: utf-8 -*-
"""
Created on Sun May 16 18:45:43 2021

@author: Raktim
"""



import multiresolutionimageinterface as mir


reader = mir.MultiResolutionImageReader()
mr_image = reader.open('C:/D_DRIVE/UNSW/Experiment/patch/WSI-analysis-master/patch_extraction/data/test_data/test_029.tif')
annotation_list = mir.AnnotationList()
xml_repository = mir.XmlRepository(annotation_list)
xml_repository.setSource('C:/D_DRIVE/UNSW/Experiment/patch/WSI-analysis-master/patch_extraction/data/test_data/anno/test_029.xml')
xml_repository.load()
annotation_mask = mir.AnnotationToMask()
label_map = {'_0': 255, '_1': 255, '_2': 0, 'Tumor': 255, 'Exclusion': 0}
conversion_order = ['_0', '_1', '_2', 'Tumor', 'Exclusion']
output_path='C:/D_DRIVE/UNSW/Experiment/patch/WSI-analysis-master/patch_extraction/data/test_data/mask/test_029_mask.tif'
annotation_mask.convert(annotation_list, output_path, mr_image.getDimensions(), mr_image.getSpacing(), label_map, conversion_order)

