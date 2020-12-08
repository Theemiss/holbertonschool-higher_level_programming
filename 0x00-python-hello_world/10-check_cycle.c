#include "lists.h"

/**
 * check_cycle - check a singly linked list has a cycle in it
 *
 * @list: linked list
 * Return: 0 or 1
 */
int check_cycle(listint_t *list)
{
	listint_t *nextn = list, *nextn_nextn = list;

	while (nextn && nextn_nextn  && nextn_nextn->next)
	{
		nextn = nextn->next;
		nextn_nextn  = nextn_nextn->next->next;
		if (nextn == nextn_nextn)
		{
			return (1);
		}
	}
	return (0);
}
