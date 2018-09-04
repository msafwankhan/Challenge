'''acc?7??sss?3rr1??????5'''


def QuestionsMarks(s):
    qnum = 0
    dig = 0
    has_10 = False
    for ch in s:
        if ch.isdigit():
            if int(ch) + dig == 10:
                if qnum != 3:
                    return 'false'
                has_10 = True
            dig = int(ch)
            qnum = 0
        elif ch == '?':
            qnum += 1
    return 'true' if has_10 else 'false'


print(QuestionsMarks('acc?7??sss?6rr1??????5'))
