#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp = *head, *new;

	if (head == NULL)
		return (NULL);
	new = (listint_t *)malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
	if (*head == NULL || number <= (*head)->n)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	while (temp && temp->next)
	{
		if (number >= temp->n && number <= temp->next->n)
		{
			new->next = temp->next;
			temp->next = new;
			return (new);
		}
		temp = temp->next;
	}
	temp->next = new;
	return (new);
}
