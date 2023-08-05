from ._scala import OMICRONscala

def load(parFile):
    '''This method load data and metadata associated to an Omicron SCALA .par file.
    
    Args:
        parFile: the name of the .par file to be loaded
    
    Returns:
        a container for the channels in the .par file with their data and metadata
    
    Examples:
        f = omicronscala.load('/path/to/file.par') # load the file
        
        ch0 = f[0] # assign first channel
        ch0.name # returns channel name
        ch0.data # returns channel data as a numpy array
        ch0.attrs # returns channel metadata as a dictionary
    '''

    return OMICRONscala(parFile) 

def to_dataset(parFile):
    '''This method load an Omicron SCALA .par file into an xarray Dataset.
    
    The xarray package is required.
    
    Args:
        parFile: the name of the .par file to be loaded
    
    Returns:
        an xarray Dataset
    
    Examples:
        ds = omicronscala.to_dataset('/path/to/file.par')
        
        ds
        <xarray.Dataset>
        
        ds.Z_Forward
        <xarray.DataArray>
    '''

    try:
        import xarray as xr
    except:
        print("Error: xarray package not found.")
        return

    f = load(parFile)

    ds = xr.Dataset()
    for ch in f:
        ds[ch.name] = xr.DataArray(ch.data,
                                   coords=ch.coords,
                                   attrs=ch.attrs,
                                   name=ch.name)

    return ds

def to_nexus(parFile, filename=None, **kwargs):
    '''This method convert an Omicron SCALA .par file into a NeXus file.
    
    The nxarray package is required.
    
    Args:
        parFile: the name of the .par file to be converted
        filename: (optional) path of the NeXus file to be saved.
            If not provided, a NeXus file is saved in the same folder
            of the .par file.
        **kwargs: any optional argument accepted by nexus NXdata.save() method
    
    Returns:
        nothing
    
    Examples:
        omicronscala.to_nexus('/path/to/file.par')
    '''

    try:
        import nxarray as nxr
    except:
        print("Error: nxarray package not found.")
        return

    if not filename:
        import os
        filename = os.path.splitext(parFile)[0]

    ds = to_dataset(parFile)
    ds.nxr.save(filename, **kwargs)
