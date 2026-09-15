"""Threads / processes / asyncio — когда что.

Dependencies: none (stdlib)
"""

# I/O-bound  -> threading или asyncio
# CPU-bound  -> multiprocessing (GIL мешает потокам на чистом Python CPU)
# много сетевых ожиданий в одном процессе -> asyncio

print("pick model by bottleneck: I/O -> threads/asyncio, CPU -> processes")
