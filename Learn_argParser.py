import argparse
import math


parser = argparse.ArgumentParser(description="calculate cyclinder volume")
parser.add_argument("--radious", "-r", "-rad", required = True, type=int, help="radius of cylinder")
parser.add_argument("--height", "-H", required = True, type=int, help="height of cylinder")
parser.add_argument("--quiet", "-q", action = "store_true",help="print quietly")
parser.add_argument("--verbose", "-v", action = "store_true",help="print verbose")

args = parser.parse_args()

def CylinderVol(radius, height):
    return (radius*radius*math.pi*height)


if(__name__=="__main__"):
    volume = CylinderVol(args.radious,args.height)

    if(args.quiet):
        print(volume)
    elif(args.verbose):
        print("The volume of Cylinder with radius %s and height %s is %s"%(args.radius, args.height, volume))
    else:
        print("Cylinder Volume = %s"%volume)