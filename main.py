import stateMachine
import networkX
import roboPy

def main():
    path = ["t_0_1", "t_1_3", "t_3_1", "t_1_4", "t_4_1", "t_1_2", "t_2_1", "t_1_5", "t_5_1", "t_1_3", "t_3_1", "t_1_6"]
    stateMachine.create()
    roboPy.run()


if __name__ == '__main__':
    main()
