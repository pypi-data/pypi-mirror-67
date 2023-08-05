depends = ('ITKPyBase', 'ITKImageFunction', )
templates = (
  ('BinomialBlurImageFilter', 'itk::BinomialBlurImageFilter', 'itkBinomialBlurImageFilterISS2ISS2', True, 'itk::Image< signed short,2 >, itk::Image< signed short,2 >'),
  ('BinomialBlurImageFilter', 'itk::BinomialBlurImageFilter', 'itkBinomialBlurImageFilterISS3ISS3', True, 'itk::Image< signed short,3 >, itk::Image< signed short,3 >'),
  ('BinomialBlurImageFilter', 'itk::BinomialBlurImageFilter', 'itkBinomialBlurImageFilterIUC2IUC2', True, 'itk::Image< unsigned char,2 >, itk::Image< unsigned char,2 >'),
  ('BinomialBlurImageFilter', 'itk::BinomialBlurImageFilter', 'itkBinomialBlurImageFilterIUC3IUC3', True, 'itk::Image< unsigned char,3 >, itk::Image< unsigned char,3 >'),
  ('BinomialBlurImageFilter', 'itk::BinomialBlurImageFilter', 'itkBinomialBlurImageFilterIUS2IUS2', True, 'itk::Image< unsigned short,2 >, itk::Image< unsigned short,2 >'),
  ('BinomialBlurImageFilter', 'itk::BinomialBlurImageFilter', 'itkBinomialBlurImageFilterIUS3IUS3', True, 'itk::Image< unsigned short,3 >, itk::Image< unsigned short,3 >'),
  ('BinomialBlurImageFilter', 'itk::BinomialBlurImageFilter', 'itkBinomialBlurImageFilterIF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >'),
  ('BinomialBlurImageFilter', 'itk::BinomialBlurImageFilter', 'itkBinomialBlurImageFilterIF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >'),
  ('BinomialBlurImageFilter', 'itk::BinomialBlurImageFilter', 'itkBinomialBlurImageFilterID2ID2', True, 'itk::Image< double,2 >, itk::Image< double,2 >'),
  ('BinomialBlurImageFilter', 'itk::BinomialBlurImageFilter', 'itkBinomialBlurImageFilterID3ID3', True, 'itk::Image< double,3 >, itk::Image< double,3 >'),
  ('DiscreteGaussianImageFilter', 'itk::DiscreteGaussianImageFilter', 'itkDiscreteGaussianImageFilterISS2ISS2', True, 'itk::Image< signed short,2 >, itk::Image< signed short,2 >'),
  ('DiscreteGaussianImageFilter', 'itk::DiscreteGaussianImageFilter', 'itkDiscreteGaussianImageFilterISS3ISS3', True, 'itk::Image< signed short,3 >, itk::Image< signed short,3 >'),
  ('DiscreteGaussianImageFilter', 'itk::DiscreteGaussianImageFilter', 'itkDiscreteGaussianImageFilterIUC2IUC2', True, 'itk::Image< unsigned char,2 >, itk::Image< unsigned char,2 >'),
  ('DiscreteGaussianImageFilter', 'itk::DiscreteGaussianImageFilter', 'itkDiscreteGaussianImageFilterIUC3IUC3', True, 'itk::Image< unsigned char,3 >, itk::Image< unsigned char,3 >'),
  ('DiscreteGaussianImageFilter', 'itk::DiscreteGaussianImageFilter', 'itkDiscreteGaussianImageFilterIUS2IUS2', True, 'itk::Image< unsigned short,2 >, itk::Image< unsigned short,2 >'),
  ('DiscreteGaussianImageFilter', 'itk::DiscreteGaussianImageFilter', 'itkDiscreteGaussianImageFilterIUS3IUS3', True, 'itk::Image< unsigned short,3 >, itk::Image< unsigned short,3 >'),
  ('DiscreteGaussianImageFilter', 'itk::DiscreteGaussianImageFilter', 'itkDiscreteGaussianImageFilterIF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >'),
  ('DiscreteGaussianImageFilter', 'itk::DiscreteGaussianImageFilter', 'itkDiscreteGaussianImageFilterIF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >'),
  ('DiscreteGaussianImageFilter', 'itk::DiscreteGaussianImageFilter', 'itkDiscreteGaussianImageFilterID2ID2', True, 'itk::Image< double,2 >, itk::Image< double,2 >'),
  ('DiscreteGaussianImageFilter', 'itk::DiscreteGaussianImageFilter', 'itkDiscreteGaussianImageFilterID3ID3', True, 'itk::Image< double,3 >, itk::Image< double,3 >'),
  ('MeanImageFilter', 'itk::MeanImageFilter', 'itkMeanImageFilterISS2ISS2', True, 'itk::Image< signed short,2 >, itk::Image< signed short,2 >'),
  ('MeanImageFilter', 'itk::MeanImageFilter', 'itkMeanImageFilterISS3ISS3', True, 'itk::Image< signed short,3 >, itk::Image< signed short,3 >'),
  ('MeanImageFilter', 'itk::MeanImageFilter', 'itkMeanImageFilterIUC2IUC2', True, 'itk::Image< unsigned char,2 >, itk::Image< unsigned char,2 >'),
  ('MeanImageFilter', 'itk::MeanImageFilter', 'itkMeanImageFilterIUC3IUC3', True, 'itk::Image< unsigned char,3 >, itk::Image< unsigned char,3 >'),
  ('MeanImageFilter', 'itk::MeanImageFilter', 'itkMeanImageFilterIUS2IUS2', True, 'itk::Image< unsigned short,2 >, itk::Image< unsigned short,2 >'),
  ('MeanImageFilter', 'itk::MeanImageFilter', 'itkMeanImageFilterIUS3IUS3', True, 'itk::Image< unsigned short,3 >, itk::Image< unsigned short,3 >'),
  ('MeanImageFilter', 'itk::MeanImageFilter', 'itkMeanImageFilterIF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >'),
  ('MeanImageFilter', 'itk::MeanImageFilter', 'itkMeanImageFilterIF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >'),
  ('MeanImageFilter', 'itk::MeanImageFilter', 'itkMeanImageFilterID2ID2', True, 'itk::Image< double,2 >, itk::Image< double,2 >'),
  ('MeanImageFilter', 'itk::MeanImageFilter', 'itkMeanImageFilterID3ID3', True, 'itk::Image< double,3 >, itk::Image< double,3 >'),
  ('MedianImageFilter', 'itk::MedianImageFilter', 'itkMedianImageFilterISS2ISS2', True, 'itk::Image< signed short,2 >, itk::Image< signed short,2 >'),
  ('MedianImageFilter', 'itk::MedianImageFilter', 'itkMedianImageFilterISS3ISS3', True, 'itk::Image< signed short,3 >, itk::Image< signed short,3 >'),
  ('MedianImageFilter', 'itk::MedianImageFilter', 'itkMedianImageFilterIUC2IUC2', True, 'itk::Image< unsigned char,2 >, itk::Image< unsigned char,2 >'),
  ('MedianImageFilter', 'itk::MedianImageFilter', 'itkMedianImageFilterIUC3IUC3', True, 'itk::Image< unsigned char,3 >, itk::Image< unsigned char,3 >'),
  ('MedianImageFilter', 'itk::MedianImageFilter', 'itkMedianImageFilterIUS2IUS2', True, 'itk::Image< unsigned short,2 >, itk::Image< unsigned short,2 >'),
  ('MedianImageFilter', 'itk::MedianImageFilter', 'itkMedianImageFilterIUS3IUS3', True, 'itk::Image< unsigned short,3 >, itk::Image< unsigned short,3 >'),
  ('MedianImageFilter', 'itk::MedianImageFilter', 'itkMedianImageFilterIF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >'),
  ('MedianImageFilter', 'itk::MedianImageFilter', 'itkMedianImageFilterIF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >'),
  ('MedianImageFilter', 'itk::MedianImageFilter', 'itkMedianImageFilterID2ID2', True, 'itk::Image< double,2 >, itk::Image< double,2 >'),
  ('MedianImageFilter', 'itk::MedianImageFilter', 'itkMedianImageFilterID3ID3', True, 'itk::Image< double,3 >, itk::Image< double,3 >'),
  ('RecursiveGaussianImageFilterEnums', 'itk::RecursiveGaussianImageFilterEnums', 'itkRecursiveGaussianImageFilterEnums', False),
  ('RecursiveGaussianImageFilter', 'itk::RecursiveGaussianImageFilter', 'itkRecursiveGaussianImageFilterISS2ISS2', True, 'itk::Image< signed short,2 >, itk::Image< signed short,2 >'),
  ('RecursiveGaussianImageFilter', 'itk::RecursiveGaussianImageFilter', 'itkRecursiveGaussianImageFilterISS3ISS3', True, 'itk::Image< signed short,3 >, itk::Image< signed short,3 >'),
  ('RecursiveGaussianImageFilter', 'itk::RecursiveGaussianImageFilter', 'itkRecursiveGaussianImageFilterIUC2IUC2', True, 'itk::Image< unsigned char,2 >, itk::Image< unsigned char,2 >'),
  ('RecursiveGaussianImageFilter', 'itk::RecursiveGaussianImageFilter', 'itkRecursiveGaussianImageFilterIUC3IUC3', True, 'itk::Image< unsigned char,3 >, itk::Image< unsigned char,3 >'),
  ('RecursiveGaussianImageFilter', 'itk::RecursiveGaussianImageFilter', 'itkRecursiveGaussianImageFilterIUS2IUS2', True, 'itk::Image< unsigned short,2 >, itk::Image< unsigned short,2 >'),
  ('RecursiveGaussianImageFilter', 'itk::RecursiveGaussianImageFilter', 'itkRecursiveGaussianImageFilterIUS3IUS3', True, 'itk::Image< unsigned short,3 >, itk::Image< unsigned short,3 >'),
  ('RecursiveGaussianImageFilter', 'itk::RecursiveGaussianImageFilter', 'itkRecursiveGaussianImageFilterIF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >'),
  ('RecursiveGaussianImageFilter', 'itk::RecursiveGaussianImageFilter', 'itkRecursiveGaussianImageFilterIF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >'),
  ('RecursiveGaussianImageFilter', 'itk::RecursiveGaussianImageFilter', 'itkRecursiveGaussianImageFilterID2ID2', True, 'itk::Image< double,2 >, itk::Image< double,2 >'),
  ('RecursiveGaussianImageFilter', 'itk::RecursiveGaussianImageFilter', 'itkRecursiveGaussianImageFilterID3ID3', True, 'itk::Image< double,3 >, itk::Image< double,3 >'),
  ('RecursiveGaussianImageFilterEnums', 'itk::RecursiveGaussianImageFilterEnums', 'itkRecursiveGaussianImageFilterEnums', False),
  ('SmoothingRecursiveGaussianImageFilter', 'itk::SmoothingRecursiveGaussianImageFilter', 'itkSmoothingRecursiveGaussianImageFilterISS2ISS2', True, 'itk::Image< signed short,2 >, itk::Image< signed short,2 >'),
  ('SmoothingRecursiveGaussianImageFilter', 'itk::SmoothingRecursiveGaussianImageFilter', 'itkSmoothingRecursiveGaussianImageFilterISS3ISS3', True, 'itk::Image< signed short,3 >, itk::Image< signed short,3 >'),
  ('SmoothingRecursiveGaussianImageFilter', 'itk::SmoothingRecursiveGaussianImageFilter', 'itkSmoothingRecursiveGaussianImageFilterIUC2IUC2', True, 'itk::Image< unsigned char,2 >, itk::Image< unsigned char,2 >'),
  ('SmoothingRecursiveGaussianImageFilter', 'itk::SmoothingRecursiveGaussianImageFilter', 'itkSmoothingRecursiveGaussianImageFilterIUC3IUC3', True, 'itk::Image< unsigned char,3 >, itk::Image< unsigned char,3 >'),
  ('SmoothingRecursiveGaussianImageFilter', 'itk::SmoothingRecursiveGaussianImageFilter', 'itkSmoothingRecursiveGaussianImageFilterIUS2IUS2', True, 'itk::Image< unsigned short,2 >, itk::Image< unsigned short,2 >'),
  ('SmoothingRecursiveGaussianImageFilter', 'itk::SmoothingRecursiveGaussianImageFilter', 'itkSmoothingRecursiveGaussianImageFilterIUS3IUS3', True, 'itk::Image< unsigned short,3 >, itk::Image< unsigned short,3 >'),
  ('SmoothingRecursiveGaussianImageFilter', 'itk::SmoothingRecursiveGaussianImageFilter', 'itkSmoothingRecursiveGaussianImageFilterIF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >'),
  ('SmoothingRecursiveGaussianImageFilter', 'itk::SmoothingRecursiveGaussianImageFilter', 'itkSmoothingRecursiveGaussianImageFilterIF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >'),
  ('SmoothingRecursiveGaussianImageFilter', 'itk::SmoothingRecursiveGaussianImageFilter', 'itkSmoothingRecursiveGaussianImageFilterID2ID2', True, 'itk::Image< double,2 >, itk::Image< double,2 >'),
  ('SmoothingRecursiveGaussianImageFilter', 'itk::SmoothingRecursiveGaussianImageFilter', 'itkSmoothingRecursiveGaussianImageFilterID3ID3', True, 'itk::Image< double,3 >, itk::Image< double,3 >'),
)
snake_case_functions = ('median_image_filter', 'binomial_blur_image_filter', 'recursive_gaussian_image_filter', 'smoothing_recursive_gaussian_image_filter', 'mean_image_filter', 'discrete_gaussian_image_filter', )
