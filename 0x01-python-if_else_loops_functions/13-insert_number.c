#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a number into
 * a sorted singly linked list
 * head: pointer to node
 * number: number to add new node
 * Return: pointer otherwise NULL
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp = *head;
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (*head == NULL || number <= (*head)->n)
	{
		new->next = *head;
		*head = new;
		return (new);
	}

	/* temp->next: helps to check if the next node is a NULL */
	while (temp != NULL && temp->next && temp->next->n < number)
	{
		temp = temp->next;
	}

	new->next = temp->next;
	temp->next = new;

	return (new);
}
