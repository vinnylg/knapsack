FLAGS = -Wall -g

cc = gcc

all: knap p_knap items/createItems

knap: knapsack.c
	$(cc) $(FLAGS) -o$@ $^

p_knap: p_knapsack.c
	$(cc) $(FLAGS) -o$@ $^ -lpthread

items/createItems: items/createItems.c
	$(cc) $(FLAGS) -o$@ $^

clean: 
	rm -rf *knap items/createItems 
