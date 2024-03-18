import argparse
import os

parser = argparse.ArgumentParser("ip checker")
parser.add_argument("-p", "--ip", help="Target Ip adrasss")
parser.add_argument("-t", "--time", help="How many Time to Run")
parser.add_argument("-o", "--output", help="OutPut file")
args = parser.parse_args()



def main():

	if args.ip and args.time and args.output:

		os.system(f"touch {args.output}")
		os.system(f" ping -c {args.time} {args.ip} -q >> {args.output}")

	else:
		os.system(f" ping -c {args.time} {args.ip}")




if __name__ == '__main__':
		main()

