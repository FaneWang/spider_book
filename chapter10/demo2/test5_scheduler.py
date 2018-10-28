import time
from multiprocessing import Process

from chapter10.demo2.test1_store import RedisClient
from chapter10.demo2.test2_generator import WeiboCookiesGenerator
from chapter10.demo2.test3_checker import WeiboValidChecker
from chapter10.demo2.test4_interface import *
from chapter10.demo2.settings import CYCLE, TESTER_MAP, GENERATOR_MAP, API_HOST, API_PORT, API_PROCESS, \
    GENERATOR_PROCESS, VALID_PROCESS


class Scheduler:
    @staticmethod
    def valid_cookie(cycle=CYCLE):
        while True:
            print('Cookies检测进程开始运行')
            try:
                for website, cls in TESTER_MAP.items():
                    tester = eval(cls + '(website="' + website + '")')
                    tester.run()
                    print('Cookies检测完成')
                    del tester
                    time.sleep(cycle)
            except Exception as e:
                print(e.args)

    @staticmethod
    def generate_cookie(cycle=CYCLE):
        while True:
            print('Cookies生成进程开始运行')
            try:
                for website, cls in GENERATOR_MAP.items():
                    generator = eval(cls + '(website="' + website + '")')
                    generator.run()
                    print('Cookies生成完成')
                    generator.close()
                    time.sleep(cycle)
            except Exception as e:
                print(e.args)

    @staticmethod
    def interface():
        print('interface接口开始运行')
        app.run(host=API_HOST, port=API_PORT)

    def run(self):
        if API_PROCESS:
            interface_process = Process(target=Scheduler.interface)
            interface_process.start()
        if GENERATOR_PROCESS:
            generator_process = Process(target=Scheduler.generate_cookie)
            generator_process.start()

        if VALID_PROCESS:
            valid_process = Process(target=Scheduler.valid_cookie())
            valid_process.start()
