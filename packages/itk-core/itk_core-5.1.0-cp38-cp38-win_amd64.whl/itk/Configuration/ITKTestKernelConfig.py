depends = ('ITKPyBase', 'ITKIOVTK', 'ITKIOTIFF', 'ITKIOPNG', 'ITKIONRRD', 'ITKIONIFTI', 'ITKIOMeta', 'ITKIOMeshVTK', 'ITKIOMeshOFF', 'ITKIOMeshOBJ', 'ITKIOMeshGifti', 'ITKIOMeshFreeSurfer', 'ITKIOMeshBYU', 'ITKIOJPEG', 'ITKIOImageBase', 'ITKIOGIPL', 'ITKIOGDCM', 'ITKIOBMP', 'ITKCommon', )
templates = (
  ('ComparisonImageFilter', 'itk::Testing::ComparisonImageFilter', 'itkComparisonImageFilterISS2ISS2', False, 'itk::Image< signed short,2 >, itk::Image< signed short,2 >'),
  ('ComparisonImageFilter', 'itk::Testing::ComparisonImageFilter', 'itkComparisonImageFilterISS3ISS3', False, 'itk::Image< signed short,3 >, itk::Image< signed short,3 >'),
  ('ComparisonImageFilter', 'itk::Testing::ComparisonImageFilter', 'itkComparisonImageFilterIUC2IUC2', False, 'itk::Image< unsigned char,2 >, itk::Image< unsigned char,2 >'),
  ('ComparisonImageFilter', 'itk::Testing::ComparisonImageFilter', 'itkComparisonImageFilterIUC3IUC3', False, 'itk::Image< unsigned char,3 >, itk::Image< unsigned char,3 >'),
  ('ComparisonImageFilter', 'itk::Testing::ComparisonImageFilter', 'itkComparisonImageFilterIUS2IUS2', False, 'itk::Image< unsigned short,2 >, itk::Image< unsigned short,2 >'),
  ('ComparisonImageFilter', 'itk::Testing::ComparisonImageFilter', 'itkComparisonImageFilterIUS3IUS3', False, 'itk::Image< unsigned short,3 >, itk::Image< unsigned short,3 >'),
  ('ComparisonImageFilter', 'itk::Testing::ComparisonImageFilter', 'itkComparisonImageFilterIF2IF2', False, 'itk::Image< float,2 >, itk::Image< float,2 >'),
  ('ComparisonImageFilter', 'itk::Testing::ComparisonImageFilter', 'itkComparisonImageFilterIF3IF3', False, 'itk::Image< float,3 >, itk::Image< float,3 >'),
  ('ComparisonImageFilter', 'itk::Testing::ComparisonImageFilter', 'itkComparisonImageFilterID2ID2', False, 'itk::Image< double,2 >, itk::Image< double,2 >'),
  ('ComparisonImageFilter', 'itk::Testing::ComparisonImageFilter', 'itkComparisonImageFilterID3ID3', False, 'itk::Image< double,3 >, itk::Image< double,3 >'),
  ('PipelineMonitorImageFilter', 'itk::PipelineMonitorImageFilter', 'itkPipelineMonitorImageFilterIRGBUC2', True, 'itk::Image< itk::RGBPixel< unsigned char >,2 >'),
  ('PipelineMonitorImageFilter', 'itk::PipelineMonitorImageFilter', 'itkPipelineMonitorImageFilterIRGBUC3', True, 'itk::Image< itk::RGBPixel< unsigned char >,3 >'),
  ('PipelineMonitorImageFilter', 'itk::PipelineMonitorImageFilter', 'itkPipelineMonitorImageFilterIRGBAUC2', True, 'itk::Image< itk::RGBAPixel< unsigned char >,2 >'),
  ('PipelineMonitorImageFilter', 'itk::PipelineMonitorImageFilter', 'itkPipelineMonitorImageFilterIRGBAUC3', True, 'itk::Image< itk::RGBAPixel< unsigned char >,3 >'),
  ('PipelineMonitorImageFilter', 'itk::PipelineMonitorImageFilter', 'itkPipelineMonitorImageFilterIVF22', True, 'itk::Image< itk::Vector< float,2 >,2 >'),
  ('PipelineMonitorImageFilter', 'itk::PipelineMonitorImageFilter', 'itkPipelineMonitorImageFilterIVF23', True, 'itk::Image< itk::Vector< float,2 >,3 >'),
  ('PipelineMonitorImageFilter', 'itk::PipelineMonitorImageFilter', 'itkPipelineMonitorImageFilterIVF32', True, 'itk::Image< itk::Vector< float,3 >,2 >'),
  ('PipelineMonitorImageFilter', 'itk::PipelineMonitorImageFilter', 'itkPipelineMonitorImageFilterIVF33', True, 'itk::Image< itk::Vector< float,3 >,3 >'),
  ('PipelineMonitorImageFilter', 'itk::PipelineMonitorImageFilter', 'itkPipelineMonitorImageFilterIVF42', True, 'itk::Image< itk::Vector< float,4 >,2 >'),
  ('PipelineMonitorImageFilter', 'itk::PipelineMonitorImageFilter', 'itkPipelineMonitorImageFilterIVF43', True, 'itk::Image< itk::Vector< float,4 >,3 >'),
  ('PipelineMonitorImageFilter', 'itk::PipelineMonitorImageFilter', 'itkPipelineMonitorImageFilterICVF22', True, 'itk::Image< itk::CovariantVector< float,2 >,2 >'),
  ('PipelineMonitorImageFilter', 'itk::PipelineMonitorImageFilter', 'itkPipelineMonitorImageFilterICVF23', True, 'itk::Image< itk::CovariantVector< float,2 >,3 >'),
  ('PipelineMonitorImageFilter', 'itk::PipelineMonitorImageFilter', 'itkPipelineMonitorImageFilterICVF32', True, 'itk::Image< itk::CovariantVector< float,3 >,2 >'),
  ('PipelineMonitorImageFilter', 'itk::PipelineMonitorImageFilter', 'itkPipelineMonitorImageFilterICVF33', True, 'itk::Image< itk::CovariantVector< float,3 >,3 >'),
  ('PipelineMonitorImageFilter', 'itk::PipelineMonitorImageFilter', 'itkPipelineMonitorImageFilterICVF42', True, 'itk::Image< itk::CovariantVector< float,4 >,2 >'),
  ('PipelineMonitorImageFilter', 'itk::PipelineMonitorImageFilter', 'itkPipelineMonitorImageFilterICVF43', True, 'itk::Image< itk::CovariantVector< float,4 >,3 >'),
  ('PipelineMonitorImageFilter', 'itk::PipelineMonitorImageFilter', 'itkPipelineMonitorImageFilterISS2', True, 'itk::Image< signed short,2 >'),
  ('PipelineMonitorImageFilter', 'itk::PipelineMonitorImageFilter', 'itkPipelineMonitorImageFilterISS3', True, 'itk::Image< signed short,3 >'),
  ('PipelineMonitorImageFilter', 'itk::PipelineMonitorImageFilter', 'itkPipelineMonitorImageFilterIUC2', True, 'itk::Image< unsigned char,2 >'),
  ('PipelineMonitorImageFilter', 'itk::PipelineMonitorImageFilter', 'itkPipelineMonitorImageFilterIUC3', True, 'itk::Image< unsigned char,3 >'),
  ('PipelineMonitorImageFilter', 'itk::PipelineMonitorImageFilter', 'itkPipelineMonitorImageFilterIUS2', True, 'itk::Image< unsigned short,2 >'),
  ('PipelineMonitorImageFilter', 'itk::PipelineMonitorImageFilter', 'itkPipelineMonitorImageFilterIUS3', True, 'itk::Image< unsigned short,3 >'),
  ('PipelineMonitorImageFilter', 'itk::PipelineMonitorImageFilter', 'itkPipelineMonitorImageFilterIF2', True, 'itk::Image< float,2 >'),
  ('PipelineMonitorImageFilter', 'itk::PipelineMonitorImageFilter', 'itkPipelineMonitorImageFilterIF3', True, 'itk::Image< float,3 >'),
  ('PipelineMonitorImageFilter', 'itk::PipelineMonitorImageFilter', 'itkPipelineMonitorImageFilterID2', True, 'itk::Image< double,2 >'),
  ('PipelineMonitorImageFilter', 'itk::PipelineMonitorImageFilter', 'itkPipelineMonitorImageFilterID3', True, 'itk::Image< double,3 >'),
  ('PipelineMonitorImageFilter', 'itk::PipelineMonitorImageFilter', 'itkPipelineMonitorImageFilterICF2', True, 'itk::Image< std::complex< float >,2 >'),
  ('PipelineMonitorImageFilter', 'itk::PipelineMonitorImageFilter', 'itkPipelineMonitorImageFilterICF3', True, 'itk::Image< std::complex< float >,3 >'),
  ('RandomImageSource', 'itk::RandomImageSource', 'itkRandomImageSourceISS2', True, 'itk::Image< signed short,2 >'),
  ('RandomImageSource', 'itk::RandomImageSource', 'itkRandomImageSourceISS3', True, 'itk::Image< signed short,3 >'),
  ('RandomImageSource', 'itk::RandomImageSource', 'itkRandomImageSourceIUC2', True, 'itk::Image< unsigned char,2 >'),
  ('RandomImageSource', 'itk::RandomImageSource', 'itkRandomImageSourceIUC3', True, 'itk::Image< unsigned char,3 >'),
  ('RandomImageSource', 'itk::RandomImageSource', 'itkRandomImageSourceIUS2', True, 'itk::Image< unsigned short,2 >'),
  ('RandomImageSource', 'itk::RandomImageSource', 'itkRandomImageSourceIUS3', True, 'itk::Image< unsigned short,3 >'),
  ('RandomImageSource', 'itk::RandomImageSource', 'itkRandomImageSourceIF2', True, 'itk::Image< float,2 >'),
  ('RandomImageSource', 'itk::RandomImageSource', 'itkRandomImageSourceIF3', True, 'itk::Image< float,3 >'),
  ('RandomImageSource', 'itk::RandomImageSource', 'itkRandomImageSourceID2', True, 'itk::Image< double,2 >'),
  ('RandomImageSource', 'itk::RandomImageSource', 'itkRandomImageSourceID3', True, 'itk::Image< double,3 >'),
)
snake_case_functions = ('comparison_image_filter', 'pipeline_monitor_image_filter', 'random_image_source', )
