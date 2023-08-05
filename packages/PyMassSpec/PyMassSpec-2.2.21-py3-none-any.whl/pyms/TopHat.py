"""
Top-hat baseline corrector
"""

################################################################################
#                                                                              #
#    PyMassSpec software for processing of mass-spectrometry data              #
#    Copyright (C) 2005-2012 Vladimir Likic                                    #
#    Copyright (C) 2019-2020 Dominic Davis-Foster                              #
#                                                                              #
#    This program is free software; you can redistribute it and/or modify      #
#    it under the terms of the GNU General Public License version 2 as         #
#    published by the Free Software Foundation.                                #
#                                                                              #
#    This program is distributed in the hope that it will be useful,           #
#    but WITHOUT ANY WARRANTY; without even the implied warranty of            #
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the             #
#    GNU General Public License for more details.                              #
#                                                                              #
#    You should have received a copy of the GNU General Public License         #
#    along with this program; if not, write to the Free Software               #
#    Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.                 #
#                                                                              #
################################################################################

# stdlib
import copy

# 3rd party
import numpy
from scipy import ndimage

# this package
from pyms.GCMS.Function import ic_window_points
from pyms.IntensityMatrix import IntensityMatrix
from pyms.IonChromatogram import IonChromatogram


# default structural element as a fraction of total number of points
_STRUCT_ELM_FRAC = 0.2


def tophat(ic, struct=None):
    """
    Top-hat baseline correction on Ion Chromatogram

    :param ic: The input ion chromatogram
    :type ic: pyms.IonChromatogram.IonChromatogram
    :param struct: Top-hat structural element as time string
    :type struct: int or str or NoneType, optional

    :return: Top-hat corrected ion chromatogram
    :rtype: pyms.IonChromatogram.IonChromatogram

    :author: Woon Wai Keen
    :author: Vladimir Likic
    :author: Dominic Davis-Foster (type assertions)
    """
    
    if not isinstance(ic, IonChromatogram):
        raise TypeError("'ic' must be an IonChromatogram object")
    ia = copy.deepcopy(ic.intensity_array)
    
    if struct:
        struct_pts = ic_window_points(ic, struct)
    else:
        struct_pts = int(round(ia.size * _STRUCT_ELM_FRAC))
    
    #    print(" -> Top-hat: structural element is %d point(s)" % ( struct_pts ))
    
    str_el = numpy.repeat([1], struct_pts)
    ia = ndimage.white_tophat(ia, None, str_el)
    
    ic_bc = copy.deepcopy(ic)
    ic_bc.intensity_array = ia
    
    return ic_bc


def tophat_im(im, struct=None):
    """
    Top-hat baseline correction on Intensity Matrix

        Wraps around the TopHat function above

    :param im: The input Intensity Matrix
    :type im: pyms.IntensityMatrix.IntensityMatrix
    :param struct: Top-hat structural element as time string
    :type struct: str

    :return: Top-hat corrected IntensityMatrix Matrix
    :rtype: pyms.IntensityMatrix.IntensityMatrix
    
    :author: Sean O'Callaghan
    """
    
    if not isinstance(im, IntensityMatrix):
        raise TypeError("'im' must be an IntensityMatrix object")

    n_scan, n_mz = im.size
    
    im_smooth = copy.deepcopy(im)
    
    for ii in range(n_mz):
        ic = im_smooth.get_ic_at_index(ii)
        ic_smooth = tophat(ic, struct)
        im_smooth.set_ic_at_index(ii, ic_smooth)
    
    return im_smooth
