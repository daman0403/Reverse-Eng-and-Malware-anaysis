import sys
import base64

if "-h" in sys.argv or len(sys.argv)<=2:
    print("Usage - "+sys.argv[0]+" - b64/b32 cipher")
    sys.exit()

if "-b64" in sys.argv:
    index = (sys.argv).index("-b64")
    print(base64.b64decode(sys.argv[index+1]))

if "-b32" in sys.argv:
    index = (sys.argv).index("-b32")
    print(base64.b32decode(sys.argv[index+1]))   

if "-b64" not in sys.argv and "-b32" not in sys.argv:
    sys.stderr.write("Encoding not supported")
