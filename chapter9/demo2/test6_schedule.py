from multiprocessing import Process
from chapter9.demo2.test5_interface import app
from chapter9.demo2.test3_get2 import Getter
from chapter9.demo2.test4_checker import Checker
import time
from chapter9.demo2.settings import TESTER_CYCLE, TESTER_ENABLED, GETTER_ENABLED, GETTER_CYCLE, API_ENABLED, API_HOST, \
    API_PORT


class Scheduler:
    def checker_scheduler(self, cycle=TESTER_CYCLE):
        checker = Checker()
        while True:
            checker.run()
            time.sleep(cycle)

    def getter_scheduler(self, cycle=GETTER_CYCLE):
        getter = Getter()
        while True:
            getter.run()
            time.sleep(cycle)

    def interface_scheduler(self):
        app.run(API_HOST, API_PORT)

    def run(self):
        print("代理池开始运行")
        if TESTER_ENABLED:
            tester_process = Process(target=self.checker_scheduler)
            tester_process.start()
        if GETTER_ENABLED:
            getter_process = Process(target=self.getter_scheduler)
            getter_process.start()
        if API_ENABLED:
            interface_process = Process(target=self.interface_scheduler)
            interface_process.start()

