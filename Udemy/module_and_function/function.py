def python_food():
    width=80
    text='spam and eggs'
    left_margin=(width-len(text))//2
    print(' '*left_margin,text)


def center_text(*args,sep=' ',end='\n',file=None,flush=False):
    text=""
    for arg in args:
        text+=str(arg)+sep
    left_margin=(80-len(text))//2
    return ' '*left_margin,text

"""with open('centered',mode='w') as centered_file:
    center_text('BET BIN')
    center_text(12)
    center_text('first','sec',3,4,'spam',sep=':')"""

python_food()

center_text('BET BIN')
center_text(12)

center_text('first','sec',3,4,'spam',sep=':')
print()
