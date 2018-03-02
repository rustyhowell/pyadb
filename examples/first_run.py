#!/usr/bin/env python
#
# Very basic PyADB example
#

try:
    import sys
    from pyadb import ADB
except ImportError as e:
    # should never be reached
    print("[f] Required module missing. %s" % e.args[0])
    sys.exit(-1)

def main():
    # creates the ADB object
    adb = ADB()
    # IMPORTANT: You should supply the absolute path to ADB binary 
    path = '/usr/bin/adb'
    if adb.set_adb_path(path):
        print("Version: %s" % adb.get_version())
    else:
        print("Check ADB binary path")
        return

        
    print(adb.get_devices())


if __name__ == "__main__":
    main()
    

