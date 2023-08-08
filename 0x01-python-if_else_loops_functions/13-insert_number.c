#include "lists.h"
#include <stddef.h>
/**
  *insert_node - inserts a number into a sorted singly linked list
  *@head: the head of the list
  *@number: the value of n in the new struct
  *
  *Return: the newly created struct
  */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *cur, *new, *prev;

	new = NULL;
	prev = NULL;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
	if (*head == NULL)
	{
		*head = new;
		return (new);
	}
	cur = *head;
	while (!(cur == NULL) && (cur->n < number))
	{
		prev = cur;
		cur = cur->next;
	}
	if (cur == NULL)
		prev->next = new;
	else if (prev == NULL)
	{
		new->next = cur;
		*head = new;
	}
	else
	{
		prev->next = new;
		new->next = cur;
	}
	return (new);
}
