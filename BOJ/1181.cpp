/*

    https://www.acmicpc.net/problem/1181
    
    단순한 이중조건 정렬


*/

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <set>

using namespace std;


int main()
{

	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	set<string> input;
	
	int n;
	cin >> n;

	while (n--)
	{

		string s;
		cin >> s;
		input.insert(s);
	}

	vector<string> vc(input.begin(), input.end());

	std::sort(vc.begin(), vc.end(), [](const auto& lhs, const auto& rhs)
		{
			if (lhs.size() != rhs.size())
			{
				return lhs.size() < rhs.size();
			}
			else
			{
				return lhs < rhs;
			}

		});

	for (auto s : vc)
		cout << s << '\n';
	
}