def what_to_do(instructions):
    if instructions.startswith("Simon says"):
        return 'I' + instructions[len("Simon says"):]
    elif instructions.endswith("Simon says"):
        return 'I ' + instructions[0:-1 - len("Simon says")]
    else:
        return "I won't do it!"
