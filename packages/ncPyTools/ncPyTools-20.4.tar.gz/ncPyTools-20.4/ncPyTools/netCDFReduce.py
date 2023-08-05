"""Collection of functions to reduce netcdf file sizes by reducing float precision."""

from netCDF4 import Dataset
from pathlib import Path
from numpy import where,rint

def netCDFRound(fname,vlist,digits,outpath="",Quiet=False):
    """ Rounds list of variables in input file to a given number of significant Xdigits.
    Writes to file in outpath with same name as input file, but inserting the .Xdigits
    suffix before the filetype suffix.

    Args:
            filename(str): input netcdf file including path
            vlist(list of str): list of variables to round
            digits(int): number of significant digits to keep
            outpath(str): path where to place reduced size file, defaults to the
                same path as input file
    """

    p=Path(fname)
    newsuffix="{}digits{}".format(digits,p.suffix)
    packedfile=p.parents[0] / "{}.{}".format(p.stem,newsuffix)
    if not Quiet: print("Rounding variables {}...".format(vlist))
    with Dataset("{}".format(p)) as src, Dataset("{}".format(packedfile), "w") as dst:
        # copy global attributes all at once via dictionary
        dst.setncatts(src.__dict__)
        # copy dimensions
        for name, dimension in src.dimensions.items():
            dst.createDimension(
                name, (len(dimension) if not dimension.isunlimited() else None))
        # copy all file data except for the excluded
        for name, variable in src.variables.items():
            attributes=src[name].__dict__
            fv=attributes.pop("_FillValue",None)
            data=src[name][:]
            if name not in vlist:
                if fv is None:
                    x = dst.createVariable(name,variable.datatype,variable.dimensions)
                else:
                    x = dst.createVariable(name,variable.datatype,variable.dimensions,fill_value=fv)
            else:
                if not Quiet: print("Rounding {}...".format(name))
                if fv is None:
                    x = dst.createVariable(name, 'f4',variable.dimensions,zlib=True,complevel=9,least_significant_digit=digits)
                else:
                    x = dst.createVariable(name, 'f4',variable.dimensions,zlib=True,complevel=9,least_significant_digit=digits,fill_value=fv)
            dst[name][:] = src[name][:]
            # copy variable attributes all at once via dictionary
            dst[name].setncatts(attributes)
    if not Quiet: print("Done.")
    return packedfilename

def netCDFPack(fname,vlist,outpath="",Quiet=False):
    """ Packs list of variables in input file into 16bits integers with scale and offset.
    Writes to file in outpath with same name as input file, but inserting the .Xdigits
    suffix before the filetype suffix.

    Args:
            filename(str): input netcdf file including path
            vlist(list of str): list of variables to round
            outpath(str): path where to place reduced size file, defaults to the
                same path as input file
            Quiet(bool): if False print log messages, otherwise operate quietly
    """

    p=Path(fname)
    bits=16
    newsuffix="{}bit{}".format(bits,p.suffix)
    packedfile=p.parents[0] / "{}.{}".format(p.stem,newsuffix)
    if not Quiet: print("Packing variables {}...".format(vlist))
    with Dataset("{}".format(p)) as src, Dataset("{}".format(packedfile), "w") as dst:
        # copy global attributes all at once via dictionary
        dst.setncatts(src.__dict__)
        # copy dimensions
        for name, dimension in src.dimensions.items():
            dst.createDimension(
                name, (len(dimension) if not dimension.isunlimited() else None))
        # copy all file data except for the excluded
        for name, variable in src.variables.items():
            attributes=src[name].__dict__
            fv=attributes.pop("_FillValue",None)
            #convert data to machine precision:
            dtp=type(0.)
            data=src[name][:].astype(dtp) #convert to 64bit floats for higher precision in scaling
            if name in vlist:
                if not Quiet: print("Packing {}...".format(name))
                dmin=data.min()
                dmax=data.max()
                N=2**bits
                N2=2**(bits-1)
                scale=(dmax-dmin)
                if fv is None:
                    x = dst.createVariable(name, 'i2',variable.dimensions,zlib=True,complevel=9)
                    scale/=(N-1) # scale data from -2**bits/2 to 2**bits/2 - 1
                    offset=dmin+N2*scale
                else:
                    fv=-N2 # Fill Value is minimum integer
                    x = dst.createVariable(name, 'i2',variable.dimensions,zlib=True,complevel=9,fill_value=fv)
                    scale/=(N-2)  # scale data from -2**bits/2 + 1 to 2**bits/2 - 1
                    offset=.5*(dmax+dmin)

                idata = rint((data-offset)/scale).astype('i2')
                if fv is None:
                    dst[name][:]=idata
                    dst[name].add_offset=offset
                    dst[name].scale_factor=scale
                else:
                    dst[name][:]=where(data[:].mask,fv,idata)
                    dst[name].add_offset=offset
                    dst[name].scale_factor=scale
            else:
                if fv is None:
                    x = dst.createVariable(name,variable.datatype,variable.dimensions)
                else:
                    x = dst.createVariable(name,variable.datatype,variable.dimensions,fill_value=fv)
                dst[name][:]=data
            # copy variable attributes all at once via dictionary
            dst[name].setncatts(attributes)
            if name in vlist:
                if "missing_value" in variable.__dict__:
                    print("Overwriting missing value...")
                    dst[name].missing_value=-N2
    if not Quiet: print("Done.")
    return packedfile

def ncdfPack():
    """
    Main entry-point function using argument parser.

    Example:
        `netCDFView -h`
    """
    import argparse
    parser = argparse.ArgumentParser(
        description='Pack selected variables of netcdf files into short integers.')
    parser.add_argument(
        'filename', type=str, nargs='?',
        help='Filename of the netfdf file to pack.'
        )
    parser.add_argument(
        '-v', '--variables', nargs="+", required=True,
        help='Variables to pack.')

    args = parser.parse_args()
    filename = args.filename
    vlist = args.variables
    if not filename:
        filename = ucstr(inpfunct('Give netCDF file name: '))
    nc = netCDFPack(filename, vlist)
    return nc


if __name__ == "__main__":
    nc = ncdfPack()
