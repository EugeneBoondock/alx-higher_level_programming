#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @listint_t: integer
 *
 * Description: singly linked list node structure
 * Return: 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	int stack[1024];
	int top = -1;
	
	while (fast != NULL && fast->next != NULL)
	{
		stack[++top] = slow->n;
		slow = slow->next;
		fast = fast->next->next;
	}
	
	if (fast != NULL)
	{
		slow = slow->next;
	}
	
	while (slow != NULL)
	{
		if (stack[top--] != slow->n)
		{
			return 0;
		}
		slow = slow->next;
	}
	
	return 1;
}
