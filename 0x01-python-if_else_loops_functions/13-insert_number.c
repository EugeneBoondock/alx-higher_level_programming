#include <stdlib.h>
#include <string.h>
#include "lists.h"
#include <stdio.h>

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current;
	listint_t *new_node;

	if (*head == NULL)
	{
		*new_node = (listint_t *)malloc(sizeof(listint_t));
		if (new_node == NULL)
		{
			return NULL;
		}
		
		new_node->n = number;
		new_node->next = NULL;
		
		*head = new_node;
		return new_node;
	}

	current = *head;
	
	if (number < current->n)
	{
		*new_node = (listint_t *)malloc(sizeof(listint_t));
		if (new_node == NULL)
		{
			return NULL;
		}
		new_node->n = number;
		new_node->next = current;
		
		*head = new_node;
		
		return new_node;
	}
	
	while (current->next != NULL && current->next->n < number)
	{
		current = current->next;
	}
	
	*new_node = (listint_t *)malloc(sizeof(listint_t));
	if (new_node == NULL)
	{
		return NULL;
	}
}
