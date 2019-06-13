#FLAGS = -Wall -O2 -shared-libgcc -g
FLAGS = -O3 -Wall

cc = gcc

all: knap p_knap createItem

knap: knapsack.c
	$(cc) $(FLAGS) -o$@ $^

p_knap: p_knapsack.c
	$(cc) $(FLAGS) -o$@ $^ -fopenmp

createItem: createItem.c
	$(cc) $(FLAGS) -o$@ $^

clean: 
	rm -rf *knap  
