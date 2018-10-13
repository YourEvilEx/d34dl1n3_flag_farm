#!/usr/bin/env python3

# Exploit format and this example was adopted
# from the exploit farm by Alexander Bersenev (https://github.com/alexbers/exploit_farm).

import random
import sys
import exrex

print("Hello! I am a little sploit. I could be written on any language, but "
      "my author loves Python. Look at my source - it is really simple. "
      "I should steal flags and print them on stdout or stderr. ")

print("I need to attack a team with host `%s`." % sys.argv[1])

print("Here are some random flags for you:")

print(exrex.getone('[A-Z0-9]{31}='), flush=True)
print(exrex.getone('[A-Z0-9]{31}='), flush=True)
