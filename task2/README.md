The Problem:
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

The Solution:
Firstly we used a for loop to iterate on the list of prices and we get the minimum value and this value will be the price that i will buy with it
Secondly we get the maximum value after the minimum value and this value will be the value we will sell with it 
thirdly the difference between them will be our profit 

