depends = ('ITKPyBase', 'ITKThresholding', 'ITKImageIntensity', 'ITKFFT', )
templates = (
  ('ConvolutionImageFilterBaseEnums', 'itk::ConvolutionImageFilterBaseEnums', 'itkConvolutionImageFilterBaseEnums', False),
  ('ConvolutionImageFilterBase', 'itk::ConvolutionImageFilterBase', 'itkConvolutionImageFilterBaseISS2ISS2', True, 'itk::Image< signed short,2 >, itk::Image< signed short,2 >'),
  ('ConvolutionImageFilterBase', 'itk::ConvolutionImageFilterBase', 'itkConvolutionImageFilterBaseISS3ISS3', True, 'itk::Image< signed short,3 >, itk::Image< signed short,3 >'),
  ('ConvolutionImageFilterBase', 'itk::ConvolutionImageFilterBase', 'itkConvolutionImageFilterBaseIUC2IUC2', True, 'itk::Image< unsigned char,2 >, itk::Image< unsigned char,2 >'),
  ('ConvolutionImageFilterBase', 'itk::ConvolutionImageFilterBase', 'itkConvolutionImageFilterBaseIUC3IUC3', True, 'itk::Image< unsigned char,3 >, itk::Image< unsigned char,3 >'),
  ('ConvolutionImageFilterBase', 'itk::ConvolutionImageFilterBase', 'itkConvolutionImageFilterBaseIUS2IUS2', True, 'itk::Image< unsigned short,2 >, itk::Image< unsigned short,2 >'),
  ('ConvolutionImageFilterBase', 'itk::ConvolutionImageFilterBase', 'itkConvolutionImageFilterBaseIUS3IUS3', True, 'itk::Image< unsigned short,3 >, itk::Image< unsigned short,3 >'),
  ('ConvolutionImageFilterBase', 'itk::ConvolutionImageFilterBase', 'itkConvolutionImageFilterBaseIF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >'),
  ('ConvolutionImageFilterBase', 'itk::ConvolutionImageFilterBase', 'itkConvolutionImageFilterBaseIF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >'),
  ('ConvolutionImageFilterBase', 'itk::ConvolutionImageFilterBase', 'itkConvolutionImageFilterBaseID2ID2', True, 'itk::Image< double,2 >, itk::Image< double,2 >'),
  ('ConvolutionImageFilterBase', 'itk::ConvolutionImageFilterBase', 'itkConvolutionImageFilterBaseID3ID3', True, 'itk::Image< double,3 >, itk::Image< double,3 >'),
  ('ConvolutionImageFilter', 'itk::ConvolutionImageFilter', 'itkConvolutionImageFilterISS2ISS2', True, 'itk::Image< signed short,2 >, itk::Image< signed short,2 >'),
  ('ConvolutionImageFilter', 'itk::ConvolutionImageFilter', 'itkConvolutionImageFilterISS3ISS3', True, 'itk::Image< signed short,3 >, itk::Image< signed short,3 >'),
  ('ConvolutionImageFilter', 'itk::ConvolutionImageFilter', 'itkConvolutionImageFilterIUC2IUC2', True, 'itk::Image< unsigned char,2 >, itk::Image< unsigned char,2 >'),
  ('ConvolutionImageFilter', 'itk::ConvolutionImageFilter', 'itkConvolutionImageFilterIUC3IUC3', True, 'itk::Image< unsigned char,3 >, itk::Image< unsigned char,3 >'),
  ('ConvolutionImageFilter', 'itk::ConvolutionImageFilter', 'itkConvolutionImageFilterIUS2IUS2', True, 'itk::Image< unsigned short,2 >, itk::Image< unsigned short,2 >'),
  ('ConvolutionImageFilter', 'itk::ConvolutionImageFilter', 'itkConvolutionImageFilterIUS3IUS3', True, 'itk::Image< unsigned short,3 >, itk::Image< unsigned short,3 >'),
  ('ConvolutionImageFilter', 'itk::ConvolutionImageFilter', 'itkConvolutionImageFilterIF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >'),
  ('ConvolutionImageFilter', 'itk::ConvolutionImageFilter', 'itkConvolutionImageFilterIF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >'),
  ('ConvolutionImageFilter', 'itk::ConvolutionImageFilter', 'itkConvolutionImageFilterID2ID2', True, 'itk::Image< double,2 >, itk::Image< double,2 >'),
  ('ConvolutionImageFilter', 'itk::ConvolutionImageFilter', 'itkConvolutionImageFilterID3ID3', True, 'itk::Image< double,3 >, itk::Image< double,3 >'),
  ('FFTConvolutionImageFilter', 'itk::FFTConvolutionImageFilter', 'itkFFTConvolutionImageFilterISS2ISS2', True, 'itk::Image< signed short,2 >, itk::Image< signed short,2 >'),
  ('FFTConvolutionImageFilter', 'itk::FFTConvolutionImageFilter', 'itkFFTConvolutionImageFilterISS3ISS3', True, 'itk::Image< signed short,3 >, itk::Image< signed short,3 >'),
  ('FFTConvolutionImageFilter', 'itk::FFTConvolutionImageFilter', 'itkFFTConvolutionImageFilterIUC2IUC2', True, 'itk::Image< unsigned char,2 >, itk::Image< unsigned char,2 >'),
  ('FFTConvolutionImageFilter', 'itk::FFTConvolutionImageFilter', 'itkFFTConvolutionImageFilterIUC3IUC3', True, 'itk::Image< unsigned char,3 >, itk::Image< unsigned char,3 >'),
  ('FFTConvolutionImageFilter', 'itk::FFTConvolutionImageFilter', 'itkFFTConvolutionImageFilterIUS2IUS2', True, 'itk::Image< unsigned short,2 >, itk::Image< unsigned short,2 >'),
  ('FFTConvolutionImageFilter', 'itk::FFTConvolutionImageFilter', 'itkFFTConvolutionImageFilterIUS3IUS3', True, 'itk::Image< unsigned short,3 >, itk::Image< unsigned short,3 >'),
  ('FFTConvolutionImageFilter', 'itk::FFTConvolutionImageFilter', 'itkFFTConvolutionImageFilterIF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >'),
  ('FFTConvolutionImageFilter', 'itk::FFTConvolutionImageFilter', 'itkFFTConvolutionImageFilterIF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >'),
  ('FFTConvolutionImageFilter', 'itk::FFTConvolutionImageFilter', 'itkFFTConvolutionImageFilterID2ID2', True, 'itk::Image< double,2 >, itk::Image< double,2 >'),
  ('FFTConvolutionImageFilter', 'itk::FFTConvolutionImageFilter', 'itkFFTConvolutionImageFilterID3ID3', True, 'itk::Image< double,3 >, itk::Image< double,3 >'),
  ('FFTNormalizedCorrelationImageFilter', 'itk::FFTNormalizedCorrelationImageFilter', 'itkFFTNormalizedCorrelationImageFilterISS2IF2', True, 'itk::Image< signed short,2 >, itk::Image< float,2 >'),
  ('FFTNormalizedCorrelationImageFilter', 'itk::FFTNormalizedCorrelationImageFilter', 'itkFFTNormalizedCorrelationImageFilterISS3IF3', True, 'itk::Image< signed short,3 >, itk::Image< float,3 >'),
  ('FFTNormalizedCorrelationImageFilter', 'itk::FFTNormalizedCorrelationImageFilter', 'itkFFTNormalizedCorrelationImageFilterISS2ID2', True, 'itk::Image< signed short,2 >, itk::Image< double,2 >'),
  ('FFTNormalizedCorrelationImageFilter', 'itk::FFTNormalizedCorrelationImageFilter', 'itkFFTNormalizedCorrelationImageFilterISS3ID3', True, 'itk::Image< signed short,3 >, itk::Image< double,3 >'),
  ('FFTNormalizedCorrelationImageFilter', 'itk::FFTNormalizedCorrelationImageFilter', 'itkFFTNormalizedCorrelationImageFilterIUC2IF2', True, 'itk::Image< unsigned char,2 >, itk::Image< float,2 >'),
  ('FFTNormalizedCorrelationImageFilter', 'itk::FFTNormalizedCorrelationImageFilter', 'itkFFTNormalizedCorrelationImageFilterIUC3IF3', True, 'itk::Image< unsigned char,3 >, itk::Image< float,3 >'),
  ('FFTNormalizedCorrelationImageFilter', 'itk::FFTNormalizedCorrelationImageFilter', 'itkFFTNormalizedCorrelationImageFilterIUC2ID2', True, 'itk::Image< unsigned char,2 >, itk::Image< double,2 >'),
  ('FFTNormalizedCorrelationImageFilter', 'itk::FFTNormalizedCorrelationImageFilter', 'itkFFTNormalizedCorrelationImageFilterIUC3ID3', True, 'itk::Image< unsigned char,3 >, itk::Image< double,3 >'),
  ('FFTNormalizedCorrelationImageFilter', 'itk::FFTNormalizedCorrelationImageFilter', 'itkFFTNormalizedCorrelationImageFilterIUS2IF2', True, 'itk::Image< unsigned short,2 >, itk::Image< float,2 >'),
  ('FFTNormalizedCorrelationImageFilter', 'itk::FFTNormalizedCorrelationImageFilter', 'itkFFTNormalizedCorrelationImageFilterIUS3IF3', True, 'itk::Image< unsigned short,3 >, itk::Image< float,3 >'),
  ('FFTNormalizedCorrelationImageFilter', 'itk::FFTNormalizedCorrelationImageFilter', 'itkFFTNormalizedCorrelationImageFilterIUS2ID2', True, 'itk::Image< unsigned short,2 >, itk::Image< double,2 >'),
  ('FFTNormalizedCorrelationImageFilter', 'itk::FFTNormalizedCorrelationImageFilter', 'itkFFTNormalizedCorrelationImageFilterIUS3ID3', True, 'itk::Image< unsigned short,3 >, itk::Image< double,3 >'),
  ('FFTNormalizedCorrelationImageFilter', 'itk::FFTNormalizedCorrelationImageFilter', 'itkFFTNormalizedCorrelationImageFilterIF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >'),
  ('FFTNormalizedCorrelationImageFilter', 'itk::FFTNormalizedCorrelationImageFilter', 'itkFFTNormalizedCorrelationImageFilterIF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >'),
  ('FFTNormalizedCorrelationImageFilter', 'itk::FFTNormalizedCorrelationImageFilter', 'itkFFTNormalizedCorrelationImageFilterIF2ID2', True, 'itk::Image< float,2 >, itk::Image< double,2 >'),
  ('FFTNormalizedCorrelationImageFilter', 'itk::FFTNormalizedCorrelationImageFilter', 'itkFFTNormalizedCorrelationImageFilterIF3ID3', True, 'itk::Image< float,3 >, itk::Image< double,3 >'),
  ('FFTNormalizedCorrelationImageFilter', 'itk::FFTNormalizedCorrelationImageFilter', 'itkFFTNormalizedCorrelationImageFilterID2IF2', True, 'itk::Image< double,2 >, itk::Image< float,2 >'),
  ('FFTNormalizedCorrelationImageFilter', 'itk::FFTNormalizedCorrelationImageFilter', 'itkFFTNormalizedCorrelationImageFilterID3IF3', True, 'itk::Image< double,3 >, itk::Image< float,3 >'),
  ('FFTNormalizedCorrelationImageFilter', 'itk::FFTNormalizedCorrelationImageFilter', 'itkFFTNormalizedCorrelationImageFilterID2ID2', True, 'itk::Image< double,2 >, itk::Image< double,2 >'),
  ('FFTNormalizedCorrelationImageFilter', 'itk::FFTNormalizedCorrelationImageFilter', 'itkFFTNormalizedCorrelationImageFilterID3ID3', True, 'itk::Image< double,3 >, itk::Image< double,3 >'),
  ('MaskedFFTNormalizedCorrelationImageFilter', 'itk::MaskedFFTNormalizedCorrelationImageFilter', 'itkMaskedFFTNormalizedCorrelationImageFilterISS2IF2', True, 'itk::Image< signed short,2 >, itk::Image< float,2 >'),
  ('MaskedFFTNormalizedCorrelationImageFilter', 'itk::MaskedFFTNormalizedCorrelationImageFilter', 'itkMaskedFFTNormalizedCorrelationImageFilterISS3IF3', True, 'itk::Image< signed short,3 >, itk::Image< float,3 >'),
  ('MaskedFFTNormalizedCorrelationImageFilter', 'itk::MaskedFFTNormalizedCorrelationImageFilter', 'itkMaskedFFTNormalizedCorrelationImageFilterISS2ID2', True, 'itk::Image< signed short,2 >, itk::Image< double,2 >'),
  ('MaskedFFTNormalizedCorrelationImageFilter', 'itk::MaskedFFTNormalizedCorrelationImageFilter', 'itkMaskedFFTNormalizedCorrelationImageFilterISS3ID3', True, 'itk::Image< signed short,3 >, itk::Image< double,3 >'),
  ('MaskedFFTNormalizedCorrelationImageFilter', 'itk::MaskedFFTNormalizedCorrelationImageFilter', 'itkMaskedFFTNormalizedCorrelationImageFilterIUC2IF2', True, 'itk::Image< unsigned char,2 >, itk::Image< float,2 >'),
  ('MaskedFFTNormalizedCorrelationImageFilter', 'itk::MaskedFFTNormalizedCorrelationImageFilter', 'itkMaskedFFTNormalizedCorrelationImageFilterIUC3IF3', True, 'itk::Image< unsigned char,3 >, itk::Image< float,3 >'),
  ('MaskedFFTNormalizedCorrelationImageFilter', 'itk::MaskedFFTNormalizedCorrelationImageFilter', 'itkMaskedFFTNormalizedCorrelationImageFilterIUC2ID2', True, 'itk::Image< unsigned char,2 >, itk::Image< double,2 >'),
  ('MaskedFFTNormalizedCorrelationImageFilter', 'itk::MaskedFFTNormalizedCorrelationImageFilter', 'itkMaskedFFTNormalizedCorrelationImageFilterIUC3ID3', True, 'itk::Image< unsigned char,3 >, itk::Image< double,3 >'),
  ('MaskedFFTNormalizedCorrelationImageFilter', 'itk::MaskedFFTNormalizedCorrelationImageFilter', 'itkMaskedFFTNormalizedCorrelationImageFilterIUS2IF2', True, 'itk::Image< unsigned short,2 >, itk::Image< float,2 >'),
  ('MaskedFFTNormalizedCorrelationImageFilter', 'itk::MaskedFFTNormalizedCorrelationImageFilter', 'itkMaskedFFTNormalizedCorrelationImageFilterIUS3IF3', True, 'itk::Image< unsigned short,3 >, itk::Image< float,3 >'),
  ('MaskedFFTNormalizedCorrelationImageFilter', 'itk::MaskedFFTNormalizedCorrelationImageFilter', 'itkMaskedFFTNormalizedCorrelationImageFilterIUS2ID2', True, 'itk::Image< unsigned short,2 >, itk::Image< double,2 >'),
  ('MaskedFFTNormalizedCorrelationImageFilter', 'itk::MaskedFFTNormalizedCorrelationImageFilter', 'itkMaskedFFTNormalizedCorrelationImageFilterIUS3ID3', True, 'itk::Image< unsigned short,3 >, itk::Image< double,3 >'),
  ('MaskedFFTNormalizedCorrelationImageFilter', 'itk::MaskedFFTNormalizedCorrelationImageFilter', 'itkMaskedFFTNormalizedCorrelationImageFilterIF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >'),
  ('MaskedFFTNormalizedCorrelationImageFilter', 'itk::MaskedFFTNormalizedCorrelationImageFilter', 'itkMaskedFFTNormalizedCorrelationImageFilterIF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >'),
  ('MaskedFFTNormalizedCorrelationImageFilter', 'itk::MaskedFFTNormalizedCorrelationImageFilter', 'itkMaskedFFTNormalizedCorrelationImageFilterIF2ID2', True, 'itk::Image< float,2 >, itk::Image< double,2 >'),
  ('MaskedFFTNormalizedCorrelationImageFilter', 'itk::MaskedFFTNormalizedCorrelationImageFilter', 'itkMaskedFFTNormalizedCorrelationImageFilterIF3ID3', True, 'itk::Image< float,3 >, itk::Image< double,3 >'),
  ('MaskedFFTNormalizedCorrelationImageFilter', 'itk::MaskedFFTNormalizedCorrelationImageFilter', 'itkMaskedFFTNormalizedCorrelationImageFilterID2IF2', True, 'itk::Image< double,2 >, itk::Image< float,2 >'),
  ('MaskedFFTNormalizedCorrelationImageFilter', 'itk::MaskedFFTNormalizedCorrelationImageFilter', 'itkMaskedFFTNormalizedCorrelationImageFilterID3IF3', True, 'itk::Image< double,3 >, itk::Image< float,3 >'),
  ('MaskedFFTNormalizedCorrelationImageFilter', 'itk::MaskedFFTNormalizedCorrelationImageFilter', 'itkMaskedFFTNormalizedCorrelationImageFilterID2ID2', True, 'itk::Image< double,2 >, itk::Image< double,2 >'),
  ('MaskedFFTNormalizedCorrelationImageFilter', 'itk::MaskedFFTNormalizedCorrelationImageFilter', 'itkMaskedFFTNormalizedCorrelationImageFilterID3ID3', True, 'itk::Image< double,3 >, itk::Image< double,3 >'),
)
snake_case_functions = ('masked_fft_normalized_correlation_image_filter', 'fft_convolution_image_filter', 'convolution_image_filter', 'convolution_image_filter_base', 'fft_normalized_correlation_image_filter', )
