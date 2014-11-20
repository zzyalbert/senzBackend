# -*- encoding:utf-8 -*- 

import sys
sys.path.append("../activity_user_mapping")
sys.path.append("../utils")
from UserActivityMapping import UserActivityMapping

def testMapping():
        mapping = UserActivityMapping()
        mapping.mapping()
        mapping.dump2file('./mapping_result.txt')


def main():
        testMapping()

if __name__ == '__main__':
        main()
