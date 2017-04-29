"""
$GOOS	$GOARCH
android	arm
darwin	386
darwin	amd64
darwin	arm
darwin	arm64
dragonfly	amd64
freebsd	386
freebsd	amd64
freebsd	arm
linux	386
linux	amd64
linux	arm
linux	arm64
linux	ppc64
linux	ppc64le
linux	mips
linux	mipsle
linux	mips64
linux	mips64le
netbsd	386
netbsd	amd64
netbsd	arm
openbsd	386
openbsd	amd64
openbsd	arm
plan9	386
plan9	amd64
solaris	amd64
windows	386
windows	amd64
"""

import os
import sys

def split(string, splitters): #MAY RESOLVE ALL PROBLEMS WITH CSV
	final = [string]
	for x in splitters:
		for i,s in enumerate(final):
			if x in s and x != s:
				left, right = s.split(x, 1)
				final[i] = left
				final.insert(i + 1, x)
				final.insert(i + 2, right)
	return final

def main():
	print("CROSSCOMPILER")
	try:
		os.makedir("./bin")
	except:
		print("DIR ERR")
	with open("config.csv", "r") as conf:
		for compilecomb in conf.readlines():
			splitted_compilecomb = split(compilecomb, ",")
			if splitted_compilecomb[0] == "windows":
				os.system(f"env GOOS={splitted_compilecomb[0]} GOARCH={splitted_compilecomb[2]} go build -o bin/{sys.argv[1]}-{sys.argv[2]}_{splitted_compilecomb[0]}-{splitted_compilecomb[2]}.exe")
			else:
				os.system(f"env GOOS={splitted_compilecomb[0]} GOARCH={splitted_compilecomb[2]} go build -o bin/{sys.argv[1]}-{sys.argv[2]}_{splitted_compilecomb[0]}-{splitted_compilecomb[2]}")

if __name__ == '__main__':
	main()