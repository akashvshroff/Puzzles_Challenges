def make_readable(s):
    time =  '{:02}:{:02}:{:02}'.format(s / 3600, s / 60 % 60, s % 60)
    return time
