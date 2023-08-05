depends = ('ITKPyBase', 'ITKImageIntensity', 'ITKImageFilterBase', )
templates = (
  ('AbsoluteValueDifferenceImageFilter', 'itk::AbsoluteValueDifferenceImageFilter', 'itkAbsoluteValueDifferenceImageFilterISS2ISS2ISS2', True, 'itk::Image< signed short,2 >, itk::Image< signed short,2 >, itk::Image< signed short,2 >'),
  ('AbsoluteValueDifferenceImageFilter', 'itk::AbsoluteValueDifferenceImageFilter', 'itkAbsoluteValueDifferenceImageFilterISS3ISS3ISS3', True, 'itk::Image< signed short,3 >, itk::Image< signed short,3 >, itk::Image< signed short,3 >'),
  ('AbsoluteValueDifferenceImageFilter', 'itk::AbsoluteValueDifferenceImageFilter', 'itkAbsoluteValueDifferenceImageFilterIUC2IUC2IUC2', True, 'itk::Image< unsigned char,2 >, itk::Image< unsigned char,2 >, itk::Image< unsigned char,2 >'),
  ('AbsoluteValueDifferenceImageFilter', 'itk::AbsoluteValueDifferenceImageFilter', 'itkAbsoluteValueDifferenceImageFilterIUC3IUC3IUC3', True, 'itk::Image< unsigned char,3 >, itk::Image< unsigned char,3 >, itk::Image< unsigned char,3 >'),
  ('AbsoluteValueDifferenceImageFilter', 'itk::AbsoluteValueDifferenceImageFilter', 'itkAbsoluteValueDifferenceImageFilterIUS2IUS2IUS2', True, 'itk::Image< unsigned short,2 >, itk::Image< unsigned short,2 >, itk::Image< unsigned short,2 >'),
  ('AbsoluteValueDifferenceImageFilter', 'itk::AbsoluteValueDifferenceImageFilter', 'itkAbsoluteValueDifferenceImageFilterIUS3IUS3IUS3', True, 'itk::Image< unsigned short,3 >, itk::Image< unsigned short,3 >, itk::Image< unsigned short,3 >'),
  ('AbsoluteValueDifferenceImageFilter', 'itk::AbsoluteValueDifferenceImageFilter', 'itkAbsoluteValueDifferenceImageFilterIF2IF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >, itk::Image< float,2 >'),
  ('AbsoluteValueDifferenceImageFilter', 'itk::AbsoluteValueDifferenceImageFilter', 'itkAbsoluteValueDifferenceImageFilterIF3IF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >, itk::Image< float,3 >'),
  ('AbsoluteValueDifferenceImageFilter', 'itk::AbsoluteValueDifferenceImageFilter', 'itkAbsoluteValueDifferenceImageFilterID2ID2ID2', True, 'itk::Image< double,2 >, itk::Image< double,2 >, itk::Image< double,2 >'),
  ('AbsoluteValueDifferenceImageFilter', 'itk::AbsoluteValueDifferenceImageFilter', 'itkAbsoluteValueDifferenceImageFilterID3ID3ID3', True, 'itk::Image< double,3 >, itk::Image< double,3 >, itk::Image< double,3 >'),
  ('CheckerBoardImageFilter', 'itk::CheckerBoardImageFilter', 'itkCheckerBoardImageFilterIRGBUC2', True, 'itk::Image< itk::RGBPixel< unsigned char >,2 >'),
  ('CheckerBoardImageFilter', 'itk::CheckerBoardImageFilter', 'itkCheckerBoardImageFilterIRGBUC3', True, 'itk::Image< itk::RGBPixel< unsigned char >,3 >'),
  ('CheckerBoardImageFilter', 'itk::CheckerBoardImageFilter', 'itkCheckerBoardImageFilterIRGBAUC2', True, 'itk::Image< itk::RGBAPixel< unsigned char >,2 >'),
  ('CheckerBoardImageFilter', 'itk::CheckerBoardImageFilter', 'itkCheckerBoardImageFilterIRGBAUC3', True, 'itk::Image< itk::RGBAPixel< unsigned char >,3 >'),
  ('CheckerBoardImageFilter', 'itk::CheckerBoardImageFilter', 'itkCheckerBoardImageFilterIVF22', True, 'itk::Image< itk::Vector< float,2 >,2 >'),
  ('CheckerBoardImageFilter', 'itk::CheckerBoardImageFilter', 'itkCheckerBoardImageFilterIVF23', True, 'itk::Image< itk::Vector< float,2 >,3 >'),
  ('CheckerBoardImageFilter', 'itk::CheckerBoardImageFilter', 'itkCheckerBoardImageFilterIVF32', True, 'itk::Image< itk::Vector< float,3 >,2 >'),
  ('CheckerBoardImageFilter', 'itk::CheckerBoardImageFilter', 'itkCheckerBoardImageFilterIVF33', True, 'itk::Image< itk::Vector< float,3 >,3 >'),
  ('CheckerBoardImageFilter', 'itk::CheckerBoardImageFilter', 'itkCheckerBoardImageFilterIVF42', True, 'itk::Image< itk::Vector< float,4 >,2 >'),
  ('CheckerBoardImageFilter', 'itk::CheckerBoardImageFilter', 'itkCheckerBoardImageFilterIVF43', True, 'itk::Image< itk::Vector< float,4 >,3 >'),
  ('CheckerBoardImageFilter', 'itk::CheckerBoardImageFilter', 'itkCheckerBoardImageFilterICVF22', True, 'itk::Image< itk::CovariantVector< float,2 >,2 >'),
  ('CheckerBoardImageFilter', 'itk::CheckerBoardImageFilter', 'itkCheckerBoardImageFilterICVF23', True, 'itk::Image< itk::CovariantVector< float,2 >,3 >'),
  ('CheckerBoardImageFilter', 'itk::CheckerBoardImageFilter', 'itkCheckerBoardImageFilterICVF32', True, 'itk::Image< itk::CovariantVector< float,3 >,2 >'),
  ('CheckerBoardImageFilter', 'itk::CheckerBoardImageFilter', 'itkCheckerBoardImageFilterICVF33', True, 'itk::Image< itk::CovariantVector< float,3 >,3 >'),
  ('CheckerBoardImageFilter', 'itk::CheckerBoardImageFilter', 'itkCheckerBoardImageFilterICVF42', True, 'itk::Image< itk::CovariantVector< float,4 >,2 >'),
  ('CheckerBoardImageFilter', 'itk::CheckerBoardImageFilter', 'itkCheckerBoardImageFilterICVF43', True, 'itk::Image< itk::CovariantVector< float,4 >,3 >'),
  ('CheckerBoardImageFilter', 'itk::CheckerBoardImageFilter', 'itkCheckerBoardImageFilterISS2', True, 'itk::Image< signed short,2 >'),
  ('CheckerBoardImageFilter', 'itk::CheckerBoardImageFilter', 'itkCheckerBoardImageFilterISS3', True, 'itk::Image< signed short,3 >'),
  ('CheckerBoardImageFilter', 'itk::CheckerBoardImageFilter', 'itkCheckerBoardImageFilterIUC2', True, 'itk::Image< unsigned char,2 >'),
  ('CheckerBoardImageFilter', 'itk::CheckerBoardImageFilter', 'itkCheckerBoardImageFilterIUC3', True, 'itk::Image< unsigned char,3 >'),
  ('CheckerBoardImageFilter', 'itk::CheckerBoardImageFilter', 'itkCheckerBoardImageFilterIUS2', True, 'itk::Image< unsigned short,2 >'),
  ('CheckerBoardImageFilter', 'itk::CheckerBoardImageFilter', 'itkCheckerBoardImageFilterIUS3', True, 'itk::Image< unsigned short,3 >'),
  ('CheckerBoardImageFilter', 'itk::CheckerBoardImageFilter', 'itkCheckerBoardImageFilterIF2', True, 'itk::Image< float,2 >'),
  ('CheckerBoardImageFilter', 'itk::CheckerBoardImageFilter', 'itkCheckerBoardImageFilterIF3', True, 'itk::Image< float,3 >'),
  ('CheckerBoardImageFilter', 'itk::CheckerBoardImageFilter', 'itkCheckerBoardImageFilterID2', True, 'itk::Image< double,2 >'),
  ('CheckerBoardImageFilter', 'itk::CheckerBoardImageFilter', 'itkCheckerBoardImageFilterID3', True, 'itk::Image< double,3 >'),
  ('CheckerBoardImageFilter', 'itk::CheckerBoardImageFilter', 'itkCheckerBoardImageFilterICF2', True, 'itk::Image< std::complex< float >,2 >'),
  ('CheckerBoardImageFilter', 'itk::CheckerBoardImageFilter', 'itkCheckerBoardImageFilterICF3', True, 'itk::Image< std::complex< float >,3 >'),
  ('STAPLEImageFilter', 'itk::STAPLEImageFilter', 'itkSTAPLEImageFilterIF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >'),
  ('STAPLEImageFilter', 'itk::STAPLEImageFilter', 'itkSTAPLEImageFilterIF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >'),
  ('STAPLEImageFilter', 'itk::STAPLEImageFilter', 'itkSTAPLEImageFilterID2ID2', True, 'itk::Image< double,2 >, itk::Image< double,2 >'),
  ('STAPLEImageFilter', 'itk::STAPLEImageFilter', 'itkSTAPLEImageFilterID3ID3', True, 'itk::Image< double,3 >, itk::Image< double,3 >'),
  ('SimilarityIndexImageFilter', 'itk::SimilarityIndexImageFilter', 'itkSimilarityIndexImageFilterISS2ISS2', True, 'itk::Image< signed short,2 >, itk::Image< signed short,2 >'),
  ('SimilarityIndexImageFilter', 'itk::SimilarityIndexImageFilter', 'itkSimilarityIndexImageFilterISS3ISS3', True, 'itk::Image< signed short,3 >, itk::Image< signed short,3 >'),
  ('SimilarityIndexImageFilter', 'itk::SimilarityIndexImageFilter', 'itkSimilarityIndexImageFilterIUC2IUC2', True, 'itk::Image< unsigned char,2 >, itk::Image< unsigned char,2 >'),
  ('SimilarityIndexImageFilter', 'itk::SimilarityIndexImageFilter', 'itkSimilarityIndexImageFilterIUC3IUC3', True, 'itk::Image< unsigned char,3 >, itk::Image< unsigned char,3 >'),
  ('SimilarityIndexImageFilter', 'itk::SimilarityIndexImageFilter', 'itkSimilarityIndexImageFilterIUS2IUS2', True, 'itk::Image< unsigned short,2 >, itk::Image< unsigned short,2 >'),
  ('SimilarityIndexImageFilter', 'itk::SimilarityIndexImageFilter', 'itkSimilarityIndexImageFilterIUS3IUS3', True, 'itk::Image< unsigned short,3 >, itk::Image< unsigned short,3 >'),
  ('SimilarityIndexImageFilter', 'itk::SimilarityIndexImageFilter', 'itkSimilarityIndexImageFilterIF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >'),
  ('SimilarityIndexImageFilter', 'itk::SimilarityIndexImageFilter', 'itkSimilarityIndexImageFilterIF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >'),
  ('SimilarityIndexImageFilter', 'itk::SimilarityIndexImageFilter', 'itkSimilarityIndexImageFilterID2ID2', True, 'itk::Image< double,2 >, itk::Image< double,2 >'),
  ('SimilarityIndexImageFilter', 'itk::SimilarityIndexImageFilter', 'itkSimilarityIndexImageFilterID3ID3', True, 'itk::Image< double,3 >, itk::Image< double,3 >'),
  ('SquaredDifferenceImageFilter', 'itk::SquaredDifferenceImageFilter', 'itkSquaredDifferenceImageFilterISS2ISS2ISS2', True, 'itk::Image< signed short,2 >, itk::Image< signed short,2 >, itk::Image< signed short,2 >'),
  ('SquaredDifferenceImageFilter', 'itk::SquaredDifferenceImageFilter', 'itkSquaredDifferenceImageFilterISS3ISS3ISS3', True, 'itk::Image< signed short,3 >, itk::Image< signed short,3 >, itk::Image< signed short,3 >'),
  ('SquaredDifferenceImageFilter', 'itk::SquaredDifferenceImageFilter', 'itkSquaredDifferenceImageFilterIUC2IUC2IUC2', True, 'itk::Image< unsigned char,2 >, itk::Image< unsigned char,2 >, itk::Image< unsigned char,2 >'),
  ('SquaredDifferenceImageFilter', 'itk::SquaredDifferenceImageFilter', 'itkSquaredDifferenceImageFilterIUC3IUC3IUC3', True, 'itk::Image< unsigned char,3 >, itk::Image< unsigned char,3 >, itk::Image< unsigned char,3 >'),
  ('SquaredDifferenceImageFilter', 'itk::SquaredDifferenceImageFilter', 'itkSquaredDifferenceImageFilterIUS2IUS2IUS2', True, 'itk::Image< unsigned short,2 >, itk::Image< unsigned short,2 >, itk::Image< unsigned short,2 >'),
  ('SquaredDifferenceImageFilter', 'itk::SquaredDifferenceImageFilter', 'itkSquaredDifferenceImageFilterIUS3IUS3IUS3', True, 'itk::Image< unsigned short,3 >, itk::Image< unsigned short,3 >, itk::Image< unsigned short,3 >'),
  ('SquaredDifferenceImageFilter', 'itk::SquaredDifferenceImageFilter', 'itkSquaredDifferenceImageFilterIF2IF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >, itk::Image< float,2 >'),
  ('SquaredDifferenceImageFilter', 'itk::SquaredDifferenceImageFilter', 'itkSquaredDifferenceImageFilterIF3IF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >, itk::Image< float,3 >'),
  ('SquaredDifferenceImageFilter', 'itk::SquaredDifferenceImageFilter', 'itkSquaredDifferenceImageFilterID2ID2ID2', True, 'itk::Image< double,2 >, itk::Image< double,2 >, itk::Image< double,2 >'),
  ('SquaredDifferenceImageFilter', 'itk::SquaredDifferenceImageFilter', 'itkSquaredDifferenceImageFilterID3ID3ID3', True, 'itk::Image< double,3 >, itk::Image< double,3 >, itk::Image< double,3 >'),
)
snake_case_functions = ('squared_difference_image_filter', 'staple_image_filter', 'similarity_index_image_filter', 'absolute_value_difference_image_filter', 'checker_board_image_filter', )
