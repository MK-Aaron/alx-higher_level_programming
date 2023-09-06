#include "lists.h"

/**
 * check_cycle - Confirms if a list has a cycle
 * @list: point to head node
 * Return: 0 if there is no cycle and 1 if there is cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (list != NULL)
	{
		slow = list;
		fast = list->next;
	
		while (slow && slow->next && fast->next->next)
		{
			if (slow == fast)
				return (1);
			slow = slow->next;
			fast = fast->next->next;
		}
	}
	return (0);
}
