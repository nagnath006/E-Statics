#!/usr/bin/env python
import os
import sys
#sys.setrecursionlimit(100000)
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "helloapp.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
