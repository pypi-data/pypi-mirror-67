depends = ('ITKPyBase', 'ITKMesh', 'ITKCommon', )
templates = (
  ('QuadEdge', 'itk::QuadEdge', 'itkQuadEdge', True),
  ('GeometricalQuadEdge', 'itk::GeometricalQuadEdge', 'itkGeometricalQuadEdgeULULBBF', True, 'unsigned long, unsigned long, bool, bool, true'),
  ('GeometricalQuadEdge', 'itk::GeometricalQuadEdge', 'itkGeometricalQuadEdgeULULBBT', True, 'unsigned long, unsigned long, bool, bool, false'),
  ('QuadEdgeMeshPoint', 'itk::QuadEdgeMeshPoint', 'itkQuadEdgeMeshPointF2GQEULULBBT', True, 'float,2,itk::GeometricalQuadEdge< unsigned long,unsigned long,bool,bool,true >'),
  ('QuadEdgeMeshPoint', 'itk::QuadEdgeMeshPoint', 'itkQuadEdgeMeshPointF3GQEULULBBT', True, 'float,3,itk::GeometricalQuadEdge< unsigned long,unsigned long,bool,bool,true >'),
  ('QuadEdgeMeshTraits', 'itk::QuadEdgeMeshTraits', 'itkQuadEdgeMeshTraitsD2BBFF', True, 'double, 2, bool, bool, float, float'),
  ('QuadEdgeMeshTraits', 'itk::QuadEdgeMeshTraits', 'itkQuadEdgeMeshTraitsD3BBFF', True, 'double, 3, bool, bool, float, float'),
  ('MapContainer', 'itk::MapContainer', 'itkMapContainerULQEMPF2GQEULULBBT', False, 'unsigned long,itk::QuadEdgeMeshPoint< float,2,itk::GeometricalQuadEdge< unsigned long,unsigned long,bool,bool,true > >'),
  ('MapContainer', 'itk::MapContainer', 'itkMapContainerULQEMPF3GQEULULBBT', False, 'unsigned long,itk::QuadEdgeMeshPoint< float,3,itk::GeometricalQuadEdge< unsigned long,unsigned long,bool,bool,true > >'),
  ('QuadEdgeMeshCellTraitsInfo', 'itk::QuadEdgeMeshCellTraitsInfo', 'itkQuadEdgeMeshCellTraitsInfo2FFULULUCQEMPGQEULQEMPF2GQEULULBBTGQE', False, '2,float,float,unsigned long,unsigned long,unsigned char,itk::QuadEdgeMeshPoint< float,2,itk::GeometricalQuadEdge< unsigned long, unsigned long,bool,bool,true > >,itk::MapContainer<unsigned long,itk::QuadEdgeMeshPoint< float,2,itk::GeometricalQuadEdge< unsigned long,unsigned long,bool,bool,true > > >,std::set< unsigned long >,itk::GeometricalQuadEdge< unsigned long,unsigned long,bool,bool,true >'),
  ('QuadEdgeMeshCellTraitsInfo', 'itk::QuadEdgeMeshCellTraitsInfo', 'itkQuadEdgeMeshCellTraitsInfo3FFULULUCQEMPGQEULQEMPF3GQEULULBBTGQE', False, '3,float,float,unsigned long,unsigned long,unsigned char,itk::QuadEdgeMeshPoint< float,3,itk::GeometricalQuadEdge< unsigned long, unsigned long,bool,bool,true > >,itk::MapContainer<unsigned long,itk::QuadEdgeMeshPoint< float,3,itk::GeometricalQuadEdge< unsigned long,unsigned long,bool,bool,true > > >,std::set< unsigned long >,itk::GeometricalQuadEdge< unsigned long,unsigned long,bool,bool,true >'),
  ('CellInterface', 'itk::CellInterface', 'itkCellInterfaceDQEMCTI2', False, 'double, itk::QuadEdgeMeshCellTraitsInfo< 2,float,float,unsigned long,unsigned long,unsigned char,itk::QuadEdgeMeshPoint< float,2,itk::GeometricalQuadEdge< unsigned long, unsigned long,bool,bool,true > >,itk::MapContainer< unsigned long,itk::QuadEdgeMeshPoint< float,2,itk::GeometricalQuadEdge< unsigned long,unsigned long,bool,bool,true > > >,std::set< unsigned long >,itk::GeometricalQuadEdge< unsigned long,unsigned long,bool,bool,true > >'),
  ('CellInterface', 'itk::CellInterface', 'itkCellInterfaceDQEMCTI3', False, 'double, itk::QuadEdgeMeshCellTraitsInfo< 3,float,float,unsigned long,unsigned long,unsigned char,itk::QuadEdgeMeshPoint< float,3,itk::GeometricalQuadEdge< unsigned long, unsigned long,bool,bool,true > >,itk::MapContainer< unsigned long,itk::QuadEdgeMeshPoint< float,3,itk::GeometricalQuadEdge< unsigned long,unsigned long,bool,bool,true > > >,std::set< unsigned long >,itk::GeometricalQuadEdge< unsigned long,unsigned long,bool,bool,true > >'),
  ('QuadEdgeMeshLineCell', 'itk::QuadEdgeMeshLineCell', 'itkQuadEdgeMeshLineCellCIDQEMCTI2', True, 'itk::CellInterface< double, itk::QuadEdgeMeshCellTraitsInfo< 2,float,float,unsigned long,unsigned long,unsigned char,itk::QuadEdgeMeshPoint< float,2,itk::GeometricalQuadEdge< unsigned long, unsigned long,bool,bool,true > >,itk::MapContainer< unsigned long,itk::QuadEdgeMeshPoint< float,2,itk::GeometricalQuadEdge< unsigned long,unsigned long,bool,bool,true > > >,std::set< unsigned long >,itk::GeometricalQuadEdge< unsigned long,unsigned long,bool,bool,true > > >'),
  ('QuadEdgeMeshLineCell', 'itk::QuadEdgeMeshLineCell', 'itkQuadEdgeMeshLineCellCIDQEMCTI3', True, 'itk::CellInterface< double, itk::QuadEdgeMeshCellTraitsInfo< 3,float,float,unsigned long,unsigned long,unsigned char,itk::QuadEdgeMeshPoint< float,3,itk::GeometricalQuadEdge< unsigned long, unsigned long,bool,bool,true > >,itk::MapContainer< unsigned long,itk::QuadEdgeMeshPoint< float,3,itk::GeometricalQuadEdge< unsigned long,unsigned long,bool,bool,true > > >,std::set< unsigned long >,itk::GeometricalQuadEdge< unsigned long,unsigned long,bool,bool,true > > >'),
  ('MapContainer', 'itk::MapContainer', 'itkMapContainerULCIDQEMCTI2', False, 'unsigned long, itk::CellInterface< double, itk::QuadEdgeMeshCellTraitsInfo< 2,float,float,unsigned long,unsigned long,unsigned char,itk::QuadEdgeMeshPoint< float,2,itk::GeometricalQuadEdge< unsigned long, unsigned long,bool,bool,true > >,itk::MapContainer< unsigned long,itk::QuadEdgeMeshPoint< float,2,itk::GeometricalQuadEdge< unsigned long,unsigned long,bool,bool,true > > >,std::set< unsigned long >,itk::GeometricalQuadEdge< unsigned long,unsigned long,bool,bool,true > > >*'),
  ('MapContainer', 'itk::MapContainer', 'itkMapContainerULCIDQEMCTI3', False, 'unsigned long, itk::CellInterface< double, itk::QuadEdgeMeshCellTraitsInfo< 3,float,float,unsigned long,unsigned long,unsigned char,itk::QuadEdgeMeshPoint< float,3,itk::GeometricalQuadEdge< unsigned long, unsigned long,bool,bool,true > >,itk::MapContainer< unsigned long,itk::QuadEdgeMeshPoint< float,3,itk::GeometricalQuadEdge< unsigned long,unsigned long,bool,bool,true > > >,std::set< unsigned long >,itk::GeometricalQuadEdge< unsigned long,unsigned long,bool,bool,true > > >*'),
  ('Mesh', 'itk::Mesh', 'itkMeshD2QEMTD2BBFF', False, 'double,2,itk::QuadEdgeMeshTraits< double,2,bool,bool,float,float >'),
  ('Mesh', 'itk::Mesh', 'itkMeshD3QEMTD3BBFF', False, 'double,3,itk::QuadEdgeMeshTraits< double,3,bool,bool,float,float >'),
  ('PointSet', 'itk::PointSet', 'itkPointSetD2QEMTD2BBFF', False, 'double,2,itk::QuadEdgeMeshTraits< double,2,bool,bool,float,float >'),
  ('PointSet', 'itk::PointSet', 'itkPointSetD3QEMTD3BBFF', False, 'double,3,itk::QuadEdgeMeshTraits< double,3,bool,bool,float,float >'),
  ('BoundingBox', 'itk::BoundingBox', 'itkBoundingBoxUL2FMCULQEMPF2', False, 'unsigned long, 2, float, itk::MapContainer< unsigned long, itk::QuadEdgeMeshPoint< float,2,itk::GeometricalQuadEdge< unsigned long,unsigned long,bool,bool,true > > >'),
  ('BoundingBox', 'itk::BoundingBox', 'itkBoundingBoxUL3FMCULQEMPF3', False, 'unsigned long, 3, float, itk::MapContainer< unsigned long, itk::QuadEdgeMeshPoint< float,3,itk::GeometricalQuadEdge< unsigned long,unsigned long,bool,bool,true > > >'),
  ('QuadEdgeMesh', 'itk::QuadEdgeMesh', 'itkQuadEdgeMeshD2', True, 'double,2'),
  ('QuadEdgeMesh', 'itk::QuadEdgeMesh', 'itkQuadEdgeMeshD3', True, 'double,3'),
  ('MeshSource', 'itk::MeshSource', 'itkMeshSourceQEMD2', False, 'itk::QuadEdgeMesh< double,2 >'),
  ('MeshSource', 'itk::MeshSource', 'itkMeshSourceMD2QEMTD2BBFF', False, 'itk::Mesh< double,2,itk::QuadEdgeMeshTraits< double,2,bool,bool,float,float > >'),
  ('MeshSource', 'itk::MeshSource', 'itkMeshSourceQEMD3', False, 'itk::QuadEdgeMesh< double,3 >'),
  ('MeshSource', 'itk::MeshSource', 'itkMeshSourceMD3QEMTD3BBFF', False, 'itk::Mesh< double,3,itk::QuadEdgeMeshTraits< double,3,bool,bool,float,float > >'),
  ('MeshToMeshFilter', 'itk::MeshToMeshFilter', 'itkMeshToMeshFilterQEMD2QEMD2', False, 'itk::QuadEdgeMesh< double,2 >, itk::QuadEdgeMesh< double,2 >'),
  ('MeshToMeshFilter', 'itk::MeshToMeshFilter', 'itkMeshToMeshFilterQEMD3QEMD3', False, 'itk::QuadEdgeMesh< double,3 >, itk::QuadEdgeMesh< double,3 >'),
  ('ImageToMeshFilter', 'itk::ImageToMeshFilter', 'itkImageToMeshFilterISS2MD2QEMTD2BBFF', False, 'itk::Image< signed short,2 >, itk::Mesh< double,2,itk::QuadEdgeMeshTraits< double,2,bool,bool,float,float > >'),
  ('ImageToMeshFilter', 'itk::ImageToMeshFilter', 'itkImageToMeshFilterIUC2MD2QEMTD2BBFF', False, 'itk::Image< unsigned char,2 >, itk::Mesh< double,2,itk::QuadEdgeMeshTraits< double,2,bool,bool,float,float > >'),
  ('ImageToMeshFilter', 'itk::ImageToMeshFilter', 'itkImageToMeshFilterIUS2MD2QEMTD2BBFF', False, 'itk::Image< unsigned short,2 >, itk::Mesh< double,2,itk::QuadEdgeMeshTraits< double,2,bool,bool,float,float > >'),
  ('ImageToMeshFilter', 'itk::ImageToMeshFilter', 'itkImageToMeshFilterISS3MD3QEMTD3BBFF', False, 'itk::Image< signed short,3 >, itk::Mesh< double,3,itk::QuadEdgeMeshTraits< double,3,bool,bool,float,float > >'),
  ('ImageToMeshFilter', 'itk::ImageToMeshFilter', 'itkImageToMeshFilterIUC3MD3QEMTD3BBFF', False, 'itk::Image< unsigned char,3 >, itk::Mesh< double,3,itk::QuadEdgeMeshTraits< double,3,bool,bool,float,float > >'),
  ('ImageToMeshFilter', 'itk::ImageToMeshFilter', 'itkImageToMeshFilterIUS3MD3QEMTD3BBFF', False, 'itk::Image< unsigned short,3 >, itk::Mesh< double,3,itk::QuadEdgeMeshTraits< double,3,bool,bool,float,float > >'),
  ('QuadEdgeMeshToQuadEdgeMeshFilter', 'itk::QuadEdgeMeshToQuadEdgeMeshFilter', 'itkQuadEdgeMeshToQuadEdgeMeshFilterQEMD2QEMD2', True, 'itk::QuadEdgeMesh< double,2 >, itk::QuadEdgeMesh< double,2 >'),
  ('QuadEdgeMeshToQuadEdgeMeshFilter', 'itk::QuadEdgeMeshToQuadEdgeMeshFilter', 'itkQuadEdgeMeshToQuadEdgeMeshFilterQEMD3QEMD3', True, 'itk::QuadEdgeMesh< double,3 >, itk::QuadEdgeMesh< double,3 >'),
)
snake_case_functions = ('quad_edge_mesh_to_quad_edge_mesh_filter', 'mesh_source', 'mesh_to_mesh_filter', 'image_to_mesh_filter', )
