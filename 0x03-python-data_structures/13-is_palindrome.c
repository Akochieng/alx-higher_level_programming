#include "lists.h"
/**
  *is_palindrome - checks whether a linked list is a palindrome
  *@head: the head of the list
  *
  *Return: 1 if palindrome, and 0 otherwise
  */
int is_palindrome(listint_t **head)
{
	int len, mid, i, low, high;
	int is_pali = 1;

	len = mid = 0;
	if (*head == NULL)
		return (is_pali);
	len = length(head);
	mid = len / 2;
	i = len % 2 == 0 ? 1 : 0;
	while (mid - i >= 0 && is_pali == 1)
	{
		low = checkint(mid - i, head);
		high = checkint(len - mid - i,head);
		if (!(low == high))
			is_pali = 0;
		i++;
	}
	return (is_pali);
}
/**
  *checkint - checks the interger at the specified location
  *@num: the number of nodes at the specified location
  *@head: the head of the list
  *
  *Return: the value of the interger in the struct
  */
int checkint(int num, listint_t **head)
{
	listint_t *temp = NULL;

	if (*head == NULL)
		return (0);
	temp = *head;
	while (num-- >= 1)
		temp = temp->next;
	return (temp->n);
}
/**
  *length - get the length of the list
  *@head: the head of the list
  *Description: function to get the number of nodes in a list
  *
  *Return: the number of nodes in the list
  */
int length(listint_t **head)
{
	listint_t *temp = NULL;
	int n = 0;

	if (*head == NULL)
		return (0);
	temp = *head;
	while (temp != NULL)
	{
		temp = temp->next;
		n++;
	}
	return (n);
}
