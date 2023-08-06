# coding: utf-8
# /*##########################################################################
#
# Copyright (c) 2015-2020 European Synchrotron Radiation Facility
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
# ###########################################################################*/

"""
This module provides global definitions and methods to transform
a tomo dataset written in edf into and hdf5/nexus file
"""

__authors__ = ["C. Nemoz", "H. Payno", "A.Sole"]
__license__ = "MIT"
__date__ = "16/01/2020"

import os
import fabio
import numpy
import h5py
import logging
from nxtomomill import utils
from nxtomomill import converter
from tomoscan.esrf.edfscan import EDFTomoScan
from ..utils import Progress


logging.basicConfig(level=logging.INFO)
_logger = logging.getLogger(__name__)


MOTOR_POS = 'motor_pos'

MOTOR_MNE = 'motor_mne'

ROT_ANGLE = "srot"
X_TRANS = "sx"
Y_TRANS = "sy"
Z_TRANS = "sz"


TO_IGNORE = ['HST', '_slice_']
TO_IGNORE = ['_slice_']

DARK_NAME = ['darkend', 'dark']

REFS_NAME = ['ref', 'refHST']

key_proj = 0
key_flat = 1
key_dark = 2
key_return = -1

def main(argv):
    """
    """
    import argparse
    parser = argparse.ArgumentParser(description='convert data acquired as '
                                                 'edf to hdf5 - nexus '
                                                 'compliant file format.')
    parser.add_argument('scan_path', help='folder containing the edf files')
    parser.add_argument('output_file', help='foutput .h5 file')
    parser.add_argument('--file_extension',
                        action="store_true",
                        default='.h5',
                        help='extension of the output file. Valid values are '
                             '' + '/'.join(utils.FileExtension.values()))
    print('******set up***********')
    options = parser.parse_args(argv[1:])
    # inputDir = '/lbsram/hair_A1_50nm_tomo3_1_'

    input_dir = options.scan_path
    scan = EDFTomoScan(input_dir)
    print('input_dir is', input_dir)

    # in old data, rot ange is unknown. Compute it as a function of the proj number
    compute_rotangle = True

    fileout_h5 = utils.get_file_name(file_name=options.output_file,
                                     extension=options.file_extension,
                                     check=True)
    _logger.info("Output file will be " + fileout_h5)
    
    DARK_ACCUM_FACT = True
    with h5py.File(fileout_h5, "w") as h5d:
        proj_urls = scan.get_proj_urls(scan=scan.path)
        
        for dark_to_find in DARK_NAME:
            dk_urls = scan.get_darks_url(scan_path=scan.path,
                                     prefix=dark_to_find)
            if len(dk_urls) > 0:
                if dark_to_find == 'dark':
                    DARK_ACCUM_FACT = False
                break
        
        for refs_to_find in REFS_NAME:
            if refs_to_find == 'ref':
                TO_IGNORE.append('HST')
            else:
                TO_IGNORE.remove('HST')
            refs_urls = scan.get_refs_url(scan_path=scan.path,
                                      prefix=refs_to_find,
                                      ignore=TO_IGNORE)
            if len(refs_urls) > 0:
                break
                                                   
        n_frames = len(proj_urls) + len(refs_urls) + len(dk_urls)

        # TODO: should be managed by tomoscan as well
        def getExtraInfo(scan):
            projections_urls = scan.projections
            indexes = sorted(projections_urls.keys())
            first_proj_file = projections_urls[indexes[0]]
            fid = fabio.open(first_proj_file.file_path())
            hd = fid.getHeader()
            try:
                rotangle_index = hd[MOTOR_MNE].split(' ').index(ROT_ANGLE)
            except:
                rotangle_index = -1
            try:
                xtrans_index = hd[MOTOR_MNE].split(' ').index(X_TRANS)
            except:
                xtrans_index = -1
            try:
                ytrans_index = hd[MOTOR_MNE].split(' ').index(Y_TRANS)
            except:
                ytrans_index = -1
            try:
                ztrans_index = hd[MOTOR_MNE].split(' ').index(Z_TRANS)
            except:
                ztrans_index = -1

            frame_type = fid.getByteCode()
            return frame_type, rotangle_index, xtrans_index, ytrans_index, ztrans_index

        frame_type, rot_angle_index, x_trans_index, y_trans_index, z_trans_index = getExtraInfo(scan=scan)
        
        data_dataset = h5d.create_dataset("/entry/instrument/detector/data",
                                          shape=(n_frames, scan.dim_2, scan.dim_1),
                                          dtype=frame_type)

        keys_dataset = h5d.create_dataset("/entry/instrument/detector/image_key",
                                          shape=(n_frames,),
                                          dtype=numpy.int32)
        
        keys_control_dataset = h5d.create_dataset("/entry/instrument/detector/image_key_control",
                                          shape=(n_frames,),
                                          dtype=numpy.int32)

        h5d["/entry/sample/name"] = os.path.basename(scan.path)

        proj_angle = scan.scan_range/scan.tomo_n

        distance = scan.retrieve_information(scan=os.path.abspath(scan.path),
                                             ref_file=None,
                                             key='Distance',
                                             type_=float,
                                             key_aliases=['distance', ])

        h5d["/entry/instrument/detector/distance"] = distance
        h5d["/entry/instrument/detector/distance"].attrs["unit"] = u"m"

        pixel_size = scan.retrieve_information(scan=os.path.abspath(scan.path),
                                               ref_file=None,
                                               key='PixelSize',
                                               type_=float,
                                               key_aliases=['pixelSize', ])
        h5d["/entry/instrument/detector/x_pixel_size"] = pixel_size
        h5d["/entry/instrument/detector/x_pixel_size"].attrs["unit"] = u"mm"
        h5d["/entry/instrument/detector/y_pixel_size"] = pixel_size
        h5d["/entry/instrument/detector/y_pixel_size"].attrs["unit"] = u"mm"

        energy = scan.retrieve_information(scan=os.path.abspath(scan.path),
                                               ref_file=None,
                                               key='Energy',
                                               type_=float,
                                               key_aliases=['energy', ])
        h5d["/entry/beam/incident_energy"] = energy
        h5d["/entry/beam/incident_energy"].attrs["unit"] = u"keV"

        # rotations values
        rotation_dataset = h5d.create_dataset("/entry/sample/rotation_angle",
                                              shape=(n_frames,),
                                              dtype=numpy.float32)

        # provision for centering motors
        x_dataset = h5d.create_dataset("/entry/sample/x_translation",
                                       shape=(n_frames,),
                                       dtype=numpy.float32)
        y_dataset = h5d.create_dataset("/entry/sample/y_translation",
                                       shape=(n_frames,),
                                       dtype=numpy.float32)
        z_dataset = h5d.create_dataset("/entry/sample/z_translation",
                                       shape=(n_frames,),
                                       dtype=numpy.float32)

        #  --------->  and now fill all datasets!

        nf = 0

        def read_url(url) -> tuple:
            data_slice = url.data_slice()
            if data_slice is None:
                data_slice = (0,)
            if data_slice is None or len(data_slice) != 1:
                raise ValueError("Fabio slice expect a single frame, "
                                 "but %s found" % data_slice)
            index = data_slice[0]
            if not isinstance(index, int):
                raise ValueError("Fabio slice expect a single integer, "
                                 "but %s found" % data_slice)

            try:
                fabio_file = fabio.open(url.file_path())
            except Exception:
                _logger.debug("Error while opening %s with fabio",
                              url.file_path(), exc_info=True)
                raise IOError("Error while opening %s with fabio (use debug"
                              " for more information)" % url.path())

            if fabio_file.nframes == 1:
                if index != 0:
                    raise ValueError(
                        "Only a single frame available. Slice %s out of range" % index)
                data = fabio_file.data
                header = fabio_file.header
            else:
                data = fabio_file.getframe(index).data
                header = fabio_file.getframe(index).header

            fabio_file.close()
            fabio_file = None
            return data, header

        progress = Progress('write dark')
        progress.set_max_advancement(len(dk_urls))

        def ignore(file_name):
            for forbid in TO_IGNORE:
                if forbid in file_name:
                    return True
            return False

        # darks        
        
        #dark in acumulation mode?
        norm_dark = 1.
        if scan.dark_n > 0 and DARK_ACCUM_FACT is True:
            norm_dark = len(dk_urls)/scan.dark_n
        dk_indexes = sorted(dk_urls.keys())
        progress.set_max_advancement(len(dk_urls))
        for dk_index in dk_indexes:
            dk_url = dk_urls[dk_index]
            if ignore(os.path.basename(dk_url.file_path())):
                _logger.info('ignore ' + dk_url.file_path())
                continue
            data, header = read_url(dk_url)
            data_dataset[nf, :, :] = data * norm_dark
            keys_dataset[nf] = key_dark
            keys_control_dataset[nf] = key_dark
            
            if MOTOR_POS in header:
                str_mot_val = header[MOTOR_POS].split(' ')
                if rot_angle_index == -1:
                    rotation_dataset[nf] = 0.
                else:
                    rotation_dataset[nf] = float(str_mot_val[rot_angle_index])
                if x_trans_index == -1:
                    x_dataset[nf] = 0.
                else:
                    x_dataset[nf] = float(str_mot_val[x_trans_index])
                if y_trans_index == -1:
                    y_dataset[nf] = 0.
                else:
                    y_dataset[nf] = float(str_mot_val[y_trans_index])
                if z_trans_index == -1:
                    z_dataset[nf] = 0.
                else:
                    z_dataset[nf] = float(str_mot_val[z_trans_index])
                
            nf += 1
            progress.increase_advancement(i=1)
            
        ref_indexes = sorted(refs_urls.keys())

        ref_projs = []
        for irf in ref_indexes:
            pjnum = int(irf)
            if pjnum not in ref_projs:
                ref_projs.append(pjnum)
                         
        # refs
        def store_refs(refIndexes, tomoN, projnum, refUrls, nF, dataDataset, keysDataset, keysCDataset, xDataset, yDataset, zDataset, rotationDataset, raix, xtix, ytix, ztix):
            nfr=nF
            progress = Progress('write refs')
            progress.set_max_advancement(len(refIndexes))        
            for ref_index in refIndexes:
                int_rf = int(ref_index)
                test_val=0
                if int_rf == projnum:
                    refUrl = refUrls[ref_index]
                    if ignore(os.path.basename(refUrl.file_path())):
                        _logger.info('ignore ' + refUrl.file_path())
                        continue
                    data, header = read_url(refUrl)
                    dataDataset[nfr, :, :] = data+test_val
                    keysDataset[nfr] = key_flat
                    keysCDataset[nfr] = key_flat
                    if MOTOR_POS in header:
                        str_mot_val = header[MOTOR_POS].split(' ')
                        if raix == -1:
                            rotationDataset[nfr] = 0.
                        else:
                            rotationDataset[nfr] = float(str_mot_val[raix])
                        if xtix == -1:
                            xDataset[nfr] = 0.
                        else:
                            xDataset[nfr] = float(str_mot_val[xtix])
                        if ytix == -1:
                            yDataset[nfr] = 0.
                        else:
                            yDataset[nfr] = float(str_mot_val[ytix])
                        if ztix == -1:
                            zDataset[nfr] = 0.
                        else:
                            zDataset[nfr] = float(str_mot_val[ztix])

                    nfr += 1
                    progress.increase_advancement(i=1)
            return nfr

        # projections
        import datetime
        proj_indexes = sorted(proj_urls.keys())
        progress = Progress('write projections')
        progress.set_max_advancement(len(proj_indexes))
        nproj=0
        iref_pj = 0

        for proj_index in proj_indexes:
            proj_url = proj_urls[proj_index]
            if ignore(os.path.basename(proj_url.file_path())):
                _logger.info('ignore ' + proj_url.file_path())
                continue
            
            # store refs if the ref serial number is = projection number
            if iref_pj < len(ref_projs) and ref_projs[iref_pj] == nproj:
                nf = store_refs(ref_indexes, scan.tomo_n,
                                ref_projs[iref_pj], 
                                refs_urls, 
                                nf, 
                                data_dataset, keys_dataset, keys_control_dataset,
                                x_dataset, y_dataset, z_dataset, rotation_dataset, 
                                rot_angle_index, x_trans_index, y_trans_index, z_trans_index)
                iref_pj += 1
            data, header = read_url(proj_url)

            data_dataset[nf, :, :] = data
            keys_dataset[nf] = key_proj
            keys_control_dataset[nf] = key_proj
            if nproj >= scan.tomo_n:
                keys_control_dataset[nf] = key_return
            
            if MOTOR_POS in header:
                str_mot_val = header[MOTOR_POS].split(' ')

                # continuous scan - rot angle is unknown. Compute it
                if compute_rotangle is True and nproj < scan.tomo_n:
                    rotation_dataset[nf] = nproj*proj_angle
                else:
                    if rot_angle_index == -1:
                        rotation_dataset[nf] = 0.
                    else:
                        rotation_dataset[nf] = float(str_mot_val[rot_angle_index])
                
                if x_trans_index == -1:
                    x_dataset[nf] = 0.
                else:
                    x_dataset[nf] = float(str_mot_val[x_trans_index])
                if y_trans_index == -1:
                    y_dataset[nf] = 0.
                else:
                    y_dataset[nf] = float(str_mot_val[y_trans_index])
                if z_trans_index == -1:
                    z_dataset[nf] = 0.
                else:
                    z_dataset[nf] = float(str_mot_val[z_trans_index])

            nf += 1
            nproj+=1
                                            
            progress.increase_advancement(i=1)

        # store last flat if any remaining in the list
        if iref_pj < len(ref_projs):
            nf = store_refs(ref_indexes, scan.tomo_n,
                            ref_projs[iref_pj], 
                            refs_urls, 
                            nf, 
                            data_dataset, keys_dataset, keys_control_dataset,
                            x_dataset, y_dataset, z_dataset, rotation_dataset, 
                            rot_angle_index, x_trans_index, y_trans_index, z_trans_index)
                            
        # we can add some more NeXus look and feel
        h5d["/entry"].attrs["NX_class"] = u"NXentry"
        h5d["/entry"].attrs["definition"] = u"NXtomo"
        h5d["/entry"].attrs["version"] = converter.CURRENT_OUTPUT_VERSION
        h5d["/entry/instrument"].attrs["NX_class"] = u"NXinstrument"
        h5d["/entry/instrument/detector"].attrs["NX_class"] = u"NXdetector"
        h5d["/entry/instrument/detector/data"].attrs["interpretation"] = u"image"
        h5d["/entry/sample"].attrs["NX_class"] = u"NXsample"

        h5d.flush()
    exit(0)


if __name__ == "__main__":
    import sys
    main(sys.argv[1:])
