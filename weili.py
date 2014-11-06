# -*- coding: utf-8 -*-

import argparse
from weiboAgent import WeiboAgent

class Weili(object):
    def __init__(self):
        self.weiboAgent = WeiboAgent()
        self.weiboAgent.authorize()

    def get_parser(self):
        parser = argparse.ArgumentParser(description="command line weibo for geeks")
        parser.add_argument('-p', '--post', help="post a weibo")
        parser.add_argument('-g', '--get', type=int, help="get my weibo")
        parser.add_argument('-i', '--image', help="uplaod image in the status")

        return parser
    
    def command_line_runner(self):
        parser = self.get_parser()
        args = vars(parser.parse_args())
    
        if args["get"]:
            all_statuses = self.weiboAgent.get_home_statuses(args["get"])
            for index,value in enumerate(all_statuses['statuses']):
                print index,value['text'].encode('utf-8')

        if args["post"]:
            if not args["image"]:
                self.weiboAgent.post_status(args["post"])
            else:
                self.weiboAgent.post_status_with_pic(args["post"], args["image"])

if __name__ == "__main__":
    weili = Weili()
    weili.command_line_runner()
