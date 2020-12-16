#include "lists.h"

int is_palindrome(listint_t **head)
{
	listint_t *temp;
	int count = 0;
	int reverse = 0, i;
	int array[1024];
	if (*head == NULL)
		return 1;
	temp = *head;
	while(temp !=NULL)
	{
		array[count] = temp->n;
		temp = temp->next;
		count += 1;
	}
	reverse = count - 1;
	for (i = 0 ; i < (count / 2); i++, reverse--)
	{
		if(array[i] != array[reverse])
			return 0;
	}
	return 1;
}
