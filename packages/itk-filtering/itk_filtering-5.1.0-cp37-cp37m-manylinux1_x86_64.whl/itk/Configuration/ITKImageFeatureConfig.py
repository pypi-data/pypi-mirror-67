depends = ('ITKPyBase', 'ITKSpatialObjects', 'ITKSmoothing', 'ITKMesh', 'ITKImageStatistics', 'ITKImageSources', 'ITKImageGradient', )
templates = (
  ('HessianRecursiveGaussianImageFilter', 'itk::HessianRecursiveGaussianImageFilter', 'itkHessianRecursiveGaussianImageFilterISS2', True, 'itk::Image< signed short,2 >'),
  ('HessianRecursiveGaussianImageFilter', 'itk::HessianRecursiveGaussianImageFilter', 'itkHessianRecursiveGaussianImageFilterISS3', True, 'itk::Image< signed short,3 >'),
  ('HessianRecursiveGaussianImageFilter', 'itk::HessianRecursiveGaussianImageFilter', 'itkHessianRecursiveGaussianImageFilterIUC2', True, 'itk::Image< unsigned char,2 >'),
  ('HessianRecursiveGaussianImageFilter', 'itk::HessianRecursiveGaussianImageFilter', 'itkHessianRecursiveGaussianImageFilterIUC3', True, 'itk::Image< unsigned char,3 >'),
  ('HessianRecursiveGaussianImageFilter', 'itk::HessianRecursiveGaussianImageFilter', 'itkHessianRecursiveGaussianImageFilterIUS2', True, 'itk::Image< unsigned short,2 >'),
  ('HessianRecursiveGaussianImageFilter', 'itk::HessianRecursiveGaussianImageFilter', 'itkHessianRecursiveGaussianImageFilterIUS3', True, 'itk::Image< unsigned short,3 >'),
  ('HessianRecursiveGaussianImageFilter', 'itk::HessianRecursiveGaussianImageFilter', 'itkHessianRecursiveGaussianImageFilterIF2', True, 'itk::Image< float,2 >'),
  ('HessianRecursiveGaussianImageFilter', 'itk::HessianRecursiveGaussianImageFilter', 'itkHessianRecursiveGaussianImageFilterIF3', True, 'itk::Image< float,3 >'),
  ('HessianRecursiveGaussianImageFilter', 'itk::HessianRecursiveGaussianImageFilter', 'itkHessianRecursiveGaussianImageFilterID2', True, 'itk::Image< double,2 >'),
  ('HessianRecursiveGaussianImageFilter', 'itk::HessianRecursiveGaussianImageFilter', 'itkHessianRecursiveGaussianImageFilterID3', True, 'itk::Image< double,3 >'),
  ('BilateralImageFilter', 'itk::BilateralImageFilter', 'itkBilateralImageFilterISS2ISS2', True, 'itk::Image< signed short,2 >, itk::Image< signed short,2 >'),
  ('BilateralImageFilter', 'itk::BilateralImageFilter', 'itkBilateralImageFilterISS3ISS3', True, 'itk::Image< signed short,3 >, itk::Image< signed short,3 >'),
  ('BilateralImageFilter', 'itk::BilateralImageFilter', 'itkBilateralImageFilterIUC2IUC2', True, 'itk::Image< unsigned char,2 >, itk::Image< unsigned char,2 >'),
  ('BilateralImageFilter', 'itk::BilateralImageFilter', 'itkBilateralImageFilterIUC3IUC3', True, 'itk::Image< unsigned char,3 >, itk::Image< unsigned char,3 >'),
  ('BilateralImageFilter', 'itk::BilateralImageFilter', 'itkBilateralImageFilterIUS2IUS2', True, 'itk::Image< unsigned short,2 >, itk::Image< unsigned short,2 >'),
  ('BilateralImageFilter', 'itk::BilateralImageFilter', 'itkBilateralImageFilterIUS3IUS3', True, 'itk::Image< unsigned short,3 >, itk::Image< unsigned short,3 >'),
  ('BilateralImageFilter', 'itk::BilateralImageFilter', 'itkBilateralImageFilterIF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >'),
  ('BilateralImageFilter', 'itk::BilateralImageFilter', 'itkBilateralImageFilterIF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >'),
  ('BilateralImageFilter', 'itk::BilateralImageFilter', 'itkBilateralImageFilterID2ID2', True, 'itk::Image< double,2 >, itk::Image< double,2 >'),
  ('BilateralImageFilter', 'itk::BilateralImageFilter', 'itkBilateralImageFilterID3ID3', True, 'itk::Image< double,3 >, itk::Image< double,3 >'),
  ('CannyEdgeDetectionImageFilter', 'itk::CannyEdgeDetectionImageFilter', 'itkCannyEdgeDetectionImageFilterIF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >'),
  ('CannyEdgeDetectionImageFilter', 'itk::CannyEdgeDetectionImageFilter', 'itkCannyEdgeDetectionImageFilterIF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >'),
  ('CannyEdgeDetectionImageFilter', 'itk::CannyEdgeDetectionImageFilter', 'itkCannyEdgeDetectionImageFilterID2ID2', True, 'itk::Image< double,2 >, itk::Image< double,2 >'),
  ('CannyEdgeDetectionImageFilter', 'itk::CannyEdgeDetectionImageFilter', 'itkCannyEdgeDetectionImageFilterID3ID3', True, 'itk::Image< double,3 >, itk::Image< double,3 >'),
  ('DerivativeImageFilter', 'itk::DerivativeImageFilter', 'itkDerivativeImageFilterISS2ISS2', True, 'itk::Image< signed short,2 >, itk::Image< signed short,2 >'),
  ('DerivativeImageFilter', 'itk::DerivativeImageFilter', 'itkDerivativeImageFilterISS3ISS3', True, 'itk::Image< signed short,3 >, itk::Image< signed short,3 >'),
  ('DerivativeImageFilter', 'itk::DerivativeImageFilter', 'itkDerivativeImageFilterIF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >'),
  ('DerivativeImageFilter', 'itk::DerivativeImageFilter', 'itkDerivativeImageFilterIF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >'),
  ('DerivativeImageFilter', 'itk::DerivativeImageFilter', 'itkDerivativeImageFilterID2ID2', True, 'itk::Image< double,2 >, itk::Image< double,2 >'),
  ('DerivativeImageFilter', 'itk::DerivativeImageFilter', 'itkDerivativeImageFilterID3ID3', True, 'itk::Image< double,3 >, itk::Image< double,3 >'),
  ('DiscreteGaussianDerivativeImageFilter', 'itk::DiscreteGaussianDerivativeImageFilter', 'itkDiscreteGaussianDerivativeImageFilterISS2ISS2', True, 'itk::Image< signed short,2 >, itk::Image< signed short,2 >'),
  ('DiscreteGaussianDerivativeImageFilter', 'itk::DiscreteGaussianDerivativeImageFilter', 'itkDiscreteGaussianDerivativeImageFilterISS3ISS3', True, 'itk::Image< signed short,3 >, itk::Image< signed short,3 >'),
  ('DiscreteGaussianDerivativeImageFilter', 'itk::DiscreteGaussianDerivativeImageFilter', 'itkDiscreteGaussianDerivativeImageFilterIUC2IUC2', True, 'itk::Image< unsigned char,2 >, itk::Image< unsigned char,2 >'),
  ('DiscreteGaussianDerivativeImageFilter', 'itk::DiscreteGaussianDerivativeImageFilter', 'itkDiscreteGaussianDerivativeImageFilterIUC3IUC3', True, 'itk::Image< unsigned char,3 >, itk::Image< unsigned char,3 >'),
  ('DiscreteGaussianDerivativeImageFilter', 'itk::DiscreteGaussianDerivativeImageFilter', 'itkDiscreteGaussianDerivativeImageFilterIUS2IUS2', True, 'itk::Image< unsigned short,2 >, itk::Image< unsigned short,2 >'),
  ('DiscreteGaussianDerivativeImageFilter', 'itk::DiscreteGaussianDerivativeImageFilter', 'itkDiscreteGaussianDerivativeImageFilterIUS3IUS3', True, 'itk::Image< unsigned short,3 >, itk::Image< unsigned short,3 >'),
  ('DiscreteGaussianDerivativeImageFilter', 'itk::DiscreteGaussianDerivativeImageFilter', 'itkDiscreteGaussianDerivativeImageFilterIF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >'),
  ('DiscreteGaussianDerivativeImageFilter', 'itk::DiscreteGaussianDerivativeImageFilter', 'itkDiscreteGaussianDerivativeImageFilterIF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >'),
  ('DiscreteGaussianDerivativeImageFilter', 'itk::DiscreteGaussianDerivativeImageFilter', 'itkDiscreteGaussianDerivativeImageFilterID2ID2', True, 'itk::Image< double,2 >, itk::Image< double,2 >'),
  ('DiscreteGaussianDerivativeImageFilter', 'itk::DiscreteGaussianDerivativeImageFilter', 'itkDiscreteGaussianDerivativeImageFilterID3ID3', True, 'itk::Image< double,3 >, itk::Image< double,3 >'),
  ('GradientVectorFlowImageFilter', 'itk::GradientVectorFlowImageFilter', 'itkGradientVectorFlowImageFilterIVF22IVF22F', True, 'itk::Image< itk::Vector< float,2 >,2 >, itk::Image< itk::Vector< float,2 >,2 >, float'),
  ('GradientVectorFlowImageFilter', 'itk::GradientVectorFlowImageFilter', 'itkGradientVectorFlowImageFilterICVF22ICVF22F', True, 'itk::Image< itk::CovariantVector< float,2 >,2 >, itk::Image< itk::CovariantVector< float,2 >,2 >, float'),
  ('GradientVectorFlowImageFilter', 'itk::GradientVectorFlowImageFilter', 'itkGradientVectorFlowImageFilterIVF33IVF33F', True, 'itk::Image< itk::Vector< float,3 >,3 >, itk::Image< itk::Vector< float,3 >,3 >, float'),
  ('GradientVectorFlowImageFilter', 'itk::GradientVectorFlowImageFilter', 'itkGradientVectorFlowImageFilterICVF33ICVF33F', True, 'itk::Image< itk::CovariantVector< float,3 >,3 >, itk::Image< itk::CovariantVector< float,3 >,3 >, float'),
  ('Hessian3DToVesselnessMeasureImageFilter', 'itk::Hessian3DToVesselnessMeasureImageFilter', 'itkHessian3DToVesselnessMeasureImageFilterSS', True, 'signed short'),
  ('Hessian3DToVesselnessMeasureImageFilter', 'itk::Hessian3DToVesselnessMeasureImageFilter', 'itkHessian3DToVesselnessMeasureImageFilterUC', True, 'unsigned char'),
  ('Hessian3DToVesselnessMeasureImageFilter', 'itk::Hessian3DToVesselnessMeasureImageFilter', 'itkHessian3DToVesselnessMeasureImageFilterUS', True, 'unsigned short'),
  ('Hessian3DToVesselnessMeasureImageFilter', 'itk::Hessian3DToVesselnessMeasureImageFilter', 'itkHessian3DToVesselnessMeasureImageFilterF', True, 'float'),
  ('Hessian3DToVesselnessMeasureImageFilter', 'itk::Hessian3DToVesselnessMeasureImageFilter', 'itkHessian3DToVesselnessMeasureImageFilterD', True, 'double'),
  ('HessianToObjectnessMeasureImageFilter', 'itk::HessianToObjectnessMeasureImageFilter', 'itkHessianToObjectnessMeasureImageFilterISSRTD22ISS2', True, 'itk::Image< itk::SymmetricSecondRankTensor< double, 2 >, 2 >, itk::Image< signed short,2 >'),
  ('HessianToObjectnessMeasureImageFilter', 'itk::HessianToObjectnessMeasureImageFilter', 'itkHessianToObjectnessMeasureImageFilterISSRTD22IUC2', True, 'itk::Image< itk::SymmetricSecondRankTensor< double, 2 >, 2 >, itk::Image< unsigned char,2 >'),
  ('HessianToObjectnessMeasureImageFilter', 'itk::HessianToObjectnessMeasureImageFilter', 'itkHessianToObjectnessMeasureImageFilterISSRTD22IUS2', True, 'itk::Image< itk::SymmetricSecondRankTensor< double, 2 >, 2 >, itk::Image< unsigned short,2 >'),
  ('HessianToObjectnessMeasureImageFilter', 'itk::HessianToObjectnessMeasureImageFilter', 'itkHessianToObjectnessMeasureImageFilterISSRTD22IF2', True, 'itk::Image< itk::SymmetricSecondRankTensor< double, 2 >, 2 >, itk::Image< float,2 >'),
  ('HessianToObjectnessMeasureImageFilter', 'itk::HessianToObjectnessMeasureImageFilter', 'itkHessianToObjectnessMeasureImageFilterISSRTD22ID2', True, 'itk::Image< itk::SymmetricSecondRankTensor< double, 2 >, 2 >, itk::Image< double,2 >'),
  ('HessianToObjectnessMeasureImageFilter', 'itk::HessianToObjectnessMeasureImageFilter', 'itkHessianToObjectnessMeasureImageFilterISSRTD33ISS3', True, 'itk::Image< itk::SymmetricSecondRankTensor< double, 3 >, 3 >, itk::Image< signed short,3 >'),
  ('HessianToObjectnessMeasureImageFilter', 'itk::HessianToObjectnessMeasureImageFilter', 'itkHessianToObjectnessMeasureImageFilterISSRTD33IUC3', True, 'itk::Image< itk::SymmetricSecondRankTensor< double, 3 >, 3 >, itk::Image< unsigned char,3 >'),
  ('HessianToObjectnessMeasureImageFilter', 'itk::HessianToObjectnessMeasureImageFilter', 'itkHessianToObjectnessMeasureImageFilterISSRTD33IUS3', True, 'itk::Image< itk::SymmetricSecondRankTensor< double, 3 >, 3 >, itk::Image< unsigned short,3 >'),
  ('HessianToObjectnessMeasureImageFilter', 'itk::HessianToObjectnessMeasureImageFilter', 'itkHessianToObjectnessMeasureImageFilterISSRTD33IF3', True, 'itk::Image< itk::SymmetricSecondRankTensor< double, 3 >, 3 >, itk::Image< float,3 >'),
  ('HessianToObjectnessMeasureImageFilter', 'itk::HessianToObjectnessMeasureImageFilter', 'itkHessianToObjectnessMeasureImageFilterISSRTD33ID3', True, 'itk::Image< itk::SymmetricSecondRankTensor< double, 3 >, 3 >, itk::Image< double,3 >'),
  ('HoughTransform2DCirclesImageFilter', 'itk::HoughTransform2DCirclesImageFilter', 'itkHoughTransform2DCirclesImageFilterSSULF', True, 'signed short, unsigned long, float'),
  ('HoughTransform2DCirclesImageFilter', 'itk::HoughTransform2DCirclesImageFilter', 'itkHoughTransform2DCirclesImageFilterUCULF', True, 'unsigned char, unsigned long, float'),
  ('HoughTransform2DCirclesImageFilter', 'itk::HoughTransform2DCirclesImageFilter', 'itkHoughTransform2DCirclesImageFilterUSULF', True, 'unsigned short, unsigned long, float'),
  ('HoughTransform2DCirclesImageFilter', 'itk::HoughTransform2DCirclesImageFilter', 'itkHoughTransform2DCirclesImageFilterFULF', True, 'float, unsigned long, float'),
  ('HoughTransform2DCirclesImageFilter', 'itk::HoughTransform2DCirclesImageFilter', 'itkHoughTransform2DCirclesImageFilterDULF', True, 'double, unsigned long, float'),
  ('HoughTransform2DLinesImageFilter', 'itk::HoughTransform2DLinesImageFilter', 'itkHoughTransform2DLinesImageFilterFF', True, 'float, float'),
  ('HoughTransform2DLinesImageFilter', 'itk::HoughTransform2DLinesImageFilter', 'itkHoughTransform2DLinesImageFilterDD', True, 'double, double'),
  ('LaplacianImageFilter', 'itk::LaplacianImageFilter', 'itkLaplacianImageFilterIF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >'),
  ('LaplacianImageFilter', 'itk::LaplacianImageFilter', 'itkLaplacianImageFilterIF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >'),
  ('LaplacianImageFilter', 'itk::LaplacianImageFilter', 'itkLaplacianImageFilterID2ID2', True, 'itk::Image< double,2 >, itk::Image< double,2 >'),
  ('LaplacianImageFilter', 'itk::LaplacianImageFilter', 'itkLaplacianImageFilterID3ID3', True, 'itk::Image< double,3 >, itk::Image< double,3 >'),
  ('LaplacianRecursiveGaussianImageFilter', 'itk::LaplacianRecursiveGaussianImageFilter', 'itkLaplacianRecursiveGaussianImageFilterISS2ISS2', True, 'itk::Image< signed short,2 >, itk::Image< signed short,2 >'),
  ('LaplacianRecursiveGaussianImageFilter', 'itk::LaplacianRecursiveGaussianImageFilter', 'itkLaplacianRecursiveGaussianImageFilterISS3ISS3', True, 'itk::Image< signed short,3 >, itk::Image< signed short,3 >'),
  ('LaplacianRecursiveGaussianImageFilter', 'itk::LaplacianRecursiveGaussianImageFilter', 'itkLaplacianRecursiveGaussianImageFilterIUC2IUC2', True, 'itk::Image< unsigned char,2 >, itk::Image< unsigned char,2 >'),
  ('LaplacianRecursiveGaussianImageFilter', 'itk::LaplacianRecursiveGaussianImageFilter', 'itkLaplacianRecursiveGaussianImageFilterIUC3IUC3', True, 'itk::Image< unsigned char,3 >, itk::Image< unsigned char,3 >'),
  ('LaplacianRecursiveGaussianImageFilter', 'itk::LaplacianRecursiveGaussianImageFilter', 'itkLaplacianRecursiveGaussianImageFilterIUS2IUS2', True, 'itk::Image< unsigned short,2 >, itk::Image< unsigned short,2 >'),
  ('LaplacianRecursiveGaussianImageFilter', 'itk::LaplacianRecursiveGaussianImageFilter', 'itkLaplacianRecursiveGaussianImageFilterIUS3IUS3', True, 'itk::Image< unsigned short,3 >, itk::Image< unsigned short,3 >'),
  ('LaplacianRecursiveGaussianImageFilter', 'itk::LaplacianRecursiveGaussianImageFilter', 'itkLaplacianRecursiveGaussianImageFilterIF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >'),
  ('LaplacianRecursiveGaussianImageFilter', 'itk::LaplacianRecursiveGaussianImageFilter', 'itkLaplacianRecursiveGaussianImageFilterIF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >'),
  ('LaplacianRecursiveGaussianImageFilter', 'itk::LaplacianRecursiveGaussianImageFilter', 'itkLaplacianRecursiveGaussianImageFilterID2ID2', True, 'itk::Image< double,2 >, itk::Image< double,2 >'),
  ('LaplacianRecursiveGaussianImageFilter', 'itk::LaplacianRecursiveGaussianImageFilter', 'itkLaplacianRecursiveGaussianImageFilterID3ID3', True, 'itk::Image< double,3 >, itk::Image< double,3 >'),
  ('LaplacianSharpeningImageFilter', 'itk::LaplacianSharpeningImageFilter', 'itkLaplacianSharpeningImageFilterISS2ISS2', True, 'itk::Image< signed short,2 >, itk::Image< signed short,2 >'),
  ('LaplacianSharpeningImageFilter', 'itk::LaplacianSharpeningImageFilter', 'itkLaplacianSharpeningImageFilterISS3ISS3', True, 'itk::Image< signed short,3 >, itk::Image< signed short,3 >'),
  ('LaplacianSharpeningImageFilter', 'itk::LaplacianSharpeningImageFilter', 'itkLaplacianSharpeningImageFilterIUC2IUC2', True, 'itk::Image< unsigned char,2 >, itk::Image< unsigned char,2 >'),
  ('LaplacianSharpeningImageFilter', 'itk::LaplacianSharpeningImageFilter', 'itkLaplacianSharpeningImageFilterIUC3IUC3', True, 'itk::Image< unsigned char,3 >, itk::Image< unsigned char,3 >'),
  ('LaplacianSharpeningImageFilter', 'itk::LaplacianSharpeningImageFilter', 'itkLaplacianSharpeningImageFilterIUS2IUS2', True, 'itk::Image< unsigned short,2 >, itk::Image< unsigned short,2 >'),
  ('LaplacianSharpeningImageFilter', 'itk::LaplacianSharpeningImageFilter', 'itkLaplacianSharpeningImageFilterIUS3IUS3', True, 'itk::Image< unsigned short,3 >, itk::Image< unsigned short,3 >'),
  ('LaplacianSharpeningImageFilter', 'itk::LaplacianSharpeningImageFilter', 'itkLaplacianSharpeningImageFilterIF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >'),
  ('LaplacianSharpeningImageFilter', 'itk::LaplacianSharpeningImageFilter', 'itkLaplacianSharpeningImageFilterIF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >'),
  ('LaplacianSharpeningImageFilter', 'itk::LaplacianSharpeningImageFilter', 'itkLaplacianSharpeningImageFilterID2ID2', True, 'itk::Image< double,2 >, itk::Image< double,2 >'),
  ('LaplacianSharpeningImageFilter', 'itk::LaplacianSharpeningImageFilter', 'itkLaplacianSharpeningImageFilterID3ID3', True, 'itk::Image< double,3 >, itk::Image< double,3 >'),
  ('MaskFeaturePointSelectionFilter', 'itk::MaskFeaturePointSelectionFilter', 'itkMaskFeaturePointSelectionFilterIF3', True, 'itk::Image< float,3 >'),
  ('MaskFeaturePointSelectionFilter', 'itk::MaskFeaturePointSelectionFilter', 'itkMaskFeaturePointSelectionFilterID3', True, 'itk::Image< double,3 >'),
  ('MultiScaleHessianBasedMeasureImageFilterEnums', 'itk::MultiScaleHessianBasedMeasureImageFilterEnums', 'itkMultiScaleHessianBasedMeasureImageFilterEnums', False),
  ('MultiScaleHessianBasedMeasureImageFilter', 'itk::MultiScaleHessianBasedMeasureImageFilter', 'itkMultiScaleHessianBasedMeasureImageFilterISS2ISSRTD22ISS2', True, 'itk::Image< signed short,2 >, itk::Image< itk::SymmetricSecondRankTensor< double, 2 >, 2 >, itk::Image< signed short,2 >'),
  ('MultiScaleHessianBasedMeasureImageFilter', 'itk::MultiScaleHessianBasedMeasureImageFilter', 'itkMultiScaleHessianBasedMeasureImageFilterIUC2ISSRTD22IUC2', True, 'itk::Image< unsigned char,2 >, itk::Image< itk::SymmetricSecondRankTensor< double, 2 >, 2 >, itk::Image< unsigned char,2 >'),
  ('MultiScaleHessianBasedMeasureImageFilter', 'itk::MultiScaleHessianBasedMeasureImageFilter', 'itkMultiScaleHessianBasedMeasureImageFilterIUS2ISSRTD22IUS2', True, 'itk::Image< unsigned short,2 >, itk::Image< itk::SymmetricSecondRankTensor< double, 2 >, 2 >, itk::Image< unsigned short,2 >'),
  ('MultiScaleHessianBasedMeasureImageFilter', 'itk::MultiScaleHessianBasedMeasureImageFilter', 'itkMultiScaleHessianBasedMeasureImageFilterIF2ISSRTD22IF2', True, 'itk::Image< float,2 >, itk::Image< itk::SymmetricSecondRankTensor< double, 2 >, 2 >, itk::Image< float,2 >'),
  ('MultiScaleHessianBasedMeasureImageFilter', 'itk::MultiScaleHessianBasedMeasureImageFilter', 'itkMultiScaleHessianBasedMeasureImageFilterID2ISSRTD22ID2', True, 'itk::Image< double,2 >, itk::Image< itk::SymmetricSecondRankTensor< double, 2 >, 2 >, itk::Image< double,2 >'),
  ('MultiScaleHessianBasedMeasureImageFilter', 'itk::MultiScaleHessianBasedMeasureImageFilter', 'itkMultiScaleHessianBasedMeasureImageFilterISS3ISSRTD33ISS3', True, 'itk::Image< signed short,3 >, itk::Image< itk::SymmetricSecondRankTensor< double, 3 >, 3 >, itk::Image< signed short,3 >'),
  ('MultiScaleHessianBasedMeasureImageFilter', 'itk::MultiScaleHessianBasedMeasureImageFilter', 'itkMultiScaleHessianBasedMeasureImageFilterIUC3ISSRTD33IUC3', True, 'itk::Image< unsigned char,3 >, itk::Image< itk::SymmetricSecondRankTensor< double, 3 >, 3 >, itk::Image< unsigned char,3 >'),
  ('MultiScaleHessianBasedMeasureImageFilter', 'itk::MultiScaleHessianBasedMeasureImageFilter', 'itkMultiScaleHessianBasedMeasureImageFilterIUS3ISSRTD33IUS3', True, 'itk::Image< unsigned short,3 >, itk::Image< itk::SymmetricSecondRankTensor< double, 3 >, 3 >, itk::Image< unsigned short,3 >'),
  ('MultiScaleHessianBasedMeasureImageFilter', 'itk::MultiScaleHessianBasedMeasureImageFilter', 'itkMultiScaleHessianBasedMeasureImageFilterIF3ISSRTD33IF3', True, 'itk::Image< float,3 >, itk::Image< itk::SymmetricSecondRankTensor< double, 3 >, 3 >, itk::Image< float,3 >'),
  ('MultiScaleHessianBasedMeasureImageFilter', 'itk::MultiScaleHessianBasedMeasureImageFilter', 'itkMultiScaleHessianBasedMeasureImageFilterID3ISSRTD33ID3', True, 'itk::Image< double,3 >, itk::Image< itk::SymmetricSecondRankTensor< double, 3 >, 3 >, itk::Image< double,3 >'),
  ('SimpleContourExtractorImageFilter', 'itk::SimpleContourExtractorImageFilter', 'itkSimpleContourExtractorImageFilterISS2ISS2', True, 'itk::Image< signed short,2 >, itk::Image< signed short,2 >'),
  ('SimpleContourExtractorImageFilter', 'itk::SimpleContourExtractorImageFilter', 'itkSimpleContourExtractorImageFilterISS3ISS3', True, 'itk::Image< signed short,3 >, itk::Image< signed short,3 >'),
  ('SimpleContourExtractorImageFilter', 'itk::SimpleContourExtractorImageFilter', 'itkSimpleContourExtractorImageFilterIUC2IUC2', True, 'itk::Image< unsigned char,2 >, itk::Image< unsigned char,2 >'),
  ('SimpleContourExtractorImageFilter', 'itk::SimpleContourExtractorImageFilter', 'itkSimpleContourExtractorImageFilterIUC3IUC3', True, 'itk::Image< unsigned char,3 >, itk::Image< unsigned char,3 >'),
  ('SimpleContourExtractorImageFilter', 'itk::SimpleContourExtractorImageFilter', 'itkSimpleContourExtractorImageFilterIUS2IUS2', True, 'itk::Image< unsigned short,2 >, itk::Image< unsigned short,2 >'),
  ('SimpleContourExtractorImageFilter', 'itk::SimpleContourExtractorImageFilter', 'itkSimpleContourExtractorImageFilterIUS3IUS3', True, 'itk::Image< unsigned short,3 >, itk::Image< unsigned short,3 >'),
  ('SimpleContourExtractorImageFilter', 'itk::SimpleContourExtractorImageFilter', 'itkSimpleContourExtractorImageFilterIF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >'),
  ('SimpleContourExtractorImageFilter', 'itk::SimpleContourExtractorImageFilter', 'itkSimpleContourExtractorImageFilterIF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >'),
  ('SimpleContourExtractorImageFilter', 'itk::SimpleContourExtractorImageFilter', 'itkSimpleContourExtractorImageFilterID2ID2', True, 'itk::Image< double,2 >, itk::Image< double,2 >'),
  ('SimpleContourExtractorImageFilter', 'itk::SimpleContourExtractorImageFilter', 'itkSimpleContourExtractorImageFilterID3ID3', True, 'itk::Image< double,3 >, itk::Image< double,3 >'),
  ('SobelEdgeDetectionImageFilter', 'itk::SobelEdgeDetectionImageFilter', 'itkSobelEdgeDetectionImageFilterIF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >'),
  ('SobelEdgeDetectionImageFilter', 'itk::SobelEdgeDetectionImageFilter', 'itkSobelEdgeDetectionImageFilterIF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >'),
  ('SobelEdgeDetectionImageFilter', 'itk::SobelEdgeDetectionImageFilter', 'itkSobelEdgeDetectionImageFilterID2ID2', True, 'itk::Image< double,2 >, itk::Image< double,2 >'),
  ('SobelEdgeDetectionImageFilter', 'itk::SobelEdgeDetectionImageFilter', 'itkSobelEdgeDetectionImageFilterID3ID3', True, 'itk::Image< double,3 >, itk::Image< double,3 >'),
  ('UnsharpMaskImageFilter', 'itk::UnsharpMaskImageFilter', 'itkUnsharpMaskImageFilterISS2ISS2', True, 'itk::Image< signed short,2 >, itk::Image< signed short,2 >'),
  ('UnsharpMaskImageFilter', 'itk::UnsharpMaskImageFilter', 'itkUnsharpMaskImageFilterISS3ISS3', True, 'itk::Image< signed short,3 >, itk::Image< signed short,3 >'),
  ('UnsharpMaskImageFilter', 'itk::UnsharpMaskImageFilter', 'itkUnsharpMaskImageFilterIUC2IUC2', True, 'itk::Image< unsigned char,2 >, itk::Image< unsigned char,2 >'),
  ('UnsharpMaskImageFilter', 'itk::UnsharpMaskImageFilter', 'itkUnsharpMaskImageFilterIUC3IUC3', True, 'itk::Image< unsigned char,3 >, itk::Image< unsigned char,3 >'),
  ('UnsharpMaskImageFilter', 'itk::UnsharpMaskImageFilter', 'itkUnsharpMaskImageFilterIUS2IUS2', True, 'itk::Image< unsigned short,2 >, itk::Image< unsigned short,2 >'),
  ('UnsharpMaskImageFilter', 'itk::UnsharpMaskImageFilter', 'itkUnsharpMaskImageFilterIUS3IUS3', True, 'itk::Image< unsigned short,3 >, itk::Image< unsigned short,3 >'),
  ('UnsharpMaskImageFilter', 'itk::UnsharpMaskImageFilter', 'itkUnsharpMaskImageFilterIF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >'),
  ('UnsharpMaskImageFilter', 'itk::UnsharpMaskImageFilter', 'itkUnsharpMaskImageFilterIF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >'),
  ('UnsharpMaskImageFilter', 'itk::UnsharpMaskImageFilter', 'itkUnsharpMaskImageFilterID2ID2', True, 'itk::Image< double,2 >, itk::Image< double,2 >'),
  ('UnsharpMaskImageFilter', 'itk::UnsharpMaskImageFilter', 'itkUnsharpMaskImageFilterID3ID3', True, 'itk::Image< double,3 >, itk::Image< double,3 >'),
  ('ZeroCrossingBasedEdgeDetectionImageFilter', 'itk::ZeroCrossingBasedEdgeDetectionImageFilter', 'itkZeroCrossingBasedEdgeDetectionImageFilterIF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >'),
  ('ZeroCrossingBasedEdgeDetectionImageFilter', 'itk::ZeroCrossingBasedEdgeDetectionImageFilter', 'itkZeroCrossingBasedEdgeDetectionImageFilterIF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >'),
  ('ZeroCrossingBasedEdgeDetectionImageFilter', 'itk::ZeroCrossingBasedEdgeDetectionImageFilter', 'itkZeroCrossingBasedEdgeDetectionImageFilterID2ID2', True, 'itk::Image< double,2 >, itk::Image< double,2 >'),
  ('ZeroCrossingBasedEdgeDetectionImageFilter', 'itk::ZeroCrossingBasedEdgeDetectionImageFilter', 'itkZeroCrossingBasedEdgeDetectionImageFilterID3ID3', True, 'itk::Image< double,3 >, itk::Image< double,3 >'),
  ('ZeroCrossingImageFilter', 'itk::ZeroCrossingImageFilter', 'itkZeroCrossingImageFilterISS2ISS2', True, 'itk::Image< signed short,2 >, itk::Image< signed short,2 >'),
  ('ZeroCrossingImageFilter', 'itk::ZeroCrossingImageFilter', 'itkZeroCrossingImageFilterISS3ISS3', True, 'itk::Image< signed short,3 >, itk::Image< signed short,3 >'),
  ('ZeroCrossingImageFilter', 'itk::ZeroCrossingImageFilter', 'itkZeroCrossingImageFilterIF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >'),
  ('ZeroCrossingImageFilter', 'itk::ZeroCrossingImageFilter', 'itkZeroCrossingImageFilterIF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >'),
  ('ZeroCrossingImageFilter', 'itk::ZeroCrossingImageFilter', 'itkZeroCrossingImageFilterID2ID2', True, 'itk::Image< double,2 >, itk::Image< double,2 >'),
  ('ZeroCrossingImageFilter', 'itk::ZeroCrossingImageFilter', 'itkZeroCrossingImageFilterID3ID3', True, 'itk::Image< double,3 >, itk::Image< double,3 >'),
)
snake_case_functions = ('bilateral_image_filter', 'laplacian_image_filter', 'simple_contour_extractor_image_filter', 'derivative_image_filter', 'gradient_vector_flow_image_filter', 'discrete_gaussian_derivative_image_filter', 'laplacian_recursive_gaussian_image_filter', 'unsharp_mask_image_filter', 'image_to_mesh_filter', 'mesh_source', 'hough_transform2_d_lines_image_filter', 'zero_crossing_based_edge_detection_image_filter', 'mask_feature_point_selection_filter', 'hessian3_d_to_vesselness_measure_image_filter', 'multi_scale_hessian_based_measure_image_filter', 'hessian_to_objectness_measure_image_filter', 'hessian_recursive_gaussian_image_filter', 'laplacian_sharpening_image_filter', 'sobel_edge_detection_image_filter', 'zero_crossing_image_filter', 'canny_edge_detection_image_filter', 'hough_transform2_d_circles_image_filter', )
