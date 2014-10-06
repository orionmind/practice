def fibonacci(n):
    if n == 0:
        print "0"
        return 0
    elif n == 1:
        a = 1
        print a
        return a
    elif n == 2:
        b = 1
        print b
        return b
    else:
        c = store_nminus1 + store_nminus2
        print c
        return c
		
def close(number, num_to_quit):
	if number == num_to_quit:
		print "Done."
		quit()

number = 0
fibonacci(number)
number_to_quit = int(raw_input("What number to stop calculating?"))

while True:
	close(number, number_to_quit)
	number += 1
	store_nminus1 = fibonacci(number)
	close(number, number_to_quit)
	number += 1
	store_nminus2 = fibonacci(number)
