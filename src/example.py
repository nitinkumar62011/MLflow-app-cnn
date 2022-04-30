import argparse


if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--a", "-c","-k" ,default=10)
    args.add_argument("--v", "-p", default=20)
    parsed_args = args.parse_args()
    print(parsed_args.a)
    print(parsed_args.v)
    print(parsed_args)