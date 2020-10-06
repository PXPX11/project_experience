import zmq


def run():
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.connect('tcp://127.0.0.1:6666')
    socket.setsockopt_string(zmq.SUBSCRIBE, '')

    print('client 1')
    while True:
        msg = socket.recv()
        print("msg: %s" % msg)


if __name__ == '__main__':
    run()


# 发布者
import time
import zmq


def run():
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.bind('tcp://*:6666')

    cnt = 1

    while True:
        time.sleep(1)
        socket.send_string('server cnt {}'.format(cnt))
        print('send {}'.format(cnt))
        cnt += 1


if __name__ == '__main__':
    run()

