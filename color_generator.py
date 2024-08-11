import itertools

def color_generator():
    colors = ['#b694fa', '#87cefa', '#94faca', '#f2d9a6', '#8cf471', '#af002a', '#6474ed', '#2b4fe2', '#e22b8a', '#f0e58c', '#008080']
    return itertools.cycle(colors)

gen = color_generator()
color = next(gen)