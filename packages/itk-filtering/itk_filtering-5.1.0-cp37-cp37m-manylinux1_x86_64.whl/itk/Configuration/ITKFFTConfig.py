depends = ('ITKPyBase', 'ITKImageGrid', 'ITKCommon', )
templates = (
  ('ComplexToComplexFFTImageFilterEnums', 'itk::ComplexToComplexFFTImageFilterEnums', 'itkComplexToComplexFFTImageFilterEnums', False),
  ('ComplexToComplexFFTImageFilter', 'itk::ComplexToComplexFFTImageFilter', 'itkComplexToComplexFFTImageFilterICF2', True, 'itk::Image< std::complex< float >,2 >'),
  ('ComplexToComplexFFTImageFilter', 'itk::ComplexToComplexFFTImageFilter', 'itkComplexToComplexFFTImageFilterICF3', True, 'itk::Image< std::complex< float >,3 >'),
  ('FFTPadImageFilter', 'itk::FFTPadImageFilter', 'itkFFTPadImageFilterIRGBUC2', True, 'itk::Image< itk::RGBPixel< unsigned char >,2 >'),
  ('FFTPadImageFilter', 'itk::FFTPadImageFilter', 'itkFFTPadImageFilterIRGBUC3', True, 'itk::Image< itk::RGBPixel< unsigned char >,3 >'),
  ('FFTPadImageFilter', 'itk::FFTPadImageFilter', 'itkFFTPadImageFilterIRGBAUC2', True, 'itk::Image< itk::RGBAPixel< unsigned char >,2 >'),
  ('FFTPadImageFilter', 'itk::FFTPadImageFilter', 'itkFFTPadImageFilterIRGBAUC3', True, 'itk::Image< itk::RGBAPixel< unsigned char >,3 >'),
  ('FFTPadImageFilter', 'itk::FFTPadImageFilter', 'itkFFTPadImageFilterIVF22', True, 'itk::Image< itk::Vector< float,2 >,2 >'),
  ('FFTPadImageFilter', 'itk::FFTPadImageFilter', 'itkFFTPadImageFilterIVF23', True, 'itk::Image< itk::Vector< float,2 >,3 >'),
  ('FFTPadImageFilter', 'itk::FFTPadImageFilter', 'itkFFTPadImageFilterIVF32', True, 'itk::Image< itk::Vector< float,3 >,2 >'),
  ('FFTPadImageFilter', 'itk::FFTPadImageFilter', 'itkFFTPadImageFilterIVF33', True, 'itk::Image< itk::Vector< float,3 >,3 >'),
  ('FFTPadImageFilter', 'itk::FFTPadImageFilter', 'itkFFTPadImageFilterIVF42', True, 'itk::Image< itk::Vector< float,4 >,2 >'),
  ('FFTPadImageFilter', 'itk::FFTPadImageFilter', 'itkFFTPadImageFilterIVF43', True, 'itk::Image< itk::Vector< float,4 >,3 >'),
  ('FFTPadImageFilter', 'itk::FFTPadImageFilter', 'itkFFTPadImageFilterICVF22', True, 'itk::Image< itk::CovariantVector< float,2 >,2 >'),
  ('FFTPadImageFilter', 'itk::FFTPadImageFilter', 'itkFFTPadImageFilterICVF23', True, 'itk::Image< itk::CovariantVector< float,2 >,3 >'),
  ('FFTPadImageFilter', 'itk::FFTPadImageFilter', 'itkFFTPadImageFilterICVF32', True, 'itk::Image< itk::CovariantVector< float,3 >,2 >'),
  ('FFTPadImageFilter', 'itk::FFTPadImageFilter', 'itkFFTPadImageFilterICVF33', True, 'itk::Image< itk::CovariantVector< float,3 >,3 >'),
  ('FFTPadImageFilter', 'itk::FFTPadImageFilter', 'itkFFTPadImageFilterICVF42', True, 'itk::Image< itk::CovariantVector< float,4 >,2 >'),
  ('FFTPadImageFilter', 'itk::FFTPadImageFilter', 'itkFFTPadImageFilterICVF43', True, 'itk::Image< itk::CovariantVector< float,4 >,3 >'),
  ('FFTPadImageFilter', 'itk::FFTPadImageFilter', 'itkFFTPadImageFilterISS2', True, 'itk::Image< signed short,2 >'),
  ('FFTPadImageFilter', 'itk::FFTPadImageFilter', 'itkFFTPadImageFilterISS3', True, 'itk::Image< signed short,3 >'),
  ('FFTPadImageFilter', 'itk::FFTPadImageFilter', 'itkFFTPadImageFilterIUC2', True, 'itk::Image< unsigned char,2 >'),
  ('FFTPadImageFilter', 'itk::FFTPadImageFilter', 'itkFFTPadImageFilterIUC3', True, 'itk::Image< unsigned char,3 >'),
  ('FFTPadImageFilter', 'itk::FFTPadImageFilter', 'itkFFTPadImageFilterIUS2', True, 'itk::Image< unsigned short,2 >'),
  ('FFTPadImageFilter', 'itk::FFTPadImageFilter', 'itkFFTPadImageFilterIUS3', True, 'itk::Image< unsigned short,3 >'),
  ('FFTPadImageFilter', 'itk::FFTPadImageFilter', 'itkFFTPadImageFilterIF2', True, 'itk::Image< float,2 >'),
  ('FFTPadImageFilter', 'itk::FFTPadImageFilter', 'itkFFTPadImageFilterIF3', True, 'itk::Image< float,3 >'),
  ('FFTPadImageFilter', 'itk::FFTPadImageFilter', 'itkFFTPadImageFilterID2', True, 'itk::Image< double,2 >'),
  ('FFTPadImageFilter', 'itk::FFTPadImageFilter', 'itkFFTPadImageFilterID3', True, 'itk::Image< double,3 >'),
  ('FFTPadImageFilter', 'itk::FFTPadImageFilter', 'itkFFTPadImageFilterICF2', True, 'itk::Image< std::complex< float >,2 >'),
  ('FFTPadImageFilter', 'itk::FFTPadImageFilter', 'itkFFTPadImageFilterICF3', True, 'itk::Image< std::complex< float >,3 >'),
  ('FFTShiftImageFilter', 'itk::FFTShiftImageFilter', 'itkFFTShiftImageFilterIRGBUC2IRGBUC2', True, 'itk::Image< itk::RGBPixel< unsigned char >,2 >, itk::Image< itk::RGBPixel< unsigned char >,2 >'),
  ('FFTShiftImageFilter', 'itk::FFTShiftImageFilter', 'itkFFTShiftImageFilterIRGBUC3IRGBUC3', True, 'itk::Image< itk::RGBPixel< unsigned char >,3 >, itk::Image< itk::RGBPixel< unsigned char >,3 >'),
  ('FFTShiftImageFilter', 'itk::FFTShiftImageFilter', 'itkFFTShiftImageFilterIRGBAUC2IRGBAUC2', True, 'itk::Image< itk::RGBAPixel< unsigned char >,2 >, itk::Image< itk::RGBAPixel< unsigned char >,2 >'),
  ('FFTShiftImageFilter', 'itk::FFTShiftImageFilter', 'itkFFTShiftImageFilterIRGBAUC3IRGBAUC3', True, 'itk::Image< itk::RGBAPixel< unsigned char >,3 >, itk::Image< itk::RGBAPixel< unsigned char >,3 >'),
  ('FFTShiftImageFilter', 'itk::FFTShiftImageFilter', 'itkFFTShiftImageFilterIVF22IVF22', True, 'itk::Image< itk::Vector< float,2 >,2 >, itk::Image< itk::Vector< float,2 >,2 >'),
  ('FFTShiftImageFilter', 'itk::FFTShiftImageFilter', 'itkFFTShiftImageFilterIVF23IVF23', True, 'itk::Image< itk::Vector< float,2 >,3 >, itk::Image< itk::Vector< float,2 >,3 >'),
  ('FFTShiftImageFilter', 'itk::FFTShiftImageFilter', 'itkFFTShiftImageFilterIVF32IVF32', True, 'itk::Image< itk::Vector< float,3 >,2 >, itk::Image< itk::Vector< float,3 >,2 >'),
  ('FFTShiftImageFilter', 'itk::FFTShiftImageFilter', 'itkFFTShiftImageFilterIVF33IVF33', True, 'itk::Image< itk::Vector< float,3 >,3 >, itk::Image< itk::Vector< float,3 >,3 >'),
  ('FFTShiftImageFilter', 'itk::FFTShiftImageFilter', 'itkFFTShiftImageFilterIVF42IVF42', True, 'itk::Image< itk::Vector< float,4 >,2 >, itk::Image< itk::Vector< float,4 >,2 >'),
  ('FFTShiftImageFilter', 'itk::FFTShiftImageFilter', 'itkFFTShiftImageFilterIVF43IVF43', True, 'itk::Image< itk::Vector< float,4 >,3 >, itk::Image< itk::Vector< float,4 >,3 >'),
  ('FFTShiftImageFilter', 'itk::FFTShiftImageFilter', 'itkFFTShiftImageFilterICVF22ICVF22', True, 'itk::Image< itk::CovariantVector< float,2 >,2 >, itk::Image< itk::CovariantVector< float,2 >,2 >'),
  ('FFTShiftImageFilter', 'itk::FFTShiftImageFilter', 'itkFFTShiftImageFilterICVF23ICVF23', True, 'itk::Image< itk::CovariantVector< float,2 >,3 >, itk::Image< itk::CovariantVector< float,2 >,3 >'),
  ('FFTShiftImageFilter', 'itk::FFTShiftImageFilter', 'itkFFTShiftImageFilterICVF32ICVF32', True, 'itk::Image< itk::CovariantVector< float,3 >,2 >, itk::Image< itk::CovariantVector< float,3 >,2 >'),
  ('FFTShiftImageFilter', 'itk::FFTShiftImageFilter', 'itkFFTShiftImageFilterICVF33ICVF33', True, 'itk::Image< itk::CovariantVector< float,3 >,3 >, itk::Image< itk::CovariantVector< float,3 >,3 >'),
  ('FFTShiftImageFilter', 'itk::FFTShiftImageFilter', 'itkFFTShiftImageFilterICVF42ICVF42', True, 'itk::Image< itk::CovariantVector< float,4 >,2 >, itk::Image< itk::CovariantVector< float,4 >,2 >'),
  ('FFTShiftImageFilter', 'itk::FFTShiftImageFilter', 'itkFFTShiftImageFilterICVF43ICVF43', True, 'itk::Image< itk::CovariantVector< float,4 >,3 >, itk::Image< itk::CovariantVector< float,4 >,3 >'),
  ('FFTShiftImageFilter', 'itk::FFTShiftImageFilter', 'itkFFTShiftImageFilterISS2ISS2', True, 'itk::Image< signed short,2 >, itk::Image< signed short,2 >'),
  ('FFTShiftImageFilter', 'itk::FFTShiftImageFilter', 'itkFFTShiftImageFilterISS3ISS3', True, 'itk::Image< signed short,3 >, itk::Image< signed short,3 >'),
  ('FFTShiftImageFilter', 'itk::FFTShiftImageFilter', 'itkFFTShiftImageFilterIUC2IUC2', True, 'itk::Image< unsigned char,2 >, itk::Image< unsigned char,2 >'),
  ('FFTShiftImageFilter', 'itk::FFTShiftImageFilter', 'itkFFTShiftImageFilterIUC3IUC3', True, 'itk::Image< unsigned char,3 >, itk::Image< unsigned char,3 >'),
  ('FFTShiftImageFilter', 'itk::FFTShiftImageFilter', 'itkFFTShiftImageFilterIUS2IUS2', True, 'itk::Image< unsigned short,2 >, itk::Image< unsigned short,2 >'),
  ('FFTShiftImageFilter', 'itk::FFTShiftImageFilter', 'itkFFTShiftImageFilterIUS3IUS3', True, 'itk::Image< unsigned short,3 >, itk::Image< unsigned short,3 >'),
  ('FFTShiftImageFilter', 'itk::FFTShiftImageFilter', 'itkFFTShiftImageFilterIF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >'),
  ('FFTShiftImageFilter', 'itk::FFTShiftImageFilter', 'itkFFTShiftImageFilterIF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >'),
  ('FFTShiftImageFilter', 'itk::FFTShiftImageFilter', 'itkFFTShiftImageFilterID2ID2', True, 'itk::Image< double,2 >, itk::Image< double,2 >'),
  ('FFTShiftImageFilter', 'itk::FFTShiftImageFilter', 'itkFFTShiftImageFilterID3ID3', True, 'itk::Image< double,3 >, itk::Image< double,3 >'),
  ('FFTShiftImageFilter', 'itk::FFTShiftImageFilter', 'itkFFTShiftImageFilterICF2ICF2', True, 'itk::Image< std::complex< float >,2 >, itk::Image< std::complex< float >,2 >'),
  ('FFTShiftImageFilter', 'itk::FFTShiftImageFilter', 'itkFFTShiftImageFilterICF3ICF3', True, 'itk::Image< std::complex< float >,3 >, itk::Image< std::complex< float >,3 >'),
  ('ForwardFFTImageFilter', 'itk::ForwardFFTImageFilter', 'itkForwardFFTImageFilterIF2ICF2', True, 'itk::Image< float,2 >, itk::Image< std::complex< float >,2 >'),
  ('ForwardFFTImageFilter', 'itk::ForwardFFTImageFilter', 'itkForwardFFTImageFilterIF3ICF3', True, 'itk::Image< float,3 >, itk::Image< std::complex< float >,3 >'),
  ('FullToHalfHermitianImageFilter', 'itk::FullToHalfHermitianImageFilter', 'itkFullToHalfHermitianImageFilterICF2', True, 'itk::Image< std::complex< float >,2 >'),
  ('FullToHalfHermitianImageFilter', 'itk::FullToHalfHermitianImageFilter', 'itkFullToHalfHermitianImageFilterICF3', True, 'itk::Image< std::complex< float >,3 >'),
  ('HalfHermitianToRealInverseFFTImageFilter', 'itk::HalfHermitianToRealInverseFFTImageFilter', 'itkHalfHermitianToRealInverseFFTImageFilterICF2IF2', True, 'itk::Image< std::complex< float >,2 >, itk::Image< float,2 >'),
  ('HalfHermitianToRealInverseFFTImageFilter', 'itk::HalfHermitianToRealInverseFFTImageFilter', 'itkHalfHermitianToRealInverseFFTImageFilterICF3IF3', True, 'itk::Image< std::complex< float >,3 >, itk::Image< float,3 >'),
  ('HalfToFullHermitianImageFilter', 'itk::HalfToFullHermitianImageFilter', 'itkHalfToFullHermitianImageFilterICF2', True, 'itk::Image< std::complex< float >,2 >'),
  ('HalfToFullHermitianImageFilter', 'itk::HalfToFullHermitianImageFilter', 'itkHalfToFullHermitianImageFilterICF3', True, 'itk::Image< std::complex< float >,3 >'),
  ('InverseFFTImageFilter', 'itk::InverseFFTImageFilter', 'itkInverseFFTImageFilterICF2IF2', True, 'itk::Image< std::complex< float >,2 >, itk::Image< float,2 >'),
  ('InverseFFTImageFilter', 'itk::InverseFFTImageFilter', 'itkInverseFFTImageFilterICF3IF3', True, 'itk::Image< std::complex< float >,3 >, itk::Image< float,3 >'),
  ('RealToHalfHermitianForwardFFTImageFilter', 'itk::RealToHalfHermitianForwardFFTImageFilter', 'itkRealToHalfHermitianForwardFFTImageFilterIF2ICF2', True, 'itk::Image< float,2 >, itk::Image< std::complex< float >,2 >'),
  ('RealToHalfHermitianForwardFFTImageFilter', 'itk::RealToHalfHermitianForwardFFTImageFilter', 'itkRealToHalfHermitianForwardFFTImageFilterIF3ICF3', True, 'itk::Image< float,3 >, itk::Image< std::complex< float >,3 >'),
  ('VnlComplexToComplexFFTImageFilter', 'itk::VnlComplexToComplexFFTImageFilter', 'itkVnlComplexToComplexFFTImageFilterICF2', True, 'itk::Image< std::complex< float >,2 >'),
  ('VnlComplexToComplexFFTImageFilter', 'itk::VnlComplexToComplexFFTImageFilter', 'itkVnlComplexToComplexFFTImageFilterICF3', True, 'itk::Image< std::complex< float >,3 >'),
  ('VnlForwardFFTImageFilter', 'itk::VnlForwardFFTImageFilter', 'itkVnlForwardFFTImageFilterIF2ICF2', True, 'itk::Image< float,2 >, itk::Image< std::complex< float >,2 >'),
  ('VnlForwardFFTImageFilter', 'itk::VnlForwardFFTImageFilter', 'itkVnlForwardFFTImageFilterIF3ICF3', True, 'itk::Image< float,3 >, itk::Image< std::complex< float >,3 >'),
  ('VnlHalfHermitianToRealInverseFFTImageFilter', 'itk::VnlHalfHermitianToRealInverseFFTImageFilter', 'itkVnlHalfHermitianToRealInverseFFTImageFilterICF2IF2', True, 'itk::Image< std::complex< float >,2 >, itk::Image< float,2 >'),
  ('VnlHalfHermitianToRealInverseFFTImageFilter', 'itk::VnlHalfHermitianToRealInverseFFTImageFilter', 'itkVnlHalfHermitianToRealInverseFFTImageFilterICF3IF3', True, 'itk::Image< std::complex< float >,3 >, itk::Image< float,3 >'),
  ('VnlInverseFFTImageFilter', 'itk::VnlInverseFFTImageFilter', 'itkVnlInverseFFTImageFilterICF2IF2', True, 'itk::Image< std::complex< float >,2 >, itk::Image< float,2 >'),
  ('VnlInverseFFTImageFilter', 'itk::VnlInverseFFTImageFilter', 'itkVnlInverseFFTImageFilterICF3IF3', True, 'itk::Image< std::complex< float >,3 >, itk::Image< float,3 >'),
  ('VnlRealToHalfHermitianForwardFFTImageFilter', 'itk::VnlRealToHalfHermitianForwardFFTImageFilter', 'itkVnlRealToHalfHermitianForwardFFTImageFilterIF2ICF2', True, 'itk::Image< float,2 >, itk::Image< std::complex< float >,2 >'),
  ('VnlRealToHalfHermitianForwardFFTImageFilter', 'itk::VnlRealToHalfHermitianForwardFFTImageFilter', 'itkVnlRealToHalfHermitianForwardFFTImageFilterIF3ICF3', True, 'itk::Image< float,3 >, itk::Image< std::complex< float >,3 >'),
)
snake_case_functions = ('half_to_full_hermitian_image_filter', 'complex_to_complex_fft_image_filter', 'inverse_fft_image_filter', 'full_to_half_hermitian_image_filter', 'real_to_half_hermitian_forward_fft_image_filter', 'fft_pad_image_filter', 'vnl_forward_fft_image_filter', 'vnl_half_hermitian_to_real_inverse_fft_image_filter', 'vnl_real_to_half_hermitian_forward_fft_image_filter', 'fft_shift_image_filter', 'vnl_complex_to_complex_fft_image_filter', 'half_hermitian_to_real_inverse_fft_image_filter', 'vnl_inverse_fft_image_filter', 'forward_fft_image_filter', )
