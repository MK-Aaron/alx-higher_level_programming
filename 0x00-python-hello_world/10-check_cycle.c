#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - Checks if linked list has cycle
 * @list: linked list to check
 * Return: 0 if there is no cycle else 1
 */

int check_cycle(listint_t *list)
{
	listint_t *fast;
	listint_t *slow;

	fast = malloc(sizeof(listint_t));
	if (fast == NULL)
		return (0);
		
	slow = malloc(sizeof(listint_t));
	if (slow == NULL)
		return (0);

	fast = slow = list;

	while (slow->next != NULL && fast->next->next != NULL)
	{
		fast = fast->next->next;
		slow = slow->next;

		if (fast == slow)
			return (1);
	}

	return (0);
}
