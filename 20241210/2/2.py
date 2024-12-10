import math
import sys
class AssemblerInterpreter:
    def __init__(self, program):
        self.program = program.splitlines()
        self.variables = {}
        self.labels = {}
        self.commands = []
        self.current_line = 0

    def parse_program(self):
        for line_number, line in enumerate(self.program):
            stripped_line = line.strip()
            if not stripped_line:
                continue

            label, _, command = stripped_line.partition(":")
            if command:
                label = label.strip()
                command = command.strip()
                self.labels[label] = len(self.commands)
            else:
                command = label.strip()

            if command:
                self.commands.append(command)

        for command in self.commands:
            parts = command.split()
            if parts[0].startswith("if") and len(parts) == 4:
                _, _, _, label = parts
                if label not in self.labels:
                    raise ValueError(f"Undefined label: {label}")

    def run(self):
        self.current_line = 0
        while self.current_line < len(self.commands):
            command = self.commands[self.current_line]
            self.execute_command(command)

    def execute_command(self, command):
        parts = command.split()
        operation = parts[0]

        match operation:
            case "stop":
                exit()

            case "store":
                if len(parts) != 3:
                    self.current_line += 1
                    return
                value = self.to_float(parts[1])
                destination = parts[2]
                self.variables[destination] = value

            case "add" | "sub" | "mul" | "div":
                if len(parts) != 4:
                    self.current_line += 1
                    return
                op1, op2, dest = parts[1:]
                result = self.perform_arithmetic(operation, op1, op2)
                self.variables[dest] = result

            case "ifeq" | "ifne" | "ifgt" | "ifge" | "iflt" | "ifle":
                if len(parts) != 4:
                    self.current_line += 1
                    return
                op1, op2, label = parts[1:]
                if self.perform_comparison(operation, op1, op2):
                    self.current_line = self.labels[label]
                    return

            case "out":
                if len(parts) != 2:
                    self.current_line += 1
                    return
                var = parts[1]
                print(self.variables.get(var, 0))

            case _:
                pass

        self.current_line += 1

    def to_float(self, value):
        try:
            return float(value)
        except ValueError:
            return 0.0

    def perform_arithmetic(self, operation, op1, op2):
        v1 = self.variables.get(op1, 0.0)
        v2 = self.variables.get(op2, 0.0)
        try:
            match operation:
                case "add":
                    return v1 + v2
                case "sub":
                    return v1 - v2
                case "mul":
                    return v1 * v2
                case "div":
                    return v1 / v2
        except ZeroDivisionError:
            return math.inf

    def perform_comparison(self, operation, op1, op2):
        v1 = self.variables.get(op1, 0.0)
        v2 = self.variables.get(op2, 0.0)
        match operation:
            case "ifeq":
                return v1 == v2
            case "ifne":
                return v1 != v2
            case "ifgt":
                return v1 > v2
            case "ifge":
                return v1 >= v2
            case "iflt":
                return v1 < v2
            case "ifle":
                return v1 <= v2


program = sys.stdin.read()
try:
    interpreter = AssemblerInterpreter(program)
    interpreter.parse_program()
    interpreter.run()
except ValueError as e:
    print(e)