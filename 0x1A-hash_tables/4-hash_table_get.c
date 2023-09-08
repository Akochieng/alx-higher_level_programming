#include "hash_tables.h"
/**
  *hash_table_get - retrieves a value associated with a key
  *@ht: the hash table
  *@key: the key
  *
  *Return: NULL if the element could not be found otherwise, the element
  */
char *hash_table_get(const hash_table_t *ht, const char *key)
{
	unsigned long int index = 0;
	hash_node_t *temp = NULL;

	index = key_index((const unsigned char *)key, ht->size);
	if (ht->array[index] == NULL)
		return (NULL);
	temp = ht->array[index];
	while (temp != NULL)
	{
		if (strcmp(temp->key, key) == 0)
			break;
		temp = temp->next;
	}
	if (temp == NULL)
		return (NULL);
	return (temp->value);
}
