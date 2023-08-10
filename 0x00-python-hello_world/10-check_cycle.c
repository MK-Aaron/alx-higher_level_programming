#include "lists.h"

/**
 * check_cycle - infinite loop list
 * list: pointer to the singly linked list
 * Return: 0 if no cyle otherwise 1
 */

int check_cycle(listint_t *list)
{
	listint_t *tmp = list;

	while (tmp != NULL && tmp->next != NULL)
	{
		tmp = tmp->next;
		if (tmp != NULL && list == tmp)
			return (1);
	}

	return (0);
}
