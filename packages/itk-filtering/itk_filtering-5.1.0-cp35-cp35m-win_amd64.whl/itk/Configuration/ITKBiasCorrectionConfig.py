depends = ('ITKPyBase', 'ITKOptimizers', 'ITKImageIntensity', 'ITKImageGrid', 'ITKCommon', )
templates = (
  ('N4BiasFieldCorrectionImageFilter', 'itk::N4BiasFieldCorrectionImageFilter', 'itkN4BiasFieldCorrectionImageFilterISS2IUC2ISS2', True, 'itk::Image< signed short,2 >, itk::Image< unsigned char,2 >, itk::Image< signed short,2 >'),
  ('N4BiasFieldCorrectionImageFilter', 'itk::N4BiasFieldCorrectionImageFilter', 'itkN4BiasFieldCorrectionImageFilterISS3IUC3ISS3', True, 'itk::Image< signed short,3 >, itk::Image< unsigned char,3 >, itk::Image< signed short,3 >'),
  ('N4BiasFieldCorrectionImageFilter', 'itk::N4BiasFieldCorrectionImageFilter', 'itkN4BiasFieldCorrectionImageFilterISS2IUC2IUC2', True, 'itk::Image< signed short,2 >, itk::Image< unsigned char,2 >, itk::Image< unsigned char,2 >'),
  ('N4BiasFieldCorrectionImageFilter', 'itk::N4BiasFieldCorrectionImageFilter', 'itkN4BiasFieldCorrectionImageFilterISS3IUC3IUC3', True, 'itk::Image< signed short,3 >, itk::Image< unsigned char,3 >, itk::Image< unsigned char,3 >'),
  ('N4BiasFieldCorrectionImageFilter', 'itk::N4BiasFieldCorrectionImageFilter', 'itkN4BiasFieldCorrectionImageFilterISS2IUC2IUS2', True, 'itk::Image< signed short,2 >, itk::Image< unsigned char,2 >, itk::Image< unsigned short,2 >'),
  ('N4BiasFieldCorrectionImageFilter', 'itk::N4BiasFieldCorrectionImageFilter', 'itkN4BiasFieldCorrectionImageFilterISS3IUC3IUS3', True, 'itk::Image< signed short,3 >, itk::Image< unsigned char,3 >, itk::Image< unsigned short,3 >'),
  ('N4BiasFieldCorrectionImageFilter', 'itk::N4BiasFieldCorrectionImageFilter', 'itkN4BiasFieldCorrectionImageFilterISS2IUC2IF2', True, 'itk::Image< signed short,2 >, itk::Image< unsigned char,2 >, itk::Image< float,2 >'),
  ('N4BiasFieldCorrectionImageFilter', 'itk::N4BiasFieldCorrectionImageFilter', 'itkN4BiasFieldCorrectionImageFilterISS3IUC3IF3', True, 'itk::Image< signed short,3 >, itk::Image< unsigned char,3 >, itk::Image< float,3 >'),
  ('N4BiasFieldCorrectionImageFilter', 'itk::N4BiasFieldCorrectionImageFilter', 'itkN4BiasFieldCorrectionImageFilterISS2IUC2ID2', True, 'itk::Image< signed short,2 >, itk::Image< unsigned char,2 >, itk::Image< double,2 >'),
  ('N4BiasFieldCorrectionImageFilter', 'itk::N4BiasFieldCorrectionImageFilter', 'itkN4BiasFieldCorrectionImageFilterISS3IUC3ID3', True, 'itk::Image< signed short,3 >, itk::Image< unsigned char,3 >, itk::Image< double,3 >'),
  ('N4BiasFieldCorrectionImageFilter', 'itk::N4BiasFieldCorrectionImageFilter', 'itkN4BiasFieldCorrectionImageFilterIUC2IUC2ISS2', True, 'itk::Image< unsigned char,2 >, itk::Image< unsigned char,2 >, itk::Image< signed short,2 >'),
  ('N4BiasFieldCorrectionImageFilter', 'itk::N4BiasFieldCorrectionImageFilter', 'itkN4BiasFieldCorrectionImageFilterIUC3IUC3ISS3', True, 'itk::Image< unsigned char,3 >, itk::Image< unsigned char,3 >, itk::Image< signed short,3 >'),
  ('N4BiasFieldCorrectionImageFilter', 'itk::N4BiasFieldCorrectionImageFilter', 'itkN4BiasFieldCorrectionImageFilterIUC2IUC2IUC2', True, 'itk::Image< unsigned char,2 >, itk::Image< unsigned char,2 >, itk::Image< unsigned char,2 >'),
  ('N4BiasFieldCorrectionImageFilter', 'itk::N4BiasFieldCorrectionImageFilter', 'itkN4BiasFieldCorrectionImageFilterIUC3IUC3IUC3', True, 'itk::Image< unsigned char,3 >, itk::Image< unsigned char,3 >, itk::Image< unsigned char,3 >'),
  ('N4BiasFieldCorrectionImageFilter', 'itk::N4BiasFieldCorrectionImageFilter', 'itkN4BiasFieldCorrectionImageFilterIUC2IUC2IUS2', True, 'itk::Image< unsigned char,2 >, itk::Image< unsigned char,2 >, itk::Image< unsigned short,2 >'),
  ('N4BiasFieldCorrectionImageFilter', 'itk::N4BiasFieldCorrectionImageFilter', 'itkN4BiasFieldCorrectionImageFilterIUC3IUC3IUS3', True, 'itk::Image< unsigned char,3 >, itk::Image< unsigned char,3 >, itk::Image< unsigned short,3 >'),
  ('N4BiasFieldCorrectionImageFilter', 'itk::N4BiasFieldCorrectionImageFilter', 'itkN4BiasFieldCorrectionImageFilterIUC2IUC2IF2', True, 'itk::Image< unsigned char,2 >, itk::Image< unsigned char,2 >, itk::Image< float,2 >'),
  ('N4BiasFieldCorrectionImageFilter', 'itk::N4BiasFieldCorrectionImageFilter', 'itkN4BiasFieldCorrectionImageFilterIUC3IUC3IF3', True, 'itk::Image< unsigned char,3 >, itk::Image< unsigned char,3 >, itk::Image< float,3 >'),
  ('N4BiasFieldCorrectionImageFilter', 'itk::N4BiasFieldCorrectionImageFilter', 'itkN4BiasFieldCorrectionImageFilterIUC2IUC2ID2', True, 'itk::Image< unsigned char,2 >, itk::Image< unsigned char,2 >, itk::Image< double,2 >'),
  ('N4BiasFieldCorrectionImageFilter', 'itk::N4BiasFieldCorrectionImageFilter', 'itkN4BiasFieldCorrectionImageFilterIUC3IUC3ID3', True, 'itk::Image< unsigned char,3 >, itk::Image< unsigned char,3 >, itk::Image< double,3 >'),
  ('N4BiasFieldCorrectionImageFilter', 'itk::N4BiasFieldCorrectionImageFilter', 'itkN4BiasFieldCorrectionImageFilterIUS2IUC2ISS2', True, 'itk::Image< unsigned short,2 >, itk::Image< unsigned char,2 >, itk::Image< signed short,2 >'),
  ('N4BiasFieldCorrectionImageFilter', 'itk::N4BiasFieldCorrectionImageFilter', 'itkN4BiasFieldCorrectionImageFilterIUS3IUC3ISS3', True, 'itk::Image< unsigned short,3 >, itk::Image< unsigned char,3 >, itk::Image< signed short,3 >'),
  ('N4BiasFieldCorrectionImageFilter', 'itk::N4BiasFieldCorrectionImageFilter', 'itkN4BiasFieldCorrectionImageFilterIUS2IUC2IUC2', True, 'itk::Image< unsigned short,2 >, itk::Image< unsigned char,2 >, itk::Image< unsigned char,2 >'),
  ('N4BiasFieldCorrectionImageFilter', 'itk::N4BiasFieldCorrectionImageFilter', 'itkN4BiasFieldCorrectionImageFilterIUS3IUC3IUC3', True, 'itk::Image< unsigned short,3 >, itk::Image< unsigned char,3 >, itk::Image< unsigned char,3 >'),
  ('N4BiasFieldCorrectionImageFilter', 'itk::N4BiasFieldCorrectionImageFilter', 'itkN4BiasFieldCorrectionImageFilterIUS2IUC2IUS2', True, 'itk::Image< unsigned short,2 >, itk::Image< unsigned char,2 >, itk::Image< unsigned short,2 >'),
  ('N4BiasFieldCorrectionImageFilter', 'itk::N4BiasFieldCorrectionImageFilter', 'itkN4BiasFieldCorrectionImageFilterIUS3IUC3IUS3', True, 'itk::Image< unsigned short,3 >, itk::Image< unsigned char,3 >, itk::Image< unsigned short,3 >'),
  ('N4BiasFieldCorrectionImageFilter', 'itk::N4BiasFieldCorrectionImageFilter', 'itkN4BiasFieldCorrectionImageFilterIUS2IUC2IF2', True, 'itk::Image< unsigned short,2 >, itk::Image< unsigned char,2 >, itk::Image< float,2 >'),
  ('N4BiasFieldCorrectionImageFilter', 'itk::N4BiasFieldCorrectionImageFilter', 'itkN4BiasFieldCorrectionImageFilterIUS3IUC3IF3', True, 'itk::Image< unsigned short,3 >, itk::Image< unsigned char,3 >, itk::Image< float,3 >'),
  ('N4BiasFieldCorrectionImageFilter', 'itk::N4BiasFieldCorrectionImageFilter', 'itkN4BiasFieldCorrectionImageFilterIUS2IUC2ID2', True, 'itk::Image< unsigned short,2 >, itk::Image< unsigned char,2 >, itk::Image< double,2 >'),
  ('N4BiasFieldCorrectionImageFilter', 'itk::N4BiasFieldCorrectionImageFilter', 'itkN4BiasFieldCorrectionImageFilterIUS3IUC3ID3', True, 'itk::Image< unsigned short,3 >, itk::Image< unsigned char,3 >, itk::Image< double,3 >'),
  ('N4BiasFieldCorrectionImageFilter', 'itk::N4BiasFieldCorrectionImageFilter', 'itkN4BiasFieldCorrectionImageFilterIF2IUC2ISS2', True, 'itk::Image< float,2 >, itk::Image< unsigned char,2 >, itk::Image< signed short,2 >'),
  ('N4BiasFieldCorrectionImageFilter', 'itk::N4BiasFieldCorrectionImageFilter', 'itkN4BiasFieldCorrectionImageFilterIF3IUC3ISS3', True, 'itk::Image< float,3 >, itk::Image< unsigned char,3 >, itk::Image< signed short,3 >'),
  ('N4BiasFieldCorrectionImageFilter', 'itk::N4BiasFieldCorrectionImageFilter', 'itkN4BiasFieldCorrectionImageFilterIF2IUC2IUC2', True, 'itk::Image< float,2 >, itk::Image< unsigned char,2 >, itk::Image< unsigned char,2 >'),
  ('N4BiasFieldCorrectionImageFilter', 'itk::N4BiasFieldCorrectionImageFilter', 'itkN4BiasFieldCorrectionImageFilterIF3IUC3IUC3', True, 'itk::Image< float,3 >, itk::Image< unsigned char,3 >, itk::Image< unsigned char,3 >'),
  ('N4BiasFieldCorrectionImageFilter', 'itk::N4BiasFieldCorrectionImageFilter', 'itkN4BiasFieldCorrectionImageFilterIF2IUC2IUS2', True, 'itk::Image< float,2 >, itk::Image< unsigned char,2 >, itk::Image< unsigned short,2 >'),
  ('N4BiasFieldCorrectionImageFilter', 'itk::N4BiasFieldCorrectionImageFilter', 'itkN4BiasFieldCorrectionImageFilterIF3IUC3IUS3', True, 'itk::Image< float,3 >, itk::Image< unsigned char,3 >, itk::Image< unsigned short,3 >'),
  ('N4BiasFieldCorrectionImageFilter', 'itk::N4BiasFieldCorrectionImageFilter', 'itkN4BiasFieldCorrectionImageFilterIF2IUC2IF2', True, 'itk::Image< float,2 >, itk::Image< unsigned char,2 >, itk::Image< float,2 >'),
  ('N4BiasFieldCorrectionImageFilter', 'itk::N4BiasFieldCorrectionImageFilter', 'itkN4BiasFieldCorrectionImageFilterIF3IUC3IF3', True, 'itk::Image< float,3 >, itk::Image< unsigned char,3 >, itk::Image< float,3 >'),
  ('N4BiasFieldCorrectionImageFilter', 'itk::N4BiasFieldCorrectionImageFilter', 'itkN4BiasFieldCorrectionImageFilterIF2IUC2ID2', True, 'itk::Image< float,2 >, itk::Image< unsigned char,2 >, itk::Image< double,2 >'),
  ('N4BiasFieldCorrectionImageFilter', 'itk::N4BiasFieldCorrectionImageFilter', 'itkN4BiasFieldCorrectionImageFilterIF3IUC3ID3', True, 'itk::Image< float,3 >, itk::Image< unsigned char,3 >, itk::Image< double,3 >'),
  ('N4BiasFieldCorrectionImageFilter', 'itk::N4BiasFieldCorrectionImageFilter', 'itkN4BiasFieldCorrectionImageFilterID2IUC2ISS2', True, 'itk::Image< double,2 >, itk::Image< unsigned char,2 >, itk::Image< signed short,2 >'),
  ('N4BiasFieldCorrectionImageFilter', 'itk::N4BiasFieldCorrectionImageFilter', 'itkN4BiasFieldCorrectionImageFilterID3IUC3ISS3', True, 'itk::Image< double,3 >, itk::Image< unsigned char,3 >, itk::Image< signed short,3 >'),
  ('N4BiasFieldCorrectionImageFilter', 'itk::N4BiasFieldCorrectionImageFilter', 'itkN4BiasFieldCorrectionImageFilterID2IUC2IUC2', True, 'itk::Image< double,2 >, itk::Image< unsigned char,2 >, itk::Image< unsigned char,2 >'),
  ('N4BiasFieldCorrectionImageFilter', 'itk::N4BiasFieldCorrectionImageFilter', 'itkN4BiasFieldCorrectionImageFilterID3IUC3IUC3', True, 'itk::Image< double,3 >, itk::Image< unsigned char,3 >, itk::Image< unsigned char,3 >'),
  ('N4BiasFieldCorrectionImageFilter', 'itk::N4BiasFieldCorrectionImageFilter', 'itkN4BiasFieldCorrectionImageFilterID2IUC2IUS2', True, 'itk::Image< double,2 >, itk::Image< unsigned char,2 >, itk::Image< unsigned short,2 >'),
  ('N4BiasFieldCorrectionImageFilter', 'itk::N4BiasFieldCorrectionImageFilter', 'itkN4BiasFieldCorrectionImageFilterID3IUC3IUS3', True, 'itk::Image< double,3 >, itk::Image< unsigned char,3 >, itk::Image< unsigned short,3 >'),
  ('N4BiasFieldCorrectionImageFilter', 'itk::N4BiasFieldCorrectionImageFilter', 'itkN4BiasFieldCorrectionImageFilterID2IUC2IF2', True, 'itk::Image< double,2 >, itk::Image< unsigned char,2 >, itk::Image< float,2 >'),
  ('N4BiasFieldCorrectionImageFilter', 'itk::N4BiasFieldCorrectionImageFilter', 'itkN4BiasFieldCorrectionImageFilterID3IUC3IF3', True, 'itk::Image< double,3 >, itk::Image< unsigned char,3 >, itk::Image< float,3 >'),
  ('N4BiasFieldCorrectionImageFilter', 'itk::N4BiasFieldCorrectionImageFilter', 'itkN4BiasFieldCorrectionImageFilterID2IUC2ID2', True, 'itk::Image< double,2 >, itk::Image< unsigned char,2 >, itk::Image< double,2 >'),
  ('N4BiasFieldCorrectionImageFilter', 'itk::N4BiasFieldCorrectionImageFilter', 'itkN4BiasFieldCorrectionImageFilterID3IUC3ID3', True, 'itk::Image< double,3 >, itk::Image< unsigned char,3 >, itk::Image< double,3 >'),
)
snake_case_functions = ('n4_bias_field_correction_image_filter', 'image_to_image_filter', )
