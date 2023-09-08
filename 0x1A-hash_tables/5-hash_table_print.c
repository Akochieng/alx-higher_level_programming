#include "hash_tables.h"
/**
  *hash_table_print - function to print the hash table
  *@ht: the hash table
  *
  *Return: void
  */
void hash_table_print(const hash_table_t *ht)
{
	unsigned long int count;
	hash_node_t *temp = NULL;
	int state = 0;

	printf("{");
	for (count = 0; count < ht->size; count++)
	{
		temp = ht->array[count];
		while (temp != NULL)
		{
			if (state == 1)
				printf(", ");
			printf("'%s': '%s'", temp->key, temp->value);
			temp = temp->next;
			if (state == 0)
				state = 1;
		}
	}
	printf("}\n");
}
