depends = ('ITKPyBase', 'ITKCommon', )
templates = (
  ('GaborImageSource', 'itk::GaborImageSource', 'itkGaborImageSourceISS2', True, 'itk::Image< signed short,2 >'),
  ('GaborImageSource', 'itk::GaborImageSource', 'itkGaborImageSourceISS3', True, 'itk::Image< signed short,3 >'),
  ('GaborImageSource', 'itk::GaborImageSource', 'itkGaborImageSourceIUC2', True, 'itk::Image< unsigned char,2 >'),
  ('GaborImageSource', 'itk::GaborImageSource', 'itkGaborImageSourceIUC3', True, 'itk::Image< unsigned char,3 >'),
  ('GaborImageSource', 'itk::GaborImageSource', 'itkGaborImageSourceIUS2', True, 'itk::Image< unsigned short,2 >'),
  ('GaborImageSource', 'itk::GaborImageSource', 'itkGaborImageSourceIUS3', True, 'itk::Image< unsigned short,3 >'),
  ('GaborImageSource', 'itk::GaborImageSource', 'itkGaborImageSourceIF2', True, 'itk::Image< float,2 >'),
  ('GaborImageSource', 'itk::GaborImageSource', 'itkGaborImageSourceIF3', True, 'itk::Image< float,3 >'),
  ('GaborImageSource', 'itk::GaborImageSource', 'itkGaborImageSourceID2', True, 'itk::Image< double,2 >'),
  ('GaborImageSource', 'itk::GaborImageSource', 'itkGaborImageSourceID3', True, 'itk::Image< double,3 >'),
  ('GaussianImageSource', 'itk::GaussianImageSource', 'itkGaussianImageSourceISS2', True, 'itk::Image< signed short,2 >'),
  ('GaussianImageSource', 'itk::GaussianImageSource', 'itkGaussianImageSourceISS3', True, 'itk::Image< signed short,3 >'),
  ('GaussianImageSource', 'itk::GaussianImageSource', 'itkGaussianImageSourceIUC2', True, 'itk::Image< unsigned char,2 >'),
  ('GaussianImageSource', 'itk::GaussianImageSource', 'itkGaussianImageSourceIUC3', True, 'itk::Image< unsigned char,3 >'),
  ('GaussianImageSource', 'itk::GaussianImageSource', 'itkGaussianImageSourceIUS2', True, 'itk::Image< unsigned short,2 >'),
  ('GaussianImageSource', 'itk::GaussianImageSource', 'itkGaussianImageSourceIUS3', True, 'itk::Image< unsigned short,3 >'),
  ('GaussianImageSource', 'itk::GaussianImageSource', 'itkGaussianImageSourceIF2', True, 'itk::Image< float,2 >'),
  ('GaussianImageSource', 'itk::GaussianImageSource', 'itkGaussianImageSourceIF3', True, 'itk::Image< float,3 >'),
  ('GaussianImageSource', 'itk::GaussianImageSource', 'itkGaussianImageSourceID2', True, 'itk::Image< double,2 >'),
  ('GaussianImageSource', 'itk::GaussianImageSource', 'itkGaussianImageSourceID3', True, 'itk::Image< double,3 >'),
  ('GenerateImageSource', 'itk::GenerateImageSource', 'itkGenerateImageSourceIRGBUC2', True, 'itk::Image< itk::RGBPixel< unsigned char >,2 >'),
  ('GenerateImageSource', 'itk::GenerateImageSource', 'itkGenerateImageSourceIRGBUC3', True, 'itk::Image< itk::RGBPixel< unsigned char >,3 >'),
  ('GenerateImageSource', 'itk::GenerateImageSource', 'itkGenerateImageSourceIRGBAUC2', True, 'itk::Image< itk::RGBAPixel< unsigned char >,2 >'),
  ('GenerateImageSource', 'itk::GenerateImageSource', 'itkGenerateImageSourceIRGBAUC3', True, 'itk::Image< itk::RGBAPixel< unsigned char >,3 >'),
  ('GenerateImageSource', 'itk::GenerateImageSource', 'itkGenerateImageSourceIVF22', True, 'itk::Image< itk::Vector< float,2 >,2 >'),
  ('GenerateImageSource', 'itk::GenerateImageSource', 'itkGenerateImageSourceIVF23', True, 'itk::Image< itk::Vector< float,2 >,3 >'),
  ('GenerateImageSource', 'itk::GenerateImageSource', 'itkGenerateImageSourceIVF32', True, 'itk::Image< itk::Vector< float,3 >,2 >'),
  ('GenerateImageSource', 'itk::GenerateImageSource', 'itkGenerateImageSourceIVF33', True, 'itk::Image< itk::Vector< float,3 >,3 >'),
  ('GenerateImageSource', 'itk::GenerateImageSource', 'itkGenerateImageSourceIVF42', True, 'itk::Image< itk::Vector< float,4 >,2 >'),
  ('GenerateImageSource', 'itk::GenerateImageSource', 'itkGenerateImageSourceIVF43', True, 'itk::Image< itk::Vector< float,4 >,3 >'),
  ('GenerateImageSource', 'itk::GenerateImageSource', 'itkGenerateImageSourceICVF22', True, 'itk::Image< itk::CovariantVector< float,2 >,2 >'),
  ('GenerateImageSource', 'itk::GenerateImageSource', 'itkGenerateImageSourceICVF23', True, 'itk::Image< itk::CovariantVector< float,2 >,3 >'),
  ('GenerateImageSource', 'itk::GenerateImageSource', 'itkGenerateImageSourceICVF32', True, 'itk::Image< itk::CovariantVector< float,3 >,2 >'),
  ('GenerateImageSource', 'itk::GenerateImageSource', 'itkGenerateImageSourceICVF33', True, 'itk::Image< itk::CovariantVector< float,3 >,3 >'),
  ('GenerateImageSource', 'itk::GenerateImageSource', 'itkGenerateImageSourceICVF42', True, 'itk::Image< itk::CovariantVector< float,4 >,2 >'),
  ('GenerateImageSource', 'itk::GenerateImageSource', 'itkGenerateImageSourceICVF43', True, 'itk::Image< itk::CovariantVector< float,4 >,3 >'),
  ('GenerateImageSource', 'itk::GenerateImageSource', 'itkGenerateImageSourceISS2', True, 'itk::Image< signed short,2 >'),
  ('GenerateImageSource', 'itk::GenerateImageSource', 'itkGenerateImageSourceISS3', True, 'itk::Image< signed short,3 >'),
  ('GenerateImageSource', 'itk::GenerateImageSource', 'itkGenerateImageSourceIUC2', True, 'itk::Image< unsigned char,2 >'),
  ('GenerateImageSource', 'itk::GenerateImageSource', 'itkGenerateImageSourceIUC3', True, 'itk::Image< unsigned char,3 >'),
  ('GenerateImageSource', 'itk::GenerateImageSource', 'itkGenerateImageSourceIUS2', True, 'itk::Image< unsigned short,2 >'),
  ('GenerateImageSource', 'itk::GenerateImageSource', 'itkGenerateImageSourceIUS3', True, 'itk::Image< unsigned short,3 >'),
  ('GenerateImageSource', 'itk::GenerateImageSource', 'itkGenerateImageSourceIF2', True, 'itk::Image< float,2 >'),
  ('GenerateImageSource', 'itk::GenerateImageSource', 'itkGenerateImageSourceIF3', True, 'itk::Image< float,3 >'),
  ('GenerateImageSource', 'itk::GenerateImageSource', 'itkGenerateImageSourceID2', True, 'itk::Image< double,2 >'),
  ('GenerateImageSource', 'itk::GenerateImageSource', 'itkGenerateImageSourceID3', True, 'itk::Image< double,3 >'),
  ('GenerateImageSource', 'itk::GenerateImageSource', 'itkGenerateImageSourceICF2', True, 'itk::Image< std::complex< float >,2 >'),
  ('GenerateImageSource', 'itk::GenerateImageSource', 'itkGenerateImageSourceICF3', True, 'itk::Image< std::complex< float >,3 >'),
  ('GenerateImageSource', 'itk::GenerateImageSource', 'itkGenerateImageSourceVIUC2', True, 'itk::VectorImage< unsigned char,2 >'),
  ('GenerateImageSource', 'itk::GenerateImageSource', 'itkGenerateImageSourceVISS2', True, 'itk::VectorImage< signed short,2 >'),
  ('GenerateImageSource', 'itk::GenerateImageSource', 'itkGenerateImageSourceVIUS2', True, 'itk::VectorImage< unsigned short,2 >'),
  ('GenerateImageSource', 'itk::GenerateImageSource', 'itkGenerateImageSourceVIF2', True, 'itk::VectorImage< float,2 >'),
  ('GenerateImageSource', 'itk::GenerateImageSource', 'itkGenerateImageSourceVID2', True, 'itk::VectorImage< double,2 >'),
  ('GenerateImageSource', 'itk::GenerateImageSource', 'itkGenerateImageSourceVIUC3', True, 'itk::VectorImage< unsigned char,3 >'),
  ('GenerateImageSource', 'itk::GenerateImageSource', 'itkGenerateImageSourceVISS3', True, 'itk::VectorImage< signed short,3 >'),
  ('GenerateImageSource', 'itk::GenerateImageSource', 'itkGenerateImageSourceVIUS3', True, 'itk::VectorImage< unsigned short,3 >'),
  ('GenerateImageSource', 'itk::GenerateImageSource', 'itkGenerateImageSourceVIF3', True, 'itk::VectorImage< float,3 >'),
  ('GenerateImageSource', 'itk::GenerateImageSource', 'itkGenerateImageSourceVID3', True, 'itk::VectorImage< double,3 >'),
  ('GridImageSource', 'itk::GridImageSource', 'itkGridImageSourceISS2', True, 'itk::Image< signed short,2 >'),
  ('GridImageSource', 'itk::GridImageSource', 'itkGridImageSourceISS3', True, 'itk::Image< signed short,3 >'),
  ('GridImageSource', 'itk::GridImageSource', 'itkGridImageSourceIUC2', True, 'itk::Image< unsigned char,2 >'),
  ('GridImageSource', 'itk::GridImageSource', 'itkGridImageSourceIUC3', True, 'itk::Image< unsigned char,3 >'),
  ('GridImageSource', 'itk::GridImageSource', 'itkGridImageSourceIUS2', True, 'itk::Image< unsigned short,2 >'),
  ('GridImageSource', 'itk::GridImageSource', 'itkGridImageSourceIUS3', True, 'itk::Image< unsigned short,3 >'),
  ('GridImageSource', 'itk::GridImageSource', 'itkGridImageSourceIF2', True, 'itk::Image< float,2 >'),
  ('GridImageSource', 'itk::GridImageSource', 'itkGridImageSourceIF3', True, 'itk::Image< float,3 >'),
  ('GridImageSource', 'itk::GridImageSource', 'itkGridImageSourceID2', True, 'itk::Image< double,2 >'),
  ('GridImageSource', 'itk::GridImageSource', 'itkGridImageSourceID3', True, 'itk::Image< double,3 >'),
  ('ParametricImageSource', 'itk::ParametricImageSource', 'itkParametricImageSourceIRGBUC2', True, 'itk::Image< itk::RGBPixel< unsigned char >,2 >'),
  ('ParametricImageSource', 'itk::ParametricImageSource', 'itkParametricImageSourceIRGBUC3', True, 'itk::Image< itk::RGBPixel< unsigned char >,3 >'),
  ('ParametricImageSource', 'itk::ParametricImageSource', 'itkParametricImageSourceIRGBAUC2', True, 'itk::Image< itk::RGBAPixel< unsigned char >,2 >'),
  ('ParametricImageSource', 'itk::ParametricImageSource', 'itkParametricImageSourceIRGBAUC3', True, 'itk::Image< itk::RGBAPixel< unsigned char >,3 >'),
  ('ParametricImageSource', 'itk::ParametricImageSource', 'itkParametricImageSourceIVF22', True, 'itk::Image< itk::Vector< float,2 >,2 >'),
  ('ParametricImageSource', 'itk::ParametricImageSource', 'itkParametricImageSourceIVF23', True, 'itk::Image< itk::Vector< float,2 >,3 >'),
  ('ParametricImageSource', 'itk::ParametricImageSource', 'itkParametricImageSourceIVF32', True, 'itk::Image< itk::Vector< float,3 >,2 >'),
  ('ParametricImageSource', 'itk::ParametricImageSource', 'itkParametricImageSourceIVF33', True, 'itk::Image< itk::Vector< float,3 >,3 >'),
  ('ParametricImageSource', 'itk::ParametricImageSource', 'itkParametricImageSourceIVF42', True, 'itk::Image< itk::Vector< float,4 >,2 >'),
  ('ParametricImageSource', 'itk::ParametricImageSource', 'itkParametricImageSourceIVF43', True, 'itk::Image< itk::Vector< float,4 >,3 >'),
  ('ParametricImageSource', 'itk::ParametricImageSource', 'itkParametricImageSourceICVF22', True, 'itk::Image< itk::CovariantVector< float,2 >,2 >'),
  ('ParametricImageSource', 'itk::ParametricImageSource', 'itkParametricImageSourceICVF23', True, 'itk::Image< itk::CovariantVector< float,2 >,3 >'),
  ('ParametricImageSource', 'itk::ParametricImageSource', 'itkParametricImageSourceICVF32', True, 'itk::Image< itk::CovariantVector< float,3 >,2 >'),
  ('ParametricImageSource', 'itk::ParametricImageSource', 'itkParametricImageSourceICVF33', True, 'itk::Image< itk::CovariantVector< float,3 >,3 >'),
  ('ParametricImageSource', 'itk::ParametricImageSource', 'itkParametricImageSourceICVF42', True, 'itk::Image< itk::CovariantVector< float,4 >,2 >'),
  ('ParametricImageSource', 'itk::ParametricImageSource', 'itkParametricImageSourceICVF43', True, 'itk::Image< itk::CovariantVector< float,4 >,3 >'),
  ('ParametricImageSource', 'itk::ParametricImageSource', 'itkParametricImageSourceISS2', True, 'itk::Image< signed short,2 >'),
  ('ParametricImageSource', 'itk::ParametricImageSource', 'itkParametricImageSourceISS3', True, 'itk::Image< signed short,3 >'),
  ('ParametricImageSource', 'itk::ParametricImageSource', 'itkParametricImageSourceIUC2', True, 'itk::Image< unsigned char,2 >'),
  ('ParametricImageSource', 'itk::ParametricImageSource', 'itkParametricImageSourceIUC3', True, 'itk::Image< unsigned char,3 >'),
  ('ParametricImageSource', 'itk::ParametricImageSource', 'itkParametricImageSourceIUS2', True, 'itk::Image< unsigned short,2 >'),
  ('ParametricImageSource', 'itk::ParametricImageSource', 'itkParametricImageSourceIUS3', True, 'itk::Image< unsigned short,3 >'),
  ('ParametricImageSource', 'itk::ParametricImageSource', 'itkParametricImageSourceIF2', True, 'itk::Image< float,2 >'),
  ('ParametricImageSource', 'itk::ParametricImageSource', 'itkParametricImageSourceIF3', True, 'itk::Image< float,3 >'),
  ('ParametricImageSource', 'itk::ParametricImageSource', 'itkParametricImageSourceID2', True, 'itk::Image< double,2 >'),
  ('ParametricImageSource', 'itk::ParametricImageSource', 'itkParametricImageSourceID3', True, 'itk::Image< double,3 >'),
  ('ParametricImageSource', 'itk::ParametricImageSource', 'itkParametricImageSourceICF2', True, 'itk::Image< std::complex< float >,2 >'),
  ('ParametricImageSource', 'itk::ParametricImageSource', 'itkParametricImageSourceICF3', True, 'itk::Image< std::complex< float >,3 >'),
  ('ParametricImageSource', 'itk::ParametricImageSource', 'itkParametricImageSourceVIUC2', True, 'itk::VectorImage< unsigned char,2 >'),
  ('ParametricImageSource', 'itk::ParametricImageSource', 'itkParametricImageSourceVISS2', True, 'itk::VectorImage< signed short,2 >'),
  ('ParametricImageSource', 'itk::ParametricImageSource', 'itkParametricImageSourceVIUS2', True, 'itk::VectorImage< unsigned short,2 >'),
  ('ParametricImageSource', 'itk::ParametricImageSource', 'itkParametricImageSourceVIF2', True, 'itk::VectorImage< float,2 >'),
  ('ParametricImageSource', 'itk::ParametricImageSource', 'itkParametricImageSourceVID2', True, 'itk::VectorImage< double,2 >'),
  ('ParametricImageSource', 'itk::ParametricImageSource', 'itkParametricImageSourceVIUC3', True, 'itk::VectorImage< unsigned char,3 >'),
  ('ParametricImageSource', 'itk::ParametricImageSource', 'itkParametricImageSourceVISS3', True, 'itk::VectorImage< signed short,3 >'),
  ('ParametricImageSource', 'itk::ParametricImageSource', 'itkParametricImageSourceVIUS3', True, 'itk::VectorImage< unsigned short,3 >'),
  ('ParametricImageSource', 'itk::ParametricImageSource', 'itkParametricImageSourceVIF3', True, 'itk::VectorImage< float,3 >'),
  ('ParametricImageSource', 'itk::ParametricImageSource', 'itkParametricImageSourceVID3', True, 'itk::VectorImage< double,3 >'),
  ('PhysicalPointImageSource', 'itk::PhysicalPointImageSource', 'itkPhysicalPointImageSourceIVF22', True, 'itk::Image< itk::Vector< float,2 >,2 >'),
  ('PhysicalPointImageSource', 'itk::PhysicalPointImageSource', 'itkPhysicalPointImageSourceIVF23', True, 'itk::Image< itk::Vector< float,2 >,3 >'),
  ('PhysicalPointImageSource', 'itk::PhysicalPointImageSource', 'itkPhysicalPointImageSourceIVF32', True, 'itk::Image< itk::Vector< float,3 >,2 >'),
  ('PhysicalPointImageSource', 'itk::PhysicalPointImageSource', 'itkPhysicalPointImageSourceIVF33', True, 'itk::Image< itk::Vector< float,3 >,3 >'),
  ('PhysicalPointImageSource', 'itk::PhysicalPointImageSource', 'itkPhysicalPointImageSourceIVF42', True, 'itk::Image< itk::Vector< float,4 >,2 >'),
  ('PhysicalPointImageSource', 'itk::PhysicalPointImageSource', 'itkPhysicalPointImageSourceIVF43', True, 'itk::Image< itk::Vector< float,4 >,3 >'),
  ('PhysicalPointImageSource', 'itk::PhysicalPointImageSource', 'itkPhysicalPointImageSourceICVF22', True, 'itk::Image< itk::CovariantVector< float,2 >,2 >'),
  ('PhysicalPointImageSource', 'itk::PhysicalPointImageSource', 'itkPhysicalPointImageSourceICVF23', True, 'itk::Image< itk::CovariantVector< float,2 >,3 >'),
  ('PhysicalPointImageSource', 'itk::PhysicalPointImageSource', 'itkPhysicalPointImageSourceICVF32', True, 'itk::Image< itk::CovariantVector< float,3 >,2 >'),
  ('PhysicalPointImageSource', 'itk::PhysicalPointImageSource', 'itkPhysicalPointImageSourceICVF33', True, 'itk::Image< itk::CovariantVector< float,3 >,3 >'),
  ('PhysicalPointImageSource', 'itk::PhysicalPointImageSource', 'itkPhysicalPointImageSourceICVF42', True, 'itk::Image< itk::CovariantVector< float,4 >,2 >'),
  ('PhysicalPointImageSource', 'itk::PhysicalPointImageSource', 'itkPhysicalPointImageSourceICVF43', True, 'itk::Image< itk::CovariantVector< float,4 >,3 >'),
  ('PhysicalPointImageSource', 'itk::PhysicalPointImageSource', 'itkPhysicalPointImageSourceVIUC2', True, 'itk::VectorImage< unsigned char,2 >'),
  ('PhysicalPointImageSource', 'itk::PhysicalPointImageSource', 'itkPhysicalPointImageSourceVISS2', True, 'itk::VectorImage< signed short,2 >'),
  ('PhysicalPointImageSource', 'itk::PhysicalPointImageSource', 'itkPhysicalPointImageSourceVIUS2', True, 'itk::VectorImage< unsigned short,2 >'),
  ('PhysicalPointImageSource', 'itk::PhysicalPointImageSource', 'itkPhysicalPointImageSourceVIF2', True, 'itk::VectorImage< float,2 >'),
  ('PhysicalPointImageSource', 'itk::PhysicalPointImageSource', 'itkPhysicalPointImageSourceVID2', True, 'itk::VectorImage< double,2 >'),
  ('PhysicalPointImageSource', 'itk::PhysicalPointImageSource', 'itkPhysicalPointImageSourceVIUC3', True, 'itk::VectorImage< unsigned char,3 >'),
  ('PhysicalPointImageSource', 'itk::PhysicalPointImageSource', 'itkPhysicalPointImageSourceVISS3', True, 'itk::VectorImage< signed short,3 >'),
  ('PhysicalPointImageSource', 'itk::PhysicalPointImageSource', 'itkPhysicalPointImageSourceVIUS3', True, 'itk::VectorImage< unsigned short,3 >'),
  ('PhysicalPointImageSource', 'itk::PhysicalPointImageSource', 'itkPhysicalPointImageSourceVIF3', True, 'itk::VectorImage< float,3 >'),
  ('PhysicalPointImageSource', 'itk::PhysicalPointImageSource', 'itkPhysicalPointImageSourceVID3', True, 'itk::VectorImage< double,3 >'),
)
snake_case_functions = ('grid_image_source', 'parametric_image_source', 'physical_point_image_source', 'generate_image_source', 'gabor_image_source', 'gaussian_image_source', )
