#include <stdio.h>
#pragma warning(disable:4996)
#include<string.h>
#include<stdlib.h>

int n;
long long h[100000];
long long max;

typedef struct tree {
	int data;
	struct tree* left;
	struct tree* right;
}tree;

tree* stack[100000];

void histo(int start, int end, tree* min) {
	if (min == NULL)return;
	if ((end - start + 1) * h[min->data] > max) max = (end - start + 1) * h[min->data];
	if (min->data != start) histo(start, min->data - 1, min->left);
	if (min->data != end) histo(min->data + 1, end, min->right);
}

int find(int st, int ed, int key) {
	if (st > ed) return st;
	int mid = (st + ed) / 2;
	
	if (h[stack[mid]->data] > h[key]) {
		return find(st, mid - 1, key);
	}
	else if (h[stack[mid]->data] == h[key]) {
		return mid+1;
	}
	else {
		return find(mid + 1, ed, key);
	}
}

int main(void) {
	int res,ed;
	tree* head;
	tree* temp;
	while (1) {
		scanf("%d", &n);
		if (n == 0) break;
		max = 0;
		ed = 0;
		scanf("%lld", &h[0]);
		head = (tree*)malloc(sizeof(tree));
		head->data = 0;
		head->left = NULL;
		head->right = NULL;
		stack[0] = head;
		for (int i = 1; i < n; i++) {
			scanf("%lld", &h[i]);
			temp = (tree*)malloc(sizeof(tree));
			temp->data = i;
			temp->left = NULL;
			temp->right = NULL;
			res = find(0, ed, i);
			ed = res;
			stack[ed] = temp;
			if (res==0) {
				temp->left = head;
				head = temp;
			}
			else {
				temp->left = stack[res - 1]->right;
				stack[res - 1]->right = temp;
			}
		}
		histo(0, n - 1, head);
		printf("%lld\n", max);
	}


	return 0;
}