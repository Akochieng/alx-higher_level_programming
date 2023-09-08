#include "hash_tables.h"
/**
  *hash_table_create - creates a hash table
  *@size: the size of the hash table
  *
  *Return: pointer to the hash table
  */
hash_table_t *hash_table_create(unsigned long int size)
{
	hash_table_t *new_table = NULL;
	unsigned long int loc;

	new_table = malloc(sizeof(hash_table_t));
	if (new_table == NULL)
		return (NULL);
	new_table->size = size;
	new_table->array = malloc(sizeof(hash_node_t *) * size);
	if (new_table->array == NULL)
	{
		free(new_table);
		return (NULL);
	}
	for (loc = 0; loc < size; loc++)
		new_table->array[loc] = NULL;
	return (new_table);
}
