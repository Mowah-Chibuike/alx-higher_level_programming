#include "lists.h"
#include <string.h>

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: pointer to the first node in the  linked list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp, *temp1, *fast, *slow, *prev;

	if (*head == NULL || (*head)->next == NULL)
		return (0);
	fast = slow = *head;
	while (fast && fast->next)
	{
		fast = fast->next->next;
		prev = slow;
		slow = slow->next;
	}
	prev->next = NULL;

	/* Reverse the second half of the linked list */
	prev = NULL;
	while (slow != NULL)
	{
		temp = slow->next;
		slow->next = prev;
		prev = slow;
		slow = temp;
	}
	temp = *head;
	temp1 = prev;

	/* check for palindrome */
	while (temp != NULL && temp1 != NULL)
	{
		if (temp->n != temp1->n)
		{
			free_listint(prev);
			return (0);
		}
		temp = temp->next;
		temp1 = temp1->next;
	}
	free_listint(prev);
	return (1);
}
