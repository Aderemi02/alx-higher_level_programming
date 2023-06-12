#include "lists.h"
/**
 * insert_node - inserting a new node to a list
 * @head: the beginning of the list
 * @number: value to be added to the list
 * Return: the address to the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *Nnode, *temp = *head;

	Nnode = malloc(sizeof(listint_t));
	if (Nnode == NULL)
		return (NULL);

	Nnode->n = number;
	if (temp == NULL || temp->n >= number)
	{
		Nnode->next = temp;
		*head = Nnode;
		return (Nnode);
	}
	while (temp && temp->next && temp->next->n < number)
	{
		temp = temp->next;
	}
	Nnode->next = temp->next;
	temp->next = Nnode;

	return (Nnode);
}
