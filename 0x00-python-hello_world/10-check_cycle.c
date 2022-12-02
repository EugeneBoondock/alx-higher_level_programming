#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
* struct listint_s - singly linked list
* @n: integer
* @next: points to the next node
*
* Description: singly linked list node structure
*/
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	slow = list;
	fast = list;

	while (fast && fast->next)
	{

		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
		{
			return 1;
		}
	}

	return 0;
}
