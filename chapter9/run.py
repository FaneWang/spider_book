from chapter9.demo2.test6_schedule import Scheduler
import sys
import io

# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def main():
    try:
        s = Scheduler()
        s.run()
    except Exception:
        main()


if __name__ == '__main__':
    main()
