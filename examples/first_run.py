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
    # creates the ADB object using the system adb
    adb = ADB()
    print("Version: %s" % adb.get_version())

    # Or create ADB object with specific version of adb
    path = '/home/chema/.android-sdks/platform-tools/adb'
    adb = ADB(path)

    if adb.set_adb_path(path):
        print("Version: %s" % adb.get_version())
    else:
        print("Check ADB binary path")
        return

    print(adb.get_devices())


if __name__ == "__main__":
    main()
    

