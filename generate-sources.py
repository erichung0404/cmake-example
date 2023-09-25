#!/usr/bin/env python3

import argparse

LIB_DIR = "src/lib"
INCLUDE_DIR = "src/include"
BIN_DIR = "src/bin"

def generate_headers(nfunc: int, id: int):
    dummy_functions = [f"void foo{id}_{i}();" for i in range(nfunc)]
    dummy_functions = "\n".join(dummy_functions)
    with open(f"{INCLUDE_DIR}/header{id}.h", "w") as f:
        f.write(f"#pragma once\n{dummy_functions}")
    return;


def generate_sources(nfunc: int, id: int):
    dummy_functions = [f"void foo{id}_{i}() {{ return; }}" for i in range(nfunc)]
    dummy_functions = "\n".join(dummy_functions)
    with open(f"{LIB_DIR}/header{id}.cpp", "w") as f:
        f.write(f"#include <header{id}.h>\n\n{dummy_functions}")
    return;


def generate_binary(n: int, id: int = -1):
    include_headers = [f"#include <header{i}.h>" for i in range(n)]
    include_headers = "\n".join(include_headers)
    call_funcs = [f"foo{i}_0();" for i in range(n)]
    call_funcs = "\n".join(call_funcs)
    filename = f"{BIN_DIR}/main.cpp" if id < 0 else f"{BIN_DIR}/main_{id}.cpp"
    with open(filename, "w") as f:
        f.write(f"{include_headers}\n\nint main() {{\n{call_funcs}\nreturn 0;\n}}")
    return;


def create(n: int, nfunc: int, nexec):
    generate_binary(n)
    for i in range(n):
        generate_headers(nfunc, i)
        generate_sources(nfunc, i)

    for i in range(nexec):
        generate_binary(n, i)
    return;


def main():
    parser = argparse.ArgumentParser(description="Generate source files")
    parser.add_argument("n", type=int, help="Number of files to generate")
    parser.add_argument("nfunc", type=int, help="Number of functions to generate")
    parser.add_argument("nexec", type=int, help="Number of executables to generate")
    args = parser.parse_args()
    create(args.n, args.nfunc, args.nexec)

if __name__ == "__main__":
    main()
