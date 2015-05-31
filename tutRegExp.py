__author__ = 'goldenxradian'
import re

def regexp():
    m = re.search('(?<=abc)def', 'abcdef')
    print m.group(0)





def main():
    regexp()

if __name__ == "__main__":
    main()