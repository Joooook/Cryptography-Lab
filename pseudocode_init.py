def head_output(s):
    if '%' in s:
        s = s.replace("%", "\\mod ")
    if '_' in s:
        s = s.replace("_", "\\_")
    if '&' in s:
        s = s.replace("&", "\\&")
    if '**' in s:
        s = s.replace("**", "^")
    if '!=' in s:
        s = s.replace("!=", "\\neq")
    if '*' in s:
        s = s.replace("*", "\times")
    if '^' in s:
        s = s.replace("^", "\oplus")
    if 'self.' in s:
        s = s.replace("self.", "")
    if 'for' in s:
        if 'range' in s:
            return s[:s.find('for')] + '\For{$' + s[s.find('for') + 3:s.find('in')] + '=0\\text{ to }' + s[s.find(
                '(') + 1:s.find(':')-1] + '$}'
        else:
            return s[:s.find('for')] + '\For{$' + s[s.find('for') + 3:s.find(':')] + '$}'
    elif 'elif' in s:
        return s[:s.find('elif')] + '\ElsIf{$' + s[s.find('elif') + 4:s.find(':')] + '$}'
    elif 'if' in s:
        return s[:s.find('if')] + '\If{$' + s[s.find('if') + 2:s.find(':')] + '$}'
    elif 'else' in s:
        return s[:s.find('else')] + '\Else{$' + s[s.find('else') + 4:s.find(':')] + '$}'
    elif 'while' in s:
        return s[:s.find('while')] + '\While{$' + s[s.find('while') + 5:s.find(':')] + '$}'
    elif 'return' in s:
        return s[:s.find('return')] + '\State\Return $' + s[s.find('return') + 6:] + '$'
    elif 'def' in s:
        return '\Function{' + s[s.find('def') + 4:s.find('(')] + '}{' + s[s.find('(') + 1:s.find(')')] + '}'
    elif '#' in s:
        return '\Comment{' + s[s.find('#') + 1:] + '}'
    else:
        return ' ' * (len(s) - len(s.lstrip())) + '\State' + '$' + s.lstrip() + '$'


def tail_output(s):
    if 'for' in s:
        return '\EndFor'
    elif 'if' in s:   #小BUG，若有else应当在else之后输出endif
        return '\EndIf'
    elif 'while' in s:
        return '\EndWhile'
    elif 'def' in s:
        return '\EndFunction'
    else:
        return ''


if __name__ == '__main__':
    print('Plz input your python code here:')
    l = []
    stack = [(0, '')]
    while True:
        s = input()
        if s:
            num = len(s) - len(s.lstrip())
            while len(stack) > 0 and num <= stack[0][0]:
                topnum, top = stack.pop(0)
                l.append(' ' * topnum + tail_output(top))
            stack.insert(0, (num, s))
            if '#' in s:
                l.append(head_output(s[:s.find('#')]))
                l.append(head_output(s[s.find('#'):]))
            else:
                l.append(head_output(s))
            if '!end' in s:
                break
    for i in l:
        if i.lstrip() != '' and '!end' not in i:
            print(i)
