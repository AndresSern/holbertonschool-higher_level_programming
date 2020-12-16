#include "lists.h"
listint_t *insert_nodeint_at_index(listint_t **head, unsigned int idx, int n);

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head, *after = *head;
	listint_t *new_node;
	int count = 1;
	while((current && after) || (after->next == NULL))
	{
		if (current->n < number && (after->next == NULL))
		{
				new_node = insert_nodeint_at_index(head, count, number);	
				return new_node;
		}

		if (current->n < number && (after->next->n > number))
		{
				new_node = insert_nodeint_at_index(head, count, number);
				return new_node;
		}

		if(after->next != NULL)
		{
			current = current->next;
			after = after->next;
		}
		printf("Position = %d\n", count);
		count++;
	}
	return NULL;
}
listint_t *insert_nodeint_at_index(listint_t **head, unsigned int idx, int n)
{
	unsigned int count = 0;
	listint_t *new_node, *current_node = *head;

	new_node = malloc(sizeof(listint_t));

	if (!new_node)
	{
		free(new_node);
		return (NULL);
	}

	new_node->n = n;
	new_node->next = NULL;
	if (*head == NULL && idx > 0)
	{
		free(new_node);
		return (NULL);
	}
	if (idx == 0)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}

	for (; count < idx - 1; count++)
	{
		current_node = current_node->next;
		if (current_node == NULL && idx - count > 0)
		{
			free(new_node);
			return (NULL);
		}
	}
	new_node->next = current_node->next;
	current_node->next = new_node;
	return (new_node);
}
