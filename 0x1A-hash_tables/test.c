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
	hash_table_t *ht = NULL;

	ht = hash_table_create(TABLESIZE);
	if (ht == NULL)
	{
		printf("Failed to create the table\n");
	}
	hash_table_print(ht);
	hash_table_set(ht, "c", "fun");
	hash_table_set(ht, "python", "awesome");
	hash_table_set(ht, "betty", "cool");
	hash_table_set(ht, "hetairas", "mentioner");
	hash_table_set(ht, "heliotropes", "neurospora");
	hash_table_set(ht, "Bob", "and Kris love asm");
	hash_table_set(ht, "N", "queens");
	hash_table_set(ht, "Asterix", "Obelix");
	hash_table_set(ht, "depravement", "serafins");
	hash_table_set(ht, "stylist", "subgenera");
	hash_table_set(ht, "Betty", "Cool");
	hash_table_set(ht, "joyful", "synaphea");
	hash_table_set(ht, "98", "Battery Street");
	hash_table_set(ht, "redescribed", "urites");
	hash_table_set(ht, "dram", "vivency");
	hash_table_set(ht, "Alphonce", "Kochieng");
	hash_table_set(ht, "Ayudo", "gino");
	hash_table_print(ht);
	hash_table_delete(ht);
	return (EXIT_SUCCESS);
}
