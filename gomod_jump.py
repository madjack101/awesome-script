#!/usr/bin/python

import os
import sys

def usage():
    print 

gfw_url = (("golang.org/x", "github.com/golang"), 
    ("google.golang.org/grpc", "github.com/grpc/grpc-go"),
    ("google.golang.org/genproto", "github.com/google/grpc-go"),
    ("google.golang.org/api", "github.com/googleapis/google-api-go-client"),
    ("google.golang.org", "github.com/golang"),
    ("cloud.google.com/go", "github.com/googleapis/google-cloud-go"))

def main():
    if len(sys.argv) < 2:
        usage()
        sys.exit(-1)
    
    filename = sys.argv[1]
    with open(filename) as fd:
        replace_line = []
        for line in fd:
            for r, l in gfw_url:
            	if r in line:
                    src = line.strip()
                    dst = src.replace(r, l)
                    replace_line.append("\t%s => %s\n" % (src, dst))
                    break

    with open(filename, 'a') as fd:
        fd.write("\nreplace (\n")
        for l in replace_line:
            fd.write(l)
        fd.write(")\n")

main()
