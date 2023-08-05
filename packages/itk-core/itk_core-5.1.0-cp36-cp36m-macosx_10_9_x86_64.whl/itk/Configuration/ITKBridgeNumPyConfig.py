depends = ('ITKPyBase', 'ITKCommon', )
templates = (
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferISS2', True, 'itk::Image< signed short,2 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferISS3', True, 'itk::Image< signed short,3 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferIUC2', True, 'itk::Image< unsigned char,2 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferIRGBUC2', True, 'itk::Image< itk::RGBPixel< unsigned char >,2 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferIRGBAUC2', True, 'itk::Image< itk::RGBAPixel< unsigned char >,2 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferIUC3', True, 'itk::Image< unsigned char,3 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferIRGBUC3', True, 'itk::Image< itk::RGBPixel< unsigned char >,3 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferIRGBAUC3', True, 'itk::Image< itk::RGBAPixel< unsigned char >,3 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferIUS2', True, 'itk::Image< unsigned short,2 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferIUS3', True, 'itk::Image< unsigned short,3 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferIF2', True, 'itk::Image< float,2 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferIVF22', True, 'itk::Image< itk::Vector< float,2 >,2 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferICVF22', True, 'itk::Image< itk::CovariantVector< float,2 >,2 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferIVF32', True, 'itk::Image< itk::Vector< float,3 >,2 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferICVF32', True, 'itk::Image< itk::CovariantVector< float,3 >,2 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferIVF42', True, 'itk::Image< itk::Vector< float,4 >,2 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferICVF42', True, 'itk::Image< itk::CovariantVector< float,4 >,2 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferIF3', True, 'itk::Image< float,3 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferIVF23', True, 'itk::Image< itk::Vector< float,2 >,3 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferICVF23', True, 'itk::Image< itk::CovariantVector< float,2 >,3 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferIVF33', True, 'itk::Image< itk::Vector< float,3 >,3 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferICVF33', True, 'itk::Image< itk::CovariantVector< float,3 >,3 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferIVF43', True, 'itk::Image< itk::Vector< float,4 >,3 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferICVF43', True, 'itk::Image< itk::CovariantVector< float,4 >,3 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferID2', True, 'itk::Image< double,2 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferISSRTD22', True, 'itk::Image< itk::SymmetricSecondRankTensor< double, 2 >, 2 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferIVD22', True, 'itk::Image< itk::Vector< double,2 >,2 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferICVD22', True, 'itk::Image< itk::CovariantVector< double,2 >,2 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferIVD32', True, 'itk::Image< itk::Vector< double,3 >,2 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferICVD32', True, 'itk::Image< itk::CovariantVector< double,3 >,2 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferIVD42', True, 'itk::Image< itk::Vector< double,4 >,2 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferICVD42', True, 'itk::Image< itk::CovariantVector< double,4 >,2 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferID3', True, 'itk::Image< double,3 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferISSRTD33', True, 'itk::Image< itk::SymmetricSecondRankTensor< double, 3 >, 3 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferIVD23', True, 'itk::Image< itk::Vector< double,2 >,3 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferICVD23', True, 'itk::Image< itk::CovariantVector< double,2 >,3 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferIVD33', True, 'itk::Image< itk::Vector< double,3 >,3 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferICVD33', True, 'itk::Image< itk::CovariantVector< double,3 >,3 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferIVD43', True, 'itk::Image< itk::Vector< double,4 >,3 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferICVD43', True, 'itk::Image< itk::CovariantVector< double,4 >,3 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferIUL2', True, 'itk::Image< unsigned long,2 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferIUL3', True, 'itk::Image< unsigned long,3 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferVISS2', True, 'itk::VectorImage< signed short,2 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferVIUC2', True, 'itk::VectorImage< unsigned char,2 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferVIUS2', True, 'itk::VectorImage< unsigned short,2 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferVIF2', True, 'itk::VectorImage< float,2 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferVID2', True, 'itk::VectorImage< double,2 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferVISS3', True, 'itk::VectorImage< signed short,3 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferVIUC3', True, 'itk::VectorImage< unsigned char,3 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferVIUS3', True, 'itk::VectorImage< unsigned short,3 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferVIF3', True, 'itk::VectorImage< float,3 >'),
  ('PyBuffer', 'itk::PyBuffer', 'itkPyBufferVID3', True, 'itk::VectorImage< double,3 >'),
  ('PyVnl', 'itk::PyVnl', 'itkPyVnlSS', True, 'signed short'),
  ('PyVnl', 'itk::PyVnl', 'itkPyVnlUC', True, 'unsigned char'),
  ('PyVnl', 'itk::PyVnl', 'itkPyVnlUS', True, 'unsigned short'),
  ('PyVnl', 'itk::PyVnl', 'itkPyVnlF', True, 'float'),
  ('PyVnl', 'itk::PyVnl', 'itkPyVnlD', True, 'double'),
  ('PyVnl', 'itk::PyVnl', 'itkPyVnlUI', True, 'unsigned int'),
  ('PyVnl', 'itk::PyVnl', 'itkPyVnlUL', True, 'unsigned long'),
  ('PyVnl', 'itk::PyVnl', 'itkPyVnlSC', True, 'signed char'),
  ('PyVnl', 'itk::PyVnl', 'itkPyVnlSI', True, 'signed int'),
  ('PyVnl', 'itk::PyVnl', 'itkPyVnlSL', True, 'signed long'),
)
snake_case_functions = ()
