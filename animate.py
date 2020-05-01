import robopy.base.model as model
import numpy as np

def config1(robot):
    a = np.transpose(np.asmatrix(np.linspace(1, 50, 200)))
    b = np.transpose(np.asmatrix(np.linspace(1, 100, 200)))
    c = np.transpose(np.asmatrix(np.linspace(1, -200, 200)))
    d = np.transpose(np.asmatrix(np.linspace(1, 0, 200)))
    e = np.asmatrix(np.zeros((200, 1)))
    f = np.concatenate(( b, a, c, d, d, d), axis=1)

    robot.animate(stances=f, frame_rate=500, unit='deg')


def config2(robot):
    a = np.transpose(np.asmatrix(np.linspace(1, 50, 200)))
    b = np.transpose(np.asmatrix(np.linspace(1, -100, 200)))
    c = np.transpose(np.asmatrix(np.linspace(1, -200, 200)))
    d = np.transpose(np.asmatrix(np.linspace(1, 0, 200)))
    e = np.asmatrix(np.zeros((200, 1)))
    f = np.concatenate(( b, a, c, d, d, d), axis=1)

    robot.animate(stances=f, frame_rate=500, unit='deg')



def main():
    robot = model.Puma560()
    config1(robot)
    config2(robot)

if __name__ == '__main__':
    main()




