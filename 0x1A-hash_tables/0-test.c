#include "hash_tables.h"
#define TABLESIZE 1024
/**
  *main - check the code for creating a hash table
  *
  *
  *Return: pointer to the created hash table
  */

int main(void)
{
	hash_table_t *table = NULL;

	table = hash_table_create(TABLESIZE);
	if (table == NULL)
	{
		printf("Failed to create the table\n");
	}
	printf("The size of the table is %lu\n", table->size);
	printf("The address of the head of the table is %p\n", (void *)table->array);
	return (0);
}
