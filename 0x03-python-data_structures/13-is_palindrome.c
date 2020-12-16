#include "lists.h"

int is_palindrome(listint_t **head)
{
	listint_t *temp;
	int count = 0;
	int i = 0;
	int array[1024];
	if (*head == NULL)
		return 1;
	temp = *head;
	while(*head != NULL || head == NULL)
	{
		array[count] = (*head)->n;
		*head = (*head)->next;
		count += 1;
	}
	while(temp != NULL)
	{
		if(array[i] != temp->n)
			return 0;
		i += 1;
		temp = temp->next;
	}
	return 1;
}
