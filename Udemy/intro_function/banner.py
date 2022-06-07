def banner_text(text='',screen_width=80):
    #screen_width=80
    if len(text)>screen_width-4:
        raise ValueError('String {0} is larger then specified width {1}'.format(text,screen_width))
    if text=='*':
        print('*'*screen_width)
    else:
        output_string='**{0}00'.format(text.center(screen_width-4))
        print(output_string)


