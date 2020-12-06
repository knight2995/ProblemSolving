/*

    https://www.acmicpc.net/problem/1018

    단순한 문제

*/

#include <iostream>

using namespace std;


char board[50][50];

//balck 1
//white 0

int h, w;

char Color[2] = { 'B','W' };

int startBlack(int i, int j)
{
	int start = 0;
	int count = 0;
	for (int k = i; k < i + 8; k++)
	{
		for (int l = j; l < j + 8; l++)
		{
			if (board[k][l] == Color[start])
				;
			else
				count++;			

			start = (start + 1) % 2;
		}
		start = (start + 1) % 2;
	}

	return count;

}

int startWhite(int i, int j)
{
	int start = 1;
	int count = 0;
	for (int k = i; k < i + 8; k++)
	{
		for (int l = j; l < j + 8; l++)
		{
			if (board[k][l] == Color[start])
				;
			else
				count++;

			start = (start + 1) % 2;
		}
		start = (start + 1) % 2;
	}

	return count;
}
int main()
{

	cin >> h >> w;

	for (int i = 0; i < h; i++)
	{
		for (int j = 0; j < w; j++)
		{
			cin >> board[i][j];
		}
	}

	int min = 64;
	for (int i = 0; i < h - 8 + 1; i++)
	{
		for (int j = 0; j < w - 8 + 1; j++)
		{

			
			int bMin = startBlack(i, j);
			int wMin = startWhite(i, j);
			int sMin = bMin < wMin ? bMin : wMin;

			min = sMin < min ? sMin : min;
			
			

		}
	}

	cout << min;
}