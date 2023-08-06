import sys

import yaml
from yaml_walker.api import YQuery, YamlDict


def query(pattern, data):
    return YQuery(pattern)(data)


def parse(yaml_path):
    with open(yaml_path) as fr:
        data = yaml.load(fr)
        return YamlDict(data)


def run_cli(argv):
    pattern = argv[0]
    yaml_path = argv[1]
    with open(yaml_path) as fr:
        data = yaml.load(fr)
        return query(pattern, data)


if __name__ == '__main__':
    result = run_cli(sys.argv[1:])
    print(f"query result for pattern '{sys.argv[1]}': {result}")
