# import curses
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
def factorialiterando(n):
    fac=1
    for i in range(1,n+1):
        fac*=i
    return fac


# def limpiar_pantalla():
#     stdscr = curses.initscr()
#     stdscr.clear()
#     curses.endwin()


