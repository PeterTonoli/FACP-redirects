#!/usr/bin/env python

out = open('redirects.out', 'w')
with open('redirects.txt') as f:
    for line in f:
        # print out comment lines as is
        if line.startswith('#'):
            out.write("  %s\n" % line.strip())
            continue

        line = line.strip().split(', ')
        if len(line) != 2:
            continue

        # print out the redirect lines
        out.write("  RedirectMatch permanent ^%s$ %s\n" % (line[0], line[1]))
out.close()