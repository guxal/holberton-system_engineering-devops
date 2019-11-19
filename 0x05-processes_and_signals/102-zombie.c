#include <stdio.h>
#include <unistd.h>
/**
 * infinite_while - infinite while
 * Return: Success 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
/**
 * main - Entry Point
 * Return: Success 0
 */
int main(void)
{
	pid_t zombie_process;
	int i;

	for (i = 0; i < 5; i++)
	{
		zombie_process = fork();
		if (!zombie_process)
			return (0);
		printf("Zombie process create, PID: %d\n", zombie_process);
	}
	infinite_while();
	return (0);
}
