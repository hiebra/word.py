__import__('com.softalks.debug')


def write(word, **parameters):
    if parameters.get('end'):
        raise Exception('Illegal argument: "end"')
    print(word, end=' ', **parameters)
