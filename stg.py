<<<<<<< HEAD
import os
from socket import *
from math import ceil 
from sig import *
import itertools
import argparse

def hex_group_formatter(iterable):
    chunks = [iter(iterable)] * 4 # (header의 perv_size, size) 청크 4개씩 분할 32byte
    return '   '.join(
        ' '.join(format(x, '0>2x') for x in chunk) # 데이터 바꾸는 부분
        for chunk in itertools.zip_longest(*chunks, fillvalue=0)) # 길이가 다른 자료형이라 zip_logest사용 해서 분할시킴(0x20,0x30,0x40,0x50)...(0,-,-,-) 이런식

def hex_view(filename, chunk_size=16): # 파일 hex값으로 읽어옴
    template = ' {:<53}'
    with open(filename, 'rb') as stream:
        for chunk_count in itertools.count(0):
            chunk = stream.read(chunk_size)
            if not chunk:
                return
            yield template.format(
                hex_group_formatter(chunk)
				)

#def file_output(header_sig):
	#global out_file_cnt
	#out_file_cnt += 1
	#print('.',file_extension[header_sig],'파일 검출','\t')

def size_rt(bytes): 
	size_result = str(bytes) + 'Byte'
	if (bytes > 1024):
		size_result = str(int(ceil(bytes/1024))) + 'KB'
	elif (bytes > 1024**2):	
		size_result = str(int(ceil(bytes/(1024**2)))) + 'MB'
	elif (bytes > 1024**3):	
		size_result = str(ceil(bytes/(1024**3))) + 'GB'
	elif (bytes > 1024**4):	
		size_result = str(int(ceil(bytes/(1024**4)))) + 'TB'
	return size_result

def stg(file_name):
	parser = argparse.ArgumentParser()
	parser.add_argument('file', nargs='?', default=file_name)
	args = parser.parse_args()
	
	file_size = os.path.getsize(file_name)

	#print('\n검사 파일:', file_name,'\t','Size :', size_rt(file_size),'\n')
	 
	cnt = -1
	out_file_cnt = 0
	check_flag = 0
	chck = 0
	string = ''

	for line in hex_view(args.file):
		string += line.replace("   ", " ")

	while (cnt < len(file_sig)-1):
		cnt += 1
		
		if (string.find(file_sig[cnt]) != -1):      
			file_index = string.index(file_sig[cnt])
			header_sig = string[file_index:file_index+len(file_sig[cnt])]
			out_file_cnt += 1
			chck = 1
			if (check_flag == 0):
				check_flag == 1
				string = string[file_index + len(file_sig[cnt]):]
				cnt -= 1
		else:
			check_flag = 0
			continue 		
	if chck == 0:
		return 0 
	else:
=======
import os
from socket import *
from math import ceil 
from sig import *
import itertools
import argparse

def hex_group_formatter(iterable):
    chunks = [iter(iterable)] * 4 # (header의 perv_size, size) 청크 4개씩 분할 32byte
    return '   '.join(
        ' '.join(format(x, '0>2x') for x in chunk) # 데이터 바꾸는 부분
        for chunk in itertools.zip_longest(*chunks, fillvalue=0)) # 길이가 다른 자료형이라 zip_logest사용 해서 분할시킴(0x20,0x30,0x40,0x50)...(0,-,-,-) 이런식

def hex_view(filename, chunk_size=16): # 파일 hex값으로 읽어옴
    template = ' {:<53}'
    with open(filename, 'rb') as stream:
        for chunk_count in itertools.count(0):
            chunk = stream.read(chunk_size)
            if not chunk:
                return
            yield template.format(
                hex_group_formatter(chunk)
				)

#def file_output(header_sig):
	#global out_file_cnt
	#out_file_cnt += 1
	#print('.',file_extension[header_sig],'파일 검출','\t')

def size_rt(bytes): 
	size_result = str(bytes) + 'Byte'
	if (bytes > 1024):
		size_result = str(int(ceil(bytes/1024))) + 'KB'
	elif (bytes > 1024**2):	
		size_result = str(int(ceil(bytes/(1024**2)))) + 'MB'
	elif (bytes > 1024**3):	
		size_result = str(ceil(bytes/(1024**3))) + 'GB'
	elif (bytes > 1024**4):	
		size_result = str(int(ceil(bytes/(1024**4)))) + 'TB'
	return size_result

def stg(file_name):
	parser = argparse.ArgumentParser()
	parser.add_argument('file', nargs='?', default=file_name)
	args = parser.parse_args()
	
	file_size = os.path.getsize(file_name)

	#print('\n검사 파일:', file_name,'\t','Size :', size_rt(file_size),'\n')
	 
	cnt = -1
	out_file_cnt = 0
	check_flag = 0
	chck = 0
	string = ''

	for line in hex_view(args.file):
		string += line.replace("   ", " ")

	while (cnt < len(file_sig)-1):
		cnt += 1
		
		if (string.find(file_sig[cnt]) != -1):      
			file_index = string.index(file_sig[cnt])
			header_sig = string[file_index:file_index+len(file_sig[cnt])]
			out_file_cnt += 1
			chck = 1
			if (check_flag == 0):
				check_flag == 1
				string = string[file_index + len(file_sig[cnt]):]
				cnt -= 1
		else:
			check_flag = 0
			continue 		
	if chck == 0:
		return 0 
	else:
>>>>>>> 802554d90f9aa68f63f58425fc10c040e174b89e
		return out_file_cnt