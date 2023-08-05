depends = ('ITKPyBase', 'ITKQuadEdgeMesh', 'ITKMesh', )
templates = (
  ('BorderQuadEdgeMeshFilter', 'itk::BorderQuadEdgeMeshFilter', 'itkBorderQuadEdgeMeshFilterQEMD2', True, 'itk::QuadEdgeMesh< double,2 >'),
  ('BorderQuadEdgeMeshFilter', 'itk::BorderQuadEdgeMeshFilter', 'itkBorderQuadEdgeMeshFilterQEMD3', True, 'itk::QuadEdgeMesh< double,3 >'),
  ('BorderQuadEdgeMeshFilterEnums', 'itk::BorderQuadEdgeMeshFilterEnums', 'itkBorderQuadEdgeMeshFilterEnums', False),
  ('CleanQuadEdgeMeshFilter', 'itk::CleanQuadEdgeMeshFilter', 'itkCleanQuadEdgeMeshFilterQEMD2', True, 'itk::QuadEdgeMesh< double,2 >'),
  ('CleanQuadEdgeMeshFilter', 'itk::CleanQuadEdgeMeshFilter', 'itkCleanQuadEdgeMeshFilterQEMD3', True, 'itk::QuadEdgeMesh< double,3 >'),
  ('DelaunayConformingQuadEdgeMeshFilter', 'itk::DelaunayConformingQuadEdgeMeshFilter', 'itkDelaunayConformingQuadEdgeMeshFilterQEMD2', True, 'itk::QuadEdgeMesh< double,2 >'),
  ('DelaunayConformingQuadEdgeMeshFilter', 'itk::DelaunayConformingQuadEdgeMeshFilter', 'itkDelaunayConformingQuadEdgeMeshFilterQEMD3', True, 'itk::QuadEdgeMesh< double,3 >'),
  ('DiscreteCurvatureQuadEdgeMeshFilter', 'itk::DiscreteCurvatureQuadEdgeMeshFilter', 'itkDiscreteCurvatureQuadEdgeMeshFilterQEMD2', True, 'itk::QuadEdgeMesh< double,2 >'),
  ('DiscreteCurvatureQuadEdgeMeshFilter', 'itk::DiscreteCurvatureQuadEdgeMeshFilter', 'itkDiscreteCurvatureQuadEdgeMeshFilterQEMD3', True, 'itk::QuadEdgeMesh< double,3 >'),
  ('DiscreteCurvatureTensorQuadEdgeMeshFilter', 'itk::DiscreteCurvatureTensorQuadEdgeMeshFilter', 'itkDiscreteCurvatureTensorQuadEdgeMeshFilterQEMD2', True, 'itk::QuadEdgeMesh< double,2 >'),
  ('DiscreteCurvatureTensorQuadEdgeMeshFilter', 'itk::DiscreteCurvatureTensorQuadEdgeMeshFilter', 'itkDiscreteCurvatureTensorQuadEdgeMeshFilterQEMD3', True, 'itk::QuadEdgeMesh< double,3 >'),
  ('DiscreteGaussianCurvatureQuadEdgeMeshFilter', 'itk::DiscreteGaussianCurvatureQuadEdgeMeshFilter', 'itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD2', True, 'itk::QuadEdgeMesh< double,2 >'),
  ('DiscreteGaussianCurvatureQuadEdgeMeshFilter', 'itk::DiscreteGaussianCurvatureQuadEdgeMeshFilter', 'itkDiscreteGaussianCurvatureQuadEdgeMeshFilterQEMD3', True, 'itk::QuadEdgeMesh< double,3 >'),
  ('DiscreteMaximumCurvatureQuadEdgeMeshFilter', 'itk::DiscreteMaximumCurvatureQuadEdgeMeshFilter', 'itkDiscreteMaximumCurvatureQuadEdgeMeshFilterQEMD2', True, 'itk::QuadEdgeMesh< double,2 >'),
  ('DiscreteMaximumCurvatureQuadEdgeMeshFilter', 'itk::DiscreteMaximumCurvatureQuadEdgeMeshFilter', 'itkDiscreteMaximumCurvatureQuadEdgeMeshFilterQEMD3', True, 'itk::QuadEdgeMesh< double,3 >'),
  ('DiscreteMeanCurvatureQuadEdgeMeshFilter', 'itk::DiscreteMeanCurvatureQuadEdgeMeshFilter', 'itkDiscreteMeanCurvatureQuadEdgeMeshFilterQEMD2', True, 'itk::QuadEdgeMesh< double,2 >'),
  ('DiscreteMeanCurvatureQuadEdgeMeshFilter', 'itk::DiscreteMeanCurvatureQuadEdgeMeshFilter', 'itkDiscreteMeanCurvatureQuadEdgeMeshFilterQEMD3', True, 'itk::QuadEdgeMesh< double,3 >'),
  ('DiscreteMinimumCurvatureQuadEdgeMeshFilter', 'itk::DiscreteMinimumCurvatureQuadEdgeMeshFilter', 'itkDiscreteMinimumCurvatureQuadEdgeMeshFilterQEMD2', True, 'itk::QuadEdgeMesh< double,2 >'),
  ('DiscreteMinimumCurvatureQuadEdgeMeshFilter', 'itk::DiscreteMinimumCurvatureQuadEdgeMeshFilter', 'itkDiscreteMinimumCurvatureQuadEdgeMeshFilterQEMD3', True, 'itk::QuadEdgeMesh< double,3 >'),
  ('DiscretePrincipalCurvaturesQuadEdgeMeshFilter', 'itk::DiscretePrincipalCurvaturesQuadEdgeMeshFilter', 'itkDiscretePrincipalCurvaturesQuadEdgeMeshFilterQEMD2', True, 'itk::QuadEdgeMesh< double,2 >'),
  ('DiscretePrincipalCurvaturesQuadEdgeMeshFilter', 'itk::DiscretePrincipalCurvaturesQuadEdgeMeshFilter', 'itkDiscretePrincipalCurvaturesQuadEdgeMeshFilterQEMD3', True, 'itk::QuadEdgeMesh< double,3 >'),
  ('MatrixCoefficients', 'itk::MatrixCoefficients', 'itkMatrixCoefficientsQEMD2', False, 'itk::QuadEdgeMesh< double,2 >'),
  ('MatrixCoefficients', 'itk::MatrixCoefficients', 'itkMatrixCoefficientsQEMD3', False, 'itk::QuadEdgeMesh< double,3 >'),
  ('OnesMatrixCoefficients', 'itk::OnesMatrixCoefficients', 'itkOnesMatrixCoefficientsQEMD2', False, 'itk::QuadEdgeMesh< double,2 >'),
  ('OnesMatrixCoefficients', 'itk::OnesMatrixCoefficients', 'itkOnesMatrixCoefficientsQEMD3', False, 'itk::QuadEdgeMesh< double,3 >'),
  ('InverseEuclideanDistanceMatrixCoefficients', 'itk::InverseEuclideanDistanceMatrixCoefficients', 'itkInverseEuclideanDistanceMatrixCoefficientsQEMD2', False, 'itk::QuadEdgeMesh< double,2 >'),
  ('InverseEuclideanDistanceMatrixCoefficients', 'itk::InverseEuclideanDistanceMatrixCoefficients', 'itkInverseEuclideanDistanceMatrixCoefficientsQEMD3', False, 'itk::QuadEdgeMesh< double,3 >'),
  ('ConformalMatrixCoefficients', 'itk::ConformalMatrixCoefficients', 'itkConformalMatrixCoefficientsQEMD2', False, 'itk::QuadEdgeMesh< double,2 >'),
  ('ConformalMatrixCoefficients', 'itk::ConformalMatrixCoefficients', 'itkConformalMatrixCoefficientsQEMD3', False, 'itk::QuadEdgeMesh< double,3 >'),
  ('AuthalicMatrixCoefficients', 'itk::AuthalicMatrixCoefficients', 'itkAuthalicMatrixCoefficientsQEMD2', False, 'itk::QuadEdgeMesh< double,2 >'),
  ('AuthalicMatrixCoefficients', 'itk::AuthalicMatrixCoefficients', 'itkAuthalicMatrixCoefficientsQEMD3', False, 'itk::QuadEdgeMesh< double,3 >'),
  ('IntrinsicMatrixCoefficients', 'itk::IntrinsicMatrixCoefficients', 'itkIntrinsicMatrixCoefficientsQEMD2', False, 'itk::QuadEdgeMesh< double,2 >'),
  ('IntrinsicMatrixCoefficients', 'itk::IntrinsicMatrixCoefficients', 'itkIntrinsicMatrixCoefficientsQEMD3', False, 'itk::QuadEdgeMesh< double,3 >'),
  ('HarmonicMatrixCoefficients', 'itk::HarmonicMatrixCoefficients', 'itkHarmonicMatrixCoefficientsQEMD2', False, 'itk::QuadEdgeMesh< double,2 >'),
  ('HarmonicMatrixCoefficients', 'itk::HarmonicMatrixCoefficients', 'itkHarmonicMatrixCoefficientsQEMD3', False, 'itk::QuadEdgeMesh< double,3 >'),
  ('SmoothingQuadEdgeMeshFilter', 'itk::SmoothingQuadEdgeMeshFilter', 'itkSmoothingQuadEdgeMeshFilterQEMD2', True, 'itk::QuadEdgeMesh< double,2 >'),
  ('SmoothingQuadEdgeMeshFilter', 'itk::SmoothingQuadEdgeMeshFilter', 'itkSmoothingQuadEdgeMeshFilterQEMD3', True, 'itk::QuadEdgeMesh< double,3 >'),
)
snake_case_functions = ('discrete_minimum_curvature_quad_edge_mesh_filter', 'discrete_principal_curvatures_quad_edge_mesh_filter', 'clean_quad_edge_mesh_filter', 'discrete_curvature_quad_edge_mesh_filter', 'smoothing_quad_edge_mesh_filter', 'discrete_maximum_curvature_quad_edge_mesh_filter', 'border_quad_edge_mesh_filter', 'discrete_gaussian_curvature_quad_edge_mesh_filter', 'delaunay_conforming_quad_edge_mesh_filter', 'discrete_mean_curvature_quad_edge_mesh_filter', 'discrete_curvature_tensor_quad_edge_mesh_filter', )
