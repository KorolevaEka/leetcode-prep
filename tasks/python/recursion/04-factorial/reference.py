def launch_orders(n):
    return 1 if n == 0 else n * launch_orders(n - 1)
