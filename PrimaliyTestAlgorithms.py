import random
import time

# Test cases for individual numbers and ranges
test_numbers = [
    1027498106806225441, 7050810642549651091, 6155568815813781257, 
    2912970412537579783, 8348960580061273493, 2407823242081768633,
    1383602730909524507, 7116242705310218687, 8042869108487301239, 9015127525509429017
]

test_ranges = [
    (1027498106806225441, 1027498106806226441),
    (7050810642549651091, 7050810642549652091),
    (6155568815813781257, 6155568815813782257),
    (2912970412537579783, 2912970412537589783),
    (8348960580061273493, 8348960580061274493),
    (2407823242081768633, 2407823242081769633),
    (1383602730909524507, 1383602730909525507),
    (7116242705310218687, 7116242705310219687),
    (8042869108487301239, 8042869108487302239),
    (9015127525509429017, 9015127525509439017)
]

# Miller–Rabin Primality Test
def miller_rabin_primality_test(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    r, d = 0, n - 1
    while d % 2 == 0:
        d //= 2
        r += 1

    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

# Lucas Primality Test
def lucas_test(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2

    u, v, d = 0, 2, 5
    while pow(d, (n - 1) // 2, n) == n - 1:
        d += 2
    return True

# Baillie–PSW Primality Test
def baillie_psw_primality_test(n):
    return miller_rabin_primality_test(n, k=5) and lucas_test(n)

# Run tests on individual numbers and measure runtime
def run_individual_tests():
    print("Testing individual numbers with runtime measurements:")

    total_mr_time, total_lucas_time, total_bpsw_time = 0, 0, 0

    for n in test_numbers:
        results = []
        
        start_time = time.time()
        if miller_rabin_primality_test(n):
            results.append("Miller–Rabin Test")
        mr_time = time.time() - start_time
        
        start_time = time.time()
        if lucas_test(n):
            results.append("Lucas Test")
        lucas_time = time.time() - start_time
        
        start_time = time.time()
        if baillie_psw_primality_test(n):
            results.append("Baillie–PSW Test")
        bpsw_time = time.time() - start_time

        print(f"Number: {n}")
        if results:
            print(f"  Prime according to: {', '.join(results)}")
        else:
            print(f"  Composite according to all tests")
        print(f"  Runtime - Miller–Rabin: {mr_time*1000:.5f}ms, Lucas: {lucas_time*1000:.5f}ms, Baillie–PSW: {bpsw_time*1000:.5f}ms")
        total_mr_time += mr_time
        total_lucas_time += lucas_time
        total_bpsw_time += bpsw_time

    print("\nTotal runtime for individual tests:")
    print(f"  Miller–Rabin: {total_mr_time*1000:.5f}ms")
    print(f"  Lucas: {total_lucas_time*1000:.5f}ms")
    print(f"  Baillie–PSW: {total_bpsw_time*1000:.5f}ms")

# Run tests on ranges and measure runtime
def run_range_tests():
    print("\nTesting ranges with runtime measurements:")

    total_mr_time, total_lucas_time, total_bpsw_time = 0, 0, 0

    for start, end in test_ranges:
        print(f"\nRange: [{start}, {end}]")
        
        # Measure runtime and find primes for each algorithm
        primes_miller_rabin, primes_lucas, primes_baillie_psw = [], [], []
        
        start_time = time.time()
        for n in range(start, end + 1):
            if miller_rabin_primality_test(n):
                primes_miller_rabin.append(n)
        mr_time = time.time() - start_time
        
        start_time = time.time()
        for n in range(start, end + 1):
            if lucas_test(n):
                primes_lucas.append(n)
        lucas_time = time.time() - start_time
        
        start_time = time.time()
        for n in range(start, end + 1):
            if baillie_psw_primality_test(n):
                primes_baillie_psw.append(n)
        bpsw_time = time.time() - start_time

        # Print results for each algorithm with runtime
        print(f"  Miller–Rabin Test")
        print(f"    Runtime: {mr_time*1000:.5f}ms, Expected primes: {len(primes_miller_rabin)}")
        print(f"  Lucas Test")
        print(f"    Runtime: {lucas_time*1000:.5f}ms, Expected primes: {len(primes_lucas)}")
        print(f"  Baillie–PSW Test")
        print(f"    Runtime: {bpsw_time*1000:.5f}ms, Expected primes: {len(primes_baillie_psw)}")

        total_mr_time += mr_time
        total_lucas_time += lucas_time
        total_bpsw_time += bpsw_time

    print("\nTotal runtime for range tests:")
    print(f"  Miller–Rabin: {total_mr_time*1000:.5f}ms")
    print(f"  Lucas: {total_lucas_time*1000:.5f}ms")
    print(f"  Baillie–PSW: {total_bpsw_time*1000:.5f}ms")

# Execute tests
run_individual_tests()
run_range_tests()
