"""
Base for PyMassSpec classes
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
import pathlib
import pickle

# 3rd party
import numpy

# this package
from pyms.Utils.IO import prepare_filepath

_list_types = (list, tuple, numpy.core.ndarray)
_path_types = (str, pathlib.Path)


class pymsBaseClass:
	"""
	Base class
	"""
	def dump(self, file_name, protocol=3):
		"""
		Dumps an object to a file through pickle.dump()

		:param file_name: Name of the file for the object dump
		:type file_name: str or pathlib.Path
		:param protocol: The pickle protocol to use. Default 3
		:type protocol: int, optional

		:author: Vladimir Likic
		:author: Dominic Davis-Foster (pathlib and pickle protocol support)
		"""
		
		if not isinstance(file_name, _path_types):
			raise TypeError("'file_name' must be a string or a pathlib.Path object")
		
		file_name = prepare_filepath(file_name)
		
		fp = file_name.open('wb')
		pickle.dump(self, fp, protocol=protocol)
		fp.close()
