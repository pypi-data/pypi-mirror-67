depends = ('ITKPyBase', 'ITKStatistics', 'ITKSpatialObjects', 'ITKSmoothing', 'ITKOptimizers', 'ITKImageIntensity', 'ITKImageGrid', 'ITKImageGradient', 'ITKImageFunction', 'ITKImageFeature', 'ITKFiniteDifference', 'ITKDisplacementField', )
templates = (
  ('BlockMatchingImageFilter', 'itk::BlockMatchingImageFilter', 'itkBlockMatchingImageFilterIF3', True, 'itk::Image< float,3 >'),
  ('BlockMatchingImageFilter', 'itk::BlockMatchingImageFilter', 'itkBlockMatchingImageFilterID3', True, 'itk::Image< double,3 >'),
  ('PointSet', 'itk::PointSet', 'itkPointSetVF33DTVF333FFVF3', False, 'itk::Vector< float, 3 >, 3, itk::DefaultStaticMeshTraits< itk::Vector< float, 3 >, 3, 3, float, float, itk::Vector< float, 3 > >'),
  ('PointSet', 'itk::PointSet', 'itkPointSetD3DTD33FFD', False, 'double, 3, itk::DefaultStaticMeshTraits< double, 3, 3, float, float, double >'),
  ('CenteredTransformInitializer', 'itk::CenteredTransformInitializer', 'itkCenteredTransformInitializerVR3DTDISS3ISS3', True, 'itk::VersorRigid3DTransform< double >,itk::Image< signed short,3 >,itk::Image< signed short,3 >'),
  ('CenteredTransformInitializer', 'itk::CenteredTransformInitializer', 'itkCenteredTransformInitializerVR3DTDIUC3IUC3', True, 'itk::VersorRigid3DTransform< double >,itk::Image< unsigned char,3 >,itk::Image< unsigned char,3 >'),
  ('CenteredTransformInitializer', 'itk::CenteredTransformInitializer', 'itkCenteredTransformInitializerVR3DTDIUS3IUS3', True, 'itk::VersorRigid3DTransform< double >,itk::Image< unsigned short,3 >,itk::Image< unsigned short,3 >'),
  ('CenteredTransformInitializer', 'itk::CenteredTransformInitializer', 'itkCenteredTransformInitializerVR3DTDIF3IF3', True, 'itk::VersorRigid3DTransform< double >,itk::Image< float,3 >,itk::Image< float,3 >'),
  ('CenteredTransformInitializer', 'itk::CenteredTransformInitializer', 'itkCenteredTransformInitializerVR3DTDID3ID3', True, 'itk::VersorRigid3DTransform< double >,itk::Image< double,3 >,itk::Image< double,3 >'),
  ('CenteredTransformInitializer', 'itk::CenteredTransformInitializer', 'itkCenteredTransformInitializerCR2DTDISS2ISS2', True, 'itk::CenteredRigid2DTransform< double >,itk::Image< signed short,2 >,itk::Image< signed short,2 >'),
  ('CenteredTransformInitializer', 'itk::CenteredTransformInitializer', 'itkCenteredTransformInitializerCR2DTDIUC2IUC2', True, 'itk::CenteredRigid2DTransform< double >,itk::Image< unsigned char,2 >,itk::Image< unsigned char,2 >'),
  ('CenteredTransformInitializer', 'itk::CenteredTransformInitializer', 'itkCenteredTransformInitializerCR2DTDIUS2IUS2', True, 'itk::CenteredRigid2DTransform< double >,itk::Image< unsigned short,2 >,itk::Image< unsigned short,2 >'),
  ('CenteredTransformInitializer', 'itk::CenteredTransformInitializer', 'itkCenteredTransformInitializerCR2DTDIF2IF2', True, 'itk::CenteredRigid2DTransform< double >,itk::Image< float,2 >,itk::Image< float,2 >'),
  ('CenteredTransformInitializer', 'itk::CenteredTransformInitializer', 'itkCenteredTransformInitializerCR2DTDID2ID2', True, 'itk::CenteredRigid2DTransform< double >,itk::Image< double,2 >,itk::Image< double,2 >'),
  ('CenteredVersorTransformInitializer', 'itk::CenteredVersorTransformInitializer', 'itkCenteredVersorTransformInitializerISS3ISS3', True, 'itk::Image< signed short,3 >, itk::Image< signed short,3 >'),
  ('CenteredVersorTransformInitializer', 'itk::CenteredVersorTransformInitializer', 'itkCenteredVersorTransformInitializerIUC3IUC3', True, 'itk::Image< unsigned char,3 >, itk::Image< unsigned char,3 >'),
  ('CenteredVersorTransformInitializer', 'itk::CenteredVersorTransformInitializer', 'itkCenteredVersorTransformInitializerIUS3IUS3', True, 'itk::Image< unsigned short,3 >, itk::Image< unsigned short,3 >'),
  ('CenteredVersorTransformInitializer', 'itk::CenteredVersorTransformInitializer', 'itkCenteredVersorTransformInitializerIF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >'),
  ('CenteredVersorTransformInitializer', 'itk::CenteredVersorTransformInitializer', 'itkCenteredVersorTransformInitializerID3ID3', True, 'itk::Image< double,3 >, itk::Image< double,3 >'),
  ('ImageRegistrationMethod', 'itk::ImageRegistrationMethod', 'itkImageRegistrationMethodISS2ISS2', True, 'itk::Image< signed short,2 >, itk::Image< signed short,2 >'),
  ('ImageRegistrationMethod', 'itk::ImageRegistrationMethod', 'itkImageRegistrationMethodISS3ISS3', True, 'itk::Image< signed short,3 >, itk::Image< signed short,3 >'),
  ('ImageRegistrationMethod', 'itk::ImageRegistrationMethod', 'itkImageRegistrationMethodIUC2IUC2', True, 'itk::Image< unsigned char,2 >, itk::Image< unsigned char,2 >'),
  ('ImageRegistrationMethod', 'itk::ImageRegistrationMethod', 'itkImageRegistrationMethodIUC3IUC3', True, 'itk::Image< unsigned char,3 >, itk::Image< unsigned char,3 >'),
  ('ImageRegistrationMethod', 'itk::ImageRegistrationMethod', 'itkImageRegistrationMethodIUS2IUS2', True, 'itk::Image< unsigned short,2 >, itk::Image< unsigned short,2 >'),
  ('ImageRegistrationMethod', 'itk::ImageRegistrationMethod', 'itkImageRegistrationMethodIUS3IUS3', True, 'itk::Image< unsigned short,3 >, itk::Image< unsigned short,3 >'),
  ('ImageRegistrationMethod', 'itk::ImageRegistrationMethod', 'itkImageRegistrationMethodIF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >'),
  ('ImageRegistrationMethod', 'itk::ImageRegistrationMethod', 'itkImageRegistrationMethodIF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >'),
  ('ImageRegistrationMethod', 'itk::ImageRegistrationMethod', 'itkImageRegistrationMethodID2ID2', True, 'itk::Image< double,2 >, itk::Image< double,2 >'),
  ('ImageRegistrationMethod', 'itk::ImageRegistrationMethod', 'itkImageRegistrationMethodID3ID3', True, 'itk::Image< double,3 >, itk::Image< double,3 >'),
  ('ImageToImageMetric', 'itk::ImageToImageMetric', 'itkImageToImageMetricISS2ISS2', True, 'itk::Image< signed short,2 >, itk::Image< signed short,2 >'),
  ('ImageToImageMetric', 'itk::ImageToImageMetric', 'itkImageToImageMetricISS3ISS3', True, 'itk::Image< signed short,3 >, itk::Image< signed short,3 >'),
  ('ImageToImageMetric', 'itk::ImageToImageMetric', 'itkImageToImageMetricIUC2IUC2', True, 'itk::Image< unsigned char,2 >, itk::Image< unsigned char,2 >'),
  ('ImageToImageMetric', 'itk::ImageToImageMetric', 'itkImageToImageMetricIUC3IUC3', True, 'itk::Image< unsigned char,3 >, itk::Image< unsigned char,3 >'),
  ('ImageToImageMetric', 'itk::ImageToImageMetric', 'itkImageToImageMetricIUS2IUS2', True, 'itk::Image< unsigned short,2 >, itk::Image< unsigned short,2 >'),
  ('ImageToImageMetric', 'itk::ImageToImageMetric', 'itkImageToImageMetricIUS3IUS3', True, 'itk::Image< unsigned short,3 >, itk::Image< unsigned short,3 >'),
  ('ImageToImageMetric', 'itk::ImageToImageMetric', 'itkImageToImageMetricIF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >'),
  ('ImageToImageMetric', 'itk::ImageToImageMetric', 'itkImageToImageMetricIF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >'),
  ('ImageToImageMetric', 'itk::ImageToImageMetric', 'itkImageToImageMetricID2ID2', True, 'itk::Image< double,2 >, itk::Image< double,2 >'),
  ('ImageToImageMetric', 'itk::ImageToImageMetric', 'itkImageToImageMetricID3ID3', True, 'itk::Image< double,3 >, itk::Image< double,3 >'),
  ('LandmarkBasedTransformInitializer', 'itk::LandmarkBasedTransformInitializer', 'itkLandmarkBasedTransformInitializerTD22', True, 'itk::Transform<double,2,2>'),
  ('LandmarkBasedTransformInitializer', 'itk::LandmarkBasedTransformInitializer', 'itkLandmarkBasedTransformInitializerTF22', True, 'itk::Transform<float,2,2>'),
  ('LandmarkBasedTransformInitializer', 'itk::LandmarkBasedTransformInitializer', 'itkLandmarkBasedTransformInitializerTD33', True, 'itk::Transform<double,3,3>'),
  ('LandmarkBasedTransformInitializer', 'itk::LandmarkBasedTransformInitializer', 'itkLandmarkBasedTransformInitializerTF33', True, 'itk::Transform<float,3,3>'),
  ('MattesMutualInformationImageToImageMetric', 'itk::MattesMutualInformationImageToImageMetric', 'itkMattesMutualInformationImageToImageMetricISS2ISS2', True, 'itk::Image< signed short,2 >, itk::Image< signed short,2 >'),
  ('MattesMutualInformationImageToImageMetric', 'itk::MattesMutualInformationImageToImageMetric', 'itkMattesMutualInformationImageToImageMetricISS3ISS3', True, 'itk::Image< signed short,3 >, itk::Image< signed short,3 >'),
  ('MattesMutualInformationImageToImageMetric', 'itk::MattesMutualInformationImageToImageMetric', 'itkMattesMutualInformationImageToImageMetricIUC2IUC2', True, 'itk::Image< unsigned char,2 >, itk::Image< unsigned char,2 >'),
  ('MattesMutualInformationImageToImageMetric', 'itk::MattesMutualInformationImageToImageMetric', 'itkMattesMutualInformationImageToImageMetricIUC3IUC3', True, 'itk::Image< unsigned char,3 >, itk::Image< unsigned char,3 >'),
  ('MattesMutualInformationImageToImageMetric', 'itk::MattesMutualInformationImageToImageMetric', 'itkMattesMutualInformationImageToImageMetricIUS2IUS2', True, 'itk::Image< unsigned short,2 >, itk::Image< unsigned short,2 >'),
  ('MattesMutualInformationImageToImageMetric', 'itk::MattesMutualInformationImageToImageMetric', 'itkMattesMutualInformationImageToImageMetricIUS3IUS3', True, 'itk::Image< unsigned short,3 >, itk::Image< unsigned short,3 >'),
  ('MattesMutualInformationImageToImageMetric', 'itk::MattesMutualInformationImageToImageMetric', 'itkMattesMutualInformationImageToImageMetricIF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >'),
  ('MattesMutualInformationImageToImageMetric', 'itk::MattesMutualInformationImageToImageMetric', 'itkMattesMutualInformationImageToImageMetricIF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >'),
  ('MattesMutualInformationImageToImageMetric', 'itk::MattesMutualInformationImageToImageMetric', 'itkMattesMutualInformationImageToImageMetricID2ID2', True, 'itk::Image< double,2 >, itk::Image< double,2 >'),
  ('MattesMutualInformationImageToImageMetric', 'itk::MattesMutualInformationImageToImageMetric', 'itkMattesMutualInformationImageToImageMetricID3ID3', True, 'itk::Image< double,3 >, itk::Image< double,3 >'),
  ('MeanReciprocalSquareDifferenceImageToImageMetric', 'itk::MeanReciprocalSquareDifferenceImageToImageMetric', 'itkMeanReciprocalSquareDifferenceImageToImageMetricISS2ISS2', True, 'itk::Image< signed short,2 >, itk::Image< signed short,2 >'),
  ('MeanReciprocalSquareDifferenceImageToImageMetric', 'itk::MeanReciprocalSquareDifferenceImageToImageMetric', 'itkMeanReciprocalSquareDifferenceImageToImageMetricISS3ISS3', True, 'itk::Image< signed short,3 >, itk::Image< signed short,3 >'),
  ('MeanReciprocalSquareDifferenceImageToImageMetric', 'itk::MeanReciprocalSquareDifferenceImageToImageMetric', 'itkMeanReciprocalSquareDifferenceImageToImageMetricIUC2IUC2', True, 'itk::Image< unsigned char,2 >, itk::Image< unsigned char,2 >'),
  ('MeanReciprocalSquareDifferenceImageToImageMetric', 'itk::MeanReciprocalSquareDifferenceImageToImageMetric', 'itkMeanReciprocalSquareDifferenceImageToImageMetricIUC3IUC3', True, 'itk::Image< unsigned char,3 >, itk::Image< unsigned char,3 >'),
  ('MeanReciprocalSquareDifferenceImageToImageMetric', 'itk::MeanReciprocalSquareDifferenceImageToImageMetric', 'itkMeanReciprocalSquareDifferenceImageToImageMetricIUS2IUS2', True, 'itk::Image< unsigned short,2 >, itk::Image< unsigned short,2 >'),
  ('MeanReciprocalSquareDifferenceImageToImageMetric', 'itk::MeanReciprocalSquareDifferenceImageToImageMetric', 'itkMeanReciprocalSquareDifferenceImageToImageMetricIUS3IUS3', True, 'itk::Image< unsigned short,3 >, itk::Image< unsigned short,3 >'),
  ('MeanReciprocalSquareDifferenceImageToImageMetric', 'itk::MeanReciprocalSquareDifferenceImageToImageMetric', 'itkMeanReciprocalSquareDifferenceImageToImageMetricIF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >'),
  ('MeanReciprocalSquareDifferenceImageToImageMetric', 'itk::MeanReciprocalSquareDifferenceImageToImageMetric', 'itkMeanReciprocalSquareDifferenceImageToImageMetricIF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >'),
  ('MeanReciprocalSquareDifferenceImageToImageMetric', 'itk::MeanReciprocalSquareDifferenceImageToImageMetric', 'itkMeanReciprocalSquareDifferenceImageToImageMetricID2ID2', True, 'itk::Image< double,2 >, itk::Image< double,2 >'),
  ('MeanReciprocalSquareDifferenceImageToImageMetric', 'itk::MeanReciprocalSquareDifferenceImageToImageMetric', 'itkMeanReciprocalSquareDifferenceImageToImageMetricID3ID3', True, 'itk::Image< double,3 >, itk::Image< double,3 >'),
  ('MeanSquaresImageToImageMetric', 'itk::MeanSquaresImageToImageMetric', 'itkMeanSquaresImageToImageMetricISS2ISS2', True, 'itk::Image< signed short,2 >, itk::Image< signed short,2 >'),
  ('MeanSquaresImageToImageMetric', 'itk::MeanSquaresImageToImageMetric', 'itkMeanSquaresImageToImageMetricISS3ISS3', True, 'itk::Image< signed short,3 >, itk::Image< signed short,3 >'),
  ('MeanSquaresImageToImageMetric', 'itk::MeanSquaresImageToImageMetric', 'itkMeanSquaresImageToImageMetricIUC2IUC2', True, 'itk::Image< unsigned char,2 >, itk::Image< unsigned char,2 >'),
  ('MeanSquaresImageToImageMetric', 'itk::MeanSquaresImageToImageMetric', 'itkMeanSquaresImageToImageMetricIUC3IUC3', True, 'itk::Image< unsigned char,3 >, itk::Image< unsigned char,3 >'),
  ('MeanSquaresImageToImageMetric', 'itk::MeanSquaresImageToImageMetric', 'itkMeanSquaresImageToImageMetricIUS2IUS2', True, 'itk::Image< unsigned short,2 >, itk::Image< unsigned short,2 >'),
  ('MeanSquaresImageToImageMetric', 'itk::MeanSquaresImageToImageMetric', 'itkMeanSquaresImageToImageMetricIUS3IUS3', True, 'itk::Image< unsigned short,3 >, itk::Image< unsigned short,3 >'),
  ('MeanSquaresImageToImageMetric', 'itk::MeanSquaresImageToImageMetric', 'itkMeanSquaresImageToImageMetricIF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >'),
  ('MeanSquaresImageToImageMetric', 'itk::MeanSquaresImageToImageMetric', 'itkMeanSquaresImageToImageMetricIF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >'),
  ('MeanSquaresImageToImageMetric', 'itk::MeanSquaresImageToImageMetric', 'itkMeanSquaresImageToImageMetricID2ID2', True, 'itk::Image< double,2 >, itk::Image< double,2 >'),
  ('MeanSquaresImageToImageMetric', 'itk::MeanSquaresImageToImageMetric', 'itkMeanSquaresImageToImageMetricID3ID3', True, 'itk::Image< double,3 >, itk::Image< double,3 >'),
  ('MultiResolutionImageRegistrationMethod', 'itk::MultiResolutionImageRegistrationMethod', 'itkMultiResolutionImageRegistrationMethodISS2ISS2', True, 'itk::Image< signed short,2 >, itk::Image< signed short,2 >'),
  ('MultiResolutionImageRegistrationMethod', 'itk::MultiResolutionImageRegistrationMethod', 'itkMultiResolutionImageRegistrationMethodISS3ISS3', True, 'itk::Image< signed short,3 >, itk::Image< signed short,3 >'),
  ('MultiResolutionImageRegistrationMethod', 'itk::MultiResolutionImageRegistrationMethod', 'itkMultiResolutionImageRegistrationMethodIUC2IUC2', True, 'itk::Image< unsigned char,2 >, itk::Image< unsigned char,2 >'),
  ('MultiResolutionImageRegistrationMethod', 'itk::MultiResolutionImageRegistrationMethod', 'itkMultiResolutionImageRegistrationMethodIUC3IUC3', True, 'itk::Image< unsigned char,3 >, itk::Image< unsigned char,3 >'),
  ('MultiResolutionImageRegistrationMethod', 'itk::MultiResolutionImageRegistrationMethod', 'itkMultiResolutionImageRegistrationMethodIUS2IUS2', True, 'itk::Image< unsigned short,2 >, itk::Image< unsigned short,2 >'),
  ('MultiResolutionImageRegistrationMethod', 'itk::MultiResolutionImageRegistrationMethod', 'itkMultiResolutionImageRegistrationMethodIUS3IUS3', True, 'itk::Image< unsigned short,3 >, itk::Image< unsigned short,3 >'),
  ('MultiResolutionImageRegistrationMethod', 'itk::MultiResolutionImageRegistrationMethod', 'itkMultiResolutionImageRegistrationMethodIF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >'),
  ('MultiResolutionImageRegistrationMethod', 'itk::MultiResolutionImageRegistrationMethod', 'itkMultiResolutionImageRegistrationMethodIF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >'),
  ('MultiResolutionImageRegistrationMethod', 'itk::MultiResolutionImageRegistrationMethod', 'itkMultiResolutionImageRegistrationMethodID2ID2', True, 'itk::Image< double,2 >, itk::Image< double,2 >'),
  ('MultiResolutionImageRegistrationMethod', 'itk::MultiResolutionImageRegistrationMethod', 'itkMultiResolutionImageRegistrationMethodID3ID3', True, 'itk::Image< double,3 >, itk::Image< double,3 >'),
  ('MultiResolutionPyramidImageFilter', 'itk::MultiResolutionPyramidImageFilter', 'itkMultiResolutionPyramidImageFilterISS2ISS2', True, 'itk::Image< signed short,2 >, itk::Image< signed short,2 >'),
  ('MultiResolutionPyramidImageFilter', 'itk::MultiResolutionPyramidImageFilter', 'itkMultiResolutionPyramidImageFilterISS3ISS3', True, 'itk::Image< signed short,3 >, itk::Image< signed short,3 >'),
  ('MultiResolutionPyramidImageFilter', 'itk::MultiResolutionPyramidImageFilter', 'itkMultiResolutionPyramidImageFilterIUC2IUC2', True, 'itk::Image< unsigned char,2 >, itk::Image< unsigned char,2 >'),
  ('MultiResolutionPyramidImageFilter', 'itk::MultiResolutionPyramidImageFilter', 'itkMultiResolutionPyramidImageFilterIUC3IUC3', True, 'itk::Image< unsigned char,3 >, itk::Image< unsigned char,3 >'),
  ('MultiResolutionPyramidImageFilter', 'itk::MultiResolutionPyramidImageFilter', 'itkMultiResolutionPyramidImageFilterIUS2IUS2', True, 'itk::Image< unsigned short,2 >, itk::Image< unsigned short,2 >'),
  ('MultiResolutionPyramidImageFilter', 'itk::MultiResolutionPyramidImageFilter', 'itkMultiResolutionPyramidImageFilterIUS3IUS3', True, 'itk::Image< unsigned short,3 >, itk::Image< unsigned short,3 >'),
  ('MultiResolutionPyramidImageFilter', 'itk::MultiResolutionPyramidImageFilter', 'itkMultiResolutionPyramidImageFilterIF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >'),
  ('MultiResolutionPyramidImageFilter', 'itk::MultiResolutionPyramidImageFilter', 'itkMultiResolutionPyramidImageFilterIF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >'),
  ('MultiResolutionPyramidImageFilter', 'itk::MultiResolutionPyramidImageFilter', 'itkMultiResolutionPyramidImageFilterID2ID2', True, 'itk::Image< double,2 >, itk::Image< double,2 >'),
  ('MultiResolutionPyramidImageFilter', 'itk::MultiResolutionPyramidImageFilter', 'itkMultiResolutionPyramidImageFilterID3ID3', True, 'itk::Image< double,3 >, itk::Image< double,3 >'),
  ('MutualInformationImageToImageMetric', 'itk::MutualInformationImageToImageMetric', 'itkMutualInformationImageToImageMetricISS2ISS2', True, 'itk::Image< signed short,2 >, itk::Image< signed short,2 >'),
  ('MutualInformationImageToImageMetric', 'itk::MutualInformationImageToImageMetric', 'itkMutualInformationImageToImageMetricISS3ISS3', True, 'itk::Image< signed short,3 >, itk::Image< signed short,3 >'),
  ('MutualInformationImageToImageMetric', 'itk::MutualInformationImageToImageMetric', 'itkMutualInformationImageToImageMetricIUC2IUC2', True, 'itk::Image< unsigned char,2 >, itk::Image< unsigned char,2 >'),
  ('MutualInformationImageToImageMetric', 'itk::MutualInformationImageToImageMetric', 'itkMutualInformationImageToImageMetricIUC3IUC3', True, 'itk::Image< unsigned char,3 >, itk::Image< unsigned char,3 >'),
  ('MutualInformationImageToImageMetric', 'itk::MutualInformationImageToImageMetric', 'itkMutualInformationImageToImageMetricIUS2IUS2', True, 'itk::Image< unsigned short,2 >, itk::Image< unsigned short,2 >'),
  ('MutualInformationImageToImageMetric', 'itk::MutualInformationImageToImageMetric', 'itkMutualInformationImageToImageMetricIUS3IUS3', True, 'itk::Image< unsigned short,3 >, itk::Image< unsigned short,3 >'),
  ('MutualInformationImageToImageMetric', 'itk::MutualInformationImageToImageMetric', 'itkMutualInformationImageToImageMetricIF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >'),
  ('MutualInformationImageToImageMetric', 'itk::MutualInformationImageToImageMetric', 'itkMutualInformationImageToImageMetricIF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >'),
  ('MutualInformationImageToImageMetric', 'itk::MutualInformationImageToImageMetric', 'itkMutualInformationImageToImageMetricID2ID2', True, 'itk::Image< double,2 >, itk::Image< double,2 >'),
  ('MutualInformationImageToImageMetric', 'itk::MutualInformationImageToImageMetric', 'itkMutualInformationImageToImageMetricID3ID3', True, 'itk::Image< double,3 >, itk::Image< double,3 >'),
  ('NormalizedCorrelationImageToImageMetric', 'itk::NormalizedCorrelationImageToImageMetric', 'itkNormalizedCorrelationImageToImageMetricISS2ISS2', True, 'itk::Image< signed short,2 >, itk::Image< signed short,2 >'),
  ('NormalizedCorrelationImageToImageMetric', 'itk::NormalizedCorrelationImageToImageMetric', 'itkNormalizedCorrelationImageToImageMetricISS3ISS3', True, 'itk::Image< signed short,3 >, itk::Image< signed short,3 >'),
  ('NormalizedCorrelationImageToImageMetric', 'itk::NormalizedCorrelationImageToImageMetric', 'itkNormalizedCorrelationImageToImageMetricIUC2IUC2', True, 'itk::Image< unsigned char,2 >, itk::Image< unsigned char,2 >'),
  ('NormalizedCorrelationImageToImageMetric', 'itk::NormalizedCorrelationImageToImageMetric', 'itkNormalizedCorrelationImageToImageMetricIUC3IUC3', True, 'itk::Image< unsigned char,3 >, itk::Image< unsigned char,3 >'),
  ('NormalizedCorrelationImageToImageMetric', 'itk::NormalizedCorrelationImageToImageMetric', 'itkNormalizedCorrelationImageToImageMetricIUS2IUS2', True, 'itk::Image< unsigned short,2 >, itk::Image< unsigned short,2 >'),
  ('NormalizedCorrelationImageToImageMetric', 'itk::NormalizedCorrelationImageToImageMetric', 'itkNormalizedCorrelationImageToImageMetricIUS3IUS3', True, 'itk::Image< unsigned short,3 >, itk::Image< unsigned short,3 >'),
  ('NormalizedCorrelationImageToImageMetric', 'itk::NormalizedCorrelationImageToImageMetric', 'itkNormalizedCorrelationImageToImageMetricIF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >'),
  ('NormalizedCorrelationImageToImageMetric', 'itk::NormalizedCorrelationImageToImageMetric', 'itkNormalizedCorrelationImageToImageMetricIF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >'),
  ('NormalizedCorrelationImageToImageMetric', 'itk::NormalizedCorrelationImageToImageMetric', 'itkNormalizedCorrelationImageToImageMetricID2ID2', True, 'itk::Image< double,2 >, itk::Image< double,2 >'),
  ('NormalizedCorrelationImageToImageMetric', 'itk::NormalizedCorrelationImageToImageMetric', 'itkNormalizedCorrelationImageToImageMetricID3ID3', True, 'itk::Image< double,3 >, itk::Image< double,3 >'),
  ('PDEDeformableRegistrationFunction', 'itk::PDEDeformableRegistrationFunction', 'itkPDEDeformableRegistrationFunctionISS2ISS2IVF22', True, 'itk::Image< signed short,2 >, itk::Image< signed short,2 >, itk::Image< itk::Vector< float,2 >,2 >'),
  ('PDEDeformableRegistrationFunction', 'itk::PDEDeformableRegistrationFunction', 'itkPDEDeformableRegistrationFunctionISS3ISS3IVF23', True, 'itk::Image< signed short,3 >, itk::Image< signed short,3 >, itk::Image< itk::Vector< float,2 >,3 >'),
  ('PDEDeformableRegistrationFunction', 'itk::PDEDeformableRegistrationFunction', 'itkPDEDeformableRegistrationFunctionISS2ISS2IVF32', True, 'itk::Image< signed short,2 >, itk::Image< signed short,2 >, itk::Image< itk::Vector< float,3 >,2 >'),
  ('PDEDeformableRegistrationFunction', 'itk::PDEDeformableRegistrationFunction', 'itkPDEDeformableRegistrationFunctionISS3ISS3IVF33', True, 'itk::Image< signed short,3 >, itk::Image< signed short,3 >, itk::Image< itk::Vector< float,3 >,3 >'),
  ('PDEDeformableRegistrationFunction', 'itk::PDEDeformableRegistrationFunction', 'itkPDEDeformableRegistrationFunctionISS2ISS2IVF42', True, 'itk::Image< signed short,2 >, itk::Image< signed short,2 >, itk::Image< itk::Vector< float,4 >,2 >'),
  ('PDEDeformableRegistrationFunction', 'itk::PDEDeformableRegistrationFunction', 'itkPDEDeformableRegistrationFunctionISS3ISS3IVF43', True, 'itk::Image< signed short,3 >, itk::Image< signed short,3 >, itk::Image< itk::Vector< float,4 >,3 >'),
  ('PDEDeformableRegistrationFunction', 'itk::PDEDeformableRegistrationFunction', 'itkPDEDeformableRegistrationFunctionIUC2IUC2IVF22', True, 'itk::Image< unsigned char,2 >, itk::Image< unsigned char,2 >, itk::Image< itk::Vector< float,2 >,2 >'),
  ('PDEDeformableRegistrationFunction', 'itk::PDEDeformableRegistrationFunction', 'itkPDEDeformableRegistrationFunctionIUC3IUC3IVF23', True, 'itk::Image< unsigned char,3 >, itk::Image< unsigned char,3 >, itk::Image< itk::Vector< float,2 >,3 >'),
  ('PDEDeformableRegistrationFunction', 'itk::PDEDeformableRegistrationFunction', 'itkPDEDeformableRegistrationFunctionIUC2IUC2IVF32', True, 'itk::Image< unsigned char,2 >, itk::Image< unsigned char,2 >, itk::Image< itk::Vector< float,3 >,2 >'),
  ('PDEDeformableRegistrationFunction', 'itk::PDEDeformableRegistrationFunction', 'itkPDEDeformableRegistrationFunctionIUC3IUC3IVF33', True, 'itk::Image< unsigned char,3 >, itk::Image< unsigned char,3 >, itk::Image< itk::Vector< float,3 >,3 >'),
  ('PDEDeformableRegistrationFunction', 'itk::PDEDeformableRegistrationFunction', 'itkPDEDeformableRegistrationFunctionIUC2IUC2IVF42', True, 'itk::Image< unsigned char,2 >, itk::Image< unsigned char,2 >, itk::Image< itk::Vector< float,4 >,2 >'),
  ('PDEDeformableRegistrationFunction', 'itk::PDEDeformableRegistrationFunction', 'itkPDEDeformableRegistrationFunctionIUC3IUC3IVF43', True, 'itk::Image< unsigned char,3 >, itk::Image< unsigned char,3 >, itk::Image< itk::Vector< float,4 >,3 >'),
  ('PDEDeformableRegistrationFunction', 'itk::PDEDeformableRegistrationFunction', 'itkPDEDeformableRegistrationFunctionIUS2IUS2IVF22', True, 'itk::Image< unsigned short,2 >, itk::Image< unsigned short,2 >, itk::Image< itk::Vector< float,2 >,2 >'),
  ('PDEDeformableRegistrationFunction', 'itk::PDEDeformableRegistrationFunction', 'itkPDEDeformableRegistrationFunctionIUS3IUS3IVF23', True, 'itk::Image< unsigned short,3 >, itk::Image< unsigned short,3 >, itk::Image< itk::Vector< float,2 >,3 >'),
  ('PDEDeformableRegistrationFunction', 'itk::PDEDeformableRegistrationFunction', 'itkPDEDeformableRegistrationFunctionIUS2IUS2IVF32', True, 'itk::Image< unsigned short,2 >, itk::Image< unsigned short,2 >, itk::Image< itk::Vector< float,3 >,2 >'),
  ('PDEDeformableRegistrationFunction', 'itk::PDEDeformableRegistrationFunction', 'itkPDEDeformableRegistrationFunctionIUS3IUS3IVF33', True, 'itk::Image< unsigned short,3 >, itk::Image< unsigned short,3 >, itk::Image< itk::Vector< float,3 >,3 >'),
  ('PDEDeformableRegistrationFunction', 'itk::PDEDeformableRegistrationFunction', 'itkPDEDeformableRegistrationFunctionIUS2IUS2IVF42', True, 'itk::Image< unsigned short,2 >, itk::Image< unsigned short,2 >, itk::Image< itk::Vector< float,4 >,2 >'),
  ('PDEDeformableRegistrationFunction', 'itk::PDEDeformableRegistrationFunction', 'itkPDEDeformableRegistrationFunctionIUS3IUS3IVF43', True, 'itk::Image< unsigned short,3 >, itk::Image< unsigned short,3 >, itk::Image< itk::Vector< float,4 >,3 >'),
  ('PDEDeformableRegistrationFunction', 'itk::PDEDeformableRegistrationFunction', 'itkPDEDeformableRegistrationFunctionIF2IF2IVF22', True, 'itk::Image< float,2 >, itk::Image< float,2 >, itk::Image< itk::Vector< float,2 >,2 >'),
  ('PDEDeformableRegistrationFunction', 'itk::PDEDeformableRegistrationFunction', 'itkPDEDeformableRegistrationFunctionIF3IF3IVF23', True, 'itk::Image< float,3 >, itk::Image< float,3 >, itk::Image< itk::Vector< float,2 >,3 >'),
  ('PDEDeformableRegistrationFunction', 'itk::PDEDeformableRegistrationFunction', 'itkPDEDeformableRegistrationFunctionIF2IF2IVF32', True, 'itk::Image< float,2 >, itk::Image< float,2 >, itk::Image< itk::Vector< float,3 >,2 >'),
  ('PDEDeformableRegistrationFunction', 'itk::PDEDeformableRegistrationFunction', 'itkPDEDeformableRegistrationFunctionIF3IF3IVF33', True, 'itk::Image< float,3 >, itk::Image< float,3 >, itk::Image< itk::Vector< float,3 >,3 >'),
  ('PDEDeformableRegistrationFunction', 'itk::PDEDeformableRegistrationFunction', 'itkPDEDeformableRegistrationFunctionIF2IF2IVF42', True, 'itk::Image< float,2 >, itk::Image< float,2 >, itk::Image< itk::Vector< float,4 >,2 >'),
  ('PDEDeformableRegistrationFunction', 'itk::PDEDeformableRegistrationFunction', 'itkPDEDeformableRegistrationFunctionIF3IF3IVF43', True, 'itk::Image< float,3 >, itk::Image< float,3 >, itk::Image< itk::Vector< float,4 >,3 >'),
  ('PDEDeformableRegistrationFunction', 'itk::PDEDeformableRegistrationFunction', 'itkPDEDeformableRegistrationFunctionID2ID2IVF22', True, 'itk::Image< double,2 >, itk::Image< double,2 >, itk::Image< itk::Vector< float,2 >,2 >'),
  ('PDEDeformableRegistrationFunction', 'itk::PDEDeformableRegistrationFunction', 'itkPDEDeformableRegistrationFunctionID3ID3IVF23', True, 'itk::Image< double,3 >, itk::Image< double,3 >, itk::Image< itk::Vector< float,2 >,3 >'),
  ('PDEDeformableRegistrationFunction', 'itk::PDEDeformableRegistrationFunction', 'itkPDEDeformableRegistrationFunctionID2ID2IVF32', True, 'itk::Image< double,2 >, itk::Image< double,2 >, itk::Image< itk::Vector< float,3 >,2 >'),
  ('PDEDeformableRegistrationFunction', 'itk::PDEDeformableRegistrationFunction', 'itkPDEDeformableRegistrationFunctionID3ID3IVF33', True, 'itk::Image< double,3 >, itk::Image< double,3 >, itk::Image< itk::Vector< float,3 >,3 >'),
  ('PDEDeformableRegistrationFunction', 'itk::PDEDeformableRegistrationFunction', 'itkPDEDeformableRegistrationFunctionID2ID2IVF42', True, 'itk::Image< double,2 >, itk::Image< double,2 >, itk::Image< itk::Vector< float,4 >,2 >'),
  ('PDEDeformableRegistrationFunction', 'itk::PDEDeformableRegistrationFunction', 'itkPDEDeformableRegistrationFunctionID3ID3IVF43', True, 'itk::Image< double,3 >, itk::Image< double,3 >, itk::Image< itk::Vector< float,4 >,3 >'),
  ('RecursiveMultiResolutionPyramidImageFilter', 'itk::RecursiveMultiResolutionPyramidImageFilter', 'itkRecursiveMultiResolutionPyramidImageFilterISS2ISS2', True, 'itk::Image< signed short,2 >, itk::Image< signed short,2 >'),
  ('RecursiveMultiResolutionPyramidImageFilter', 'itk::RecursiveMultiResolutionPyramidImageFilter', 'itkRecursiveMultiResolutionPyramidImageFilterISS3ISS3', True, 'itk::Image< signed short,3 >, itk::Image< signed short,3 >'),
  ('RecursiveMultiResolutionPyramidImageFilter', 'itk::RecursiveMultiResolutionPyramidImageFilter', 'itkRecursiveMultiResolutionPyramidImageFilterIUC2IUC2', True, 'itk::Image< unsigned char,2 >, itk::Image< unsigned char,2 >'),
  ('RecursiveMultiResolutionPyramidImageFilter', 'itk::RecursiveMultiResolutionPyramidImageFilter', 'itkRecursiveMultiResolutionPyramidImageFilterIUC3IUC3', True, 'itk::Image< unsigned char,3 >, itk::Image< unsigned char,3 >'),
  ('RecursiveMultiResolutionPyramidImageFilter', 'itk::RecursiveMultiResolutionPyramidImageFilter', 'itkRecursiveMultiResolutionPyramidImageFilterIUS2IUS2', True, 'itk::Image< unsigned short,2 >, itk::Image< unsigned short,2 >'),
  ('RecursiveMultiResolutionPyramidImageFilter', 'itk::RecursiveMultiResolutionPyramidImageFilter', 'itkRecursiveMultiResolutionPyramidImageFilterIUS3IUS3', True, 'itk::Image< unsigned short,3 >, itk::Image< unsigned short,3 >'),
  ('RecursiveMultiResolutionPyramidImageFilter', 'itk::RecursiveMultiResolutionPyramidImageFilter', 'itkRecursiveMultiResolutionPyramidImageFilterIF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >'),
  ('RecursiveMultiResolutionPyramidImageFilter', 'itk::RecursiveMultiResolutionPyramidImageFilter', 'itkRecursiveMultiResolutionPyramidImageFilterIF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >'),
  ('RecursiveMultiResolutionPyramidImageFilter', 'itk::RecursiveMultiResolutionPyramidImageFilter', 'itkRecursiveMultiResolutionPyramidImageFilterID2ID2', True, 'itk::Image< double,2 >, itk::Image< double,2 >'),
  ('RecursiveMultiResolutionPyramidImageFilter', 'itk::RecursiveMultiResolutionPyramidImageFilter', 'itkRecursiveMultiResolutionPyramidImageFilterID3ID3', True, 'itk::Image< double,3 >, itk::Image< double,3 >'),
  ('TransformParametersAdaptorBase', 'itk::TransformParametersAdaptorBase', 'itkTransformParametersAdaptorBaseF2', True, 'itk::Transform< float,2,2 >'),
  ('TransformParametersAdaptorBase', 'itk::TransformParametersAdaptorBase', 'itkTransformParametersAdaptorBaseD2', True, 'itk::Transform< double,2,2 >'),
  ('TransformParametersAdaptorBase', 'itk::TransformParametersAdaptorBase', 'itkTransformParametersAdaptorBaseF3', True, 'itk::Transform< float,3,3 >'),
  ('TransformParametersAdaptorBase', 'itk::TransformParametersAdaptorBase', 'itkTransformParametersAdaptorBaseD3', True, 'itk::Transform< double,3,3 >'),
)
snake_case_functions = ('multi_resolution_pyramid_image_filter', 'image_registration_method', 'multi_resolution_image_registration_method', 'recursive_multi_resolution_pyramid_image_filter', 'mesh_source', 'block_matching_image_filter', 'mesh_to_mesh_filter', )
