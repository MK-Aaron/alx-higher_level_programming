#include "lists.h"

/**
 * check_cycle - Confirms if a list has a cycle
 * list: point to head node
 * Return: 0 if there is no cycle and 1 if there is cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *constant = list;

	list = list->next;

	while (list)
	{
		if (list == constant)
			return (1);
		list = list->next;
	}
	return (0);
}
