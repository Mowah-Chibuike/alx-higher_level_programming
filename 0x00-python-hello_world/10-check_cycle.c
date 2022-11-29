#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: linked list to be checked
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *temp = list, *temp2;

	if (temp == NULL)
		return (0);
	while (temp != NULL)
	{
		temp2 = temp->next;
		while (temp2 != NULL)
		{
			if (temp == temp2)
				return (1);
			temp2 = temp2->next;
		}
		temp = temp->next;
	}
	return (0);
}
