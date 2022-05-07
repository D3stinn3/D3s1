"""password protocol involving the annoying while loop and if statements"""

jina = ''

while jina != 'Destinne':
    print('password protocol initialized...')
    jina = input('Please input your name sir: ')
print('Welcome aboard sir please do continue')

pass_word = ''

while pass_word != 'des':
    print('password protocol initialized again')
    pass_word = input('Please input your password sir: ')
    if pass_word == 'destinne':
        print('close! try again')
    elif pass_word == 'tinne':
        print('that was what you input last time, try again')
print('Welcome aboard sir')
