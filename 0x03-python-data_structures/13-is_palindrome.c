#include "lists.h"
/**
  *is_palindrome - checks whether a linked list is a palindrome
  *@head: the head of the list
  *
  *Return: 1 if palindrome, and 0 otherwise
  */
int is_palindrome(listint_t **head)
{
	int len, i, start, stop;
	int is_pali = 1;
	int *bufr = NULL;
	listint_t *temp;

	if (*head == NULL)
		return (is_pali);
	len = length(head);
	bufr = malloc(len * sizeof(int));
	if (bufr == NULL)
		exit(1);
	temp = *head;
	for (i = 0; i < len; i++)
	{
		bufr[i] = temp->n;
		temp = temp->next;
	}
	start = 0;
	stop = len - 1;
	while ((start <= len / 2 && stop >= len / 2) && is_pali)
	{
		if (bufr[start] != bufr[stop])
			is_pali = 0;
		start++;
		stop--;
	}
	free(bufr);
	return (is_pali);
}
/**length - get the length of the list
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
	while (!(temp == NULL))
	{
		temp = temp->next;
		n++;
	}
	return (n);
}
