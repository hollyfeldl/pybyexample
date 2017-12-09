# the gorountines example using asyncio tasks

import asyncio

def f(fromVar):
    """Undecorated version of F"""
    for i in range(0,3):
        show("nodeco", fromVar, i)

@asyncio.coroutine
def fio(idx):
    """Decorated version of F for asyncio. swap it around so it can be a generator"""
    show("deco", "coroutine", idx)
        

def show(callfrom, msg, idx):
    """Pull out the print from both"""
    print(callfrom, msg, ":", idx)


def main():

    # first the direct calls to function f
    f("direct")

    # set up event loop
    loop = asyncio.get_event_loop()

    # have a generator for the event loop
    to_do = [fio(i) for i in range(0,3)]
    wait_coro = asyncio.wait(to_do)
    res, _ = loop.run_until_complete(wait_coro)
    loop.close()

    print("The example goroutines.py needs work")

if __name__ == "__main__":
    main()

