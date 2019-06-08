# FLAGS = -Wall -O2 -shared-libgcc -g
FLAGS = -O3 -Wall

cc = gcc

all: knap p_knap createItems doitems

knap: knapsack.c
	$(cc) $(FLAGS) -o$@ $^

p_knap: p_knapsack.c
	$(cc) $(FLAGS) -o$@ $^ -fopenmp

createItems: createItems.c
	$(cc) $(FLAGS) -o$@ $^

doitems: doitems.c
	$(cc) $(FLAGS) -o$@ $^

clean: 
	rm -rf *knap *tems
