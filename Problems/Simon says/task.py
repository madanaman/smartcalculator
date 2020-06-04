def what_to_do(instructions):
    if instructions.startswith("Simon says"):
        return "I" + instructions[10:]
    elif instructions.endswith("Simon says"):
        return "I " + instructions[:len(instructions)-10]
    else:
        return "I won't do it!"
