depends = ('ITKPyBase', 'ITKMathematicalMorphology', 'ITKLabelMap', )
templates = (
  ('BinaryClosingByReconstructionImageFilter', 'itk::BinaryClosingByReconstructionImageFilter', 'itkBinaryClosingByReconstructionImageFilterIUC2SE2', True, 'itk::Image< unsigned char,2 >,itk::FlatStructuringElement< 2 >'),
  ('BinaryClosingByReconstructionImageFilter', 'itk::BinaryClosingByReconstructionImageFilter', 'itkBinaryClosingByReconstructionImageFilterIUS2SE2', True, 'itk::Image< unsigned short,2 >,itk::FlatStructuringElement< 2 >'),
  ('BinaryClosingByReconstructionImageFilter', 'itk::BinaryClosingByReconstructionImageFilter', 'itkBinaryClosingByReconstructionImageFilterIUC3SE3', True, 'itk::Image< unsigned char,3 >,itk::FlatStructuringElement< 3 >'),
  ('BinaryClosingByReconstructionImageFilter', 'itk::BinaryClosingByReconstructionImageFilter', 'itkBinaryClosingByReconstructionImageFilterIUS3SE3', True, 'itk::Image< unsigned short,3 >,itk::FlatStructuringElement< 3 >'),
  ('BinaryDilateImageFilter', 'itk::BinaryDilateImageFilter', 'itkBinaryDilateImageFilterISS2ISS2SE2', True, 'itk::Image< signed short,2 >,itk::Image< signed short,2 >,itk::FlatStructuringElement< 2 >'),
  ('BinaryDilateImageFilter', 'itk::BinaryDilateImageFilter', 'itkBinaryDilateImageFilterIUC2IUC2SE2', True, 'itk::Image< unsigned char,2 >,itk::Image< unsigned char,2 >,itk::FlatStructuringElement< 2 >'),
  ('BinaryDilateImageFilter', 'itk::BinaryDilateImageFilter', 'itkBinaryDilateImageFilterIUS2IUS2SE2', True, 'itk::Image< unsigned short,2 >,itk::Image< unsigned short,2 >,itk::FlatStructuringElement< 2 >'),
  ('BinaryDilateImageFilter', 'itk::BinaryDilateImageFilter', 'itkBinaryDilateImageFilterIF2IF2SE2', True, 'itk::Image< float,2 >,itk::Image< float,2 >,itk::FlatStructuringElement< 2 >'),
  ('BinaryDilateImageFilter', 'itk::BinaryDilateImageFilter', 'itkBinaryDilateImageFilterID2ID2SE2', True, 'itk::Image< double,2 >,itk::Image< double,2 >,itk::FlatStructuringElement< 2 >'),
  ('BinaryDilateImageFilter', 'itk::BinaryDilateImageFilter', 'itkBinaryDilateImageFilterISS3ISS3SE3', True, 'itk::Image< signed short,3 >,itk::Image< signed short,3 >,itk::FlatStructuringElement< 3 >'),
  ('BinaryDilateImageFilter', 'itk::BinaryDilateImageFilter', 'itkBinaryDilateImageFilterIUC3IUC3SE3', True, 'itk::Image< unsigned char,3 >,itk::Image< unsigned char,3 >,itk::FlatStructuringElement< 3 >'),
  ('BinaryDilateImageFilter', 'itk::BinaryDilateImageFilter', 'itkBinaryDilateImageFilterIUS3IUS3SE3', True, 'itk::Image< unsigned short,3 >,itk::Image< unsigned short,3 >,itk::FlatStructuringElement< 3 >'),
  ('BinaryDilateImageFilter', 'itk::BinaryDilateImageFilter', 'itkBinaryDilateImageFilterIF3IF3SE3', True, 'itk::Image< float,3 >,itk::Image< float,3 >,itk::FlatStructuringElement< 3 >'),
  ('BinaryDilateImageFilter', 'itk::BinaryDilateImageFilter', 'itkBinaryDilateImageFilterID3ID3SE3', True, 'itk::Image< double,3 >,itk::Image< double,3 >,itk::FlatStructuringElement< 3 >'),
  ('BinaryErodeImageFilter', 'itk::BinaryErodeImageFilter', 'itkBinaryErodeImageFilterISS2ISS2SE2', True, 'itk::Image< signed short,2 >,itk::Image< signed short,2 >,itk::FlatStructuringElement< 2 >'),
  ('BinaryErodeImageFilter', 'itk::BinaryErodeImageFilter', 'itkBinaryErodeImageFilterIUC2IUC2SE2', True, 'itk::Image< unsigned char,2 >,itk::Image< unsigned char,2 >,itk::FlatStructuringElement< 2 >'),
  ('BinaryErodeImageFilter', 'itk::BinaryErodeImageFilter', 'itkBinaryErodeImageFilterIUS2IUS2SE2', True, 'itk::Image< unsigned short,2 >,itk::Image< unsigned short,2 >,itk::FlatStructuringElement< 2 >'),
  ('BinaryErodeImageFilter', 'itk::BinaryErodeImageFilter', 'itkBinaryErodeImageFilterIF2IF2SE2', True, 'itk::Image< float,2 >,itk::Image< float,2 >,itk::FlatStructuringElement< 2 >'),
  ('BinaryErodeImageFilter', 'itk::BinaryErodeImageFilter', 'itkBinaryErodeImageFilterID2ID2SE2', True, 'itk::Image< double,2 >,itk::Image< double,2 >,itk::FlatStructuringElement< 2 >'),
  ('BinaryErodeImageFilter', 'itk::BinaryErodeImageFilter', 'itkBinaryErodeImageFilterISS3ISS3SE3', True, 'itk::Image< signed short,3 >,itk::Image< signed short,3 >,itk::FlatStructuringElement< 3 >'),
  ('BinaryErodeImageFilter', 'itk::BinaryErodeImageFilter', 'itkBinaryErodeImageFilterIUC3IUC3SE3', True, 'itk::Image< unsigned char,3 >,itk::Image< unsigned char,3 >,itk::FlatStructuringElement< 3 >'),
  ('BinaryErodeImageFilter', 'itk::BinaryErodeImageFilter', 'itkBinaryErodeImageFilterIUS3IUS3SE3', True, 'itk::Image< unsigned short,3 >,itk::Image< unsigned short,3 >,itk::FlatStructuringElement< 3 >'),
  ('BinaryErodeImageFilter', 'itk::BinaryErodeImageFilter', 'itkBinaryErodeImageFilterIF3IF3SE3', True, 'itk::Image< float,3 >,itk::Image< float,3 >,itk::FlatStructuringElement< 3 >'),
  ('BinaryErodeImageFilter', 'itk::BinaryErodeImageFilter', 'itkBinaryErodeImageFilterID3ID3SE3', True, 'itk::Image< double,3 >,itk::Image< double,3 >,itk::FlatStructuringElement< 3 >'),
  ('BinaryMorphologicalClosingImageFilter', 'itk::BinaryMorphologicalClosingImageFilter', 'itkBinaryMorphologicalClosingImageFilterISS2ISS2SE2', True, 'itk::Image< signed short,2 >,itk::Image< signed short,2 >,itk::FlatStructuringElement< 2 >'),
  ('BinaryMorphologicalClosingImageFilter', 'itk::BinaryMorphologicalClosingImageFilter', 'itkBinaryMorphologicalClosingImageFilterIUC2IUC2SE2', True, 'itk::Image< unsigned char,2 >,itk::Image< unsigned char,2 >,itk::FlatStructuringElement< 2 >'),
  ('BinaryMorphologicalClosingImageFilter', 'itk::BinaryMorphologicalClosingImageFilter', 'itkBinaryMorphologicalClosingImageFilterIUS2IUS2SE2', True, 'itk::Image< unsigned short,2 >,itk::Image< unsigned short,2 >,itk::FlatStructuringElement< 2 >'),
  ('BinaryMorphologicalClosingImageFilter', 'itk::BinaryMorphologicalClosingImageFilter', 'itkBinaryMorphologicalClosingImageFilterIF2IF2SE2', True, 'itk::Image< float,2 >,itk::Image< float,2 >,itk::FlatStructuringElement< 2 >'),
  ('BinaryMorphologicalClosingImageFilter', 'itk::BinaryMorphologicalClosingImageFilter', 'itkBinaryMorphologicalClosingImageFilterID2ID2SE2', True, 'itk::Image< double,2 >,itk::Image< double,2 >,itk::FlatStructuringElement< 2 >'),
  ('BinaryMorphologicalClosingImageFilter', 'itk::BinaryMorphologicalClosingImageFilter', 'itkBinaryMorphologicalClosingImageFilterISS3ISS3SE3', True, 'itk::Image< signed short,3 >,itk::Image< signed short,3 >,itk::FlatStructuringElement< 3 >'),
  ('BinaryMorphologicalClosingImageFilter', 'itk::BinaryMorphologicalClosingImageFilter', 'itkBinaryMorphologicalClosingImageFilterIUC3IUC3SE3', True, 'itk::Image< unsigned char,3 >,itk::Image< unsigned char,3 >,itk::FlatStructuringElement< 3 >'),
  ('BinaryMorphologicalClosingImageFilter', 'itk::BinaryMorphologicalClosingImageFilter', 'itkBinaryMorphologicalClosingImageFilterIUS3IUS3SE3', True, 'itk::Image< unsigned short,3 >,itk::Image< unsigned short,3 >,itk::FlatStructuringElement< 3 >'),
  ('BinaryMorphologicalClosingImageFilter', 'itk::BinaryMorphologicalClosingImageFilter', 'itkBinaryMorphologicalClosingImageFilterIF3IF3SE3', True, 'itk::Image< float,3 >,itk::Image< float,3 >,itk::FlatStructuringElement< 3 >'),
  ('BinaryMorphologicalClosingImageFilter', 'itk::BinaryMorphologicalClosingImageFilter', 'itkBinaryMorphologicalClosingImageFilterID3ID3SE3', True, 'itk::Image< double,3 >,itk::Image< double,3 >,itk::FlatStructuringElement< 3 >'),
  ('BinaryMorphologicalOpeningImageFilter', 'itk::BinaryMorphologicalOpeningImageFilter', 'itkBinaryMorphologicalOpeningImageFilterISS2ISS2SE2', True, 'itk::Image< signed short,2 >,itk::Image< signed short,2 >,itk::FlatStructuringElement< 2 >'),
  ('BinaryMorphologicalOpeningImageFilter', 'itk::BinaryMorphologicalOpeningImageFilter', 'itkBinaryMorphologicalOpeningImageFilterIUC2IUC2SE2', True, 'itk::Image< unsigned char,2 >,itk::Image< unsigned char,2 >,itk::FlatStructuringElement< 2 >'),
  ('BinaryMorphologicalOpeningImageFilter', 'itk::BinaryMorphologicalOpeningImageFilter', 'itkBinaryMorphologicalOpeningImageFilterIUS2IUS2SE2', True, 'itk::Image< unsigned short,2 >,itk::Image< unsigned short,2 >,itk::FlatStructuringElement< 2 >'),
  ('BinaryMorphologicalOpeningImageFilter', 'itk::BinaryMorphologicalOpeningImageFilter', 'itkBinaryMorphologicalOpeningImageFilterIF2IF2SE2', True, 'itk::Image< float,2 >,itk::Image< float,2 >,itk::FlatStructuringElement< 2 >'),
  ('BinaryMorphologicalOpeningImageFilter', 'itk::BinaryMorphologicalOpeningImageFilter', 'itkBinaryMorphologicalOpeningImageFilterID2ID2SE2', True, 'itk::Image< double,2 >,itk::Image< double,2 >,itk::FlatStructuringElement< 2 >'),
  ('BinaryMorphologicalOpeningImageFilter', 'itk::BinaryMorphologicalOpeningImageFilter', 'itkBinaryMorphologicalOpeningImageFilterISS3ISS3SE3', True, 'itk::Image< signed short,3 >,itk::Image< signed short,3 >,itk::FlatStructuringElement< 3 >'),
  ('BinaryMorphologicalOpeningImageFilter', 'itk::BinaryMorphologicalOpeningImageFilter', 'itkBinaryMorphologicalOpeningImageFilterIUC3IUC3SE3', True, 'itk::Image< unsigned char,3 >,itk::Image< unsigned char,3 >,itk::FlatStructuringElement< 3 >'),
  ('BinaryMorphologicalOpeningImageFilter', 'itk::BinaryMorphologicalOpeningImageFilter', 'itkBinaryMorphologicalOpeningImageFilterIUS3IUS3SE3', True, 'itk::Image< unsigned short,3 >,itk::Image< unsigned short,3 >,itk::FlatStructuringElement< 3 >'),
  ('BinaryMorphologicalOpeningImageFilter', 'itk::BinaryMorphologicalOpeningImageFilter', 'itkBinaryMorphologicalOpeningImageFilterIF3IF3SE3', True, 'itk::Image< float,3 >,itk::Image< float,3 >,itk::FlatStructuringElement< 3 >'),
  ('BinaryMorphologicalOpeningImageFilter', 'itk::BinaryMorphologicalOpeningImageFilter', 'itkBinaryMorphologicalOpeningImageFilterID3ID3SE3', True, 'itk::Image< double,3 >,itk::Image< double,3 >,itk::FlatStructuringElement< 3 >'),
  ('BinaryOpeningByReconstructionImageFilter', 'itk::BinaryOpeningByReconstructionImageFilter', 'itkBinaryOpeningByReconstructionImageFilterIUC2SE2', True, 'itk::Image< unsigned char,2 >,itk::FlatStructuringElement< 2 >'),
  ('BinaryOpeningByReconstructionImageFilter', 'itk::BinaryOpeningByReconstructionImageFilter', 'itkBinaryOpeningByReconstructionImageFilterIUS2SE2', True, 'itk::Image< unsigned short,2 >,itk::FlatStructuringElement< 2 >'),
  ('BinaryOpeningByReconstructionImageFilter', 'itk::BinaryOpeningByReconstructionImageFilter', 'itkBinaryOpeningByReconstructionImageFilterIUC3SE3', True, 'itk::Image< unsigned char,3 >,itk::FlatStructuringElement< 3 >'),
  ('BinaryOpeningByReconstructionImageFilter', 'itk::BinaryOpeningByReconstructionImageFilter', 'itkBinaryOpeningByReconstructionImageFilterIUS3SE3', True, 'itk::Image< unsigned short,3 >,itk::FlatStructuringElement< 3 >'),
  ('BinaryPruningImageFilter', 'itk::BinaryPruningImageFilter', 'itkBinaryPruningImageFilterIUC2IUC2', True, 'itk::Image< unsigned char,2 >, itk::Image< unsigned char,2 >'),
  ('BinaryPruningImageFilter', 'itk::BinaryPruningImageFilter', 'itkBinaryPruningImageFilterIUS2IUS2', True, 'itk::Image< unsigned short,2 >, itk::Image< unsigned short,2 >'),
  ('BinaryPruningImageFilter', 'itk::BinaryPruningImageFilter', 'itkBinaryPruningImageFilterIF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >'),
  ('BinaryPruningImageFilter', 'itk::BinaryPruningImageFilter', 'itkBinaryPruningImageFilterID2ID2', True, 'itk::Image< double,2 >, itk::Image< double,2 >'),
  ('BinaryThinningImageFilter', 'itk::BinaryThinningImageFilter', 'itkBinaryThinningImageFilterIUC2IUC2', True, 'itk::Image< unsigned char,2 >, itk::Image< unsigned char,2 >'),
  ('BinaryThinningImageFilter', 'itk::BinaryThinningImageFilter', 'itkBinaryThinningImageFilterIUS2IUS2', True, 'itk::Image< unsigned short,2 >, itk::Image< unsigned short,2 >'),
  ('BinaryThinningImageFilter', 'itk::BinaryThinningImageFilter', 'itkBinaryThinningImageFilterISS2ISS2', True, 'itk::Image< signed short,2 >, itk::Image< signed short,2 >'),
  ('DilateObjectMorphologyImageFilter', 'itk::DilateObjectMorphologyImageFilter', 'itkDilateObjectMorphologyImageFilterISS2ISS2SE2', True, 'itk::Image< signed short,2 >,itk::Image< signed short,2 >,itk::FlatStructuringElement< 2 >'),
  ('DilateObjectMorphologyImageFilter', 'itk::DilateObjectMorphologyImageFilter', 'itkDilateObjectMorphologyImageFilterIUC2IUC2SE2', True, 'itk::Image< unsigned char,2 >,itk::Image< unsigned char,2 >,itk::FlatStructuringElement< 2 >'),
  ('DilateObjectMorphologyImageFilter', 'itk::DilateObjectMorphologyImageFilter', 'itkDilateObjectMorphologyImageFilterIUS2IUS2SE2', True, 'itk::Image< unsigned short,2 >,itk::Image< unsigned short,2 >,itk::FlatStructuringElement< 2 >'),
  ('DilateObjectMorphologyImageFilter', 'itk::DilateObjectMorphologyImageFilter', 'itkDilateObjectMorphologyImageFilterIF2IF2SE2', True, 'itk::Image< float,2 >,itk::Image< float,2 >,itk::FlatStructuringElement< 2 >'),
  ('DilateObjectMorphologyImageFilter', 'itk::DilateObjectMorphologyImageFilter', 'itkDilateObjectMorphologyImageFilterID2ID2SE2', True, 'itk::Image< double,2 >,itk::Image< double,2 >,itk::FlatStructuringElement< 2 >'),
  ('DilateObjectMorphologyImageFilter', 'itk::DilateObjectMorphologyImageFilter', 'itkDilateObjectMorphologyImageFilterISS3ISS3SE3', True, 'itk::Image< signed short,3 >,itk::Image< signed short,3 >,itk::FlatStructuringElement< 3 >'),
  ('DilateObjectMorphologyImageFilter', 'itk::DilateObjectMorphologyImageFilter', 'itkDilateObjectMorphologyImageFilterIUC3IUC3SE3', True, 'itk::Image< unsigned char,3 >,itk::Image< unsigned char,3 >,itk::FlatStructuringElement< 3 >'),
  ('DilateObjectMorphologyImageFilter', 'itk::DilateObjectMorphologyImageFilter', 'itkDilateObjectMorphologyImageFilterIUS3IUS3SE3', True, 'itk::Image< unsigned short,3 >,itk::Image< unsigned short,3 >,itk::FlatStructuringElement< 3 >'),
  ('DilateObjectMorphologyImageFilter', 'itk::DilateObjectMorphologyImageFilter', 'itkDilateObjectMorphologyImageFilterIF3IF3SE3', True, 'itk::Image< float,3 >,itk::Image< float,3 >,itk::FlatStructuringElement< 3 >'),
  ('DilateObjectMorphologyImageFilter', 'itk::DilateObjectMorphologyImageFilter', 'itkDilateObjectMorphologyImageFilterID3ID3SE3', True, 'itk::Image< double,3 >,itk::Image< double,3 >,itk::FlatStructuringElement< 3 >'),
  ('ErodeObjectMorphologyImageFilter', 'itk::ErodeObjectMorphologyImageFilter', 'itkErodeObjectMorphologyImageFilterISS2ISS2SE2', True, 'itk::Image< signed short,2 >,itk::Image< signed short,2 >,itk::FlatStructuringElement< 2 >'),
  ('ErodeObjectMorphologyImageFilter', 'itk::ErodeObjectMorphologyImageFilter', 'itkErodeObjectMorphologyImageFilterIUC2IUC2SE2', True, 'itk::Image< unsigned char,2 >,itk::Image< unsigned char,2 >,itk::FlatStructuringElement< 2 >'),
  ('ErodeObjectMorphologyImageFilter', 'itk::ErodeObjectMorphologyImageFilter', 'itkErodeObjectMorphologyImageFilterIUS2IUS2SE2', True, 'itk::Image< unsigned short,2 >,itk::Image< unsigned short,2 >,itk::FlatStructuringElement< 2 >'),
  ('ErodeObjectMorphologyImageFilter', 'itk::ErodeObjectMorphologyImageFilter', 'itkErodeObjectMorphologyImageFilterIF2IF2SE2', True, 'itk::Image< float,2 >,itk::Image< float,2 >,itk::FlatStructuringElement< 2 >'),
  ('ErodeObjectMorphologyImageFilter', 'itk::ErodeObjectMorphologyImageFilter', 'itkErodeObjectMorphologyImageFilterID2ID2SE2', True, 'itk::Image< double,2 >,itk::Image< double,2 >,itk::FlatStructuringElement< 2 >'),
  ('ErodeObjectMorphologyImageFilter', 'itk::ErodeObjectMorphologyImageFilter', 'itkErodeObjectMorphologyImageFilterISS3ISS3SE3', True, 'itk::Image< signed short,3 >,itk::Image< signed short,3 >,itk::FlatStructuringElement< 3 >'),
  ('ErodeObjectMorphologyImageFilter', 'itk::ErodeObjectMorphologyImageFilter', 'itkErodeObjectMorphologyImageFilterIUC3IUC3SE3', True, 'itk::Image< unsigned char,3 >,itk::Image< unsigned char,3 >,itk::FlatStructuringElement< 3 >'),
  ('ErodeObjectMorphologyImageFilter', 'itk::ErodeObjectMorphologyImageFilter', 'itkErodeObjectMorphologyImageFilterIUS3IUS3SE3', True, 'itk::Image< unsigned short,3 >,itk::Image< unsigned short,3 >,itk::FlatStructuringElement< 3 >'),
  ('ErodeObjectMorphologyImageFilter', 'itk::ErodeObjectMorphologyImageFilter', 'itkErodeObjectMorphologyImageFilterIF3IF3SE3', True, 'itk::Image< float,3 >,itk::Image< float,3 >,itk::FlatStructuringElement< 3 >'),
  ('ErodeObjectMorphologyImageFilter', 'itk::ErodeObjectMorphologyImageFilter', 'itkErodeObjectMorphologyImageFilterID3ID3SE3', True, 'itk::Image< double,3 >,itk::Image< double,3 >,itk::FlatStructuringElement< 3 >'),
)
snake_case_functions = ('binary_pruning_image_filter', 'object_morphology_image_filter', 'binary_opening_by_reconstruction_image_filter', 'binary_morphological_opening_image_filter', 'binary_morphological_closing_image_filter', 'dilate_object_morphology_image_filter', 'binary_closing_by_reconstruction_image_filter', 'binary_erode_image_filter', 'binary_morphology_image_filter', 'binary_thinning_image_filter', 'binary_dilate_image_filter', 'erode_object_morphology_image_filter', )
