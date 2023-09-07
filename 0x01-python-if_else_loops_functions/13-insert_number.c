#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a node in list
 * @head: Pointer to first node
 * @number: Number inside new node
 * Return: New node or NULL if it fails
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *temp = (*head);

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;

	if ((*head) == NULL || number <= (*head)->n)
	{
		new->next = *head;
		(*head) = new;
	}
	else
	{
		while (temp->next != NULL)
		{
			if (temp->next->n < number)
				temp = temp->next;
			else
				break;
		}
		new->next = temp->next;
		temp->next = new;
	}
	return (new);
}
