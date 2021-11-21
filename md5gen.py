import hashlib


def md5Generator(content=None):
    if content is None:
        return ''
    md5gen = hashlib.md5()
    md5gen.update(content)
    md5code = md5gen.hexdigest()
    md5gen = None
    return md5code


if __name__ == '__main__':
    print('fuck')
