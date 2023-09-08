#include "hash_tables.h"
/**
  *hash_table_delete - deletes a hash table
  *@ht: the hash table
  *
  *Return: void
  */
void hash_table_delete(hash_table_t *ht)
{
	hash_node_t *temp = NULL;
	hash_node_t *nxt = NULL;
	unsigned long int count;

	for (count = 0; count < ht->size; count++)
	{
		temp = ht->array[count];
		if (temp != NULL)
			while (temp != NULL)
			{
				nxt = temp->next;
				free(temp->key);
				free(temp->value);
				free(temp);
				temp = nxt;
			}
		ht->array[count] = NULL;
	}
	free(ht->array);
	free(ht);
}
