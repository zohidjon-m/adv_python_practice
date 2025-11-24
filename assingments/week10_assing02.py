import sys
import time

def memory_comparison(N=1_000_000):
    print(f"\n[Assignment 2] Memory comparison for N={N:,}\n")

    # list comprehension
    start = time.perf_counter()
    A = [x * x for x in range(N)]
    end = time.perf_counter()
    print(f"List comprehension (A): {sys.getsizeof(A):,} bytes, time = {end - start:.4f}s")

    # generator expression
    start = time.perf_counter()
    B = (x * x for x in range(N))
    end = time.perf_counter()
    print(f"Generator expression (B): {sys.getsizeof(B):,} bytes, time = {end - start:.4f}s")

    # tuple created from generator
    start = time.perf_counter()
    C = tuple(x * x for x in range(N))
    end = time.perf_counter()
    print(f"Tuple from generator (C): {sys.getsizeof(C):,} bytes, time = {end - start:.4f}s")

memory_comparison()