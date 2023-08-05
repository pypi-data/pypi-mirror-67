#-*-coding:utf-8-*-
from Crypto.Cipher import AES as AES_
from Crypto.Util.Padding import pad, unpad
from Crypto.Hash import SHA256,SHA1,MD5,SHA224
from Crypto import Random
from Crypto.Util.RFC1751 import english_to_key

from shaonutil.security import generateCryptographicallySecureRandomString
from base64 import b64encode,b64decode
from uuid import UUID
from io import BytesIO

import hashlib
import shaonutil
import binascii
import os
import struct




__RANDOM__ = True
__KILO_BYTE__ = 1024 # 1024 bytes = 1 kilo byte
__byte__ = 8


class AES:
	"""
		chunksize:
			Sets the size of the chunk which the function uses to read and encrypt the file
			Larger chunk sizes can be faster for some files and machines.
			chunksize must be divisible by 16.
	"""
	
	"""To Do: avoid appending filesize in begining, rather hide in middle or else"""
	## Rules to maintain for AES
	# Data must be padded to 16 byte boundary in CBC mode, so padding is used
	# key must be 16, 24, 32 for 128,192,256 bit encryption
	# initialization vector length 16
	"""
	 When Decryption : all the chunk size is multiple of 16 bytes because,
	 				   As when AES encryption happend All data was read to
	 				   multiple of or equal to 16 bytes and then encrypted.
	"""


	## Method
	# if iv is not passed during initialization then randomly generated
	# check sum is added at last of string and then encrypts the string
	# if iv is not passed , it is added at last of encrypted string
	# has_iv state is added at last of string





	"""
	use SHA-256 over our key to get a proper-sized AES key from any size of string bytes, output length 32
	- For AES 256 is encryption
	Keep in mind that this 32-byte key only has as much entropy as your original password.
	So be wary of brute-force password guessing,
	and pick a relatively strong password (kitty probably won't do).
	What's useful about this technique is that you don't have to worry about manually padding your password
	SHA-256 will scramble a 32-byte block out of any password for you.
	"""
	#key = SHA256.new(key).digest() 
	"""
	For maximal security, the IV should be randomly generated for every new encryption and
	can be stored together with the ciphertext.
	Knowledge of the IV won't help the attacker crack your encryption.
	What can help him, however, is your reusing the same IV with the same encryption key for multiple encryptions.
	"""
	#iv = ''.join(chr(random.randint(0, 0xFF)) for i in range(16))




	def __init__(self,KEY,IV='',bit=256,log=True):
		# AES Block Size = 16 bit print(AES_.block_size)
		self.log = log
		self.has_iv_str_block_length = 16 # Part of user configuration
		self.check_sum=True # Part of user configuration
		self.check_sum_str_length = 32
		self.stringify_enable = True

		self.bit = bit
		# if storing key in object is safe or it can be read from cracking process
		# at least key can not be empty in first initialization, handle generate random and save key
		self.new(key=KEY,iv=IV)

	def new(self,key='',iv=''):

		if key != '' and iv != '':
			key,iv = self.process_keys(bit=self.bit,key=key,iv=iv)
			self.check_keys(bit=self.bit,key=key,iv=iv)
		elif key == '' and iv == '':
			key = self.KEY
			iv = self.IV
		elif key != '':
			# key is not empty
			key = self.process_keys(key=key,bit=self.bit)
			self.check_keys(key=key,bit=self.bit)
			# iv must be empty then
			try:
				iv = self.IV
			except:
				# when iv is not passed on initialization of class
				iv = os.urandom(AES_.block_size)
			# here
		elif iv != '':
			iv = self.process_keys(iv=iv,bit=self.bit)
			self.check_keys(iv=iv,bit=self.bit)
			# key must be empty then
			key = self.KEY
			

		self.aes = AES_.new(key, AES_.MODE_CBC, iv)
		self.KEY = key
		self.IV = iv


	def check_keys(self,bit,key='',iv=''):
		if iv != '':		
			if len(iv) != AES_.block_size : raise ValueError("Initialization Vector must be 16 characters long")
		if key != '':
			key_length = len(key)
			if not (key_length == 1*AES_.block_size or key_length == 1.5*AES_.block_size or key_length == 2*AES_.block_size): raise ValueError("Key length needs to be 16/24/32 characters long or 16/24/32 bytes long, depending if we want to use AES-128, AES-192 or AES-256 respectively")
			if bit == 256 and key_length != 2*AES_.block_size:
				raise ValueError(f'AES-256 encryption needs the key to be 32 characters long. {key_length} characters long key given.')
			elif bit == 192 and key_length != 1.5*AES_.block_size:
				raise ValueError(f'AES-192 encryption needs the key to be 24 characters long. {key_length} characters long key given.')
			elif bit == 128 and key_length != 1*AES_.block_size:
				raise ValueError(f'AES-128 encryption needs the key to be 16 characters long. {key_length} characters long key given.')
		if iv == '' and key == '':
			raise ValueError("Both key and iv can not be empty in check_keys")
		"""
		AES Encryption bits depends on key size
		Ex - 32 byte or 32 chracter long password creates 32*8 = 256 bit encryption so get 32 byte long key we use sha256 which gives 32 byte long hash always
		Key Round and key schedule ?
		"""
		# my assumption
		"""
		AES Encryption bits depends on key size
		Ex - 32 byte or 32 chracter long password creates 32*8 = 256 bit encryption so get 32 byte long key we use sha256 which gives 32 byte long hash always
		Key Round and key schedule ?

		 32*8 = 256
		 24*8 = 192
		 16*8 = 128

		SHA256 = 512 bits - 32 byte or character length
		         192 bits - 24 byte or character length ?
		 MD5 =   128 bits - 16 byte or character length

		 192 bits hashing algorithm needed - SHA224 bits - 28 bytes - cut to 24 bytes
		"""

		

	def process_keys(self,bit,key='',iv=''):
		if key != '':
			key = key.encode('ascii')

			if bit == 256:
				#256/8 = 32 byte or character key
				key = SHA256.new(key).digest() # use SHA-256 over our key to get a proper-sized AES key from any size of string bytes, output length 32
			elif bit == 192:
				#128/8 = 16 byte or character key
				key = SHA224.new(key).digest()[:-4] # 28 character to 24 character
			elif bit == 128:
				#128/8 = 16 byte or character key
				key = MD5.new(key).digest()
		

		if iv != '':
			if type(iv) == str: iv = iv.encode('ascii')
			
			self.has_iv = False
			
		else:
			self.has_iv = True
			#print("Needs to mix iv with encrypted text at starting.")
			
		

		if key != '' and iv != '':
			return key,iv
		elif key != '':
			return key
		elif iv != '':
			return iv
		else:
			raise ValueError("No parameter given to process.")

	def get_has_iv_str_length(self,PARSE_PARAM):
		int_sum = sum( [ int(i) for i in PARSE_PARAM[:self.has_iv_str_block_length] ] )
		# Added +1 at end for avoiding 0 sum
		# Added -1 from divisor. So, it will never exced the desire block length.
		reminder = int_sum % (self.has_iv_str_block_length - 1) + 1
		return reminder

	def parse_has_iv_combined(self,filebuffer_or_bytesio,input_buffersize):
		"""Parse has_iv from encrypted buffer"""
		# data_type = file/str

		if self.log : print("Log : has_iv state has been extracted.")
		has_iv_str_length = self.get_has_iv_str_length(self.KEY)
		EN_ = self.KEY[:self.has_iv_str_block_length]
		# 20 byte{ripemd160/sha1} encription hash but taken 16 byte{has_iv_str_block_length} so that actual algorithm of hashing is not revealed
		hash_algo1 = 'sha1'
		h = hashlib.new(hash_algo1)
		h.update(EN_) #b"byte"
		has_iv_str1 = h.digest()[:has_iv_str_length]

		hash_algo2 = 'ripemd160'
		h = hashlib.new(hash_algo2)
		h.update(EN_) #b"byte"
		has_iv_str2 = h.digest()[:has_iv_str_length]


		encrypted_filesize = input_buffersize
		St_ = encrypted_filesize - has_iv_str_length
		previous_position = filebuffer_or_bytesio.tell()
		filebuffer_or_bytesio.seek(St_)
		has_iv_str = filebuffer_or_bytesio.read(has_iv_str_length)
		filebuffer_or_bytesio.seek(previous_position)
		if self.log : print("Log : Get IV_STATE", has_iv_str)

		if has_iv_str == has_iv_str1:
			return True
		elif has_iv_str == has_iv_str2:
			return False
		else:
			raise ValueError("Data Corrupted")


	def get_has_iv(self,has_iv):
		has_iv_str_length = self.get_has_iv_str_length(self.KEY)
		EN_ = self.KEY[:self.has_iv_str_block_length]
		if has_iv :
			# 20 byte{ripemd160/sha1} encription hash but taken 16 byte{has_iv_str_block_length} so that actual algorithm of hashing is not revealed
			hash_algo = 'sha1'
		else:
			hash_algo = 'ripemd160'

		h = hashlib.new(hash_algo)
		h.update(EN_) #b"byte"
		has_iv_str = h.digest()[:has_iv_str_length]
			
		#print(h.digest())
		#print(h.hexdigest())
		# remove in release
		if self.log : print("Log : has_iv state has been created.")
		return has_iv_str

	def append_has_iv(self,has_iv,filebuffer_or_bytesio,input_buffersize):
		"""adding iv at begining and state at end"""
		#need to be in write mode
		# check if in read mode
		# check if in append mode

		#returns writing position of encrypted byte of filebuffer or string

		#data_type = file/str
		# adding iv and state

		check_sum_length = self.check_sum_str_length if self.check_sum else 0
		has_iv_str = self.get_has_iv(has_iv)

		#keep the file buffer open
		outfile = filebuffer_or_bytesio
		file_size_str_length = len(struct.pack('<Q', input_buffersize))

		if self.has_iv:
			outfile.seek(file_size_str_length)
			outfile.write(self.IV)
			IV_length = len(self.IV) 
		else:
			IV_length = 0

		file_size = input_buffersize
		padding_size = self.get_padding_size(file_size)
		outfile.seek(file_size_str_length + IV_length + file_size + padding_size + check_sum_length )
		# now added at end of file, which mention if iv is added in begining
		outfile.write(has_iv_str)

		if self.log : print("Log : Set IV_STATE", has_iv_str)
		outfile.seek(file_size_str_length+IV_length)
		return outfile

	
	def get_padding_size(self,original_filesize):
		return AES_.block_size - (original_filesize % AES_.block_size)  if original_filesize % AES_.block_size != 0 else 0

	def calculate_encrypted_buffersize(self,in_filename):
		"""fix me"""
		original_filesize = os.path.getsize(in_filename)
		original_filesize_str_length = len(struct.pack('<Q', original_filesize))
		IV_length = len(self.IV) if self.has_iv else 0
		padded_size = self.get_padding_size(original_filesize)
		has_iv_str_size = len(self.get_has_iv(self.has_iv))
		total_file_size_or_buffer_size = original_filesize_str_length + IV_length + original_filesize + padded_size + has_iv_str_size
		print(f'original_filesize_str_length({original_filesize_str_length}) + IV_length({IV_length}) + original_filesize({original_filesize}) + padded_size({padded_size}) + has_iv_str_size({has_iv_str_size})')
		print("total_outfilesize",total_file_size_or_buffer_size)
		return total_file_size_or_buffer_size


	def calculate_md5_sum(self,file_or_iobuffer,encrypt=False):
		file_or_iobuffer.seek(0)
		md5_hash = hashlib.md5()
		for byte_block in iter(lambda: file_or_iobuffer.read(4*__KILO_BYTE__),b""):
			md5_hash.update(byte_block)
		
		file_or_iobuffer.seek(0)

		return_ = self.aes.encrypt(md5_hash.hexdigest()) if encrypt else md5_hash.hexdigest()
		return return_

	def calculate_sha256_sum(file_or_iobuffer):
		file_or_iobuffer.seek(0)
		sha256_hash = hashlib.md5()
		
		for byte_block in iter(lambda: file_or_iobuffer.read(4*__KILO_BYTE__),b""):
			sha256_hash.update(byte_block)
		
		file_or_iobuffer.seek(0)
		return sha256_hash.hexdigest()


	def anybyte_to_string(self,byte,stringify_method):
		if stringify_method == 'b64':
			byte = b64encode(byte)
		elif stringify_method == 'hex':
			byte = binascii.hexlify(byte)
		
		return byte.decode('utf-8')

	def string_to_anybyte(self,string,stringify_method):
		byte = string.encode('utf-8')
		if stringify_method == 'b64':
			string = b64decode(byte)
		elif stringify_method == 'hex':
			string = binascii.unhexlify(byte)
		return string


	def encrypt_common(self,inbuffer,outbuffer,understand,buffersize,chunksize):
		if understand: print("File pointer position",outbuffer.tell())
		outbuffer.write(struct.pack('<Q', buffersize))
		if understand: print("File pointer position",outbuffer.tell())

		# adding iv and state
		# can be used anywhere after the opening of file and before writing the chunks
		outbuffer = self.append_has_iv(self.has_iv,outbuffer,buffersize)
		
		if self.check_sum : md5_hash = hashlib.md5()
		while True:
			chunk = inbuffer.read(chunksize)
			if self.check_sum : md5_hash.update(chunk)
			if len(chunk) == 0:
				break
			elif len(chunk) % 16 != 0:
				# last chunk of data is padded, as previous chunksized data has reminder of 0
				chunk += b' ' * (16 - len(chunk) % 16)

			
			encryption_chunk = self.aes.encrypt(chunk) # #print(len(chunk) == len(encryption_chunk))
			outbuffer.write(encryption_chunk)

		if self.check_sum :
			check_sum_str = md5_hash.hexdigest().encode('utf-8')
			md5_hash_encrypted = self.aes.encrypt(check_sum_str)
			outbuffer.write(md5_hash_encrypted)

			

	def decrypt_common(self,inbuffer,outbuffer,encrypted_filesize,chunksize,understand):
		if self.check_sum : md5_hash = hashlib.md5()
		# do inbuffer is attached with struct.calcsize('Q') without any identifier ?
		original_filesize_str_length = struct.calcsize('Q')
		size_byte = inbuffer.read(original_filesize_str_length)
		if understand : print(" After Reading filesize_chunk length Pointer Position",inbuffer.tell())
		original_size = struct.unpack('<Q', size_byte) # outputs (orginal_size,)
		original_size = original_size[0]
		#remove has_iv_str
		#inbuffer.truncate(original_size)
		has_iv = self.parse_has_iv_combined(inbuffer,encrypted_filesize)
		if has_iv :
			extracted_iv = inbuffer.read(AES_.block_size)
			if understand : print("File pointer at position (<24>= 16 - <8>) after 16 bytes IV chunk . Pointer Position", inbuffer.tell() )
			# inbuffer - file pointer is at the begining of the actual file data
			# That means pointer is ready to read the rest of the chunks where actual file data is stored
			self.new(iv=extracted_iv)
			IV_length = len(extracted_iv)
		else:
			IV_length = 0

		file_read_up_to = original_filesize_str_length + IV_length + original_size + self.get_padding_size(original_size)

		#outbuffer starts

		decrypted_size = 0
		while True:
			# After every reading of chunksized data, file pointer go after chunksize

			#stopping mechanism to read untill reach the begining of has_iv_str
			chunk_reading_size = file_read_up_to - inbuffer.tell() if inbuffer.tell() + chunksize > file_read_up_to else chunksize
			if chunk_reading_size == 0: break #End Of File # may fail if there is something at end of chunk like checksum
			chunk = inbuffer.read(chunk_reading_size)
			decrypted_text = self.aes.decrypt(chunk)
			decrypted_size += len(decrypted_text)
			if decrypted_size > original_size : decrypted_text = decrypted_text[:-(decrypted_size - original_size)]
			outbuffer.write(decrypted_text)
			if self.check_sum : md5_hash.update(decrypted_text)
			# unpad is not necessary as aes read encrypt and decrypt data equal to chunksize( multiple of 16 bytes ) at a time
			# so, padding automatically goes away when deencryption is given
			# but still as we are not sure error may occur then uncomment and use below line
			# this works because of padding is for binary file data not string, for string it may create spaces
			#decrypted_text = unpad(decrypted_text,16)


		#outbuffer.truncate(original_size)
		#if understand: print("File pointer position",inbuffer.tell())

		if self.check_sum:
			check_sum_str = inbuffer.read(self.check_sum_str_length)
			extracted_check_sum_str = self.aes.decrypt(check_sum_str)
			calculated_check_sum_str = md5_hash.hexdigest().encode("utf-8")
			if extracted_check_sum_str == calculated_check_sum_str:
				if self.log : print("Log : Successfully Decrypted")
			else:
				if self.log : print("Log : Data Corrupted")
				raise ValueError("Data Corrupted")

		"""
		Adjust Last Block
		The third issue is that AES encryption requires that,
		each block being written be a multiple of 16 bytes in size. 
		So we read, encrypt and write the data in chunks.
		The chunk size is required to be a multiple of 16.
		This means the last block written might require some padding applied to it.
		This is the reason why the file size needs to be stored in the output.
		SO that at the timme of decryption, we can chop the padding out,
		so we use truncate to chop off the padding
		"""

	def encrypt_to_readable_text(self,data,stringify_method='b64',chunksize=16):
		# stringify_method = b64/hex -> byte to string method
		data_byte = data.encode('utf-8') ## length = 16 - (len(data) % 16) ## data = data + chr(length)*length
		
		understand = False

		filesize = len(data_byte)
		if self.log : print("Log : BYTE Size",filesize)

		#total_outfilesize = self.calculate_encrypted_buffersize(in_filename)
		with BytesIO(data_byte) as infile:
			with BytesIO(b'') as outfile:
				self.encrypt_common(infile,outfile,understand,filesize,chunksize)
				
				encrypted_byte = outfile.getvalue()

		encrypted_byte = self.anybyte_to_string(encrypted_byte,stringify_method) if self.stringify_enable else encrypted_byte
		return encrypted_byte

	def encrypt_file(self, in_filename, out_filename=None, chunksize=64*__KILO_BYTE__):
		""" Encrypts a file using AES (CBC mode) with the given key."""
		if not out_filename: out_filename = in_filename + '.enc'
		
		understand = False
		
		filesize = os.path.getsize(in_filename) # 84497257
		if self.log : print("Log : FILE Size",filesize)
		if understand: print(type(struct.pack('<Q', filesize)))

		#total_outfilesize = self.calculate_encrypted_buffersize(in_filename)
		with open(in_filename, 'rb') as infile:
			with open(out_filename, 'wb') as outfile:
				self.encrypt_common(infile,outfile,understand,filesize,chunksize)
			

	def encrypt_string_to_file(self, string, out_filename, chunksize=64*__KILO_BYTE__, data_encoding='ascii'):
		# stringify_method = b64/hex -> byte to string method
		data_byte = string.encode('utf-8') ## length = 16 - (len(data) % 16) ## data = data + chr(length)*length
				
		understand = False

		filesize = len(data_byte)
		if self.log : print("Log : BYTE Size",filesize)

		#total_outfilesize = self.calculate_encrypted_buffersize(in_filename)
		with BytesIO(data_byte) as infile:
			with open(out_filename, 'wb') as outfile:
				self.encrypt_common(infile,outfile,understand,filesize,chunksize)

	def decrypt_to_readable_text(self,encrypted_string,stringify_method='b64',chunksize=16):
		# stringify_method = b64/hex -> byte to string method
		string_encrypted_byte = self.string_to_anybyte(encrypted_string,stringify_method) if self.stringify_enable else encrypted_string
		
		understand = False
		encrypted_filesize = len(string_encrypted_byte)

		with BytesIO(string_encrypted_byte) as infile:
			# run one time by 'with'
			with BytesIO(b'') as outfile:
				# run one time by 'with'
				self.decrypt_common(infile,outfile,encrypted_filesize,chunksize,understand)
				
				decrypted_data_byte = outfile.getvalue()

		data = decrypted_data_byte.decode('utf-8')
		return data
	
	def decrypt_file(self, in_filename, out_filename=None, chunksize=24*__KILO_BYTE__):
		""" Decrypts a file using AES (CBC mode) with"""		
		if not out_filename: out_filename = os.path.splitext(in_filename)[0]

		understand = False
		encrypted_filesize = os.path.getsize(in_filename)

		with open(in_filename, 'rb') as infile:
			# run one time by 'with'
			with open(out_filename, 'wb') as outfile:
				# run one time by 'with'
				self.decrypt_common(infile,outfile,encrypted_filesize,chunksize,understand)

	def decrypt_file_to_string(self, in_filename, chunksize=24*__KILO_BYTE__, data_encoding='ascii'):
		understand = False
		encrypted_filesize = os.path.getsize(in_filename)	

		with open(in_filename, 'rb') as infile:
			# run one time by 'with'
			with BytesIO(b'') as outfile:
				# run one time by 'with'
				self.decrypt_common(infile,outfile,encrypted_filesize,chunksize,understand)

				decrypted_data_byte = outfile.getvalue()

		data = decrypted_data_byte.decode(data_encoding)
		return data