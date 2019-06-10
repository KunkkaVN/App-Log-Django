import argparse
from DjangoLogAnalysis import login_analysis,level_analysis,realtime_log
parser = argparse.ArgumentParser(description='APP log')
parser.add_argument('--m', dest='mode', help='choose mode run app!')
parser.add_argument('--p', dest='path', help='choose mode run app!')
args = parser.parse_args()

if args.mode == 'login':
    path = args.path
    #login_analysis.main(path)
    #level_analysis.main(path)
    realtime_log.main(path)
