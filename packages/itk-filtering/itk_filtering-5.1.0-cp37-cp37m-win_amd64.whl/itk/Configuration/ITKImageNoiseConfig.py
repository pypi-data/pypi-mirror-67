depends = ('ITKPyBase', 'ITKStatistics', )
templates = (
  ('AdditiveGaussianNoiseImageFilter', 'itk::AdditiveGaussianNoiseImageFilter', 'itkAdditiveGaussianNoiseImageFilterISS2ISS2', True, 'itk::Image< signed short,2 >, itk::Image< signed short,2 >'),
  ('AdditiveGaussianNoiseImageFilter', 'itk::AdditiveGaussianNoiseImageFilter', 'itkAdditiveGaussianNoiseImageFilterISS3ISS3', True, 'itk::Image< signed short,3 >, itk::Image< signed short,3 >'),
  ('AdditiveGaussianNoiseImageFilter', 'itk::AdditiveGaussianNoiseImageFilter', 'itkAdditiveGaussianNoiseImageFilterIUC2IUC2', True, 'itk::Image< unsigned char,2 >, itk::Image< unsigned char,2 >'),
  ('AdditiveGaussianNoiseImageFilter', 'itk::AdditiveGaussianNoiseImageFilter', 'itkAdditiveGaussianNoiseImageFilterIUC3IUC3', True, 'itk::Image< unsigned char,3 >, itk::Image< unsigned char,3 >'),
  ('AdditiveGaussianNoiseImageFilter', 'itk::AdditiveGaussianNoiseImageFilter', 'itkAdditiveGaussianNoiseImageFilterIUS2IUS2', True, 'itk::Image< unsigned short,2 >, itk::Image< unsigned short,2 >'),
  ('AdditiveGaussianNoiseImageFilter', 'itk::AdditiveGaussianNoiseImageFilter', 'itkAdditiveGaussianNoiseImageFilterIUS3IUS3', True, 'itk::Image< unsigned short,3 >, itk::Image< unsigned short,3 >'),
  ('AdditiveGaussianNoiseImageFilter', 'itk::AdditiveGaussianNoiseImageFilter', 'itkAdditiveGaussianNoiseImageFilterIF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >'),
  ('AdditiveGaussianNoiseImageFilter', 'itk::AdditiveGaussianNoiseImageFilter', 'itkAdditiveGaussianNoiseImageFilterIF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >'),
  ('AdditiveGaussianNoiseImageFilter', 'itk::AdditiveGaussianNoiseImageFilter', 'itkAdditiveGaussianNoiseImageFilterID2ID2', True, 'itk::Image< double,2 >, itk::Image< double,2 >'),
  ('AdditiveGaussianNoiseImageFilter', 'itk::AdditiveGaussianNoiseImageFilter', 'itkAdditiveGaussianNoiseImageFilterID3ID3', True, 'itk::Image< double,3 >, itk::Image< double,3 >'),
  ('NoiseBaseImageFilter', 'itk::NoiseBaseImageFilter', 'itkNoiseBaseImageFilterISS2ISS2', True, 'itk::Image< signed short,2 >, itk::Image< signed short,2 >'),
  ('NoiseBaseImageFilter', 'itk::NoiseBaseImageFilter', 'itkNoiseBaseImageFilterISS3ISS3', True, 'itk::Image< signed short,3 >, itk::Image< signed short,3 >'),
  ('NoiseBaseImageFilter', 'itk::NoiseBaseImageFilter', 'itkNoiseBaseImageFilterIUC2IUC2', True, 'itk::Image< unsigned char,2 >, itk::Image< unsigned char,2 >'),
  ('NoiseBaseImageFilter', 'itk::NoiseBaseImageFilter', 'itkNoiseBaseImageFilterIUC3IUC3', True, 'itk::Image< unsigned char,3 >, itk::Image< unsigned char,3 >'),
  ('NoiseBaseImageFilter', 'itk::NoiseBaseImageFilter', 'itkNoiseBaseImageFilterIUS2IUS2', True, 'itk::Image< unsigned short,2 >, itk::Image< unsigned short,2 >'),
  ('NoiseBaseImageFilter', 'itk::NoiseBaseImageFilter', 'itkNoiseBaseImageFilterIUS3IUS3', True, 'itk::Image< unsigned short,3 >, itk::Image< unsigned short,3 >'),
  ('NoiseBaseImageFilter', 'itk::NoiseBaseImageFilter', 'itkNoiseBaseImageFilterIF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >'),
  ('NoiseBaseImageFilter', 'itk::NoiseBaseImageFilter', 'itkNoiseBaseImageFilterIF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >'),
  ('NoiseBaseImageFilter', 'itk::NoiseBaseImageFilter', 'itkNoiseBaseImageFilterID2ID2', True, 'itk::Image< double,2 >, itk::Image< double,2 >'),
  ('NoiseBaseImageFilter', 'itk::NoiseBaseImageFilter', 'itkNoiseBaseImageFilterID3ID3', True, 'itk::Image< double,3 >, itk::Image< double,3 >'),
  ('SaltAndPepperNoiseImageFilter', 'itk::SaltAndPepperNoiseImageFilter', 'itkSaltAndPepperNoiseImageFilterISS2ISS2', True, 'itk::Image< signed short,2 >, itk::Image< signed short,2 >'),
  ('SaltAndPepperNoiseImageFilter', 'itk::SaltAndPepperNoiseImageFilter', 'itkSaltAndPepperNoiseImageFilterISS3ISS3', True, 'itk::Image< signed short,3 >, itk::Image< signed short,3 >'),
  ('SaltAndPepperNoiseImageFilter', 'itk::SaltAndPepperNoiseImageFilter', 'itkSaltAndPepperNoiseImageFilterIUC2IUC2', True, 'itk::Image< unsigned char,2 >, itk::Image< unsigned char,2 >'),
  ('SaltAndPepperNoiseImageFilter', 'itk::SaltAndPepperNoiseImageFilter', 'itkSaltAndPepperNoiseImageFilterIUC3IUC3', True, 'itk::Image< unsigned char,3 >, itk::Image< unsigned char,3 >'),
  ('SaltAndPepperNoiseImageFilter', 'itk::SaltAndPepperNoiseImageFilter', 'itkSaltAndPepperNoiseImageFilterIUS2IUS2', True, 'itk::Image< unsigned short,2 >, itk::Image< unsigned short,2 >'),
  ('SaltAndPepperNoiseImageFilter', 'itk::SaltAndPepperNoiseImageFilter', 'itkSaltAndPepperNoiseImageFilterIUS3IUS3', True, 'itk::Image< unsigned short,3 >, itk::Image< unsigned short,3 >'),
  ('SaltAndPepperNoiseImageFilter', 'itk::SaltAndPepperNoiseImageFilter', 'itkSaltAndPepperNoiseImageFilterIF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >'),
  ('SaltAndPepperNoiseImageFilter', 'itk::SaltAndPepperNoiseImageFilter', 'itkSaltAndPepperNoiseImageFilterIF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >'),
  ('SaltAndPepperNoiseImageFilter', 'itk::SaltAndPepperNoiseImageFilter', 'itkSaltAndPepperNoiseImageFilterID2ID2', True, 'itk::Image< double,2 >, itk::Image< double,2 >'),
  ('SaltAndPepperNoiseImageFilter', 'itk::SaltAndPepperNoiseImageFilter', 'itkSaltAndPepperNoiseImageFilterID3ID3', True, 'itk::Image< double,3 >, itk::Image< double,3 >'),
  ('ShotNoiseImageFilter', 'itk::ShotNoiseImageFilter', 'itkShotNoiseImageFilterISS2ISS2', True, 'itk::Image< signed short,2 >, itk::Image< signed short,2 >'),
  ('ShotNoiseImageFilter', 'itk::ShotNoiseImageFilter', 'itkShotNoiseImageFilterISS3ISS3', True, 'itk::Image< signed short,3 >, itk::Image< signed short,3 >'),
  ('ShotNoiseImageFilter', 'itk::ShotNoiseImageFilter', 'itkShotNoiseImageFilterIUC2IUC2', True, 'itk::Image< unsigned char,2 >, itk::Image< unsigned char,2 >'),
  ('ShotNoiseImageFilter', 'itk::ShotNoiseImageFilter', 'itkShotNoiseImageFilterIUC3IUC3', True, 'itk::Image< unsigned char,3 >, itk::Image< unsigned char,3 >'),
  ('ShotNoiseImageFilter', 'itk::ShotNoiseImageFilter', 'itkShotNoiseImageFilterIUS2IUS2', True, 'itk::Image< unsigned short,2 >, itk::Image< unsigned short,2 >'),
  ('ShotNoiseImageFilter', 'itk::ShotNoiseImageFilter', 'itkShotNoiseImageFilterIUS3IUS3', True, 'itk::Image< unsigned short,3 >, itk::Image< unsigned short,3 >'),
  ('ShotNoiseImageFilter', 'itk::ShotNoiseImageFilter', 'itkShotNoiseImageFilterIF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >'),
  ('ShotNoiseImageFilter', 'itk::ShotNoiseImageFilter', 'itkShotNoiseImageFilterIF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >'),
  ('ShotNoiseImageFilter', 'itk::ShotNoiseImageFilter', 'itkShotNoiseImageFilterID2ID2', True, 'itk::Image< double,2 >, itk::Image< double,2 >'),
  ('ShotNoiseImageFilter', 'itk::ShotNoiseImageFilter', 'itkShotNoiseImageFilterID3ID3', True, 'itk::Image< double,3 >, itk::Image< double,3 >'),
  ('SpeckleNoiseImageFilter', 'itk::SpeckleNoiseImageFilter', 'itkSpeckleNoiseImageFilterISS2ISS2', True, 'itk::Image< signed short,2 >, itk::Image< signed short,2 >'),
  ('SpeckleNoiseImageFilter', 'itk::SpeckleNoiseImageFilter', 'itkSpeckleNoiseImageFilterISS3ISS3', True, 'itk::Image< signed short,3 >, itk::Image< signed short,3 >'),
  ('SpeckleNoiseImageFilter', 'itk::SpeckleNoiseImageFilter', 'itkSpeckleNoiseImageFilterIUC2IUC2', True, 'itk::Image< unsigned char,2 >, itk::Image< unsigned char,2 >'),
  ('SpeckleNoiseImageFilter', 'itk::SpeckleNoiseImageFilter', 'itkSpeckleNoiseImageFilterIUC3IUC3', True, 'itk::Image< unsigned char,3 >, itk::Image< unsigned char,3 >'),
  ('SpeckleNoiseImageFilter', 'itk::SpeckleNoiseImageFilter', 'itkSpeckleNoiseImageFilterIUS2IUS2', True, 'itk::Image< unsigned short,2 >, itk::Image< unsigned short,2 >'),
  ('SpeckleNoiseImageFilter', 'itk::SpeckleNoiseImageFilter', 'itkSpeckleNoiseImageFilterIUS3IUS3', True, 'itk::Image< unsigned short,3 >, itk::Image< unsigned short,3 >'),
  ('SpeckleNoiseImageFilter', 'itk::SpeckleNoiseImageFilter', 'itkSpeckleNoiseImageFilterIF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >'),
  ('SpeckleNoiseImageFilter', 'itk::SpeckleNoiseImageFilter', 'itkSpeckleNoiseImageFilterIF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >'),
  ('SpeckleNoiseImageFilter', 'itk::SpeckleNoiseImageFilter', 'itkSpeckleNoiseImageFilterID2ID2', True, 'itk::Image< double,2 >, itk::Image< double,2 >'),
  ('SpeckleNoiseImageFilter', 'itk::SpeckleNoiseImageFilter', 'itkSpeckleNoiseImageFilterID3ID3', True, 'itk::Image< double,3 >, itk::Image< double,3 >'),
)
snake_case_functions = ('salt_and_pepper_noise_image_filter', 'shot_noise_image_filter', 'noise_base_image_filter', 'speckle_noise_image_filter', 'additive_gaussian_noise_image_filter', )
