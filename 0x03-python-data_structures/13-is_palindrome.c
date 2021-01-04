#include "lists.h"

listint_t *reverse_listint(listint_t **head);
	
int is_palindrome(listint_t **head)
{
	listint_t *aux = *head, *current = *head;
	if (*head == NULL)
		return 1;
	if((*head)->next == NULL)
		return 1;
	while (current != NULL && aux != NULL && aux->next != NULL)
	{
		current = current->next;
		aux = aux->next->next;
	}
	current = reverse_listint(&current);
	aux = *head;
	while(aux != NULL && current != NULL)
	{	
		if (aux->n != current->n)
			return 0;
		aux = aux->next;
		current = current->next;
	}
	(void)aux;
	return 1;
}
listint_t *reverse_listint(listint_t **head)
{
	listint_t *next = *head, *current = NULL;

	if (*head == NULL)
		return (NULL);
	if ((*head)->next == NULL)
		return (*head);
	while (*head != NULL)
	{
		next = (*head)->next;
		(*head)->next = current;
		current = *head;
		*head = next;
	}
	*head = current;
	return (*head);
}
