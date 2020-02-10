'''
Name of file:  maoyan
Author: Jun Yang, Yingxin Liang, Yan Pan, Puxing Zhao, Shaoqing Zhang
Purpose: This module is to acquire data from maoyan.com to retrieve the comment data through JSON format data.
Module imports it: main
'''

from urllib import request
import json
import time
from datetime import datetime
from datetime import timedelta

def maoyan():
    # acquire data according to url
    def get_data(url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'
        }
        req = request.Request(url, headers=headers)
        response = request.urlopen(req)
        if response.getcode() == 200:
            return response.read()
        return None


    html = get_data('http://m.maoyan.com/mmdb/comments/movie/246127.json?_v_=yes&offset=20&startTime=2019-04-24%2002:56:46')
    print(html)

    # parse data from html page.
    def parse_data(html):
        data = json.loads(html)['cmts']
        comments = []
        for item in data:
            comment = {
                'id': item['id'],
                'nickName': item['nickName'],
                'cityName': item['cityName'] if 'cityName' in item else '',
                'content': item['content'].replace('\n', ' ', 10),
                'score': item['score'],
                'startTime': item['startTime']
            }
            comments.append(comment)
        return comments

    html = get_data('http://m.maoyan.com/mmdb/comments/movie/246127.json?_v_=yes&offset=0&startTime=2019-04-24%2022%3A25%3A03')
    comments = parse_data(html)
    print(comments)


    # save the comment data to txt file with designated format.
    def save_to_txt():
        start_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        end_time = '2018-08-10 00:00:00'
        while start_time > end_time:
            url = 'http://m.maoyan.com/mmdb/comments/movie/246127.json?_v_=yes&offset=0&startTime=' + start_time.replace(' ', '%20')
            html = None

            try:
                html = get_data(url)
            except Exception as e:
                time.sleep(0.5)
                html = get_data(url)
            else:
                time.sleep(0.1)

            comments = parse_data(html)
            print(comments)
            start_time = comments[14]['startTime']
            start_time = datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S') + timedelta(seconds=-1)
            start_time = datetime.strftime(start_time, '%Y-%m-%d %H:%M:%S')

            for item in comments:
                with open('comments.txt', 'a', encoding='utf-8') as f:
                    f.write(str(item['id'])+','+item['nickName'] + ',' + item['cityName'] + ',' + item['content'] + ',' + str(item['score'])+ ',' + item['startTime'] + '\n')

    save_to_txt()

    print('Finish')



