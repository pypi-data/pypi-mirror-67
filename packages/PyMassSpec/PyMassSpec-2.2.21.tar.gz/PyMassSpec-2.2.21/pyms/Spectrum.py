"""
Classes to model Mass Spectra and Scans
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
import re

# 3rd party
import deprecation

# this package
from pyms import __version__
from pyms.Base import _list_types, pymsBaseClass
from pyms.Mixins import MassListMixin
from pyms.Utils.jcamp import xydata_tags


class Scan(pymsBaseClass, MassListMixin):
	"""
	Generic object for a single Scan's raw data

	:param mass_list: mass values
	:type mass_list: list
	:param intensity_list: intensity values
	:type intensity_list: list

	:authors: Andrew Isaac, Qiao Wang, Vladimir Likic, Dominic Davis-Foster (type assertions and properties)
	"""

	def __init__(self, mass_list, intensity_list):
		"""
		Initialise the class
		"""
		
		if not isinstance(mass_list, _list_types) or \
			not isinstance(mass_list[0], (int, float)):
			raise TypeError("'mass_list' must be a list of numbers")
		
		if not isinstance(intensity_list, _list_types) or \
			not isinstance(intensity_list[0], (int, float)):
			raise TypeError("'intensity_list' must be a list of numbers")
		
		if not len(mass_list) == len(intensity_list):
			raise ValueError("'mass_list' is not the same size as 'intensity_list'")
		
		self._mass_list = list(mass_list)
		self._intensity_list = list(intensity_list)
		self._min_mass = min(mass_list)
		self._max_mass = max(mass_list)
	
	def __len__(self):
		"""
		Returns the length of the object

		:rtype: int

		:authors: Andrew Isaac, Qiao Wang, Vladimir Likic
		"""
		
		return len(self._mass_list)
	
	def __eq__(self, other):
		"""
		Return whether this object is equal to another object

		:param other: The other object to test equality with
		:type other: object

		:rtype: bool
		"""
		
		if isinstance(other, self.__class__):
			return self._intensity_list == other.intensity_list \
					and self._mass_list == other.mass_list
		
		return NotImplemented
	
	def __copy__(self):
		"""Returns a copy of the object"""
		
		return self.__class__(self._mass_list[:], self._intensity_list[:])
	
	def __deepcopy__(self, memodict={}):
		return self.__copy__()
		
	def __dict__(self):
		return {
				"intensity_list": self.intensity_list,
				"mass_list": self.mass_list,
				}
	
	def __iter__(self):
		for key, value in self.__dict__().items():
			yield key, value
	
	def __getstate__(self):
		return self.__dict__()
	
	def __setstate__(self, state):
		self.__init__(**state)
	
	def iter_peaks(self):
		"""
		Iterate over the peaks in the mass spectrum
		"""
		
		for mz, intensity in zip(self.mass_list, self.intensity_list):
			yield mz, intensity
	
	@property
	def intensity_list(self):
		"""
		Returns a copy of the intensity list

		:rtype: list

		:authors: Qiao Wang, Andrew Isaac, Vladimir Likic
		"""
		
		return self._intensity_list[:]
	
	@property
	def mass_spec(self):
		"""
		Returns the intensity list

		:rtype: list

		:authors: Qiao Wang, Andrew Isaac, Vladimir Likic
		"""
		
		return self._intensity_list

	@deprecation.deprecated(deprecated_in="2.1.2", removed_in="2.2.0",
							current_version=__version__,
							details="Use :attr:`pyms.Spectrum.Scan.intensity_list` instead")
	def get_intensity_list(self):
		"""
		Returns the intensities for the current scan

		:rtype: list

		:authors: Qiao Wang, Andrew Isaac, Vladimir Likic
		"""
		
		return self.intensity_list
	
	@deprecation.deprecated(deprecated_in="2.1.2", removed_in="2.2.0",
							current_version=__version__,
							details="Use :attr:`pyms.Spectrum.Scan.min_mass` instead")
	def get_min_mass(self):
		"""
		Returns the minimum m/z value in the scan

		:rtype: float

		:author: Andrew Isaac
		"""
		
		return self.min_mass
	
	@deprecation.deprecated(deprecated_in="2.1.2", removed_in="2.2.0",
							current_version=__version__,
							details="Use :attr:`pyms.Spectrum.Scan.max_mass` instead")
	def get_max_mass(self):
		"""
		Returns the maximum m/z value in the scan

		:rtype: float

		:author: Andrew Isaac
		"""
		
		return self.max_mass
	
	@classmethod
	def from_dict(cls, dictionary):
		return cls(**dictionary)


class MassSpectrum(Scan):
	"""
	Models a binned mass spectrum

	:param mass_list: mass values
	:type mass_list: list
	:param intensity_list: intensity values
	:type intensity_list: list

	:authors: Andrew Isaac, Qiao Wang, Vladimir Likic, Dominic Davis-Foster (type assertions and properties)
	"""
	
	def __init__(self, mass_list, intensity_list):
		"""
		Initialise the class
		"""
		
		Scan.__init__(self, mass_list, intensity_list)
	
	@Scan.intensity_list.setter
	def intensity_list(self, value):
		"""
		Set the intensity values for the spectrum
		
		:param value: list of intensity value for each mass in `mass_list`
		:type value: list
		"""
		
		if not isinstance(value, _list_types) or not isinstance(value[0], (int, float)):
			raise TypeError("'intensity_list' must be a list of numbers")
		
		# if not len(self.mass_list) == len(value):
		# 	raise ValueError("'mass_list' and 'intensity_list' are not the same size")
		
		self._intensity_list = value
		
	@Scan.mass_spec.setter
	def mass_spec(self, value):
		"""
		Set the intensity values for the spectrum

		:param value: list of intensity value for each mass in `mass_list`
		:type value: list
		"""
		
		if not isinstance(value, _list_types) or not isinstance(value[0], (int, float)):
			raise TypeError("'intensity_list' must be a list of numbers")
		
		# if not len(self.mass_list) == len(value):
		# 	raise ValueError("'mass_list' and 'intensity_list' are not the same size")
		
		self._intensity_list = value
		
	@MassListMixin.mass_list.setter
	def mass_list(self, value):
		"""
		Set the mass values for the spectrum

		:param value: list of mass values for the spectrum
		:type value: list
		"""
		
		if not isinstance(value, _list_types) or not isinstance(value[0], (int, float)):
			raise TypeError("'mass_list' must be a list of numbers")
		
		# if not len(self.mass_list) == len(value):
		# 	raise ValueError("'mass_list' and 'intensity_list' are not the same size")
		
		self._mass_list = value
	
	def crop(self, min_mz=None, max_mz=None, inplace=False):
		"""
		Crop the Mass Spectrum between the given mz values
		
		:param min_mz: The minimum mz for the new mass spectrum
		:type min_mz: int or float, optional
		:param max_mz: The maximum mz for the new mass spectrum
		:type max_mz: int or float, optional
		:param inplace: Whether the cropping should be applied this instance or to a copy (default behaviour).
		:type inplace: bool, optional
		
		:return: The cropped Mass Spectrum
		:rtype: :class:`pyms.Spectrum.MassSpectrum`
		"""
		
		if min_mz is None:
			min_mz = self.min_mass
		
		if max_mz is None:
			max_mz = self.max_mass
			
		min_mz_idx = self.intensity_list.index(min_mz)
		max_mz_idx = self.intensity_list.index(max_mz)+1
		
		return self.icrop(min_mz_idx, max_mz_idx, inplace)
		
	def icrop(self, min_index=0, max_index=-1, inplace=False):
		"""
		Crop the Mass Spectrum between the given indices
		
		:param min_index: The minimum index for the new mass spectrum
		:type min_index: int or float, optional
		:param max_index: The maximum index for the new mass spectrum
		:type max_index: int or float, optional
		:param inplace: Whether the cropping should be applied this instance or to a copy (default behaviour).
		:type inplace: bool, optional
		
		:return: The cropped Mass Spectrum
		:rtype: :class:`pyms.Spectrum.MassSpectrum`
		"""
		
		cropped_intensity_list = self.intensity_list[min_index:max_index]
		cropped_mass_list = self.mass_list[min_index:max_index]
		
		if inplace:
			self.intensity_list = cropped_intensity_list
			self.mass_list = cropped_mass_list
			return self
		else:
			return MassSpectrum(
					intensity_list=cropped_intensity_list,
					mass_list=cropped_intensity_list,
					)
		
	def n_largest_peaks(self, n):
		"""
		Returns the indices of the n largest peaks in the Mass Spectrum
		
		:param n: The number of peaks to return the indices for
		:type n:
		:return:
		:rtype:
		"""
		
		# Make copies of the intensity_list
		intensity_list = self.intensity_list
		
		largest_indices = []
		
		for i in range(0, n):
			max_int_index = max(range(len(intensity_list)), key=intensity_list.__getitem__)
			
			del intensity_list[max_int_index]
			
			largest_indices.append(max_int_index)
		
		return largest_indices
	
	def get_intensity_for_mass(self, mass):
		"""
		Returns the intensity for the given mass.
		
		:param mass:
		:type mass:
		
		:return:
		:rtype:
		"""
		
		mass_idx = self._mass_list.index(mass)
		return self._intensity_list[mass_idx]

	def get_mass_for_intensity(self, intensity):
		"""
		Returns the mass for the given intensity.
		If more than one mass has the given intensity, the first mass is returned.
		
		:param intensity:
		:type intensity:
		
		:return:
		:rtype:
		"""
		
		intensity_idx = self._intensity_list.index(intensity)
		return self._mass_list[intensity_idx]
	
	@classmethod
	def from_jcamp(cls, file_name):
		"""
		Create a MassSpectrum from a JCAMP-DX file

		:param file_name: Path of the file to read
		:type file_name: str or pathlib.Path

		:return: MassSpectrum
		:rtype: :class:`pyms.Spectrum.MassSpectrum`

		:authors: Qiao Wang, Andrew Isaac, Vladimir Likic, David Kainer, Dominic Davis-Foster
		"""
		
		if not isinstance(file_name, (str, pathlib.Path)):
			raise TypeError("'file_name' must be a string or a pathlib.Path object")
		
		if not isinstance(file_name, pathlib.Path):
			file_name = pathlib.Path(file_name)
		
		print(f" -> Reading JCAMP file '{file_name}'")
		lines_list = file_name.open('r')
		xydata = []
		last_tag = None
		
		for line in lines_list:
			
			if len(line.strip()):
				if line.startswith("##"):
					# key word or information
					fields = line.split('=', 1)
					current_tag = fields[0] = fields[0].lstrip("##").upper()
					last_tag = fields[0]
					
					if current_tag.upper().startswith("END"):
						break
				
				else:
					if last_tag in xydata_tags:
						line_sub = re.split(",| ", line.strip())
						for item in line_sub:
							if not len(item.strip()) == 0:
								xydata.append(float(item.strip()))
		
		# By this point we should have all of the xydata
		if len(xydata) % 2 == 1:
			# TODO: This means the data is not in x, y pairs
			#  Make a better error message
			raise ValueError("data not in pair !")
		
		mass_list = []
		intensity_list = []
		for i in range(len(xydata) // 2):
			mass_list.append(xydata[i * 2])
			intensity_list.append(xydata[i * 2 + 1])
		
		return cls(mass_list, intensity_list)
	
	@classmethod
	def from_mz_int_pairs(cls, mz_int_pairs):
		"""
		Construct a MassSpectrum from a list of (m/z, intensity) tuples.
		
		:param mz_int_pairs:
		:type mz_int_pairs: list of tuple
		"""
		
		err_msg = "`mz_int_pairs` must be a list of (m/z, intensity) tuples."
		
		if (
				not isinstance(mz_int_pairs, _list_types)
				or not isinstance(mz_int_pairs[0], _list_types)
				# or not isinstance(mz_int_pairs[0][0], (int, float))
			):
			raise TypeError(err_msg)
		
		if not len(mz_int_pairs[0]) == 2:
			raise ValueError(err_msg)
		
		mass_list = []
		intensity_list = []
		for mass, intensity in mz_int_pairs:
			mass_list.append(float(mass))
			intensity_list.append(float(intensity))
	
		return cls(mass_list, intensity_list)
		

def normalize_mass_spec(mass_spec, relative_to=None, inplace=False, max_intensity=100):
	"""
	Normalize the intensities in the given Mass Spectrum to values between 0 and ``max_intensity``,
	which by default is 100.0.

	:param mass_spec: The Mass Spectrum to normalize
	:type mass_spec: :class:`pyms.Spectrum.MassSpectrum`
	:param relative_to: The largest intensity in the original data set.
		If not None the intensities are computed relative to this value.
		If None the value is calculated from the mass spectrum.
		This can be useful when normalizing several mass spectra to each other.
	:type relative_to: int or float
	:param inplace: Whether the normalization should be applied to the
		:class:`~pyms.Spectrum.MassSpectrum` object given, or to a copy (default behaviour).
	:type inplace: bool, optional.
	:param max_intensity: The maximum intensity in the normalized spectrum.
		If omitted the range 0-100.0 is used.
		If an integer the normalized intensities will be integers.
	:type max_intensity: int, float
	:return: The normalized mass spectrum
	:rtype: :class:`pyms.Spectrum.MassSpectrum`
	"""
	
	if relative_to is None:
		relative_to = max(mass_spec.intensity_list)
	
	normalized_intensity_list = [
			(x / float(relative_to)) * max_intensity
			for x in mass_spec.intensity_list]
	
	if isinstance(max_intensity, int):
		normalized_intensity_list = [round(x) for x in normalized_intensity_list]
	
	if inplace:
		mass_spec.intensity_list = normalized_intensity_list
		return mass_spec
	else:
		normalized_mass_spec = MassSpectrum(mass_spec.mass_list, normalized_intensity_list)
		
		return normalized_mass_spec
