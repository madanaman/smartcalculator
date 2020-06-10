from hstest.stage_test import *
from hstest.test_case import TestCase


class CalcTest(StageTest):
    def generate(self) -> List[TestCase]:
        return [TestCase(stdin=['/help', self.test_1, self.test_2, self.test_3, self.test_4, self.test_5, self.test_6,
                                self.test_7, self.test_8, self.test_9, self.test_10, self.test_11, self.test_12,
                                self.test_13, self.test_14, self.test_15, self.test_16, self.test_17, self.test_18,
                                self.test_19, self.test_20, self.test_21, self.test_22, self.test_23, self.test_exit])]

    # test of previous steps' functionality ####################################
    # help message test
    def test_1(self, output):
        output = str(output).lower().strip()
        if len(output.split(" ")) < 3:
            return CheckResult.wrong("It seems like there was no any \"help\" message.")
        return ""

    # empty string test
    def test_2(self, output):
        output = str(output)
        if len(output) != 0:
            return CheckResult.wrong("Incorrect response to an empty string. "
                                     "The program should not print anything.")
        return "n = -32"

    # assignment test
    def test_3(self, output):
        if len(output) != 0:
            return CheckResult.wrong("Unexpected reaction after assignment." +
                                     "The program should not print anything in this case.")
        return "33 + 20 + 11 + 49 - 32 - 9 + 1 - 80 + 4"

    # addition and subtraction test
    def test_4(self, output):
        output = str(output).lower().strip()
        if output != "-3":
            return CheckResult.wrong("The program cannot process addition and subtraction operations correctly.")
        return "33 + 20 + 11 + 49 + n - 9 + 1 - 80 + 4"

    # addition and subtraction with variables
    def test_5(self, output):
        output = str(output).lower().strip()
        if output != "-3":
            return CheckResult.wrong("The program cannot process addition and subtraction operations correctly.")
        return "c = n \nc = -2"

    # assignment by a variable and reassignment
    def test_6(self, output):
        if len(output) != 0:
            return CheckResult.wrong("Unexpected reaction after assignment."
                                     "The program should not print anything in this case.")
        return "  c   "

    # checking the value of variable
    def test_7(self, output):
        output = str(output).lower().strip()
        if output != "-2":
            return CheckResult.wrong("The variable stores not a correct value."
                                     "May be the program could not assign the value of one variable to another one.")
        return "11 - 9 + с"

    # zero sum test
    def test_8(self, output):
        output = str(output).lower().strip()
        if output != "0":
            return CheckResult.wrong("The problem when sum is equal to 0 has occurred.")
        return "5 --- 2 ++++++ 4 -- 2 ---- 1"

    # multiple operations with several operators
    def test_9(self, output):
        output = str(output).lower().strip()
        if output != "10":
            return CheckResult.wrong("The program cannot process multiple operations with several operators.")
        return "/start"

    # nonexistent command
    def test_10(self, output):
        output = str(output).lower().strip()
        if "unknown" not in output:
            return CheckResult.wrong("The program should print \"Unknown command\" "
                                     "when a nonexistent command is entered.")
        return "var1 = 1"

    # invalid name of variable
    def test_11(self, output):
        output = str(output).lower().strip()
        if "invalid" not in output:
            return CheckResult.wrong("The value can be an integer number or a value of another variable")
        return "c = 7 - 1 = 5"

    # invalid assignment
    def test_12(self, output):
        output = str(output).lower().strip()
        if "invalid" not in output:
            return CheckResult.wrong("The program could not handle a invalid assignment.")
        return "variable = f"

    # assignment by unassigned variable
    def test_13(self, output):
        output = str(output).lower().strip()
        if "unknown" not in output or "invalid" not in output:
            return CheckResult.wrong("The program should not allow an assignment by unassigned variable.")
        return "variable = 777 \n Variable"

    # a test suit for the current stage ########################################
    # test of case sensitivity
    def test_14(self, output):
        output = str(output).lower().strip()
        if "unknown" not in output:
            return CheckResult.wrong("The program should be case sensitive.")
        return "4 * 3"

    # multiplication operation test
    def test_15(self, output):
        output = str(output).lower().strip()
        if output != "12":
            return CheckResult.wrong("The program has problems with multiplication operation.")
        return "91 / 13"

    # division operation test
    def test_16(self, output):
        output = str(output).lower().strip()
        if output != "7":
            return CheckResult.wrong("The program has problems with division operation.")
        return " a= 7 \n b =2\na * 4 / b - (3 - 1)"

    # test of mixed operations with a variable
    def test_17(self, output):
        output = str(output).lower().strip()
        if output != "16":
            return CheckResult.wrong("The program cannot correctly process several operations.")
        return "7 + 3 * ((4 + 3) * 7 + 1) - 6 / (2 + 1)"

    # test of an example from the task
    def test_18(self, output):
        output = str(output).lower().strip()
        if output != "155":
            return CheckResult.wrong("The program cannot reproduce an example from the task.")
        return "3 + (9 + ( 68 * 3/9)) * ((7-2 * 5) / 2 * 6"

    # test of multi-level parentheses
    def test_19(self, output):
        output = str(output).lower().strip()
        if output != "288":
            return CheckResult.wrong("Program incorrectly solves expressions with multi-level parentheses")
        return "8 * (2 + 3"

    # negative tests for this stage ############################################
    # unclosed brackets from the right
    def test_20(self, output):
        output = str(output).lower().strip()
        if "invalid" not in output:
            return CheckResult.wrong("The program could not handle an invalid expression.")
        return "4 + 5)"

    # unclosed brackets from the left
    def test_21(self, output):
        output = str(output).lower().strip()
        if "invalid" not in output:
            return CheckResult.wrong("The program could not handle an invalid expression.")
        return "2 ************ 2"

    # sequence of "*"
    def test_22(self, output):
        output = str(output).lower().strip()
        if "invalid" not in output:
            return CheckResult.wrong("A sequence of \"*\" should return \"Invalid expression\".")
        return "2 // 2"

    # sequence of "/"
    def test_23(self, output):
        output = str(output).lower().strip()
        if "invalid" not in output:
            return CheckResult.wrong("A sequence of \"/\" should return \"Invalid expression\".")
        return "/exit"

    # test of exit
    def test_exit(self, output):
        output = str(output).lower().strip()
        if "bye" not in output:
            return CheckResult.wrong("Your program didn't print \"bye\" after entering \"/exit\".")
        return CheckResult.correct()

    def check(self, reply: str, attach) -> CheckResult:
        return CheckResult.correct()


if __name__ == '__main__':
    CalcTest("calculator.calculator").run_tests()
