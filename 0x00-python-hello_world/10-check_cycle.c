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

	temp = temp2 = list;
	while (temp && temp2 && temp2->next)
	{
		temp = temp->next;
		temp2 = temp2->next->next;
		if (temp == temp2)
			return (1);
	}
	return (0);
}
