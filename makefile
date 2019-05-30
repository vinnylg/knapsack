FLAGS = -Wall -g

cc = gcc

all: knapsack createItems

knapsack: knapsack.c
	$(cc) $(FLAGS) -o$@ $^

createItems: createItems.c
	$(cc) $(FLAGS) -o$@ $^

clean: 
	rm -rf knapsack createItems
