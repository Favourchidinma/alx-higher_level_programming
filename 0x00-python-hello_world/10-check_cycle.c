#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - a function that checks if a singly linked list has a
 * cycle in it
 * @list: a pointer to the singly linked list
 * Return: returns 0 if there is no cycle, returns 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *prv = list;
	listint_t *nxt = list;

	if (!list)
		return (0);
	while (prv && nxt && nxt->next)
	{
		prv = prv->next;
		nxt = nxt->next->next;

		if (prv == nxt)
			return (1);
	}
	return (0);
}
