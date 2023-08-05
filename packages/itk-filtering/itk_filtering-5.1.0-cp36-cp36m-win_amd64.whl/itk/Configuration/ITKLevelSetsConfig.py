depends = ('ITKPyBase', 'ITKThresholding', 'ITKSignedDistanceFunction', 'ITKOptimizers', 'ITKNarrowBand', 'ITKImageFeature', 'ITKImageCompare', 'ITKIOImageBase', 'ITKFiniteDifference', 'ITKFastMarching', 'ITKDistanceMap', 'ITKAnisotropicSmoothing', )
templates = (
  ('LevelSetFunction', 'itk::LevelSetFunction', 'itkLevelSetFunctionIF2', True, 'itk::Image< float,2 >'),
  ('LevelSetFunction', 'itk::LevelSetFunction', 'itkLevelSetFunctionIF3', True, 'itk::Image< float,3 >'),
  ('LevelSetFunction', 'itk::LevelSetFunction', 'itkLevelSetFunctionID2', True, 'itk::Image< double,2 >'),
  ('LevelSetFunction', 'itk::LevelSetFunction', 'itkLevelSetFunctionID3', True, 'itk::Image< double,3 >'),
  ('SparseFieldLevelSetImageFilter', 'itk::SparseFieldLevelSetImageFilter', 'itkSparseFieldLevelSetImageFilterIF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >'),
  ('SparseFieldLevelSetImageFilter', 'itk::SparseFieldLevelSetImageFilter', 'itkSparseFieldLevelSetImageFilterIF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >'),
  ('SparseFieldLevelSetImageFilter', 'itk::SparseFieldLevelSetImageFilter', 'itkSparseFieldLevelSetImageFilterID2ID2', True, 'itk::Image< double,2 >, itk::Image< double,2 >'),
  ('SparseFieldLevelSetImageFilter', 'itk::SparseFieldLevelSetImageFilter', 'itkSparseFieldLevelSetImageFilterID3ID3', True, 'itk::Image< double,3 >, itk::Image< double,3 >'),
  ('SparseFieldLevelSetNode', 'itk::SparseFieldLevelSetNode', 'itkSparseFieldLevelSetNodeI2', False, 'itk::Index< 2 >'),
  ('SparseFieldLevelSetNode', 'itk::SparseFieldLevelSetNode', 'itkSparseFieldLevelSetNodeI3', False, 'itk::Index< 3 >'),
  ('SparseFieldLayer', 'itk::SparseFieldLayer', 'itkSparseFieldLayerSFLSNI2', False, 'itk::SparseFieldLevelSetNode< itk::Index< 2 > >'),
  ('SparseFieldLayer', 'itk::SparseFieldLayer', 'itkSparseFieldLayerSFLSNI3', False, 'itk::SparseFieldLevelSetNode< itk::Index< 3 > >'),
  ('NormalBandNode', 'itk::NormalBandNode', 'itkNormalBandNodeIF2', False, 'itk::Image< float,2 >'),
  ('NormalBandNode', 'itk::NormalBandNode', 'itkNormalBandNodeIF3', False, 'itk::Image< float,3 >'),
  ('NormalBandNode', 'itk::NormalBandNode', 'itkNormalBandNodeID2', False, 'itk::Image< double,2 >'),
  ('NormalBandNode', 'itk::NormalBandNode', 'itkNormalBandNodeID3', False, 'itk::Image< double,3 >'),
  ('Image', 'itk::Image', 'itkImageNBNIF22', False, 'itk::NormalBandNode< itk::Image< float,2 > >*, 2'),
  ('vector', 'std::vector', 'vectoritkImageNBNIF22', False, 'itk::Image< itk::NormalBandNode< itk::Image< float,2 > >*, 2  > '),
  ('Image', 'itk::Image', 'itkImageNBNID22', False, 'itk::NormalBandNode< itk::Image< double,2 > >*, 2'),
  ('vector', 'std::vector', 'vectoritkImageNBNID22', False, 'itk::Image< itk::NormalBandNode< itk::Image< double,2 > >*, 2  > '),
  ('Image', 'itk::Image', 'itkImageNBNIF33', False, 'itk::NormalBandNode< itk::Image< float,3 > >*, 3'),
  ('vector', 'std::vector', 'vectoritkImageNBNIF33', False, 'itk::Image< itk::NormalBandNode< itk::Image< float,3 > >*, 3  > '),
  ('Image', 'itk::Image', 'itkImageNBNID33', False, 'itk::NormalBandNode< itk::Image< double,3 > >*, 3'),
  ('vector', 'std::vector', 'vectoritkImageNBNID33', False, 'itk::Image< itk::NormalBandNode< itk::Image< double,3 > >*, 3  > '),
  ('SparseFieldFourthOrderLevelSetImageFilter', 'itk::SparseFieldFourthOrderLevelSetImageFilter', 'itkSparseFieldFourthOrderLevelSetImageFilterIF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >'),
  ('SparseFieldFourthOrderLevelSetImageFilter', 'itk::SparseFieldFourthOrderLevelSetImageFilter', 'itkSparseFieldFourthOrderLevelSetImageFilterIF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >'),
  ('SparseFieldFourthOrderLevelSetImageFilter', 'itk::SparseFieldFourthOrderLevelSetImageFilter', 'itkSparseFieldFourthOrderLevelSetImageFilterID2ID2', True, 'itk::Image< double,2 >, itk::Image< double,2 >'),
  ('SparseFieldFourthOrderLevelSetImageFilter', 'itk::SparseFieldFourthOrderLevelSetImageFilter', 'itkSparseFieldFourthOrderLevelSetImageFilterID3ID3', True, 'itk::Image< double,3 >, itk::Image< double,3 >'),
  ('SparseImage', 'itk::SparseImage', 'itkSparseImageNBNIF22', False, 'itk::NormalBandNode< itk::Image< float,2 > >, 2'),
  ('SparseImage', 'itk::SparseImage', 'itkSparseImageNBNID22', False, 'itk::NormalBandNode< itk::Image< double,2 > >, 2'),
  ('SparseImage', 'itk::SparseImage', 'itkSparseImageNBNIF33', False, 'itk::NormalBandNode< itk::Image< float,3 > >, 3'),
  ('SparseImage', 'itk::SparseImage', 'itkSparseImageNBNID33', False, 'itk::NormalBandNode< itk::Image< double,3 > >, 3'),
  ('LevelSetFunctionWithRefitTerm', 'itk::LevelSetFunctionWithRefitTerm', 'itkLevelSetFunctionWithRefitTermIF2SINBNIF22', True, 'itk::Image< float,2 >, itk::SparseImage< itk::NormalBandNode< itk::Image< float,2 > >, 2 >'),
  ('LevelSetFunctionWithRefitTerm', 'itk::LevelSetFunctionWithRefitTerm', 'itkLevelSetFunctionWithRefitTermID2SINBNID22', True, 'itk::Image< double,2 >, itk::SparseImage< itk::NormalBandNode< itk::Image< double,2 > >, 2 >'),
  ('LevelSetFunctionWithRefitTerm', 'itk::LevelSetFunctionWithRefitTerm', 'itkLevelSetFunctionWithRefitTermIF3SINBNIF33', True, 'itk::Image< float,3 >, itk::SparseImage< itk::NormalBandNode< itk::Image< float,3 > >, 3 >'),
  ('LevelSetFunctionWithRefitTerm', 'itk::LevelSetFunctionWithRefitTerm', 'itkLevelSetFunctionWithRefitTermID3SINBNID33', True, 'itk::Image< double,3 >, itk::SparseImage< itk::NormalBandNode< itk::Image< double,3 > >, 3 >'),
  ('SparseFieldLayer', 'itk::SparseFieldLayer', 'itkSparseFieldLayerNBNIF2', False, 'itk::NormalBandNode< itk::Image< float,2 > >'),
  ('SparseFieldLayer', 'itk::SparseFieldLayer', 'itkSparseFieldLayerNBNID2', False, 'itk::NormalBandNode< itk::Image< double,2 > >'),
  ('SparseFieldLayer', 'itk::SparseFieldLayer', 'itkSparseFieldLayerNBNIF3', False, 'itk::NormalBandNode< itk::Image< float,3 > >'),
  ('SparseFieldLayer', 'itk::SparseFieldLayer', 'itkSparseFieldLayerNBNID3', False, 'itk::NormalBandNode< itk::Image< double,3 > >'),
  ('SegmentationLevelSetImageFilter', 'itk::SegmentationLevelSetImageFilter', 'itkSegmentationLevelSetImageFilterIF2IF2F', True, 'itk::Image< float,2 >,itk::Image< float,2 >,float'),
  ('SegmentationLevelSetImageFilter', 'itk::SegmentationLevelSetImageFilter', 'itkSegmentationLevelSetImageFilterIF2IVF22F', True, 'itk::Image< float,2 >,itk::Image< itk::Vector< float,2 >,2 >,float'),
  ('SegmentationLevelSetImageFilter', 'itk::SegmentationLevelSetImageFilter', 'itkSegmentationLevelSetImageFilterID2ID2D', True, 'itk::Image< double,2 >,itk::Image< double,2 >,double'),
  ('SegmentationLevelSetImageFilter', 'itk::SegmentationLevelSetImageFilter', 'itkSegmentationLevelSetImageFilterID2IVF22D', True, 'itk::Image< double,2 >,itk::Image< itk::Vector< float,2 >,2 >,double'),
  ('SegmentationLevelSetImageFilter', 'itk::SegmentationLevelSetImageFilter', 'itkSegmentationLevelSetImageFilterIF3IF3F', True, 'itk::Image< float,3 >,itk::Image< float,3 >,float'),
  ('SegmentationLevelSetImageFilter', 'itk::SegmentationLevelSetImageFilter', 'itkSegmentationLevelSetImageFilterIF3IVF33F', True, 'itk::Image< float,3 >,itk::Image< itk::Vector< float,3 >,3 >,float'),
  ('SegmentationLevelSetImageFilter', 'itk::SegmentationLevelSetImageFilter', 'itkSegmentationLevelSetImageFilterID3ID3D', True, 'itk::Image< double,3 >,itk::Image< double,3 >,double'),
  ('SegmentationLevelSetImageFilter', 'itk::SegmentationLevelSetImageFilter', 'itkSegmentationLevelSetImageFilterID3IVF33D', True, 'itk::Image< double,3 >,itk::Image< itk::Vector< float,3 >,3 >,double'),
  ('ShapePriorSegmentationLevelSetImageFilter', 'itk::ShapePriorSegmentationLevelSetImageFilter', 'itkShapePriorSegmentationLevelSetImageFilterIF2IF2F', True, 'itk::Image< float,2 >,itk::Image< float,2 >,float'),
  ('ShapePriorSegmentationLevelSetImageFilter', 'itk::ShapePriorSegmentationLevelSetImageFilter', 'itkShapePriorSegmentationLevelSetImageFilterID2ID2D', True, 'itk::Image< double,2 >,itk::Image< double,2 >,double'),
  ('ShapePriorSegmentationLevelSetImageFilter', 'itk::ShapePriorSegmentationLevelSetImageFilter', 'itkShapePriorSegmentationLevelSetImageFilterIF3IF3F', True, 'itk::Image< float,3 >,itk::Image< float,3 >,float'),
  ('ShapePriorSegmentationLevelSetImageFilter', 'itk::ShapePriorSegmentationLevelSetImageFilter', 'itkShapePriorSegmentationLevelSetImageFilterID3ID3D', True, 'itk::Image< double,3 >,itk::Image< double,3 >,double'),
  ('AnisotropicFourthOrderLevelSetImageFilter', 'itk::AnisotropicFourthOrderLevelSetImageFilter', 'itkAnisotropicFourthOrderLevelSetImageFilterIF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >'),
  ('AnisotropicFourthOrderLevelSetImageFilter', 'itk::AnisotropicFourthOrderLevelSetImageFilter', 'itkAnisotropicFourthOrderLevelSetImageFilterIF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >'),
  ('AnisotropicFourthOrderLevelSetImageFilter', 'itk::AnisotropicFourthOrderLevelSetImageFilter', 'itkAnisotropicFourthOrderLevelSetImageFilterID2ID2', True, 'itk::Image< double,2 >, itk::Image< double,2 >'),
  ('AnisotropicFourthOrderLevelSetImageFilter', 'itk::AnisotropicFourthOrderLevelSetImageFilter', 'itkAnisotropicFourthOrderLevelSetImageFilterID3ID3', True, 'itk::Image< double,3 >, itk::Image< double,3 >'),
  ('BinaryMaskToNarrowBandPointSetFilter', 'itk::BinaryMaskToNarrowBandPointSetFilter', 'itkBinaryMaskToNarrowBandPointSetFilterISS2PSSS2', True, 'itk::Image< signed short,2 >, itk::PointSet< signed short,2 >'),
  ('BinaryMaskToNarrowBandPointSetFilter', 'itk::BinaryMaskToNarrowBandPointSetFilter', 'itkBinaryMaskToNarrowBandPointSetFilterISS2MSS2', True, 'itk::Image< signed short,2 >, itk::Mesh< signed short,2 >'),
  ('BinaryMaskToNarrowBandPointSetFilter', 'itk::BinaryMaskToNarrowBandPointSetFilter', 'itkBinaryMaskToNarrowBandPointSetFilterISS2PSUC2', True, 'itk::Image< signed short,2 >, itk::PointSet< unsigned char,2 >'),
  ('BinaryMaskToNarrowBandPointSetFilter', 'itk::BinaryMaskToNarrowBandPointSetFilter', 'itkBinaryMaskToNarrowBandPointSetFilterISS2MUC2', True, 'itk::Image< signed short,2 >, itk::Mesh< unsigned char,2 >'),
  ('BinaryMaskToNarrowBandPointSetFilter', 'itk::BinaryMaskToNarrowBandPointSetFilter', 'itkBinaryMaskToNarrowBandPointSetFilterISS2PSUS2', True, 'itk::Image< signed short,2 >, itk::PointSet< unsigned short,2 >'),
  ('BinaryMaskToNarrowBandPointSetFilter', 'itk::BinaryMaskToNarrowBandPointSetFilter', 'itkBinaryMaskToNarrowBandPointSetFilterISS2MUS2', True, 'itk::Image< signed short,2 >, itk::Mesh< unsigned short,2 >'),
  ('BinaryMaskToNarrowBandPointSetFilter', 'itk::BinaryMaskToNarrowBandPointSetFilter', 'itkBinaryMaskToNarrowBandPointSetFilterISS2PSF2', True, 'itk::Image< signed short,2 >, itk::PointSet< float,2 >'),
  ('BinaryMaskToNarrowBandPointSetFilter', 'itk::BinaryMaskToNarrowBandPointSetFilter', 'itkBinaryMaskToNarrowBandPointSetFilterISS2MF2', True, 'itk::Image< signed short,2 >, itk::Mesh< float,2 >'),
  ('BinaryMaskToNarrowBandPointSetFilter', 'itk::BinaryMaskToNarrowBandPointSetFilter', 'itkBinaryMaskToNarrowBandPointSetFilterISS2PSD2', True, 'itk::Image< signed short,2 >, itk::PointSet< double,2 >'),
  ('BinaryMaskToNarrowBandPointSetFilter', 'itk::BinaryMaskToNarrowBandPointSetFilter', 'itkBinaryMaskToNarrowBandPointSetFilterISS2MD2', True, 'itk::Image< signed short,2 >, itk::Mesh< double,2 >'),
  ('BinaryMaskToNarrowBandPointSetFilter', 'itk::BinaryMaskToNarrowBandPointSetFilter', 'itkBinaryMaskToNarrowBandPointSetFilterIUC2PSSS2', True, 'itk::Image< unsigned char,2 >, itk::PointSet< signed short,2 >'),
  ('BinaryMaskToNarrowBandPointSetFilter', 'itk::BinaryMaskToNarrowBandPointSetFilter', 'itkBinaryMaskToNarrowBandPointSetFilterIUC2MSS2', True, 'itk::Image< unsigned char,2 >, itk::Mesh< signed short,2 >'),
  ('BinaryMaskToNarrowBandPointSetFilter', 'itk::BinaryMaskToNarrowBandPointSetFilter', 'itkBinaryMaskToNarrowBandPointSetFilterIUC2PSUC2', True, 'itk::Image< unsigned char,2 >, itk::PointSet< unsigned char,2 >'),
  ('BinaryMaskToNarrowBandPointSetFilter', 'itk::BinaryMaskToNarrowBandPointSetFilter', 'itkBinaryMaskToNarrowBandPointSetFilterIUC2MUC2', True, 'itk::Image< unsigned char,2 >, itk::Mesh< unsigned char,2 >'),
  ('BinaryMaskToNarrowBandPointSetFilter', 'itk::BinaryMaskToNarrowBandPointSetFilter', 'itkBinaryMaskToNarrowBandPointSetFilterIUC2PSUS2', True, 'itk::Image< unsigned char,2 >, itk::PointSet< unsigned short,2 >'),
  ('BinaryMaskToNarrowBandPointSetFilter', 'itk::BinaryMaskToNarrowBandPointSetFilter', 'itkBinaryMaskToNarrowBandPointSetFilterIUC2MUS2', True, 'itk::Image< unsigned char,2 >, itk::Mesh< unsigned short,2 >'),
  ('BinaryMaskToNarrowBandPointSetFilter', 'itk::BinaryMaskToNarrowBandPointSetFilter', 'itkBinaryMaskToNarrowBandPointSetFilterIUC2PSF2', True, 'itk::Image< unsigned char,2 >, itk::PointSet< float,2 >'),
  ('BinaryMaskToNarrowBandPointSetFilter', 'itk::BinaryMaskToNarrowBandPointSetFilter', 'itkBinaryMaskToNarrowBandPointSetFilterIUC2MF2', True, 'itk::Image< unsigned char,2 >, itk::Mesh< float,2 >'),
  ('BinaryMaskToNarrowBandPointSetFilter', 'itk::BinaryMaskToNarrowBandPointSetFilter', 'itkBinaryMaskToNarrowBandPointSetFilterIUC2PSD2', True, 'itk::Image< unsigned char,2 >, itk::PointSet< double,2 >'),
  ('BinaryMaskToNarrowBandPointSetFilter', 'itk::BinaryMaskToNarrowBandPointSetFilter', 'itkBinaryMaskToNarrowBandPointSetFilterIUC2MD2', True, 'itk::Image< unsigned char,2 >, itk::Mesh< double,2 >'),
  ('BinaryMaskToNarrowBandPointSetFilter', 'itk::BinaryMaskToNarrowBandPointSetFilter', 'itkBinaryMaskToNarrowBandPointSetFilterIUS2PSSS2', True, 'itk::Image< unsigned short,2 >, itk::PointSet< signed short,2 >'),
  ('BinaryMaskToNarrowBandPointSetFilter', 'itk::BinaryMaskToNarrowBandPointSetFilter', 'itkBinaryMaskToNarrowBandPointSetFilterIUS2MSS2', True, 'itk::Image< unsigned short,2 >, itk::Mesh< signed short,2 >'),
  ('BinaryMaskToNarrowBandPointSetFilter', 'itk::BinaryMaskToNarrowBandPointSetFilter', 'itkBinaryMaskToNarrowBandPointSetFilterIUS2PSUC2', True, 'itk::Image< unsigned short,2 >, itk::PointSet< unsigned char,2 >'),
  ('BinaryMaskToNarrowBandPointSetFilter', 'itk::BinaryMaskToNarrowBandPointSetFilter', 'itkBinaryMaskToNarrowBandPointSetFilterIUS2MUC2', True, 'itk::Image< unsigned short,2 >, itk::Mesh< unsigned char,2 >'),
  ('BinaryMaskToNarrowBandPointSetFilter', 'itk::BinaryMaskToNarrowBandPointSetFilter', 'itkBinaryMaskToNarrowBandPointSetFilterIUS2PSUS2', True, 'itk::Image< unsigned short,2 >, itk::PointSet< unsigned short,2 >'),
  ('BinaryMaskToNarrowBandPointSetFilter', 'itk::BinaryMaskToNarrowBandPointSetFilter', 'itkBinaryMaskToNarrowBandPointSetFilterIUS2MUS2', True, 'itk::Image< unsigned short,2 >, itk::Mesh< unsigned short,2 >'),
  ('BinaryMaskToNarrowBandPointSetFilter', 'itk::BinaryMaskToNarrowBandPointSetFilter', 'itkBinaryMaskToNarrowBandPointSetFilterIUS2PSF2', True, 'itk::Image< unsigned short,2 >, itk::PointSet< float,2 >'),
  ('BinaryMaskToNarrowBandPointSetFilter', 'itk::BinaryMaskToNarrowBandPointSetFilter', 'itkBinaryMaskToNarrowBandPointSetFilterIUS2MF2', True, 'itk::Image< unsigned short,2 >, itk::Mesh< float,2 >'),
  ('BinaryMaskToNarrowBandPointSetFilter', 'itk::BinaryMaskToNarrowBandPointSetFilter', 'itkBinaryMaskToNarrowBandPointSetFilterIUS2PSD2', True, 'itk::Image< unsigned short,2 >, itk::PointSet< double,2 >'),
  ('BinaryMaskToNarrowBandPointSetFilter', 'itk::BinaryMaskToNarrowBandPointSetFilter', 'itkBinaryMaskToNarrowBandPointSetFilterIUS2MD2', True, 'itk::Image< unsigned short,2 >, itk::Mesh< double,2 >'),
  ('BinaryMaskToNarrowBandPointSetFilter', 'itk::BinaryMaskToNarrowBandPointSetFilter', 'itkBinaryMaskToNarrowBandPointSetFilterISS3PSSS3', True, 'itk::Image< signed short,3 >, itk::PointSet< signed short,3 >'),
  ('BinaryMaskToNarrowBandPointSetFilter', 'itk::BinaryMaskToNarrowBandPointSetFilter', 'itkBinaryMaskToNarrowBandPointSetFilterISS3MSS3', True, 'itk::Image< signed short,3 >, itk::Mesh< signed short,3 >'),
  ('BinaryMaskToNarrowBandPointSetFilter', 'itk::BinaryMaskToNarrowBandPointSetFilter', 'itkBinaryMaskToNarrowBandPointSetFilterISS3PSUC3', True, 'itk::Image< signed short,3 >, itk::PointSet< unsigned char,3 >'),
  ('BinaryMaskToNarrowBandPointSetFilter', 'itk::BinaryMaskToNarrowBandPointSetFilter', 'itkBinaryMaskToNarrowBandPointSetFilterISS3MUC3', True, 'itk::Image< signed short,3 >, itk::Mesh< unsigned char,3 >'),
  ('BinaryMaskToNarrowBandPointSetFilter', 'itk::BinaryMaskToNarrowBandPointSetFilter', 'itkBinaryMaskToNarrowBandPointSetFilterISS3PSUS3', True, 'itk::Image< signed short,3 >, itk::PointSet< unsigned short,3 >'),
  ('BinaryMaskToNarrowBandPointSetFilter', 'itk::BinaryMaskToNarrowBandPointSetFilter', 'itkBinaryMaskToNarrowBandPointSetFilterISS3MUS3', True, 'itk::Image< signed short,3 >, itk::Mesh< unsigned short,3 >'),
  ('BinaryMaskToNarrowBandPointSetFilter', 'itk::BinaryMaskToNarrowBandPointSetFilter', 'itkBinaryMaskToNarrowBandPointSetFilterISS3PSF3', True, 'itk::Image< signed short,3 >, itk::PointSet< float,3 >'),
  ('BinaryMaskToNarrowBandPointSetFilter', 'itk::BinaryMaskToNarrowBandPointSetFilter', 'itkBinaryMaskToNarrowBandPointSetFilterISS3MF3', True, 'itk::Image< signed short,3 >, itk::Mesh< float,3 >'),
  ('BinaryMaskToNarrowBandPointSetFilter', 'itk::BinaryMaskToNarrowBandPointSetFilter', 'itkBinaryMaskToNarrowBandPointSetFilterISS3PSD3', True, 'itk::Image< signed short,3 >, itk::PointSet< double,3 >'),
  ('BinaryMaskToNarrowBandPointSetFilter', 'itk::BinaryMaskToNarrowBandPointSetFilter', 'itkBinaryMaskToNarrowBandPointSetFilterISS3MD3', True, 'itk::Image< signed short,3 >, itk::Mesh< double,3 >'),
  ('BinaryMaskToNarrowBandPointSetFilter', 'itk::BinaryMaskToNarrowBandPointSetFilter', 'itkBinaryMaskToNarrowBandPointSetFilterIUC3PSSS3', True, 'itk::Image< unsigned char,3 >, itk::PointSet< signed short,3 >'),
  ('BinaryMaskToNarrowBandPointSetFilter', 'itk::BinaryMaskToNarrowBandPointSetFilter', 'itkBinaryMaskToNarrowBandPointSetFilterIUC3MSS3', True, 'itk::Image< unsigned char,3 >, itk::Mesh< signed short,3 >'),
  ('BinaryMaskToNarrowBandPointSetFilter', 'itk::BinaryMaskToNarrowBandPointSetFilter', 'itkBinaryMaskToNarrowBandPointSetFilterIUC3PSUC3', True, 'itk::Image< unsigned char,3 >, itk::PointSet< unsigned char,3 >'),
  ('BinaryMaskToNarrowBandPointSetFilter', 'itk::BinaryMaskToNarrowBandPointSetFilter', 'itkBinaryMaskToNarrowBandPointSetFilterIUC3MUC3', True, 'itk::Image< unsigned char,3 >, itk::Mesh< unsigned char,3 >'),
  ('BinaryMaskToNarrowBandPointSetFilter', 'itk::BinaryMaskToNarrowBandPointSetFilter', 'itkBinaryMaskToNarrowBandPointSetFilterIUC3PSUS3', True, 'itk::Image< unsigned char,3 >, itk::PointSet< unsigned short,3 >'),
  ('BinaryMaskToNarrowBandPointSetFilter', 'itk::BinaryMaskToNarrowBandPointSetFilter', 'itkBinaryMaskToNarrowBandPointSetFilterIUC3MUS3', True, 'itk::Image< unsigned char,3 >, itk::Mesh< unsigned short,3 >'),
  ('BinaryMaskToNarrowBandPointSetFilter', 'itk::BinaryMaskToNarrowBandPointSetFilter', 'itkBinaryMaskToNarrowBandPointSetFilterIUC3PSF3', True, 'itk::Image< unsigned char,3 >, itk::PointSet< float,3 >'),
  ('BinaryMaskToNarrowBandPointSetFilter', 'itk::BinaryMaskToNarrowBandPointSetFilter', 'itkBinaryMaskToNarrowBandPointSetFilterIUC3MF3', True, 'itk::Image< unsigned char,3 >, itk::Mesh< float,3 >'),
  ('BinaryMaskToNarrowBandPointSetFilter', 'itk::BinaryMaskToNarrowBandPointSetFilter', 'itkBinaryMaskToNarrowBandPointSetFilterIUC3PSD3', True, 'itk::Image< unsigned char,3 >, itk::PointSet< double,3 >'),
  ('BinaryMaskToNarrowBandPointSetFilter', 'itk::BinaryMaskToNarrowBandPointSetFilter', 'itkBinaryMaskToNarrowBandPointSetFilterIUC3MD3', True, 'itk::Image< unsigned char,3 >, itk::Mesh< double,3 >'),
  ('BinaryMaskToNarrowBandPointSetFilter', 'itk::BinaryMaskToNarrowBandPointSetFilter', 'itkBinaryMaskToNarrowBandPointSetFilterIUS3PSSS3', True, 'itk::Image< unsigned short,3 >, itk::PointSet< signed short,3 >'),
  ('BinaryMaskToNarrowBandPointSetFilter', 'itk::BinaryMaskToNarrowBandPointSetFilter', 'itkBinaryMaskToNarrowBandPointSetFilterIUS3MSS3', True, 'itk::Image< unsigned short,3 >, itk::Mesh< signed short,3 >'),
  ('BinaryMaskToNarrowBandPointSetFilter', 'itk::BinaryMaskToNarrowBandPointSetFilter', 'itkBinaryMaskToNarrowBandPointSetFilterIUS3PSUC3', True, 'itk::Image< unsigned short,3 >, itk::PointSet< unsigned char,3 >'),
  ('BinaryMaskToNarrowBandPointSetFilter', 'itk::BinaryMaskToNarrowBandPointSetFilter', 'itkBinaryMaskToNarrowBandPointSetFilterIUS3MUC3', True, 'itk::Image< unsigned short,3 >, itk::Mesh< unsigned char,3 >'),
  ('BinaryMaskToNarrowBandPointSetFilter', 'itk::BinaryMaskToNarrowBandPointSetFilter', 'itkBinaryMaskToNarrowBandPointSetFilterIUS3PSUS3', True, 'itk::Image< unsigned short,3 >, itk::PointSet< unsigned short,3 >'),
  ('BinaryMaskToNarrowBandPointSetFilter', 'itk::BinaryMaskToNarrowBandPointSetFilter', 'itkBinaryMaskToNarrowBandPointSetFilterIUS3MUS3', True, 'itk::Image< unsigned short,3 >, itk::Mesh< unsigned short,3 >'),
  ('BinaryMaskToNarrowBandPointSetFilter', 'itk::BinaryMaskToNarrowBandPointSetFilter', 'itkBinaryMaskToNarrowBandPointSetFilterIUS3PSF3', True, 'itk::Image< unsigned short,3 >, itk::PointSet< float,3 >'),
  ('BinaryMaskToNarrowBandPointSetFilter', 'itk::BinaryMaskToNarrowBandPointSetFilter', 'itkBinaryMaskToNarrowBandPointSetFilterIUS3MF3', True, 'itk::Image< unsigned short,3 >, itk::Mesh< float,3 >'),
  ('BinaryMaskToNarrowBandPointSetFilter', 'itk::BinaryMaskToNarrowBandPointSetFilter', 'itkBinaryMaskToNarrowBandPointSetFilterIUS3PSD3', True, 'itk::Image< unsigned short,3 >, itk::PointSet< double,3 >'),
  ('BinaryMaskToNarrowBandPointSetFilter', 'itk::BinaryMaskToNarrowBandPointSetFilter', 'itkBinaryMaskToNarrowBandPointSetFilterIUS3MD3', True, 'itk::Image< unsigned short,3 >, itk::Mesh< double,3 >'),
  ('CannySegmentationLevelSetImageFilter', 'itk::CannySegmentationLevelSetImageFilter', 'itkCannySegmentationLevelSetImageFilterIF2IF2F', True, 'itk::Image< float,2 >,itk::Image< float,2 >,float'),
  ('CannySegmentationLevelSetImageFilter', 'itk::CannySegmentationLevelSetImageFilter', 'itkCannySegmentationLevelSetImageFilterID2ID2D', True, 'itk::Image< double,2 >,itk::Image< double,2 >,double'),
  ('CannySegmentationLevelSetImageFilter', 'itk::CannySegmentationLevelSetImageFilter', 'itkCannySegmentationLevelSetImageFilterIF3IF3F', True, 'itk::Image< float,3 >,itk::Image< float,3 >,float'),
  ('CannySegmentationLevelSetImageFilter', 'itk::CannySegmentationLevelSetImageFilter', 'itkCannySegmentationLevelSetImageFilterID3ID3D', True, 'itk::Image< double,3 >,itk::Image< double,3 >,double'),
  ('CollidingFrontsImageFilter', 'itk::CollidingFrontsImageFilter', 'itkCollidingFrontsImageFilterIF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >'),
  ('CollidingFrontsImageFilter', 'itk::CollidingFrontsImageFilter', 'itkCollidingFrontsImageFilterIF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >'),
  ('CollidingFrontsImageFilter', 'itk::CollidingFrontsImageFilter', 'itkCollidingFrontsImageFilterID2ID2', True, 'itk::Image< double,2 >, itk::Image< double,2 >'),
  ('CollidingFrontsImageFilter', 'itk::CollidingFrontsImageFilter', 'itkCollidingFrontsImageFilterID3ID3', True, 'itk::Image< double,3 >, itk::Image< double,3 >'),
  ('CurvesLevelSetImageFilter', 'itk::CurvesLevelSetImageFilter', 'itkCurvesLevelSetImageFilterIF2IF2F', True, 'itk::Image< float,2 >,itk::Image< float,2 >,float'),
  ('CurvesLevelSetImageFilter', 'itk::CurvesLevelSetImageFilter', 'itkCurvesLevelSetImageFilterID2ID2D', True, 'itk::Image< double,2 >,itk::Image< double,2 >,double'),
  ('CurvesLevelSetImageFilter', 'itk::CurvesLevelSetImageFilter', 'itkCurvesLevelSetImageFilterIF3IF3F', True, 'itk::Image< float,3 >,itk::Image< float,3 >,float'),
  ('CurvesLevelSetImageFilter', 'itk::CurvesLevelSetImageFilter', 'itkCurvesLevelSetImageFilterID3ID3D', True, 'itk::Image< double,3 >,itk::Image< double,3 >,double'),
  ('GeodesicActiveContourLevelSetImageFilter', 'itk::GeodesicActiveContourLevelSetImageFilter', 'itkGeodesicActiveContourLevelSetImageFilterIF2IF2F', True, 'itk::Image< float,2 >,itk::Image< float,2 >,float'),
  ('GeodesicActiveContourLevelSetImageFilter', 'itk::GeodesicActiveContourLevelSetImageFilter', 'itkGeodesicActiveContourLevelSetImageFilterID2ID2D', True, 'itk::Image< double,2 >,itk::Image< double,2 >,double'),
  ('GeodesicActiveContourLevelSetImageFilter', 'itk::GeodesicActiveContourLevelSetImageFilter', 'itkGeodesicActiveContourLevelSetImageFilterIF3IF3F', True, 'itk::Image< float,3 >,itk::Image< float,3 >,float'),
  ('GeodesicActiveContourLevelSetImageFilter', 'itk::GeodesicActiveContourLevelSetImageFilter', 'itkGeodesicActiveContourLevelSetImageFilterID3ID3D', True, 'itk::Image< double,3 >,itk::Image< double,3 >,double'),
  ('GeodesicActiveContourShapePriorLevelSetImageFilter', 'itk::GeodesicActiveContourShapePriorLevelSetImageFilter', 'itkGeodesicActiveContourShapePriorLevelSetImageFilterIF2IF2F', True, 'itk::Image< float,2 >,itk::Image< float,2 >,float'),
  ('GeodesicActiveContourShapePriorLevelSetImageFilter', 'itk::GeodesicActiveContourShapePriorLevelSetImageFilter', 'itkGeodesicActiveContourShapePriorLevelSetImageFilterID2ID2D', True, 'itk::Image< double,2 >,itk::Image< double,2 >,double'),
  ('GeodesicActiveContourShapePriorLevelSetImageFilter', 'itk::GeodesicActiveContourShapePriorLevelSetImageFilter', 'itkGeodesicActiveContourShapePriorLevelSetImageFilterIF3IF3F', True, 'itk::Image< float,3 >,itk::Image< float,3 >,float'),
  ('GeodesicActiveContourShapePriorLevelSetImageFilter', 'itk::GeodesicActiveContourShapePriorLevelSetImageFilter', 'itkGeodesicActiveContourShapePriorLevelSetImageFilterID3ID3D', True, 'itk::Image< double,3 >,itk::Image< double,3 >,double'),
  ('IsotropicFourthOrderLevelSetImageFilter', 'itk::IsotropicFourthOrderLevelSetImageFilter', 'itkIsotropicFourthOrderLevelSetImageFilterIF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >'),
  ('IsotropicFourthOrderLevelSetImageFilter', 'itk::IsotropicFourthOrderLevelSetImageFilter', 'itkIsotropicFourthOrderLevelSetImageFilterIF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >'),
  ('IsotropicFourthOrderLevelSetImageFilter', 'itk::IsotropicFourthOrderLevelSetImageFilter', 'itkIsotropicFourthOrderLevelSetImageFilterID2ID2', True, 'itk::Image< double,2 >, itk::Image< double,2 >'),
  ('IsotropicFourthOrderLevelSetImageFilter', 'itk::IsotropicFourthOrderLevelSetImageFilter', 'itkIsotropicFourthOrderLevelSetImageFilterID3ID3', True, 'itk::Image< double,3 >, itk::Image< double,3 >'),
  ('LaplacianSegmentationLevelSetImageFilter', 'itk::LaplacianSegmentationLevelSetImageFilter', 'itkLaplacianSegmentationLevelSetImageFilterIF2IF2F', True, 'itk::Image< float,2 >,itk::Image< float,2 >,float'),
  ('LaplacianSegmentationLevelSetImageFilter', 'itk::LaplacianSegmentationLevelSetImageFilter', 'itkLaplacianSegmentationLevelSetImageFilterID2ID2D', True, 'itk::Image< double,2 >,itk::Image< double,2 >,double'),
  ('LaplacianSegmentationLevelSetImageFilter', 'itk::LaplacianSegmentationLevelSetImageFilter', 'itkLaplacianSegmentationLevelSetImageFilterIF3IF3F', True, 'itk::Image< float,3 >,itk::Image< float,3 >,float'),
  ('LaplacianSegmentationLevelSetImageFilter', 'itk::LaplacianSegmentationLevelSetImageFilter', 'itkLaplacianSegmentationLevelSetImageFilterID3ID3D', True, 'itk::Image< double,3 >,itk::Image< double,3 >,double'),
  ('NarrowBandCurvesLevelSetImageFilter', 'itk::NarrowBandCurvesLevelSetImageFilter', 'itkNarrowBandCurvesLevelSetImageFilterIF2IF2F', True, 'itk::Image< float,2 >,itk::Image< float,2 >,float'),
  ('NarrowBandCurvesLevelSetImageFilter', 'itk::NarrowBandCurvesLevelSetImageFilter', 'itkNarrowBandCurvesLevelSetImageFilterID2ID2D', True, 'itk::Image< double,2 >,itk::Image< double,2 >,double'),
  ('NarrowBandCurvesLevelSetImageFilter', 'itk::NarrowBandCurvesLevelSetImageFilter', 'itkNarrowBandCurvesLevelSetImageFilterIF3IF3F', True, 'itk::Image< float,3 >,itk::Image< float,3 >,float'),
  ('NarrowBandCurvesLevelSetImageFilter', 'itk::NarrowBandCurvesLevelSetImageFilter', 'itkNarrowBandCurvesLevelSetImageFilterID3ID3D', True, 'itk::Image< double,3 >,itk::Image< double,3 >,double'),
  ('NarrowBandLevelSetImageFilter', 'itk::NarrowBandLevelSetImageFilter', 'itkNarrowBandLevelSetImageFilterIF2IF2F', True, 'itk::Image< float,2 >,itk::Image< float,2 >,float'),
  ('NarrowBandLevelSetImageFilter', 'itk::NarrowBandLevelSetImageFilter', 'itkNarrowBandLevelSetImageFilterID2ID2D', True, 'itk::Image< double,2 >,itk::Image< double,2 >,double'),
  ('NarrowBandLevelSetImageFilter', 'itk::NarrowBandLevelSetImageFilter', 'itkNarrowBandLevelSetImageFilterIF3IF3F', True, 'itk::Image< float,3 >,itk::Image< float,3 >,float'),
  ('NarrowBandLevelSetImageFilter', 'itk::NarrowBandLevelSetImageFilter', 'itkNarrowBandLevelSetImageFilterID3ID3D', True, 'itk::Image< double,3 >,itk::Image< double,3 >,double'),
  ('NarrowBandThresholdSegmentationLevelSetImageFilter', 'itk::NarrowBandThresholdSegmentationLevelSetImageFilter', 'itkNarrowBandThresholdSegmentationLevelSetImageFilterIF2IF2F', True, 'itk::Image< float,2 >,itk::Image< float,2 >,float'),
  ('NarrowBandThresholdSegmentationLevelSetImageFilter', 'itk::NarrowBandThresholdSegmentationLevelSetImageFilter', 'itkNarrowBandThresholdSegmentationLevelSetImageFilterID2ID2D', True, 'itk::Image< double,2 >,itk::Image< double,2 >,double'),
  ('NarrowBandThresholdSegmentationLevelSetImageFilter', 'itk::NarrowBandThresholdSegmentationLevelSetImageFilter', 'itkNarrowBandThresholdSegmentationLevelSetImageFilterIF3IF3F', True, 'itk::Image< float,3 >,itk::Image< float,3 >,float'),
  ('NarrowBandThresholdSegmentationLevelSetImageFilter', 'itk::NarrowBandThresholdSegmentationLevelSetImageFilter', 'itkNarrowBandThresholdSegmentationLevelSetImageFilterID3ID3D', True, 'itk::Image< double,3 >,itk::Image< double,3 >,double'),
  ('ParallelSparseFieldLevelSetImageFilter', 'itk::ParallelSparseFieldLevelSetImageFilter', 'itkParallelSparseFieldLevelSetImageFilterIF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >'),
  ('ParallelSparseFieldLevelSetImageFilter', 'itk::ParallelSparseFieldLevelSetImageFilter', 'itkParallelSparseFieldLevelSetImageFilterIF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >'),
  ('ParallelSparseFieldLevelSetImageFilter', 'itk::ParallelSparseFieldLevelSetImageFilter', 'itkParallelSparseFieldLevelSetImageFilterID2ID2', True, 'itk::Image< double,2 >, itk::Image< double,2 >'),
  ('ParallelSparseFieldLevelSetImageFilter', 'itk::ParallelSparseFieldLevelSetImageFilter', 'itkParallelSparseFieldLevelSetImageFilterID3ID3', True, 'itk::Image< double,3 >, itk::Image< double,3 >'),
  ('ParallelSparseFieldLevelSetNode', 'itk::ParallelSparseFieldLevelSetNode', 'itkParallelSparseFieldLevelSetNodeI2', False, 'itk::Index< 2 >'),
  ('ParallelSparseFieldLevelSetNode', 'itk::ParallelSparseFieldLevelSetNode', 'itkParallelSparseFieldLevelSetNodeI3', False, 'itk::Index< 3 >'),
  ('SparseFieldLayer', 'itk::SparseFieldLayer', 'itkSparseFieldLayerPSFLSNI2', False, 'itk::ParallelSparseFieldLevelSetNode< itk::Index< 2 > >'),
  ('SparseFieldLayer', 'itk::SparseFieldLayer', 'itkSparseFieldLayerPSFLSNI3', False, 'itk::ParallelSparseFieldLevelSetNode< itk::Index< 3 > >'),
  ('ReinitializeLevelSetImageFilter', 'itk::ReinitializeLevelSetImageFilter', 'itkReinitializeLevelSetImageFilterIF2', True, 'itk::Image< float,2 >'),
  ('ReinitializeLevelSetImageFilter', 'itk::ReinitializeLevelSetImageFilter', 'itkReinitializeLevelSetImageFilterIF3', True, 'itk::Image< float,3 >'),
  ('ReinitializeLevelSetImageFilter', 'itk::ReinitializeLevelSetImageFilter', 'itkReinitializeLevelSetImageFilterID2', True, 'itk::Image< double,2 >'),
  ('ReinitializeLevelSetImageFilter', 'itk::ReinitializeLevelSetImageFilter', 'itkReinitializeLevelSetImageFilterID3', True, 'itk::Image< double,3 >'),
  ('SegmentationLevelSetFunction', 'itk::SegmentationLevelSetFunction', 'itkSegmentationLevelSetFunctionIF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >'),
  ('SegmentationLevelSetFunction', 'itk::SegmentationLevelSetFunction', 'itkSegmentationLevelSetFunctionIF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >'),
  ('SegmentationLevelSetFunction', 'itk::SegmentationLevelSetFunction', 'itkSegmentationLevelSetFunctionID2ID2', True, 'itk::Image< double,2 >, itk::Image< double,2 >'),
  ('SegmentationLevelSetFunction', 'itk::SegmentationLevelSetFunction', 'itkSegmentationLevelSetFunctionID3ID3', True, 'itk::Image< double,3 >, itk::Image< double,3 >'),
  ('ShapeDetectionLevelSetImageFilter', 'itk::ShapeDetectionLevelSetImageFilter', 'itkShapeDetectionLevelSetImageFilterIF2IF2F', True, 'itk::Image< float,2 >,itk::Image< float,2 >,float'),
  ('ShapeDetectionLevelSetImageFilter', 'itk::ShapeDetectionLevelSetImageFilter', 'itkShapeDetectionLevelSetImageFilterID2ID2D', True, 'itk::Image< double,2 >,itk::Image< double,2 >,double'),
  ('ShapeDetectionLevelSetImageFilter', 'itk::ShapeDetectionLevelSetImageFilter', 'itkShapeDetectionLevelSetImageFilterIF3IF3F', True, 'itk::Image< float,3 >,itk::Image< float,3 >,float'),
  ('ShapeDetectionLevelSetImageFilter', 'itk::ShapeDetectionLevelSetImageFilter', 'itkShapeDetectionLevelSetImageFilterID3ID3D', True, 'itk::Image< double,3 >,itk::Image< double,3 >,double'),
  ('ShapePriorMAPCostFunction', 'itk::ShapePriorMAPCostFunction', 'itkShapePriorMAPCostFunctionIF2F', True, 'itk::Image< float,2 >,float'),
  ('ShapePriorMAPCostFunction', 'itk::ShapePriorMAPCostFunction', 'itkShapePriorMAPCostFunctionID2D', True, 'itk::Image< double,2 >,double'),
  ('ShapePriorMAPCostFunction', 'itk::ShapePriorMAPCostFunction', 'itkShapePriorMAPCostFunctionIF3F', True, 'itk::Image< float,3 >,float'),
  ('ShapePriorMAPCostFunction', 'itk::ShapePriorMAPCostFunction', 'itkShapePriorMAPCostFunctionID3D', True, 'itk::Image< double,3 >,double'),
  ('ShapePriorMAPCostFunctionBase', 'itk::ShapePriorMAPCostFunctionBase', 'itkShapePriorMAPCostFunctionBaseIF2F', True, 'itk::Image< float,2 >,float'),
  ('ShapePriorMAPCostFunctionBase', 'itk::ShapePriorMAPCostFunctionBase', 'itkShapePriorMAPCostFunctionBaseID2D', True, 'itk::Image< double,2 >,double'),
  ('ShapePriorMAPCostFunctionBase', 'itk::ShapePriorMAPCostFunctionBase', 'itkShapePriorMAPCostFunctionBaseIF3F', True, 'itk::Image< float,3 >,float'),
  ('ShapePriorMAPCostFunctionBase', 'itk::ShapePriorMAPCostFunctionBase', 'itkShapePriorMAPCostFunctionBaseID3D', True, 'itk::Image< double,3 >,double'),
  ('ThresholdSegmentationLevelSetImageFilter', 'itk::ThresholdSegmentationLevelSetImageFilter', 'itkThresholdSegmentationLevelSetImageFilterIF2IF2F', True, 'itk::Image< float,2 >,itk::Image< float,2 >,float'),
  ('ThresholdSegmentationLevelSetImageFilter', 'itk::ThresholdSegmentationLevelSetImageFilter', 'itkThresholdSegmentationLevelSetImageFilterID2ID2D', True, 'itk::Image< double,2 >,itk::Image< double,2 >,double'),
  ('ThresholdSegmentationLevelSetImageFilter', 'itk::ThresholdSegmentationLevelSetImageFilter', 'itkThresholdSegmentationLevelSetImageFilterIF3IF3F', True, 'itk::Image< float,3 >,itk::Image< float,3 >,float'),
  ('ThresholdSegmentationLevelSetImageFilter', 'itk::ThresholdSegmentationLevelSetImageFilter', 'itkThresholdSegmentationLevelSetImageFilterID3ID3D', True, 'itk::Image< double,3 >,itk::Image< double,3 >,double'),
  ('UnsharpMaskLevelSetImageFilter', 'itk::UnsharpMaskLevelSetImageFilter', 'itkUnsharpMaskLevelSetImageFilterIF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >'),
  ('UnsharpMaskLevelSetImageFilter', 'itk::UnsharpMaskLevelSetImageFilter', 'itkUnsharpMaskLevelSetImageFilterIF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >'),
  ('UnsharpMaskLevelSetImageFilter', 'itk::UnsharpMaskLevelSetImageFilter', 'itkUnsharpMaskLevelSetImageFilterID2ID2', True, 'itk::Image< double,2 >, itk::Image< double,2 >'),
  ('UnsharpMaskLevelSetImageFilter', 'itk::UnsharpMaskLevelSetImageFilter', 'itkUnsharpMaskLevelSetImageFilterID3ID3', True, 'itk::Image< double,3 >, itk::Image< double,3 >'),
  ('VectorThresholdSegmentationLevelSetImageFilter', 'itk::VectorThresholdSegmentationLevelSetImageFilter', 'itkVectorThresholdSegmentationLevelSetImageFilterIF2IVF22F', True, 'itk::Image< float,2 >,itk::Image< itk::Vector< float,2 >,2 >,float'),
  ('VectorThresholdSegmentationLevelSetImageFilter', 'itk::VectorThresholdSegmentationLevelSetImageFilter', 'itkVectorThresholdSegmentationLevelSetImageFilterID2IVF22D', True, 'itk::Image< double,2 >,itk::Image< itk::Vector< float,2 >,2 >,double'),
  ('VectorThresholdSegmentationLevelSetImageFilter', 'itk::VectorThresholdSegmentationLevelSetImageFilter', 'itkVectorThresholdSegmentationLevelSetImageFilterIF3IVF33F', True, 'itk::Image< float,3 >,itk::Image< itk::Vector< float,3 >,3 >,float'),
  ('VectorThresholdSegmentationLevelSetImageFilter', 'itk::VectorThresholdSegmentationLevelSetImageFilter', 'itkVectorThresholdSegmentationLevelSetImageFilterID3IVF33D', True, 'itk::Image< double,3 >,itk::Image< itk::Vector< float,3 >,3 >,double'),
)
snake_case_functions = ('unsharp_mask_level_set_image_filter', 'sparse_field_level_set_image_filter', 'shape_prior_segmentation_level_set_image_filter', 'binary_mask_to_narrow_band_point_set_filter', 'parallel_sparse_field_level_set_image_filter', 'laplacian_segmentation_level_set_image_filter', 'curves_level_set_image_filter', 'geodesic_active_contour_shape_prior_level_set_image_filter', 'isotropic_fourth_order_level_set_image_filter', 'narrow_band_threshold_segmentation_level_set_image_filter', 'vector_threshold_segmentation_level_set_image_filter', 'sparse_field_fourth_order_level_set_image_filter', 'anisotropic_fourth_order_level_set_image_filter', 'reinitialize_level_set_image_filter', 'colliding_fronts_image_filter', 'geodesic_active_contour_level_set_image_filter', 'segmentation_level_set_image_filter', 'threshold_segmentation_level_set_image_filter', 'shape_detection_level_set_image_filter', 'narrow_band_level_set_image_filter', 'canny_segmentation_level_set_image_filter', 'narrow_band_curves_level_set_image_filter', )
