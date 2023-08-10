#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    attrs = dir(hidden_4)
    for name in attrs:
        if name[:2] != "__":
            print(name)
