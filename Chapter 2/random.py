import numpy
def rand(probs):
    s = sum(probs) 
    if s == 0:
        return
    else:
        div = probs/s
        numpy.random.choice(numpy.arange(0, len(probs)-1), p=div)


