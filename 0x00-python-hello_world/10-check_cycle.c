#include "lists.h"

/**
 * check_cycle - Confirms if a list has a cycle
 * @list: point to head node
 * Return: 0 if there is no cycle and 1 if there is cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *fast;

	fast = list;

	if (list == NULL)
		return (0);

	while (list->next && fast->next->next)
	{
		fast = fast->next->next;
		if (list == fast)
			return (1);
		list = list->next;
	}
	return (0);
}
