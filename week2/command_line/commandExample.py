# modules needed
import numpy as np
import argparse



def readCommands():
  '''
  Read commandline arguments
  '''
  p = argparse.ArgumentParser(description=("An illustration of a command line parser"))
  p.add_argument("--numb", dest ="numb", type=int, default=10, help=("Lenght of array to generate\nDefault = 10"))

    # create an argparse object with a useful help comment
  # read a string
  p.add_argument("--input",dest="inName",type=str,default='test.txt',help=("Input filename\nDefault=test.txt"))
  # read an integer
  p.add_argument("--lat", dest ="lat", type=int, default=5, help=("Latitude in degrees\nDefault = 5"))
  # read a float
  p.add_argument("--max_vcf",dest ="maxVcf",type=float, default=100.0, help=("Maximum VCF value to use\nDefault = 100"))
  # read a bollian (logic)
  p.add_argument("--useSnow",dest="useSnow", action='store_true', default=False, help=("Use snow switch\nDefault = False"))
  # read a variable length array. Also, we can have multiple commands to invoke this
  p.add_argument("-p","--power_beams",dest = "pow_beam_list", type=int, nargs='*', default=[5,6], help=("Track numbers of power beams\nDefault = 5 and 6"))
  # parse the command line into an object
  p.add_argument("--output",dest="outName",type=str,default='test.txt',help=("Output filename\nDefault=test.txt"))
  cmdargs = p.parse_args()
  return cmdargs



def makeRand(n):
  '''Make an array of random numbers'''
  x=np.random.rand(n)
  return(x)


if __name__=="__main__":
  args=readCommands()
  y=makeRand(args.numb)
  print(y)

