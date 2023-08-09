#include "lists.h"
/**
  *check_cycle - function that checks if a singly linked list has cycles in it
  *@list: the head of the list
  *
  *Return: 0 if no cycle, otherwise 1
  */
int check_cycle(listint_t *list)
{
	listint_t *slow;
	listint_t *fast;
	int cycle = 0;

	if (list == NULL)
		return (cycle);
	slow = list;
	fast = list->next;
	if (fast != NULL)
		fast = fast->next;
	while (slow != NULL)
	{
		if (slow == fast && fast != NULL)
		{
			cycle = 1;
			break;
		}
		else if (fast == NULL)
			break;
		slow = slow->next;
		fast = fast->next;
		if (fast != NULL)
			fast = fast->next;
	}
	return (cycle);
}
