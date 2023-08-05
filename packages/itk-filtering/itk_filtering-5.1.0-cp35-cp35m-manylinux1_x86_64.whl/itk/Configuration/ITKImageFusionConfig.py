depends = ('ITKPyBase', 'ITKImageLabel', 'ITKBinaryMathematicalMorphology', )
templates = (
  ('LabelMapContourOverlayImageFilter', 'itk::LabelMapContourOverlayImageFilter', 'itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2', True, 'itk::LabelMap< itk::StatisticsLabelObject< unsigned long, 2 > >, itk::Image< unsigned char,2 >, itk::Image< itk::RGBPixel< unsigned char >,2 >'),
  ('LabelMapContourOverlayImageFilter', 'itk::LabelMapContourOverlayImageFilter', 'itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3', True, 'itk::LabelMap< itk::StatisticsLabelObject< unsigned long, 3 > >, itk::Image< unsigned char,3 >, itk::Image< itk::RGBPixel< unsigned char >,3 >'),
  ('LabelMapOverlayImageFilter', 'itk::LabelMapOverlayImageFilter', 'itkLabelMapOverlayImageFilterLM2IUC2IRGBUC2', True, 'itk::LabelMap< itk::StatisticsLabelObject< unsigned long, 2 > >, itk::Image< unsigned char,2 >, itk::Image< itk::RGBPixel< unsigned char >,2 >'),
  ('LabelMapOverlayImageFilter', 'itk::LabelMapOverlayImageFilter', 'itkLabelMapOverlayImageFilterLM3IUC3IRGBUC3', True, 'itk::LabelMap< itk::StatisticsLabelObject< unsigned long, 3 > >, itk::Image< unsigned char,3 >, itk::Image< itk::RGBPixel< unsigned char >,3 >'),
  ('LabelMapToRGBImageFilter', 'itk::LabelMapToRGBImageFilter', 'itkLabelMapToRGBImageFilterLM2IRGBUC2', True, 'itk::LabelMap< itk::StatisticsLabelObject< unsigned long, 2 > >, itk::Image< itk::RGBPixel< unsigned char >,2 >'),
  ('LabelMapToRGBImageFilter', 'itk::LabelMapToRGBImageFilter', 'itkLabelMapToRGBImageFilterLM3IRGBUC3', True, 'itk::LabelMap< itk::StatisticsLabelObject< unsigned long, 3 > >, itk::Image< itk::RGBPixel< unsigned char >,3 >'),
  ('LabelOverlayImageFilter', 'itk::LabelOverlayImageFilter', 'itkLabelOverlayImageFilterIUC2ISS2IRGBUC2', True, 'itk::Image< unsigned char,2 >, itk::Image< signed short,2 >, itk::Image< itk::RGBPixel< unsigned char >,2 >'),
  ('LabelOverlayImageFilter', 'itk::LabelOverlayImageFilter', 'itkLabelOverlayImageFilterIUC3ISS3IRGBUC3', True, 'itk::Image< unsigned char,3 >, itk::Image< signed short,3 >, itk::Image< itk::RGBPixel< unsigned char >,3 >'),
  ('LabelOverlayImageFilter', 'itk::LabelOverlayImageFilter', 'itkLabelOverlayImageFilterIUC2IUC2IRGBUC2', True, 'itk::Image< unsigned char,2 >, itk::Image< unsigned char,2 >, itk::Image< itk::RGBPixel< unsigned char >,2 >'),
  ('LabelOverlayImageFilter', 'itk::LabelOverlayImageFilter', 'itkLabelOverlayImageFilterIUC3IUC3IRGBUC3', True, 'itk::Image< unsigned char,3 >, itk::Image< unsigned char,3 >, itk::Image< itk::RGBPixel< unsigned char >,3 >'),
  ('LabelOverlayImageFilter', 'itk::LabelOverlayImageFilter', 'itkLabelOverlayImageFilterIUC2IUS2IRGBUC2', True, 'itk::Image< unsigned char,2 >, itk::Image< unsigned short,2 >, itk::Image< itk::RGBPixel< unsigned char >,2 >'),
  ('LabelOverlayImageFilter', 'itk::LabelOverlayImageFilter', 'itkLabelOverlayImageFilterIUC3IUS3IRGBUC3', True, 'itk::Image< unsigned char,3 >, itk::Image< unsigned short,3 >, itk::Image< itk::RGBPixel< unsigned char >,3 >'),
  ('LabelOverlayImageFilter', 'itk::LabelOverlayImageFilter', 'itkLabelOverlayImageFilterIUC2IUL2IRGBUC2', True, 'itk::Image< unsigned char,2 >, itk::Image< unsigned long,2 >, itk::Image< itk::RGBPixel< unsigned char >,2 >'),
  ('LabelOverlayImageFilter', 'itk::LabelOverlayImageFilter', 'itkLabelOverlayImageFilterIUC3IUL3IRGBUC3', True, 'itk::Image< unsigned char,3 >, itk::Image< unsigned long,3 >, itk::Image< itk::RGBPixel< unsigned char >,3 >'),
  ('LabelToRGBImageFilter', 'itk::LabelToRGBImageFilter', 'itkLabelToRGBImageFilterISS2IRGBUC2', True, 'itk::Image< signed short,2 >, itk::Image< itk::RGBPixel< unsigned char >,2 >'),
  ('LabelToRGBImageFilter', 'itk::LabelToRGBImageFilter', 'itkLabelToRGBImageFilterISS3IRGBUC3', True, 'itk::Image< signed short,3 >, itk::Image< itk::RGBPixel< unsigned char >,3 >'),
  ('LabelToRGBImageFilter', 'itk::LabelToRGBImageFilter', 'itkLabelToRGBImageFilterIUC2IRGBUC2', True, 'itk::Image< unsigned char,2 >, itk::Image< itk::RGBPixel< unsigned char >,2 >'),
  ('LabelToRGBImageFilter', 'itk::LabelToRGBImageFilter', 'itkLabelToRGBImageFilterIUC3IRGBUC3', True, 'itk::Image< unsigned char,3 >, itk::Image< itk::RGBPixel< unsigned char >,3 >'),
  ('LabelToRGBImageFilter', 'itk::LabelToRGBImageFilter', 'itkLabelToRGBImageFilterIUS2IRGBUC2', True, 'itk::Image< unsigned short,2 >, itk::Image< itk::RGBPixel< unsigned char >,2 >'),
  ('LabelToRGBImageFilter', 'itk::LabelToRGBImageFilter', 'itkLabelToRGBImageFilterIUS3IRGBUC3', True, 'itk::Image< unsigned short,3 >, itk::Image< itk::RGBPixel< unsigned char >,3 >'),
  ('LabelToRGBImageFilter', 'itk::LabelToRGBImageFilter', 'itkLabelToRGBImageFilterIUL2IRGBUC2', True, 'itk::Image< unsigned long,2 >, itk::Image< itk::RGBPixel< unsigned char >,2 >'),
  ('LabelToRGBImageFilter', 'itk::LabelToRGBImageFilter', 'itkLabelToRGBImageFilterIUL3IRGBUC3', True, 'itk::Image< unsigned long,3 >, itk::Image< itk::RGBPixel< unsigned char >,3 >'),
)
snake_case_functions = ('unary_functor_image_filter', 'label_map_to_rgb_image_filter', 'label_map_contour_overlay_image_filter', 'label_overlay_image_filter', 'label_map_overlay_image_filter', 'label_to_rgb_image_filter', )
