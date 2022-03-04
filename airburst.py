import vtk
import vtk.util.numpy_support as VN
import numpy as np
import glob
import argparse





def render_something(file_cur, daryNames):
    filename = filenames[file_cur]
    
    print('Loading data from {}'.format(filename))

    # for accessing build-in color access
    colors = vtk.vtkNamedColors() 
    
    reader = None

    
    # Remove all the existing actors and volumes
    for actor in aRenderer.GetActors():
        aRenderer.RemoveActor(actor)
    for v in aRenderer.GetVolumes():
        aRenderer.RemoveVolume(v)
    aRenderer.Clear()
    renWin.Render()
    
    if daryNames['v02']:
    
        daryName = 'v02'
    
        # data reader
        reader = vtk.vtkXMLImageDataReader()
        reader.SetFileName(filename)
        reader.Update()

        # specify the data array in the file to processq
        reader.GetOutput().GetPointData().SetActiveAttribute(daryName, 0)

        # convert the data array to numpy array and get the min and maximum valule
        dary = VN.vtk_to_numpy(reader.GetOutput().GetPointData().GetScalars(daryName))
        dMax = np.amax(dary)
        dMin = np.amin(dary)
        dRange = dMax - dMin
        dMean = np.mean(dary)
        dStd = np.std(dary)
        
        opacityTransferFunction = vtk.vtkPiecewiseFunction()
        opacityTransferFunction.AddPoint(dMin, 0.0)
        opacityTransferFunction.AddPoint(dMin+dRange/4, 0.0)
        opacityTransferFunction.AddPoint(dMax, 0.2)
        
        # Create transfer mapping scalar value to color
        colorTransferFunction = vtk.vtkColorTransferFunction()
        colorTransferFunction.AddRGBPoint(dMin, 0.0, 0.0, 0.0)
        colorTransferFunction.AddRGBPoint(dMin+dRange/4, 0.0, 0.0, 0.0)
        colorTransferFunction.AddRGBPoint(dMax, 0.0, 0.0, 0.8)
        
        # The property describes how the data will look
        volumeProperty = vtk.vtkVolumeProperty()
        volumeProperty.SetColor(colorTransferFunction)
        volumeProperty.SetScalarOpacity(opacityTransferFunction)
        volumeProperty.ShadeOn()  ### on/off shader 
        volumeProperty.SetInterpolationTypeToLinear()

        # The mapper / ray cast function know how to render the data
        volumeMapper = vtk.vtkGPUVolumeRayCastMapper()
        volumeMapper.SetBlendModeToComposite()
        volumeMapper.SetInputConnection(reader.GetOutputPort())
        
        # The volume holds the mapper and the property and
        # can be used to position/orient the volume
        volume = vtk.vtkVolume()
        volume.SetMapper(volumeMapper)
        volume.SetProperty(volumeProperty)
        aRenderer.AddVolume(volume)
        
        # a colorbar to display the colormap
        scalarBar = scalarBarWater
        scalarBar.SetLookupTable( colorTransferFunction )
        scalarBar.SetTitle(daryName)
        scalarBar.SetOrientationToHorizontal()
        scalarBar.GetLabelTextProperty().SetColor(0, 0, 0.8)
        scalarBar.GetTitleTextProperty().SetColor(0, 0, 0.8)
        
        # position it in window
        coord = scalarBar.GetPositionCoordinate()
        coord.SetCoordinateSystemToNormalizedViewport()
        coord.SetValue(0.6,0.05)
        scalarBar.SetWidth(.4)
        scalarBar.SetHeight(.05)
        
        aRenderer.AddActor(scalarBar)
    if daryNames['v03']:
        
        daryName = 'v03'
        
        # data reader
        reader = vtk.vtkXMLImageDataReader()
        reader.SetFileName(filename)
        reader.Update()

        # specify the data array in the file to processq
        reader.GetOutput().GetPointData().SetActiveAttribute(daryName, 0)

        # convert the data array to numpy array and get the min and maximum valule
        dary = VN.vtk_to_numpy(reader.GetOutput().GetPointData().GetScalars(daryName))
        dMax = np.amax(dary)
        dMin = np.amin(dary)
        dRange = dMax - dMin
        dMean = np.mean(dary)
        dStd = np.std(dary)
        
        # Create transfer mapping scalar value to opacity
        opacityTransferFunction = vtk.vtkPiecewiseFunction()
        opacityTransferFunction.AddPoint(dMin, 0.0)
        opacityTransferFunction.AddPoint(dMin + dRange/2, 0.0)
        opacityTransferFunction.AddPoint(dMax, 0.1)

        # Create transfer mapping scalar value to color
        colorTransferFunction = vtk.vtkColorTransferFunction()
        colorTransferFunction.AddRGBPoint(dMin, 0.0, 0.0, 0.0)
        colorTransferFunction.AddRGBPoint(dMin + (dRange/4)*1, 0.0, 0.0, 0.0)
        colorTransferFunction.AddRGBPoint(dMin + (dRange/4)*2, 0.0, 0.0, 0.0)
        colorTransferFunction.AddRGBPoint(dMin + (dRange/4)*3, 0.5, 0.0, 0.0)
        colorTransferFunction.AddRGBPoint(dMin + (dRange/4)*4, 1.0, 0.0, 0.0)

        # The property describes how the data will look
        volumeProperty = vtk.vtkVolumeProperty()
        volumeProperty.SetColor(colorTransferFunction)
        volumeProperty.SetScalarOpacity(opacityTransferFunction)
        volumeProperty.ShadeOn()  ### on/off shader 
        volumeProperty.SetInterpolationTypeToLinear()

        # The mapper / ray cast function know how to render the data
        volumeMapper = vtk.vtkGPUVolumeRayCastMapper()
        volumeMapper.SetBlendModeToComposite()
        volumeMapper.SetInputConnection(reader.GetOutputPort())
        
        # The volume holds the mapper and the property and
        # can be used to position/orient the volume
        volume = vtk.vtkVolume()
        volume.SetMapper(volumeMapper)
        volume.SetProperty(volumeProperty)
        aRenderer.AddVolume(volume)
        
        # a colorbar to display the colormap
        scalarBar = scalarBarAsteroid
        scalarBar.SetLookupTable( colorTransferFunction )
        scalarBar.SetTitle(daryName)
        scalarBar.SetOrientationToHorizontal()
        scalarBar.GetLabelTextProperty().SetColor(0.8, 0, 0)
        scalarBar.GetTitleTextProperty().SetColor(0.8, 0, 0)
        
        # position it in window
        coord = scalarBar.GetPositionCoordinate()
        coord.SetCoordinateSystemToNormalizedViewport()
        coord.SetValue(0.1,0.05)
        scalarBar.SetWidth(.4)
        scalarBar.SetHeight(.05)
        
        aRenderer.AddActor(scalarBar)
    
    if daryNames['tev']:
        daryName = 'tev'
        
        # data reader
        reader = vtk.vtkXMLImageDataReader()
        reader.SetFileName(filename)
        reader.Update()

        # specify the data array in the file to processq
        reader.GetOutput().GetPointData().SetActiveAttribute(daryName, 0)

        # convert the data array to numpy array and get the min and maximum valule
        dary = VN.vtk_to_numpy(reader.GetOutput().GetPointData().GetScalars(daryName))
        dMax = np.amax(dary)
        dMin = np.amin(dary)
        dRange = dMax - dMin
        dMean = np.mean(dary)
        dStd = np.std(dary)
        
        print(dMax, dMin, dRange, dMean, dStd)
        
        '''#isovalue1 = dMin + 0.9*dRange
        isovalue1 = dMin + 0.5*dRange
        # extract a isosurface and specify its color
        iso1 = vtk.vtkContourFilter()
        iso1.SetInputConnection(reader.GetOutputPort())
        iso1.SetValue(0, isovalue1)

        isoMapper1 = vtk.vtkPolyDataMapper()
        isoMapper1.SetInputConnection(iso1.GetOutputPort())
        isoMapper1.ScalarVisibilityOff()

        isoActor1 = vtk.vtkActor()
        isoActor1.SetMapper(isoMapper1)
        isoActor1.GetProperty().SetColor(colors.GetColor3d("banana"))
        isoActor1.GetProperty().SetOpacity(1)
        aRenderer.AddActor(isoActor1)'''
        
        lwf = vtk.vtkContourFilter()
        lwf.SetInputConnection(reader.GetOutputPort())
        lwf.SetValue(0, 0.5)

        lwfMapper = vtk.vtkPolyDataMapper()
        lwfMapper.SetInputConnection(lwf.GetOutputPort())
        lwfMapper.ScalarVisibilityOff()

        lwfActor = vtk.vtkActor()
        lwfActor.SetMapper(lwfMapper)
        lwfActor.GetProperty().SetColor(colors.GetColor3d("Banana"))
        lwfActor.GetProperty().SetSpecular(.3)
        lwfActor.GetProperty().SetSpecularPower(20)
        
        aRenderer.AddActor(lwfActor)
        lwfActor.GetProperty().SetOpacity(0.2)
        
    if reader is not None:
    
        txt.SetInput('time = {} ms'.format(20*file_cur))
        txtprop=txt.GetTextProperty()
        txtprop.SetFontFamilyToArial()
        txtprop.SetFontSize(18)
        txtprop.SetColor(1,1,1)
        txt.SetDisplayPosition(10, 10)
        aRenderer.AddActor(txt)
        
        # An outline provides context around the data.
        outline.SetInputConnection(reader.GetOutputPort())
        outlineMapper = vtk.vtkPolyDataMapper()
        outlineMapper.SetInputConnection(outline.GetOutputPort())
        outlineActor = vtk.vtkActor()
        outlineActor.SetMapper(outlineMapper)
        aRenderer.AddActor(outlineActor)
   

    # Calling Render() directly on a vtkRenderer is strictly forbidden.
    # Only calling Render() on the vtkRenderWindow is a valid call.
    renWin.Render()

    aRenderer.ResetCamera()
    aCamera.Dolly(1.5)

    # Note that when camera movement occurs (as it does in the Dolly()
    # method), the clipping planes often need adjusting. Clipping planes
    # consist of two planes: near and far along the view direction. The
    # near plane clips out objects in front of the plane; the far plane
    # clips out objects behind the plane. This way only what is drawn
    # between the planes is actually rendered.
    aRenderer.ResetCameraClippingRange()

    # Interact with the data.
    renWin.Render()
    

def screenshot():
    global renWin
    # screenshot code:
    w2if = vtk.vtkWindowToImageFilter()
    w2if.SetInput(renWin)
    w2if.Update()

    writer = vtk.vtkPNGWriter()
    writer.SetFileName("screenshot_{}.png".format(file_cur))
    writer.SetInputData(w2if.GetOutput())
    writer.Write()    


def keypress_callback(obj, ev):
    global file_cur, daryNames
    key = obj.GetKeySym()
    print(key, 'was pressed', key in 'adws')
    
    if key == 'j':
        file_cur = (file_cur-1)%len(filenames)
    if key == 'k':
        file_cur = (file_cur+1)%len(filenames)
    if key == 'a':
        daryNames['v02'] = not daryNames['v02']
    if key == 's':
        daryNames['v03'] = not daryNames['v03']
    if key == 'd':
        daryNames['tev'] = not daryNames['tev']
    if key == 'space':
        screenshot()
            
    if key in 'jkasd':
        render_something(file_cur, daryNames)

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='This app generates a VTK visualization')
    parser.add_argument('data', type=str,
                    help='Location of the data vti files')

    args = parser.parse_args()
    
    aRenderer = vtk.vtkRenderer()
    renWin = vtk.vtkRenderWindow()
    renWin.AddRenderer(aRenderer)
    iren = vtk.vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)
    aRenderer.SetBackground(0, 0, 0)
    renWin.SetSize(600, 600)



    filenames = glob.glob('{}/*.vti'.format(args.data))
    filenames.sort()
    file_cur = 0
    print(filenames)

    scalars = ['v02', 'v03', 'prs', 'tev']
    daryNames = {'v02':True, 'v03':False, 'tev':False}

    # It is convenient to create an initial view of the data. The
    # FocalPoint and Position form a vector direction. Later on
    # (ResetCamera() method) this vector is used to position the camera
    # to look at the data in this direction.
    aCamera = vtk.vtkCamera()
    aCamera.SetViewUp(1, 0, 1)
    aCamera.SetPosition(1, 0, 1)
    aCamera.SetFocalPoint(0, 0, 0)
    aCamera.ComputeViewPlaneNormal()
    aCamera.Azimuth(30.0)
    aCamera.Elevation(30.0)

    txt = vtk.vtkTextActor()
    outline = vtk.vtkOutlineFilter()
    scalarBarWater = vtk.vtkScalarBarActor()
    scalarBarAsteroid = vtk.vtkScalarBarActor()

    # An initial camera view is created.  The Dolly() method moves
    # the camera towards the FocalPoint, thereby enlarging the image.
    aRenderer.SetActiveCamera(aCamera)

    iren.AddObserver('KeyPressEvent', keypress_callback, 1.0)

    iren.Initialize()
    iren.Start()

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
