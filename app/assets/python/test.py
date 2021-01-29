#!/usr/bin/env python3

import sys

sys.path.append('/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages')

import stt


file_path_to_output="/Users/macbook/RubymineProjects/proiect_sac/public/uploads/" + str(sys.argv[1]) + "_files/output/testfile.txt"
file_path_to_input="/Users/macbook/RubymineProjects/proiect_sac/public/uploads/" + str(sys.argv[1]) + "_files/" + str(sys.argv[2])
f = open(file_path_to_output, "w")

text = stt.stt_with_ambient(file_path_to_input)


f.write(text)
f.close()