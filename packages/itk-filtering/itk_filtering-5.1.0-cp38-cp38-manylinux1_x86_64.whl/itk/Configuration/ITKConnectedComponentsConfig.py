depends = ('ITKPyBase', 'ITKThresholding', 'ITKImageLabel', 'ITKImageIntensity', 'ITKImageGrid', )
templates = (
  ('ConnectedComponentImageFilter', 'itk::ConnectedComponentImageFilter', 'itkConnectedComponentImageFilterISS2IUL2', True, 'itk::Image< signed short,2 >, itk::Image< unsigned long,2 >'),
  ('ConnectedComponentImageFilter', 'itk::ConnectedComponentImageFilter', 'itkConnectedComponentImageFilterISS3IUL3', True, 'itk::Image< signed short,3 >, itk::Image< unsigned long,3 >'),
  ('ConnectedComponentImageFilter', 'itk::ConnectedComponentImageFilter', 'itkConnectedComponentImageFilterISS2ISS2', True, 'itk::Image< signed short,2 >, itk::Image< signed short,2 >'),
  ('ConnectedComponentImageFilter', 'itk::ConnectedComponentImageFilter', 'itkConnectedComponentImageFilterISS3ISS3', True, 'itk::Image< signed short,3 >, itk::Image< signed short,3 >'),
  ('ConnectedComponentImageFilter', 'itk::ConnectedComponentImageFilter', 'itkConnectedComponentImageFilterISS2IUC2', True, 'itk::Image< signed short,2 >, itk::Image< unsigned char,2 >'),
  ('ConnectedComponentImageFilter', 'itk::ConnectedComponentImageFilter', 'itkConnectedComponentImageFilterISS3IUC3', True, 'itk::Image< signed short,3 >, itk::Image< unsigned char,3 >'),
  ('ConnectedComponentImageFilter', 'itk::ConnectedComponentImageFilter', 'itkConnectedComponentImageFilterISS2IUS2', True, 'itk::Image< signed short,2 >, itk::Image< unsigned short,2 >'),
  ('ConnectedComponentImageFilter', 'itk::ConnectedComponentImageFilter', 'itkConnectedComponentImageFilterISS3IUS3', True, 'itk::Image< signed short,3 >, itk::Image< unsigned short,3 >'),
  ('ConnectedComponentImageFilter', 'itk::ConnectedComponentImageFilter', 'itkConnectedComponentImageFilterIUC2IUL2', True, 'itk::Image< unsigned char,2 >, itk::Image< unsigned long,2 >'),
  ('ConnectedComponentImageFilter', 'itk::ConnectedComponentImageFilter', 'itkConnectedComponentImageFilterIUC3IUL3', True, 'itk::Image< unsigned char,3 >, itk::Image< unsigned long,3 >'),
  ('ConnectedComponentImageFilter', 'itk::ConnectedComponentImageFilter', 'itkConnectedComponentImageFilterIUC2ISS2', True, 'itk::Image< unsigned char,2 >, itk::Image< signed short,2 >'),
  ('ConnectedComponentImageFilter', 'itk::ConnectedComponentImageFilter', 'itkConnectedComponentImageFilterIUC3ISS3', True, 'itk::Image< unsigned char,3 >, itk::Image< signed short,3 >'),
  ('ConnectedComponentImageFilter', 'itk::ConnectedComponentImageFilter', 'itkConnectedComponentImageFilterIUC2IUC2', True, 'itk::Image< unsigned char,2 >, itk::Image< unsigned char,2 >'),
  ('ConnectedComponentImageFilter', 'itk::ConnectedComponentImageFilter', 'itkConnectedComponentImageFilterIUC3IUC3', True, 'itk::Image< unsigned char,3 >, itk::Image< unsigned char,3 >'),
  ('ConnectedComponentImageFilter', 'itk::ConnectedComponentImageFilter', 'itkConnectedComponentImageFilterIUC2IUS2', True, 'itk::Image< unsigned char,2 >, itk::Image< unsigned short,2 >'),
  ('ConnectedComponentImageFilter', 'itk::ConnectedComponentImageFilter', 'itkConnectedComponentImageFilterIUC3IUS3', True, 'itk::Image< unsigned char,3 >, itk::Image< unsigned short,3 >'),
  ('ConnectedComponentImageFilter', 'itk::ConnectedComponentImageFilter', 'itkConnectedComponentImageFilterIUS2IUL2', True, 'itk::Image< unsigned short,2 >, itk::Image< unsigned long,2 >'),
  ('ConnectedComponentImageFilter', 'itk::ConnectedComponentImageFilter', 'itkConnectedComponentImageFilterIUS3IUL3', True, 'itk::Image< unsigned short,3 >, itk::Image< unsigned long,3 >'),
  ('ConnectedComponentImageFilter', 'itk::ConnectedComponentImageFilter', 'itkConnectedComponentImageFilterIUS2ISS2', True, 'itk::Image< unsigned short,2 >, itk::Image< signed short,2 >'),
  ('ConnectedComponentImageFilter', 'itk::ConnectedComponentImageFilter', 'itkConnectedComponentImageFilterIUS3ISS3', True, 'itk::Image< unsigned short,3 >, itk::Image< signed short,3 >'),
  ('ConnectedComponentImageFilter', 'itk::ConnectedComponentImageFilter', 'itkConnectedComponentImageFilterIUS2IUC2', True, 'itk::Image< unsigned short,2 >, itk::Image< unsigned char,2 >'),
  ('ConnectedComponentImageFilter', 'itk::ConnectedComponentImageFilter', 'itkConnectedComponentImageFilterIUS3IUC3', True, 'itk::Image< unsigned short,3 >, itk::Image< unsigned char,3 >'),
  ('ConnectedComponentImageFilter', 'itk::ConnectedComponentImageFilter', 'itkConnectedComponentImageFilterIUS2IUS2', True, 'itk::Image< unsigned short,2 >, itk::Image< unsigned short,2 >'),
  ('ConnectedComponentImageFilter', 'itk::ConnectedComponentImageFilter', 'itkConnectedComponentImageFilterIUS3IUS3', True, 'itk::Image< unsigned short,3 >, itk::Image< unsigned short,3 >'),
  ('ConnectedComponentImageFilter', 'itk::ConnectedComponentImageFilter', 'itkConnectedComponentImageFilterIVF22ISS2', True, 'itk::Image< itk::Vector< float,2 >,2 >, itk::Image< signed short,2 >'),
  ('ConnectedComponentImageFilter', 'itk::ConnectedComponentImageFilter', 'itkConnectedComponentImageFilterIVF23ISS3', True, 'itk::Image< itk::Vector< float,2 >,3 >, itk::Image< signed short,3 >'),
  ('ConnectedComponentImageFilter', 'itk::ConnectedComponentImageFilter', 'itkConnectedComponentImageFilterIVF32ISS2', True, 'itk::Image< itk::Vector< float,3 >,2 >, itk::Image< signed short,2 >'),
  ('ConnectedComponentImageFilter', 'itk::ConnectedComponentImageFilter', 'itkConnectedComponentImageFilterIVF33ISS3', True, 'itk::Image< itk::Vector< float,3 >,3 >, itk::Image< signed short,3 >'),
  ('ConnectedComponentImageFilter', 'itk::ConnectedComponentImageFilter', 'itkConnectedComponentImageFilterIVF42ISS2', True, 'itk::Image< itk::Vector< float,4 >,2 >, itk::Image< signed short,2 >'),
  ('ConnectedComponentImageFilter', 'itk::ConnectedComponentImageFilter', 'itkConnectedComponentImageFilterIVF43ISS3', True, 'itk::Image< itk::Vector< float,4 >,3 >, itk::Image< signed short,3 >'),
  ('ConnectedComponentImageFilter', 'itk::ConnectedComponentImageFilter', 'itkConnectedComponentImageFilterIVF22IUC2', True, 'itk::Image< itk::Vector< float,2 >,2 >, itk::Image< unsigned char,2 >'),
  ('ConnectedComponentImageFilter', 'itk::ConnectedComponentImageFilter', 'itkConnectedComponentImageFilterIVF23IUC3', True, 'itk::Image< itk::Vector< float,2 >,3 >, itk::Image< unsigned char,3 >'),
  ('ConnectedComponentImageFilter', 'itk::ConnectedComponentImageFilter', 'itkConnectedComponentImageFilterIVF32IUC2', True, 'itk::Image< itk::Vector< float,3 >,2 >, itk::Image< unsigned char,2 >'),
  ('ConnectedComponentImageFilter', 'itk::ConnectedComponentImageFilter', 'itkConnectedComponentImageFilterIVF33IUC3', True, 'itk::Image< itk::Vector< float,3 >,3 >, itk::Image< unsigned char,3 >'),
  ('ConnectedComponentImageFilter', 'itk::ConnectedComponentImageFilter', 'itkConnectedComponentImageFilterIVF42IUC2', True, 'itk::Image< itk::Vector< float,4 >,2 >, itk::Image< unsigned char,2 >'),
  ('ConnectedComponentImageFilter', 'itk::ConnectedComponentImageFilter', 'itkConnectedComponentImageFilterIVF43IUC3', True, 'itk::Image< itk::Vector< float,4 >,3 >, itk::Image< unsigned char,3 >'),
  ('ConnectedComponentImageFilter', 'itk::ConnectedComponentImageFilter', 'itkConnectedComponentImageFilterIVF22IUS2', True, 'itk::Image< itk::Vector< float,2 >,2 >, itk::Image< unsigned short,2 >'),
  ('ConnectedComponentImageFilter', 'itk::ConnectedComponentImageFilter', 'itkConnectedComponentImageFilterIVF23IUS3', True, 'itk::Image< itk::Vector< float,2 >,3 >, itk::Image< unsigned short,3 >'),
  ('ConnectedComponentImageFilter', 'itk::ConnectedComponentImageFilter', 'itkConnectedComponentImageFilterIVF32IUS2', True, 'itk::Image< itk::Vector< float,3 >,2 >, itk::Image< unsigned short,2 >'),
  ('ConnectedComponentImageFilter', 'itk::ConnectedComponentImageFilter', 'itkConnectedComponentImageFilterIVF33IUS3', True, 'itk::Image< itk::Vector< float,3 >,3 >, itk::Image< unsigned short,3 >'),
  ('ConnectedComponentImageFilter', 'itk::ConnectedComponentImageFilter', 'itkConnectedComponentImageFilterIVF42IUS2', True, 'itk::Image< itk::Vector< float,4 >,2 >, itk::Image< unsigned short,2 >'),
  ('ConnectedComponentImageFilter', 'itk::ConnectedComponentImageFilter', 'itkConnectedComponentImageFilterIVF43IUS3', True, 'itk::Image< itk::Vector< float,4 >,3 >, itk::Image< unsigned short,3 >'),
  ('ConnectedComponentImageFilter', 'itk::ConnectedComponentImageFilter', 'itkConnectedComponentImageFilterICVF22ISS2', True, 'itk::Image< itk::CovariantVector< float,2 >,2 >, itk::Image< signed short,2 >'),
  ('ConnectedComponentImageFilter', 'itk::ConnectedComponentImageFilter', 'itkConnectedComponentImageFilterICVF23ISS3', True, 'itk::Image< itk::CovariantVector< float,2 >,3 >, itk::Image< signed short,3 >'),
  ('ConnectedComponentImageFilter', 'itk::ConnectedComponentImageFilter', 'itkConnectedComponentImageFilterICVF32ISS2', True, 'itk::Image< itk::CovariantVector< float,3 >,2 >, itk::Image< signed short,2 >'),
  ('ConnectedComponentImageFilter', 'itk::ConnectedComponentImageFilter', 'itkConnectedComponentImageFilterICVF33ISS3', True, 'itk::Image< itk::CovariantVector< float,3 >,3 >, itk::Image< signed short,3 >'),
  ('ConnectedComponentImageFilter', 'itk::ConnectedComponentImageFilter', 'itkConnectedComponentImageFilterICVF42ISS2', True, 'itk::Image< itk::CovariantVector< float,4 >,2 >, itk::Image< signed short,2 >'),
  ('ConnectedComponentImageFilter', 'itk::ConnectedComponentImageFilter', 'itkConnectedComponentImageFilterICVF43ISS3', True, 'itk::Image< itk::CovariantVector< float,4 >,3 >, itk::Image< signed short,3 >'),
  ('ConnectedComponentImageFilter', 'itk::ConnectedComponentImageFilter', 'itkConnectedComponentImageFilterICVF22IUC2', True, 'itk::Image< itk::CovariantVector< float,2 >,2 >, itk::Image< unsigned char,2 >'),
  ('ConnectedComponentImageFilter', 'itk::ConnectedComponentImageFilter', 'itkConnectedComponentImageFilterICVF23IUC3', True, 'itk::Image< itk::CovariantVector< float,2 >,3 >, itk::Image< unsigned char,3 >'),
  ('ConnectedComponentImageFilter', 'itk::ConnectedComponentImageFilter', 'itkConnectedComponentImageFilterICVF32IUC2', True, 'itk::Image< itk::CovariantVector< float,3 >,2 >, itk::Image< unsigned char,2 >'),
  ('ConnectedComponentImageFilter', 'itk::ConnectedComponentImageFilter', 'itkConnectedComponentImageFilterICVF33IUC3', True, 'itk::Image< itk::CovariantVector< float,3 >,3 >, itk::Image< unsigned char,3 >'),
  ('ConnectedComponentImageFilter', 'itk::ConnectedComponentImageFilter', 'itkConnectedComponentImageFilterICVF42IUC2', True, 'itk::Image< itk::CovariantVector< float,4 >,2 >, itk::Image< unsigned char,2 >'),
  ('ConnectedComponentImageFilter', 'itk::ConnectedComponentImageFilter', 'itkConnectedComponentImageFilterICVF43IUC3', True, 'itk::Image< itk::CovariantVector< float,4 >,3 >, itk::Image< unsigned char,3 >'),
  ('ConnectedComponentImageFilter', 'itk::ConnectedComponentImageFilter', 'itkConnectedComponentImageFilterICVF22IUS2', True, 'itk::Image< itk::CovariantVector< float,2 >,2 >, itk::Image< unsigned short,2 >'),
  ('ConnectedComponentImageFilter', 'itk::ConnectedComponentImageFilter', 'itkConnectedComponentImageFilterICVF23IUS3', True, 'itk::Image< itk::CovariantVector< float,2 >,3 >, itk::Image< unsigned short,3 >'),
  ('ConnectedComponentImageFilter', 'itk::ConnectedComponentImageFilter', 'itkConnectedComponentImageFilterICVF32IUS2', True, 'itk::Image< itk::CovariantVector< float,3 >,2 >, itk::Image< unsigned short,2 >'),
  ('ConnectedComponentImageFilter', 'itk::ConnectedComponentImageFilter', 'itkConnectedComponentImageFilterICVF33IUS3', True, 'itk::Image< itk::CovariantVector< float,3 >,3 >, itk::Image< unsigned short,3 >'),
  ('ConnectedComponentImageFilter', 'itk::ConnectedComponentImageFilter', 'itkConnectedComponentImageFilterICVF42IUS2', True, 'itk::Image< itk::CovariantVector< float,4 >,2 >, itk::Image< unsigned short,2 >'),
  ('ConnectedComponentImageFilter', 'itk::ConnectedComponentImageFilter', 'itkConnectedComponentImageFilterICVF43IUS3', True, 'itk::Image< itk::CovariantVector< float,4 >,3 >, itk::Image< unsigned short,3 >'),
  ('HardConnectedComponentImageFilter', 'itk::HardConnectedComponentImageFilter', 'itkHardConnectedComponentImageFilterISS2IUL2', True, 'itk::Image< signed short,2 >, itk::Image< unsigned long,2 >'),
  ('HardConnectedComponentImageFilter', 'itk::HardConnectedComponentImageFilter', 'itkHardConnectedComponentImageFilterISS3IUL3', True, 'itk::Image< signed short,3 >, itk::Image< unsigned long,3 >'),
  ('HardConnectedComponentImageFilter', 'itk::HardConnectedComponentImageFilter', 'itkHardConnectedComponentImageFilterISS2ISS2', True, 'itk::Image< signed short,2 >, itk::Image< signed short,2 >'),
  ('HardConnectedComponentImageFilter', 'itk::HardConnectedComponentImageFilter', 'itkHardConnectedComponentImageFilterISS3ISS3', True, 'itk::Image< signed short,3 >, itk::Image< signed short,3 >'),
  ('HardConnectedComponentImageFilter', 'itk::HardConnectedComponentImageFilter', 'itkHardConnectedComponentImageFilterISS2IUC2', True, 'itk::Image< signed short,2 >, itk::Image< unsigned char,2 >'),
  ('HardConnectedComponentImageFilter', 'itk::HardConnectedComponentImageFilter', 'itkHardConnectedComponentImageFilterISS3IUC3', True, 'itk::Image< signed short,3 >, itk::Image< unsigned char,3 >'),
  ('HardConnectedComponentImageFilter', 'itk::HardConnectedComponentImageFilter', 'itkHardConnectedComponentImageFilterISS2IUS2', True, 'itk::Image< signed short,2 >, itk::Image< unsigned short,2 >'),
  ('HardConnectedComponentImageFilter', 'itk::HardConnectedComponentImageFilter', 'itkHardConnectedComponentImageFilterISS3IUS3', True, 'itk::Image< signed short,3 >, itk::Image< unsigned short,3 >'),
  ('HardConnectedComponentImageFilter', 'itk::HardConnectedComponentImageFilter', 'itkHardConnectedComponentImageFilterIUC2IUL2', True, 'itk::Image< unsigned char,2 >, itk::Image< unsigned long,2 >'),
  ('HardConnectedComponentImageFilter', 'itk::HardConnectedComponentImageFilter', 'itkHardConnectedComponentImageFilterIUC3IUL3', True, 'itk::Image< unsigned char,3 >, itk::Image< unsigned long,3 >'),
  ('HardConnectedComponentImageFilter', 'itk::HardConnectedComponentImageFilter', 'itkHardConnectedComponentImageFilterIUC2ISS2', True, 'itk::Image< unsigned char,2 >, itk::Image< signed short,2 >'),
  ('HardConnectedComponentImageFilter', 'itk::HardConnectedComponentImageFilter', 'itkHardConnectedComponentImageFilterIUC3ISS3', True, 'itk::Image< unsigned char,3 >, itk::Image< signed short,3 >'),
  ('HardConnectedComponentImageFilter', 'itk::HardConnectedComponentImageFilter', 'itkHardConnectedComponentImageFilterIUC2IUC2', True, 'itk::Image< unsigned char,2 >, itk::Image< unsigned char,2 >'),
  ('HardConnectedComponentImageFilter', 'itk::HardConnectedComponentImageFilter', 'itkHardConnectedComponentImageFilterIUC3IUC3', True, 'itk::Image< unsigned char,3 >, itk::Image< unsigned char,3 >'),
  ('HardConnectedComponentImageFilter', 'itk::HardConnectedComponentImageFilter', 'itkHardConnectedComponentImageFilterIUC2IUS2', True, 'itk::Image< unsigned char,2 >, itk::Image< unsigned short,2 >'),
  ('HardConnectedComponentImageFilter', 'itk::HardConnectedComponentImageFilter', 'itkHardConnectedComponentImageFilterIUC3IUS3', True, 'itk::Image< unsigned char,3 >, itk::Image< unsigned short,3 >'),
  ('HardConnectedComponentImageFilter', 'itk::HardConnectedComponentImageFilter', 'itkHardConnectedComponentImageFilterIUS2IUL2', True, 'itk::Image< unsigned short,2 >, itk::Image< unsigned long,2 >'),
  ('HardConnectedComponentImageFilter', 'itk::HardConnectedComponentImageFilter', 'itkHardConnectedComponentImageFilterIUS3IUL3', True, 'itk::Image< unsigned short,3 >, itk::Image< unsigned long,3 >'),
  ('HardConnectedComponentImageFilter', 'itk::HardConnectedComponentImageFilter', 'itkHardConnectedComponentImageFilterIUS2ISS2', True, 'itk::Image< unsigned short,2 >, itk::Image< signed short,2 >'),
  ('HardConnectedComponentImageFilter', 'itk::HardConnectedComponentImageFilter', 'itkHardConnectedComponentImageFilterIUS3ISS3', True, 'itk::Image< unsigned short,3 >, itk::Image< signed short,3 >'),
  ('HardConnectedComponentImageFilter', 'itk::HardConnectedComponentImageFilter', 'itkHardConnectedComponentImageFilterIUS2IUC2', True, 'itk::Image< unsigned short,2 >, itk::Image< unsigned char,2 >'),
  ('HardConnectedComponentImageFilter', 'itk::HardConnectedComponentImageFilter', 'itkHardConnectedComponentImageFilterIUS3IUC3', True, 'itk::Image< unsigned short,3 >, itk::Image< unsigned char,3 >'),
  ('HardConnectedComponentImageFilter', 'itk::HardConnectedComponentImageFilter', 'itkHardConnectedComponentImageFilterIUS2IUS2', True, 'itk::Image< unsigned short,2 >, itk::Image< unsigned short,2 >'),
  ('HardConnectedComponentImageFilter', 'itk::HardConnectedComponentImageFilter', 'itkHardConnectedComponentImageFilterIUS3IUS3', True, 'itk::Image< unsigned short,3 >, itk::Image< unsigned short,3 >'),
  ('RelabelComponentImageFilter', 'itk::RelabelComponentImageFilter', 'itkRelabelComponentImageFilterIUC2IUC2', True, 'itk::Image< unsigned char,2 >, itk::Image< unsigned char,2 >'),
  ('RelabelComponentImageFilter', 'itk::RelabelComponentImageFilter', 'itkRelabelComponentImageFilterIUC3IUC3', True, 'itk::Image< unsigned char,3 >, itk::Image< unsigned char,3 >'),
  ('RelabelComponentImageFilter', 'itk::RelabelComponentImageFilter', 'itkRelabelComponentImageFilterIUS2IUS2', True, 'itk::Image< unsigned short,2 >, itk::Image< unsigned short,2 >'),
  ('RelabelComponentImageFilter', 'itk::RelabelComponentImageFilter', 'itkRelabelComponentImageFilterIUS3IUS3', True, 'itk::Image< unsigned short,3 >, itk::Image< unsigned short,3 >'),
  ('RelabelComponentImageFilter', 'itk::RelabelComponentImageFilter', 'itkRelabelComponentImageFilterISS2ISS2', True, 'itk::Image< signed short,2 >, itk::Image< signed short,2 >'),
  ('RelabelComponentImageFilter', 'itk::RelabelComponentImageFilter', 'itkRelabelComponentImageFilterISS3ISS3', True, 'itk::Image< signed short,3 >, itk::Image< signed short,3 >'),
  ('RelabelComponentImageFilter', 'itk::RelabelComponentImageFilter', 'itkRelabelComponentImageFilterIUL2ISS2', True, 'itk::Image< unsigned long,2 >, itk::Image< signed short,2 >'),
  ('RelabelComponentImageFilter', 'itk::RelabelComponentImageFilter', 'itkRelabelComponentImageFilterIUL3ISS3', True, 'itk::Image< unsigned long,3 >, itk::Image< signed short,3 >'),
  ('RelabelComponentImageFilter', 'itk::RelabelComponentImageFilter', 'itkRelabelComponentImageFilterIUL2IUC2', True, 'itk::Image< unsigned long,2 >, itk::Image< unsigned char,2 >'),
  ('RelabelComponentImageFilter', 'itk::RelabelComponentImageFilter', 'itkRelabelComponentImageFilterIUL3IUC3', True, 'itk::Image< unsigned long,3 >, itk::Image< unsigned char,3 >'),
  ('RelabelComponentImageFilter', 'itk::RelabelComponentImageFilter', 'itkRelabelComponentImageFilterIUL2IUS2', True, 'itk::Image< unsigned long,2 >, itk::Image< unsigned short,2 >'),
  ('RelabelComponentImageFilter', 'itk::RelabelComponentImageFilter', 'itkRelabelComponentImageFilterIUL3IUS3', True, 'itk::Image< unsigned long,3 >, itk::Image< unsigned short,3 >'),
  ('ScalarConnectedComponentImageFilter', 'itk::ScalarConnectedComponentImageFilter', 'itkScalarConnectedComponentImageFilterISS2ISS2', True, 'itk::Image< signed short,2 >, itk::Image< signed short,2 >'),
  ('ScalarConnectedComponentImageFilter', 'itk::ScalarConnectedComponentImageFilter', 'itkScalarConnectedComponentImageFilterISS3ISS3', True, 'itk::Image< signed short,3 >, itk::Image< signed short,3 >'),
  ('ScalarConnectedComponentImageFilter', 'itk::ScalarConnectedComponentImageFilter', 'itkScalarConnectedComponentImageFilterIUC2IUC2', True, 'itk::Image< unsigned char,2 >, itk::Image< unsigned char,2 >'),
  ('ScalarConnectedComponentImageFilter', 'itk::ScalarConnectedComponentImageFilter', 'itkScalarConnectedComponentImageFilterIUC3IUC3', True, 'itk::Image< unsigned char,3 >, itk::Image< unsigned char,3 >'),
  ('ScalarConnectedComponentImageFilter', 'itk::ScalarConnectedComponentImageFilter', 'itkScalarConnectedComponentImageFilterIUS2IUS2', True, 'itk::Image< unsigned short,2 >, itk::Image< unsigned short,2 >'),
  ('ScalarConnectedComponentImageFilter', 'itk::ScalarConnectedComponentImageFilter', 'itkScalarConnectedComponentImageFilterIUS3IUS3', True, 'itk::Image< unsigned short,3 >, itk::Image< unsigned short,3 >'),
  ('ThresholdMaximumConnectedComponentsImageFilter', 'itk::ThresholdMaximumConnectedComponentsImageFilter', 'itkThresholdMaximumConnectedComponentsImageFilterISS2', True, 'itk::Image< signed short,2 >'),
  ('ThresholdMaximumConnectedComponentsImageFilter', 'itk::ThresholdMaximumConnectedComponentsImageFilter', 'itkThresholdMaximumConnectedComponentsImageFilterISS3', True, 'itk::Image< signed short,3 >'),
  ('ThresholdMaximumConnectedComponentsImageFilter', 'itk::ThresholdMaximumConnectedComponentsImageFilter', 'itkThresholdMaximumConnectedComponentsImageFilterIUC2', True, 'itk::Image< unsigned char,2 >'),
  ('ThresholdMaximumConnectedComponentsImageFilter', 'itk::ThresholdMaximumConnectedComponentsImageFilter', 'itkThresholdMaximumConnectedComponentsImageFilterIUC3', True, 'itk::Image< unsigned char,3 >'),
  ('ThresholdMaximumConnectedComponentsImageFilter', 'itk::ThresholdMaximumConnectedComponentsImageFilter', 'itkThresholdMaximumConnectedComponentsImageFilterIUS2', True, 'itk::Image< unsigned short,2 >'),
  ('ThresholdMaximumConnectedComponentsImageFilter', 'itk::ThresholdMaximumConnectedComponentsImageFilter', 'itkThresholdMaximumConnectedComponentsImageFilterIUS3', True, 'itk::Image< unsigned short,3 >'),
  ('VectorConnectedComponentImageFilter', 'itk::VectorConnectedComponentImageFilter', 'itkVectorConnectedComponentImageFilterIVF22ISS2', True, 'itk::Image< itk::Vector< float,2 >,2 >, itk::Image< signed short,2 >'),
  ('VectorConnectedComponentImageFilter', 'itk::VectorConnectedComponentImageFilter', 'itkVectorConnectedComponentImageFilterIVF23ISS3', True, 'itk::Image< itk::Vector< float,2 >,3 >, itk::Image< signed short,3 >'),
  ('VectorConnectedComponentImageFilter', 'itk::VectorConnectedComponentImageFilter', 'itkVectorConnectedComponentImageFilterIVF32ISS2', True, 'itk::Image< itk::Vector< float,3 >,2 >, itk::Image< signed short,2 >'),
  ('VectorConnectedComponentImageFilter', 'itk::VectorConnectedComponentImageFilter', 'itkVectorConnectedComponentImageFilterIVF33ISS3', True, 'itk::Image< itk::Vector< float,3 >,3 >, itk::Image< signed short,3 >'),
  ('VectorConnectedComponentImageFilter', 'itk::VectorConnectedComponentImageFilter', 'itkVectorConnectedComponentImageFilterIVF42ISS2', True, 'itk::Image< itk::Vector< float,4 >,2 >, itk::Image< signed short,2 >'),
  ('VectorConnectedComponentImageFilter', 'itk::VectorConnectedComponentImageFilter', 'itkVectorConnectedComponentImageFilterIVF43ISS3', True, 'itk::Image< itk::Vector< float,4 >,3 >, itk::Image< signed short,3 >'),
  ('VectorConnectedComponentImageFilter', 'itk::VectorConnectedComponentImageFilter', 'itkVectorConnectedComponentImageFilterIVF22IUC2', True, 'itk::Image< itk::Vector< float,2 >,2 >, itk::Image< unsigned char,2 >'),
  ('VectorConnectedComponentImageFilter', 'itk::VectorConnectedComponentImageFilter', 'itkVectorConnectedComponentImageFilterIVF23IUC3', True, 'itk::Image< itk::Vector< float,2 >,3 >, itk::Image< unsigned char,3 >'),
  ('VectorConnectedComponentImageFilter', 'itk::VectorConnectedComponentImageFilter', 'itkVectorConnectedComponentImageFilterIVF32IUC2', True, 'itk::Image< itk::Vector< float,3 >,2 >, itk::Image< unsigned char,2 >'),
  ('VectorConnectedComponentImageFilter', 'itk::VectorConnectedComponentImageFilter', 'itkVectorConnectedComponentImageFilterIVF33IUC3', True, 'itk::Image< itk::Vector< float,3 >,3 >, itk::Image< unsigned char,3 >'),
  ('VectorConnectedComponentImageFilter', 'itk::VectorConnectedComponentImageFilter', 'itkVectorConnectedComponentImageFilterIVF42IUC2', True, 'itk::Image< itk::Vector< float,4 >,2 >, itk::Image< unsigned char,2 >'),
  ('VectorConnectedComponentImageFilter', 'itk::VectorConnectedComponentImageFilter', 'itkVectorConnectedComponentImageFilterIVF43IUC3', True, 'itk::Image< itk::Vector< float,4 >,3 >, itk::Image< unsigned char,3 >'),
  ('VectorConnectedComponentImageFilter', 'itk::VectorConnectedComponentImageFilter', 'itkVectorConnectedComponentImageFilterIVF22IUS2', True, 'itk::Image< itk::Vector< float,2 >,2 >, itk::Image< unsigned short,2 >'),
  ('VectorConnectedComponentImageFilter', 'itk::VectorConnectedComponentImageFilter', 'itkVectorConnectedComponentImageFilterIVF23IUS3', True, 'itk::Image< itk::Vector< float,2 >,3 >, itk::Image< unsigned short,3 >'),
  ('VectorConnectedComponentImageFilter', 'itk::VectorConnectedComponentImageFilter', 'itkVectorConnectedComponentImageFilterIVF32IUS2', True, 'itk::Image< itk::Vector< float,3 >,2 >, itk::Image< unsigned short,2 >'),
  ('VectorConnectedComponentImageFilter', 'itk::VectorConnectedComponentImageFilter', 'itkVectorConnectedComponentImageFilterIVF33IUS3', True, 'itk::Image< itk::Vector< float,3 >,3 >, itk::Image< unsigned short,3 >'),
  ('VectorConnectedComponentImageFilter', 'itk::VectorConnectedComponentImageFilter', 'itkVectorConnectedComponentImageFilterIVF42IUS2', True, 'itk::Image< itk::Vector< float,4 >,2 >, itk::Image< unsigned short,2 >'),
  ('VectorConnectedComponentImageFilter', 'itk::VectorConnectedComponentImageFilter', 'itkVectorConnectedComponentImageFilterIVF43IUS3', True, 'itk::Image< itk::Vector< float,4 >,3 >, itk::Image< unsigned short,3 >'),
  ('VectorConnectedComponentImageFilter', 'itk::VectorConnectedComponentImageFilter', 'itkVectorConnectedComponentImageFilterICVF22ISS2', True, 'itk::Image< itk::CovariantVector< float,2 >,2 >, itk::Image< signed short,2 >'),
  ('VectorConnectedComponentImageFilter', 'itk::VectorConnectedComponentImageFilter', 'itkVectorConnectedComponentImageFilterICVF23ISS3', True, 'itk::Image< itk::CovariantVector< float,2 >,3 >, itk::Image< signed short,3 >'),
  ('VectorConnectedComponentImageFilter', 'itk::VectorConnectedComponentImageFilter', 'itkVectorConnectedComponentImageFilterICVF32ISS2', True, 'itk::Image< itk::CovariantVector< float,3 >,2 >, itk::Image< signed short,2 >'),
  ('VectorConnectedComponentImageFilter', 'itk::VectorConnectedComponentImageFilter', 'itkVectorConnectedComponentImageFilterICVF33ISS3', True, 'itk::Image< itk::CovariantVector< float,3 >,3 >, itk::Image< signed short,3 >'),
  ('VectorConnectedComponentImageFilter', 'itk::VectorConnectedComponentImageFilter', 'itkVectorConnectedComponentImageFilterICVF42ISS2', True, 'itk::Image< itk::CovariantVector< float,4 >,2 >, itk::Image< signed short,2 >'),
  ('VectorConnectedComponentImageFilter', 'itk::VectorConnectedComponentImageFilter', 'itkVectorConnectedComponentImageFilterICVF43ISS3', True, 'itk::Image< itk::CovariantVector< float,4 >,3 >, itk::Image< signed short,3 >'),
  ('VectorConnectedComponentImageFilter', 'itk::VectorConnectedComponentImageFilter', 'itkVectorConnectedComponentImageFilterICVF22IUC2', True, 'itk::Image< itk::CovariantVector< float,2 >,2 >, itk::Image< unsigned char,2 >'),
  ('VectorConnectedComponentImageFilter', 'itk::VectorConnectedComponentImageFilter', 'itkVectorConnectedComponentImageFilterICVF23IUC3', True, 'itk::Image< itk::CovariantVector< float,2 >,3 >, itk::Image< unsigned char,3 >'),
  ('VectorConnectedComponentImageFilter', 'itk::VectorConnectedComponentImageFilter', 'itkVectorConnectedComponentImageFilterICVF32IUC2', True, 'itk::Image< itk::CovariantVector< float,3 >,2 >, itk::Image< unsigned char,2 >'),
  ('VectorConnectedComponentImageFilter', 'itk::VectorConnectedComponentImageFilter', 'itkVectorConnectedComponentImageFilterICVF33IUC3', True, 'itk::Image< itk::CovariantVector< float,3 >,3 >, itk::Image< unsigned char,3 >'),
  ('VectorConnectedComponentImageFilter', 'itk::VectorConnectedComponentImageFilter', 'itkVectorConnectedComponentImageFilterICVF42IUC2', True, 'itk::Image< itk::CovariantVector< float,4 >,2 >, itk::Image< unsigned char,2 >'),
  ('VectorConnectedComponentImageFilter', 'itk::VectorConnectedComponentImageFilter', 'itkVectorConnectedComponentImageFilterICVF43IUC3', True, 'itk::Image< itk::CovariantVector< float,4 >,3 >, itk::Image< unsigned char,3 >'),
  ('VectorConnectedComponentImageFilter', 'itk::VectorConnectedComponentImageFilter', 'itkVectorConnectedComponentImageFilterICVF22IUS2', True, 'itk::Image< itk::CovariantVector< float,2 >,2 >, itk::Image< unsigned short,2 >'),
  ('VectorConnectedComponentImageFilter', 'itk::VectorConnectedComponentImageFilter', 'itkVectorConnectedComponentImageFilterICVF23IUS3', True, 'itk::Image< itk::CovariantVector< float,2 >,3 >, itk::Image< unsigned short,3 >'),
  ('VectorConnectedComponentImageFilter', 'itk::VectorConnectedComponentImageFilter', 'itkVectorConnectedComponentImageFilterICVF32IUS2', True, 'itk::Image< itk::CovariantVector< float,3 >,2 >, itk::Image< unsigned short,2 >'),
  ('VectorConnectedComponentImageFilter', 'itk::VectorConnectedComponentImageFilter', 'itkVectorConnectedComponentImageFilterICVF33IUS3', True, 'itk::Image< itk::CovariantVector< float,3 >,3 >, itk::Image< unsigned short,3 >'),
  ('VectorConnectedComponentImageFilter', 'itk::VectorConnectedComponentImageFilter', 'itkVectorConnectedComponentImageFilterICVF42IUS2', True, 'itk::Image< itk::CovariantVector< float,4 >,2 >, itk::Image< unsigned short,2 >'),
  ('VectorConnectedComponentImageFilter', 'itk::VectorConnectedComponentImageFilter', 'itkVectorConnectedComponentImageFilterICVF43IUS3', True, 'itk::Image< itk::CovariantVector< float,4 >,3 >, itk::Image< unsigned short,3 >'),
)
snake_case_functions = ('scalar_connected_component_image_filter', 'relabel_component_image_filter', 'connected_component_image_filter', 'vector_connected_component_image_filter', 'connected_component_functor_image_filter', 'threshold_maximum_connected_components_image_filter', 'hard_connected_component_image_filter', )
