#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - Check list if is palindrome
 * @head: pointer to a node
 * Return: 1 if true 0 false
 */

int is_palindrome(listint_t **head)
{
	listint_t *temp, *current;
	unsigned int num_nod;
	int *arr, i;

	temp = *head;

	num_nod = 0;
	while (temp != NULL)
	{
		num_nod++;
		temp = temp->next;
	}

	arr = malloc(num_nod * sizeof(arr));
	if (arr == NULL)
		return (0);

	temp = *head;
	for (i = 0; temp != NULL; i++)
	{
		arr[i] = temp->n;
		temp = temp->next;
	}

	current = *head;
	for (i = num_nod - 1; current != NULL; i--)
	{
		if (current->n != arr[i])
		{
			free(arr);
			return (0);
		}
		currrent = cuurent->next;
	}
	free(arr);

	return (1);
}
