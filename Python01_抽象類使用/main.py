from action_package.action import Action
from action_package.create_student_action import CreateStudentAction
from action_package.delete_student_action import DeleteStudentAction


def execute_action(action: Action):
    action.execute()


def main():
    # 報錯，不可實例化抽象類
    # TypeError: Can't instantiate abstract class Action with abstract method execute
    # action_package = Action()
    action1 = CreateStudentAction()
    action2 = DeleteStudentAction()
    execute_action(action1)
    execute_action(action2)


if __name__ == '__main__':
    main()
