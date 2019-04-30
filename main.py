import argparse
import realtime_log
parser = argparse.ArgumentParser(description='APP log')
parser.add_argument('--m', dest='mode', help='choose mode run app!')
args = parser.parse_args()

if args.mode == 'realtime':
	realtime_log.main()
