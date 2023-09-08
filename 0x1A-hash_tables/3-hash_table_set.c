#include "hash_tables.h"
/**
  *hash_table_set - adds an element to the hash table
  *@ht: the hash table
  *@key: the key
  *@value: value associated with key
  *
  *Return: 1 for success and 0 otherwise
  */
int hash_table_set(hash_table_t *ht, const char *key, const char *value)
{
	unsigned long int index = 0;
	hash_node_t *new = NULL;
	hash_node_t *temp = NULL;
	int state = 0;

	index = key_index((const unsigned char *)key, ht->size);
	new = malloc(sizeof(hash_node_t));
	if (new == NULL)
		return (state);
	new->value = strdup(value);
	new->key = strdup(key);
	if (new->value == NULL || new->value == NULL)
		return (state);
	new->next = NULL;
	if (ht->array[index] == NULL)
		ht->array[index] = new;
	else
	{
		temp = ht->array[index];
		while (temp->next != NULL)
			temp = temp->next;
		temp->next = new;
	}
	state = 1;
	return (state);
}
