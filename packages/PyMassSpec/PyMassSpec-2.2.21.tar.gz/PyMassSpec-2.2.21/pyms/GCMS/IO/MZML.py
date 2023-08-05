"""
Functions for reading mzML format data files
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

# 3rd party
import pymzml

try:
	from mpi4py import MPI
except ModuleNotFoundError:
	pass

# this package
from pyms.GCMS.Class import GCMS_data
from pyms.Spectrum import Scan


def mzML_reader(file_name):
	"""
	A reader for mzML files

	:param file_name: The name of the mzML file
	:type file_name: str or pathlib.Path

	:return: GC-MS data object
	:rtype: :class:`pyms.GCMS.Class.GCMS_data`

	:author: Sean O'Callaghan
	:author: Dominic Davis-Foster (pathlib support)
	"""
	
	if not isinstance(file_name, (str, pathlib.Path)):
		raise TypeError("'file_name' must be a string or a pathlib.Path object")
	
	mzml_file = pymzml.run.Reader(str(file_name))
	
	try:  # avoid printing from each rank
		comm = MPI.COMM_WORLD
		rank = comm.Get_rank()
		size = comm.Get_size()
		
		if rank == 0:
			file_names = []
			
			for i in range(1, size):
				recv_buffer = ""
				file_n = comm.recv(recv_buffer, i)
				file_names.append(file_n)
			
			print(" -> Reading mzML files:")
			print(file_name)
			for file_n in file_names:
				print(file_n)
		else:
			comm.send(file_name, dest=0)
	# TODO: Find specific error
	except Exception as e:
		print(e)
		print(f" -> Reading mzML file '{file_name}'")
	
	scan_list = []
	time_list = []
	
	for spectrum in mzml_file:
		mass_list = []
		intensity_list = []
		
		for mz, i in spectrum.peaks:
			mass_list.append(mz)
			intensity_list.append(i)
		
		# scan_list.append(Scan(mass_list, intensity_list))
		for element in spectrum.xmlTree:
			# For some reason there are spectra with no time value,
			# Ignore these????????????
			if element.get('accession') == "MS:1000016":  # time value
				# We need time in seconds not minutes
				time_list.append(60 * float(element.get('value')))
				scan_list.append(Scan(mass_list, intensity_list))
	
	# print("time:", len(time_list))
	# print("scan:", len(scan_list))
	
	data = GCMS_data(time_list, scan_list)
	
	return data
