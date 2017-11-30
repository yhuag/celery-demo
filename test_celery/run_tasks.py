from .tasks import longtime_add, shorttime_add
import time

if __name__ == '__main__':
    result = longtime_add.delay(1,2)
    ans = shorttime_add.delay(3,4)
    # at this time, our task is not finished, so it will return False
    print('Long Task finished? ', result.ready())
    print('Long Task result: ', result.result)
    print('Short Task finished? ', ans.ready())
    print('Short Task result: ', ans.result)
    # sleep 10 seconds to ensure the task has been finished
    time.sleep(3)
    print('Long Task finished? ', result.ready())
    print('Long Task result: ', result.result)
    print('Short Task finished? ', ans.ready())
    print('Short Task result: ', ans.result)
    time.sleep(10)
    # now the task should be finished and ready method will return True
    print('Long Task finished? ', result.ready())
    print('Long Task result: ', result.result)
    print('Short Task finished? ', ans.ready())
    print('Short Task result: ', ans.result)