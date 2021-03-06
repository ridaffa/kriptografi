from array import *
import numpy as num 
import copy 

sbox =  [0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67,
            0x2b, 0xfe, 0xd7, 0xab, 0x76, 0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59,
            0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0, 0xb7,
            0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1,
            0x71, 0xd8, 0x31, 0x15, 0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05,
            0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75, 0x09, 0x83,
            0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29,
            0xe3, 0x2f, 0x84, 0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b,
            0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf, 0xd0, 0xef, 0xaa,
            0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c,
            0x9f, 0xa8, 0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc,
            0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2, 0xcd, 0x0c, 0x13, 0xec,
            0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19,
            0x73, 0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee,
            0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb, 0xe0, 0x32, 0x3a, 0x0a, 0x49,
            0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79,
            0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4,
            0xea, 0x65, 0x7a, 0xae, 0x08, 0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6,
            0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a, 0x70,
            0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9,
            0x86, 0xc1, 0x1d, 0x9e, 0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e,
            0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf, 0x8c, 0xa1,
            0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0,
            0x54, 0xbb, 0x16]
rcon = [['0x01','0x02','0x04','0x08','0x10','0x20','0x40','0x80','0x1b','0x36'],
	['0x00','0x00','0x00','0x00','0x00','0x00','0x00','0x00','0x00','0x00'],
	['0x00','0x00','0x00','0x00','0x00','0x00','0x00','0x00','0x00','0x00'],
	['0x00','0x00','0x00','0x00','0x00','0x00','0x00','0x00','0x00','0x00']]
m_mc = [['0x2', '0x3', '0x1', '0x1'], ['0x1', '0x2', '0x3', '0x1'], ['0x1', '0x1', '0x2', '0x3'], ['0x3', '0x1', '0x1', '0x2']]
	
def changestringtohex(str):
	res = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
	n = 0
	for i in range(4):
		for j in range(4):
			res[j][i] = hex(ord(str[n]))
			n+=1
	return res
def changehextostr(hex):
	res = ''
	for i in range(len(hex)):
		for j in range(len(hex[i])):
			for k in range(2,len(hex[j][i])):
				if(len(hex[j][i]) == 3):
					res = res+ '0'
				res = res + hex[j][i][k]
			# res = res + ' '
	return res
def subbyte(a):
	res = a.copy()
	for i in range(len(a)):
		res[i] = hex(sbox[int(a[i],0)])
	return res

def subbytes(str):
	res = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
	for i in range(4):
		for j in range(4):
			res[i][j] = hex(sbox[int(str[i][j],0)])
	return res

def shifrows(str):
	res = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
	for i in range(4):
		if i == 0:
			for j in range(4):
				res[i][j] = str[i][j]
		if i == 1:
			for j in range(4):
				res[i][j] = str[i][num.mod(j+1,4)]
		if i == 2:
			for j in range(4):
				res[i][j] = str[i][num.mod(j+2,4)]
		if i == 3:
			for j in range(4):
				res[i][j] = str[i][num.mod(j+3,4)]
	return res
def modgf28(x):
	bin_mod = '0b100011011'
	list_x = list(x)
	while len(list_x)>10:
		i = 2
		while i<len(bin_mod):
			if bin_mod[i] != list_x[i]:
				list_x[i] = '1'
			else:
				list_x[i] = '0'
			i+=1
		str_x = ''
		str_x = str_x.join(list_x)
		list_x = list(bin(int(str_x,2)))
	str_res = ''
	return str_res.join(list_x)

def multiplegf28(x,y):
	i = 2
	bin_x = []
	while i < len(x):
		bin_x.append(int(x[i]))
		i+=1
	i = 2
	bin_y = []
	while i < len(y):
		bin_y.append(int(y[i]))
		i+=1
	bin_x = num.poly1d(bin_x)
	bin_y = num.poly1d(bin_y)
	res = bin_x*bin_y
	i = 0
	bin_res = '0b'
	for i in res:
		if num.mod(int(i),2) == 0:
			bin_res+='0'
		else:
			bin_res+='1'
	return modgf28(bin_res)
def xor(bin1,bin2):
	res = ''
	bin1_len = len(bin1)-1
	bin2_len = len(bin2)-1
	i = max(bin1_len,bin2_len)
	while i > 1:
		if bin1_len > 1:
			cek_bin1 = bin1[bin1_len]
		else:
			cek_bin1 = '0'
		if bin2_len > 1:
			cek_bin2 = bin2[bin2_len]
		else:
			cek_bin2 = '0'
		if cek_bin1 != cek_bin2:
			res = '1'+res
		else:
			res = '0'+res
		bin1_len -= 1
		bin2_len -= 1
		i -= 1
	return '0b'+res

def addroundkey(plain,key):
	res = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]] 
	for i in range(4):
		for j in range(4):
			plainx = bin(int(plain[i][j],0))
			keyx = bin(int(key[i][j],0))
			res[i][j] = hex(int(xor(plainx,keyx),2))
	return res

def mixcolumn(strx):
	res = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]] 
	
	for i in range(4):
		for j in range(4):
			cek = ['','','','']
			for k in range(4):
				cek[k] = multiplegf28(bin(int(strx[k][i],0)),bin(int(m_mc[j][k],0)))
			cek_xor = xor(cek[0],cek[1])
			cek_xor = xor(cek_xor,cek[2])
			cek_xor = xor(cek_xor,cek[3])
			res[j][i] = hex(int(cek_xor,2))
	return res
def getNewKey(chiperhex,rcon):
	newKey = chiperhex.copy()
	rotWord = [row[len(chiperhex)-1] for row in chiperhex]
	temp = rotWord[0]
	for i in range(0,len(rotWord)-1):
		rotWord[i] = rotWord[i+1]
	rotWord[len(rotWord)-1] = temp
	rotWord = subbyte(rotWord)
	firstWord = [row[0] for row in chiperhex]
	res = []
	for i in range(len(rcon)):
		res.append(hex(int(xor(bin(int(rotWord[i],0)),bin(int(firstWord[i],0))),2)))
	for i in range(len(res)):
		res[i] = hex(int(xor(bin(int(res[i],0)),bin(int(rcon[i],0))),2))
	for i in range(len(res)):
		newKey[i][0] = res[i]
	for k in range(1,len(chiperhex)):
		firstWord = [row[k] for row in chiperhex]
		prevWord = [row[k-1] for row in chiperhex]
		res = []
		for i in range(len(rcon)):
			res.append(hex(int(xor(bin(int(prevWord[i],0)),bin(int(firstWord[i],0))),2)))
		for i in range(len(res)):
			newKey[i][k] = res[i]
	return newKey
def getroundkey(firstkey,indexRound):
	key = copy.deepcopy(firstkey)
	for i in range(indexRound):
		key = getNewKey(key,[row[i] for row in rcon])
	return key
def showHex(hexs):
	for i in hexs:
		str_hex = ''
		for j in i:
			for k in range(2,len(j)):
				str_hex = str_hex + j[k]
			str_hex = str_hex + ' '
		print(str_hex)

plaintext = 'portal123p123456'
chiperkey = 'keyskeyskeyskeys'
print('Plaintext: ',plaintext)
print('Key: ',chiperkey)
# plainhex = [['0x32','0x88','0x31','0xe0'],['0x43','0x5a','0x31','0x37'],['0xf6','0x30','0x98','0x07'],['0xa8','0x8d','0xa2','0x34']]
plainhex = changestringtohex(plaintext)
plainhex_str = changehextostr(plainhex)
# chiperhex = [['0x2b','0x28','0xab','0x09'],['0x7e','0xae','0xf7','0xcf'],['0x15','0xd2','0x15','0x4f'],['0x16','0xa6','0x88','0x3c']]
chiperhex = changestringtohex(chiperkey)
chiperhex_str = changehextostr(chiperhex)
print('INPUT')
print('Plain Hex:')
showHex(plainhex)
print('Key:')
showHex(chiperhex)
addround = addroundkey(plainhex,chiperhex)
print('Addround: ')
showHex(addround)
print('')
for i in range(1,10):
	print('ROUND ',i)
	key = getroundkey(chiperhex,i)
	subbytesx = subbytes(addround)
	print('After Subbytes:')
	showHex(subbytesx)	
	shifrowsx = shifrows(subbytesx)
	print('After Shiftrows:')
	showHex(shifrowsx)	
	mixcolumns = mixcolumn(shifrowsx)
	print('After MixColumn:')
	showHex(mixcolumns)	
	addround = addroundkey(mixcolumns,key)
	print('Key:')
	showHex(key)	
	print('After AddRound:')
	showHex(addround)	
	print('')

print('ROUND 10')
key = getroundkey(chiperhex,10)
subbytesx = subbytes(addround)
print('After Subbytes:')
showHex(subbytesx)	
shifrowsx = shifrows(subbytesx)
print('After Shiftrows:')
showHex(shifrowsx)	
addround = addroundkey(shifrowsx,key)
print('Chipertext:')
showHex(addround)	
# print('Plain Text: ',plaintext,' Hex: ',plainhex_str)
# print('Plain Key: ',chiperkey,' Hex: ',chiperhex_str)
print('Encrypted Text: ',changehextostr(addround))	

